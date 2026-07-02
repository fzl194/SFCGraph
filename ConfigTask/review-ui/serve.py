"""Task 层审查 UI 服务（v2：父子树导航 + 单 task 视图 + 审查记录/状态/历史）。

用法：python serve.py [port]   # 默认 http://localhost:8765

端点：
  GET  /                     → index.html
  GET  /app.js /<静态>       → review-ui/ 下静态文件
  GET  /api/assets           → 全部 task/DP/rule + 复用统计 + 父子树(tree)
  GET  /api/review-state     → review-state.json（审查记录，状态由此推导）
  POST /api/review           → {object_id,verdict,note} 追加一条审查记录（并镜像到 manual-feedback.md）
"""
import json
import sys
import webbrowser
import datetime
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 pyyaml：pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent          # ConfigTask/
ASSETS = ROOT / "task-assets" / "UDG" / "20.15.2"
REVIEW_STATE = ASSETS / "review-state.json"
FEEDBACK_FILE = ASSETS / "review" / "manual-feedback.md"
UI_DIR = Path(__file__).resolve().parent
_LOCK = threading.Lock()
VERDICTS = {"通过", "驳回", "待补"}
MIME = {".html": "text/html; charset=utf-8", ".js": "application/javascript; charset=utf-8",
        ".css": "text/css; charset=utf-8", ".json": "application/json; charset=utf-8"}


def short(ref: str) -> str:
    return ref.split("@")[-1] if ref else ""


def load_yaml_dir(d: Path):
    out = []
    if not d.exists():
        return out
    for p in sorted(d.glob("*.yaml")):
        try:
            out.append(yaml.safe_load(p.read_text(encoding="utf-8")) or {})
        except Exception as e:
            out.append({"_file": p.name, "_error": str(e)})
    return out


def build_reuse(tasks):
    """跨特性复用（传递）：feature/generalized 经 compound 间接引用的 atom 也算"""
    compounds_atoms = {}
    for t in tasks:
        if t.get("task_layer") == "compound":
            atoms = set()
            for r in (t.get("task_relations") or []):
                for ref in (r.get("from_task_ref"), r.get("to_task_ref")):
                    if ref and short(ref).startswith("0-"):
                        atoms.add(ref)
            compounds_atoms[t.get("task_id", "")] = atoms
    reuse = {}
    for t in tasks:
        if t.get("task_layer") in ("feature", "generalized"):
            used = set()
            for r in (t.get("task_relations") or []):
                for ref in (r.get("from_task_ref"), r.get("to_task_ref")):
                    if not ref:
                        continue
                    s = short(ref)
                    if s.startswith("0-"):
                        used.add(ref)
                    elif s.startswith("1-"):
                        used |= compounds_atoms.get(ref, set())
            for a in used:
                reuse.setdefault(a, []).append(t.get("task_id", ""))
    return reuse


def build_tree(tasks):
    """父子树：generalized→feature→compound→atom。每个 task 恰一个 tree-parent。
    tree-parent 规则：在上层引用方中取最近的一层（atom 优先 compound，其次 feature…）。
    返回 tree_parent / children / roots / dfs_order(深度优先) / containers(全部引用方)。"""
    by_short = {short(t.get("task_id", "")): t for t in tasks if t.get("task_id")}
    rank = {"atom": 0, "compound": 1, "feature": 2, "generalized": 3, "solution": 2}

    def rk(s):
        return rank.get(by_short.get(s, {}).get("task_layer", ""), -1)

    containers = {}  # child_short -> set(parent_short)（仅记录上层引用方）
    for t in tasks:
        ps = short(t.get("task_id", ""))
        for r in (t.get("task_relations") or []):
            for k in ("from_task_ref", "to_task_ref"):
                c = short(r.get(k, ""))
                if c and c in by_short and c != ps and rk(c) < rk(ps):
                    containers.setdefault(c, set()).add(ps)

    tree_parent = {}
    for c, parents in containers.items():
        cands = sorted(parents, key=lambda p: (rk(p), p))  # 最近上层优先，id 兜底
        if cands:
            tree_parent[c] = cands[0]

    children = {}
    for c, p in tree_parent.items():
        children.setdefault(p, []).append(c)
    for p in children:
        children[p].sort()

    roots = [s for s in by_short if s not in tree_parent]
    roots.sort(key=lambda s: (-rk(s), s))  # generalized 在前

    dfs = []
    seen = set()

    def visit(n):
        if n in seen:
            return
        seen.add(n)
        dfs.append(n)
        for ch in sorted(children.get(n, [])):
            visit(ch)

    for r in roots:
        visit(r)

    return {"tree_parent": tree_parent, "children": children, "roots": roots,
            "dfs_order": dfs, "containers": {k: sorted(v) for k, v in containers.items()}}


def build_assets():
    tasks = load_yaml_dir(ASSETS / "tasks")
    dps = load_yaml_dir(ASSETS / "decision_points")
    rules = load_yaml_dir(ASSETS / "task_rules")
    reuse = build_reuse(tasks)
    for t in tasks:
        t["_short"] = short(t.get("task_id", ""))
        t["_params"] = len(t.get("parameter_bindings") or [])
        t["_relations"] = len(t.get("task_relations") or [])
        if t.get("task_layer") == "atom":
            t["_reuse_by"] = reuse.get(t.get("task_id", ""), [])
    tree = build_tree(tasks)
    # spec §4 by_layer: 按 task_layer 分组,_short 升序。solution 层 v2 体系未使用,不出现在 by_layer。
    by_layer = {"atom": [], "compound": [], "feature": [], "generalized": []}
    for t in tasks:
        layer = t.get("task_layer", "")
        if layer in by_layer:
            by_layer[layer].append(t["_short"])
    for layer in by_layer:
        by_layer[layer].sort()
    # spec §4 relation_targets: 该 task 经 task_relations 引用到的所有其他 task 短 id(去重 + 排除自身 + 升序)。
    # 与 tree.children(单一 parent)/ tree.containers(全部上层引用方)互补。
    relation_targets = {t["_short"]: set() for t in tasks}
    known_sids = set(relation_targets.keys())
    for t in tasks:
        ps = t["_short"]
        for r in (t.get("task_relations") or []):
            for ref in (r.get("from_task_ref"), r.get("to_task_ref")):
                if not ref:
                    continue
                s = ref.split("@")[-1]
                if s != ps and s in known_sids:
                    relation_targets[ps].add(s)
    relation_targets = {k: sorted(v) for k, v in relation_targets.items()}
    return {"tasks": tasks, "dps": dps, "rules": rules, "reuse": reuse, "tree": tree,
            "by_layer": by_layer, "relation_targets": relation_targets,
            "nf_version": "UDG@20.15.2"}


def read_review_state():
    if not REVIEW_STATE.exists():
        return {"nf_version": "UDG@20.15.2", "records": {}}
    try:
        d = json.loads(REVIEW_STATE.read_text(encoding="utf-8"))
        d.setdefault("records", {})
        return d
    except Exception:
        return {"nf_version": "UDG@20.15.2", "records": {}}


def write_review_state(d):
    tmp = REVIEW_STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(REVIEW_STATE)


def derive_status(records_for_obj):
    if not records_for_obj:
        return "待审查"
    return records_for_obj[-1].get("verdict", "待审查")


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _static(self, rel):
        fp = (UI_DIR / rel).resolve()
        try:
            fp.relative_to(UI_DIR.resolve())
        except ValueError:
            self._send(403, b"forbidden")
            return
        if not fp.is_file():
            self._send(404, b"not found")
            return
        ctype = MIME.get(fp.suffix, "application/octet-stream")
        self._send(200, fp.read_bytes(), ctype)

    def do_GET(self):
        if self.path == "/api/assets":
            self._send(200, json.dumps(build_assets(), ensure_ascii=False).encode("utf-8"))
        elif self.path == "/api/review-state":
            self._send(200, json.dumps(read_review_state(), ensure_ascii=False).encode("utf-8"))
        elif self.path == "/" or self.path == "/index.html":
            idx = UI_DIR / "index.html"
            if idx.exists():
                self._send(200, idx.read_bytes(), "text/html; charset=utf-8")
            else:
                self._send(404, b"index.html missing")
        else:
            self._static(self.path.lstrip("/"))

    def do_POST(self):
        if self.path != "/api/review":
            self._send(404, b"not found")
            return
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length) or b"{}"
        try:
            data = json.loads(raw.decode("utf-8"))
        except UnicodeDecodeError:
            data = json.loads(raw.decode("gbk", errors="replace"))
        oid = (data.get("object_id") or "").strip()
        verdict = (data.get("verdict") or "").strip()
        note = (data.get("note") or "").strip()
        if not oid or verdict not in VERDICTS:
            self._send(400, json.dumps({"ok": False, "msg": "需 object_id + verdict∈{通过,驳回,待补}"}).encode("utf-8"))
            return
        with _LOCK:
            rs = read_review_state()
            recs = rs["records"].setdefault(oid, [])
            ts = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
            recs.append({"ts": ts, "reviewer": "人工", "verdict": verdict, "note": note})
            write_review_state(rs)
            # 镜像到 manual-feedback.md（供下一 pass Agent 按 SKILL §8.2 挖取反哺）
            try:
                FEEDBACK_FILE.parent.mkdir(parents=True, exist_ok=True)
                with FEEDBACK_FILE.open("a", encoding="utf-8") as f:
                    f.write(f"\n## {ts} — {oid} [{verdict}]\n- 意见: {note or '(无)'}\n  影响: {oid}\n  反哺Skill条款: (待 Agent 下一 pass 归类)\n")
            except Exception:
                pass
            status = derive_status(recs)
        self._send(200, json.dumps({"ok": True, "status": status, "records": recs}).encode("utf-8"))


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    url = f"http://localhost:{port}"
    print(f"审查 UI v2：{url}   （保持窗口开着；Ctrl+C 停止）")
    print(f"审查记录落盘：{REVIEW_STATE.relative_to(ROOT)}  + 镜像 {FEEDBACK_FILE.relative_to(ROOT)}")
    print("若浏览器没自动打开，手动访问上面的地址。")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    try:
        ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\n已停止，再见。")


if __name__ == "__main__":
    main()
