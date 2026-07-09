# 图谱总览前端 Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 platform-next 新增「图谱总览」tab——assets/ typed wiki 的三栏 Obsidian 式浏览器（左树分类导航 + 中区 md + 右栏 1 跳邻域图谱），点链接/节点自由跳转，图谱随跳转自动重画。

**Architecture:** 新增独立后端模块 `platform-next/wiki/`（只读 assets/），含预编译链接索引构建器（扫全量 md → nodes/edges/反邻接 JSON）+ service + router。前端新增 `frontend/src/wiki/`（三栏组件），复用现有 DocViewer 链接拦截 + CommandGraph vis-network 模式，URL 驱动跳转。

**Tech Stack:** Python 3 / FastAPI / PyYAML / pytest（后端）；Vue 3 + TypeScript + vue-router + Element Plus + markdown-it + DOMPurify + vis-network（前端）。

**Spec:** `docs/superpowers/specs/2026-07-09-graph-overview-frontend-design.md`
**约定：** 工作在 master 分支直提（用户偏好，不开 worktree）。提交信息不加 Co-Authored-By（项目 attribution 全局关闭）。后端走 TDD（pytest），前端无测试框架走 `npm run build` 类型检查 + 人工 e2e 清单。

---

## File Structure

> 本清单权威。与 spec §8 的文件清单有几处等价简化差异（config 用 `config.yaml`+内联 `get_service()` 而非独立 `config.py`；前端 api 用独立 `wikiApi.ts` 而非改 `api.ts`）——以本 plan 为准。

**后端新建**
- `platform-next/wiki/__init__.py` — 空
- `platform-next/wiki/models.py` — frozen dataclass：`Node` / `Edge` / `Index`（不可变，python 规范）
- `platform-next/wiki/parser.py` — front-matter 解析 + 正文链接/占位解析 + 关系类型推断（纯函数，无 IO）
- `platform-next/wiki/build_wiki_index.py` — 扫 assets/ 树 → 组装 Index → 写 JSON；含 `main()` CLI
- `platform-next/wiki/service.py` — 载入索引到内存 + 查询方法（categories/group/list/neighborhood/md/search）
- `platform-next/wiki/router.py` — FastAPI 端点 `/api/v1/wiki/*`

**后端测试**
- `platform-next/tests/wiki/__init__.py`
- `platform-next/tests/wiki/conftest.py` — 微型 assets 样例树 fixture
- `platform-next/tests/wiki/test_parser.py`
- `platform-next/tests/wiki/test_build_index.py`
- `platform-next/tests/wiki/test_service.py`
- `platform-next/tests/wiki/test_router.py`

**前端新建**
- `frontend/src/wiki/wikiApi.ts` — api 工厂（仿现有 `commandGraphApi`）
- `frontend/src/wiki/CategoryTree.vue` — 左栏分类树（懒加载 + 桶内搜索）
- `frontend/src/wiki/MdPane.vue` — 中区 md 渲染 + 链接拦截跳转（改造 DocViewer）
- `frontend/src/wiki/NeighborGraph.vue` — 右栏 1 跳图谱（改造 CommandGraph）
- `frontend/src/wiki/WikiIndex.vue` — 三栏 shell + 历史面包屑 + 路由 watch

**修改**
- `platform-next/config.yaml` — 加 `wiki: {assets_root: "../assets"}`
- `platform-next/main.py` — include wiki router + lifespan 触发索引载入/构建
- `frontend/src/router.ts` — 加 `/graph-overview` 两条路由
- `frontend/src/shared/TopBar.vue` — 加「图谱总览」链接
- `platform-next/.gitignore`（若无则在 wiki/data/ 加）— 排除 `wiki_index.json`

---

## Chunk 1: 后端索引构建器（parser + models + builder）

### Task 1: 数据模型 + config

**Files:**
- Create: `platform-next/wiki/__init__.py`
- Create: `platform-next/wiki/models.py`
- Modify: `platform-next/config.yaml`

- [ ] **Step 1: 写 models.py（frozen dataclass）**

```python
"""wiki 索引数据模型（不可变）。"""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Node:
    path: str            # assets 根相对路径, 如 command/UDG/20.15.2/ADD-URR.md
    id: str              # front-matter id
    type: str            # ObjectType: MMLCommand/ConfigObject/Feature/License/Task/...
    name: str
    nf: str | None
    version: str | None
    status: str
    title: str           # 首个 H1 或 name
    group: tuple[tuple[str, str], ...]  # 分组字段, 如 (("category_path","用户面服务管理/..."),("verb","ADD"))


@dataclass(frozen=True)
class Edge:
    src: str             # 源 node path（必为真实文件）
    dst: str             # 目标 path（resolved）或 对象ID（未解析占位）
    relation_type: str
    resolved: bool       # dst 是否有对应文件


@dataclass(frozen=True)
class Index:
    nodes: dict[str, Node]                       # path -> Node
    id_to_path: dict[str, str]                   # 对象ID -> path
    out_edges: dict[str, tuple[Edge, ...]]       # src path -> 出向边
    reverse: dict[str, tuple[str, ...]]          # dst path -> 源 path 列表（反链）
```

- [ ] **Step 2: 加 config**

在 `platform-next/config.yaml` 末尾追加：
```yaml
wiki:
  assets_root: "../assets"
```

- [ ] **Step 3: 建 `__init__.py`（空）**
- [ ] **Step 4: Commit**

```bash
git add platform-next/wiki/__init__.py platform-next/wiki/models.py platform-next/config.yaml
git commit -m "feat(wiki): 索引数据模型 + config 骨架"
```

---

### Task 2: parser —— front-matter + 关系推断（纯函数）

**Files:**
- Create: `platform-next/wiki/parser.py`
- Create: `platform-next/tests/wiki/__init__.py`
- Create: `platform-next/tests/wiki/conftest.py`
- Create: `platform-next/tests/wiki/test_parser.py`

- [ ] **Step 1: 写 conftest 微型样例**

```python
# platform-next/tests/wiki/conftest.py
import textwrap
from pathlib import Path
import pytest


@pytest.fixture
def sample_assets(tmp_path: Path) -> Path:
    """微型 assets 样例树，覆盖命令/配置对象/特性/任务/证据 + 占位。"""
    root = tmp_path / "assets"
    (root / "command/UDG/20.15.2").mkdir(parents=True)
    (root / "configobject/UDG/20.15.2").mkdir(parents=True)
    (root / "feature/UDG/20.15.2").mkdir(parents=True)
    (root / "task/UDG/20.15.2").mkdir(parents=True)
    (root / "evidence/UDG/20.15.2").mkdir(parents=True)

    (root / "command/UDG/20.15.2/ADD-URR.md").write_text(textwrap.dedent("""\
        ---
        id: UDG@20.15.2@MMLCommand@ADD URR
        type: MMLCommand
        name: ADD URR
        nf: UDG
        version: 20.15.2
        verb: ADD
        object_keyword: URR
        category_path:
        - 用户面服务管理
        - 计费控制
        status: active
        ---
        # ADD URR（增加URR）

        ## 操作的配置对象

        - [URR](configobject/UDG/20.15.2/URR.md)

        ## 关联任务

        - [0-00001](task/UDG/20.15.2/0-00001.md)

        ## 证据

        - 原始手册：`evidence/UDG/20.15.2/增加URR（ADD-URR）_82837629.md`
    """), encoding="utf-8")

    (root / "configobject/UDG/20.15.2/URR.md").write_text(textwrap.dedent("""\
        ---
        id: UDG@20.15.2@ConfigObject@URR
        type: ConfigObject
        name: URR
        nf: UDG
        version: 20.15.2
        object_kind: entity
        status: active
        ---
        # URR

        ## 操作本对象的命令

        - [ADD URR](command/UDG/20.15.2/ADD-URR.md)
    """), encoding="utf-8")

    (root / "task/UDG/20.15.2/0-00001.md").write_text(textwrap.dedent("""\
        ---
        id: UDG@20.15.2@Task@0-00001
        type: Task
        task_layer: atom
        name: 配置URR
        ref: UDG@20.15.2@MMLCommand@ADD URR
        nf: UDG
        version: 20.15.2
        status: inferred
        ---
        # 配置URR（ADD URR）

        ## 命令

        命令静态知识见 [ADD URR](command/UDG/20.15.2/ADD-URR.md)。关联对象 [[UDG@20.15.2@ConfigObject@URRGROUP]] 待建。
    """), encoding="utf-8")

    (root / "evidence/UDG/20.15.2/增加URR（ADD-URR）_82837629.md").write_text("# 手册原文\n", encoding="utf-8")
    return root
```

- [ ] **Step 2: 写失败测试 test_parser.py**

```python
# platform-next/tests/wiki/test_parser.py
from wiki import parser


def test_split_front_matter():
    fm, body = parser.split_front_matter("---\nid: x\n---\n# t\nbody")
    assert fm == "id: x\n"
    assert body == "# t\nbody"


def test_parse_front_matter_fields():
    fm = parser.split_front_matter("---\ntype: MMLCommand\ncategory_path:\n- a\n- b\n---\n# x")[0]
    meta = parser.parse_front_matter(fm)
    assert meta["type"] == "MMLCommand"
    assert meta["category_path"] == ["a", "b"]


def test_relation_type_from_heading():
    assert parser.relation_for_heading("操作的配置对象") == "operates_on"
    assert parser.relation_for_heading("操作本对象的命令") == "operated_by"
    assert parser.relation_for_heading("关联任务") == "has_task"
    assert parser.relation_for_heading("所需 License") == "requires_license"
    assert parser.relation_for_heading("所属目录") == "parent"
    assert parser.relation_for_heading("证据") == "evidenced_by"
    assert parser.relation_for_heading("某个未知小节") == "related"


def test_extract_md_links_resolved():
    body = "## 操作的配置对象\n\n- [URR](configobject/UDG/20.15.2/URR.md)\n"
    links = parser.extract_links(body)
    assert len(links) == 1
    assert links[0].dst == "configobject/UDG/20.15.2/URR.md"
    assert links[0].relation_type == "operates_on"
    assert links[0].resolved is True


def test_extract_placeholder_unresolved():
    body = "关联对象 [[UDG@20.15.2@ConfigObject@URRGROUP]] 待建。"
    links = parser.extract_links(body)
    assert len(links) == 1
    assert links[0].resolved is False
    assert links[0].dst == "UDG@20.15.2@ConfigObject@URRGROUP"
    assert links[0].relation_type == "related"


def test_extract_skips_images_and_external():
    body = "![图](x.png) 和 [外](https://e.com) 和 [文](a.md)"
    links = parser.extract_links(body)
    assert [l.dst for l in links] == ["a.md"]


def test_id_to_object_type():
    assert parser.object_type_of("UDG@20.15.2@Task@0-00001") == "Task"
    assert parser.object_type_of("ConfigurationSolution@charging") == "ConfigurationSolution"
    assert parser.object_type_of("no-at-id") == ""
```

- [ ] **Step 3: 运行测试，确认失败**

Run: `cd platform-next && python -m pytest tests/wiki/test_parser.py -v`
Expected: FAIL（ImportError：`wiki` 包未建/函数未定义）。

- [ ] **Step 4: 实现 parser.py**

> 导入路径：项目 `main.py` 把 `platform-next/` 加进 `sys.path`，测试统一用包内绝对 `from wiki import ...`。需在 conftest 顶部确保 `platform-next/` 在 `sys.path`（见 Step 5）。

```python
"""wiki md 解析器（纯函数，无 IO）。

链接约定（assets/CLAUDE.md §5.5）：
- 标准 markdown 链接 [text](path.md) → assets 根相对路径，目标存在则 resolved。
- [[对象ID]] 占位 → 双方括号，目标通常未建，resolved=False。
"""
from __future__ import annotations
import re
import posixpath
from dataclasses import dataclass

import yaml

from wiki.models import Edge

_FM_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n?(.*)$", re.S)
_MD_LINK_RE = re.compile(r'(?<!\!)\[([^\]]+)\]\(([^)\s]+?)(?:\s+"[^"]*")?\)')
_PLACEHOLDER_RE = re.compile(r"\[\[([^\]]+)\]\]")
_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")

# 小节标题关键词 -> 关系类型（小写包含匹配）
_HEADING_RULES: list[tuple[str, str]] = [
    ("操作的配置对象", "operates_on"),
    ("操作本对象的命令", "operated_by"),
    ("关联任务", "has_task"),
    ("关联命令", "ref_command"),
    ("命令", "ref_command"),
    ("所属目录", "parent"),
    ("子特性", "child"),
    ("所需", "requires_license"),       # 所需 License / 所需的License
    ("控制的能力", "controls_feature"),
    ("关联对象", "relates_to"),
    ("证据", "evidenced_by"),
    ("depends_on", "depends_on"),
    ("conflicts_with", "conflicts_with"),
    ("interacts_with", "interacts_with"),
    ("affects", "affects"),
    ("supports", "supports"),
]
_DEFAULT_RELATION = "related"


@dataclass(frozen=True)
class RawLink:
    dst: str
    relation_type: str
    resolved: bool


def split_front_matter(text: str) -> tuple[str, str]:
    m = _FM_RE.match(text)
    if not m:
        return "", text
    return m.group(1), m.group(2)


def parse_front_matter(fm: str) -> dict:
    if not fm.strip():
        return {}
    data = yaml.safe_load(fm)
    return data or {}


def relation_for_heading(heading: str) -> str:
    h = heading.strip().lower()
    for kw, rel in _HEADING_RULES:
        if kw.lower() in h:
            return rel
    return _DEFAULT_RELATION


def object_type_of(obj_id: str) -> str:
    parts = obj_id.split("@")
    # 四段式 {nf}@{version}@{ObjectType}@{local} 或 两段式 {ObjectType}@{slug}
    if len(parts) >= 4:
        return parts[2]
    if len(parts) == 2:
        return parts[0]
    return ""


def _normalize_href(href: str) -> str:
    """assets 根相对规范化（容忍偶发 ../）。"""
    if href.startswith(("http://", "https://", "data:", "#", "mailto:")):
        return href
    return posixpath.normpath(href).replace("\\", "/")


def extract_links(body: str) -> list[RawLink]:
    """逐行扫描正文，按当前 ## 小节推断关系类型，抽 markdown 链接 + [[ID]] 占位。"""
    # 先移除图片，避免图片 alt 被当成链接
    body_no_img = _IMAGE_RE.sub("", body)
    current_relation = _DEFAULT_RELATION
    out: list[RawLink] = []
    for line in body_no_img.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("#"):
            heading = stripped.lstrip("#").strip()
            current_relation = relation_for_heading(heading)
            continue
        for _text, raw_href in _MD_LINK_RE.findall(line):
            href = _normalize_href(raw_href)
            if not href.endswith(".md"):
                continue
            out.append(RawLink(dst=href, relation_type=current_relation, resolved=True))
        for pid in _PLACEHOLDER_RE.findall(line):
            out.append(RawLink(dst=pid, relation_type=current_relation, resolved=False))
    # 去重（同 dst+relation）
    seen: set[tuple[str, str]] = set()
    dedup: list[RawLink] = []
    for lk in out:
        key = (lk.dst, lk.relation_type)
        if key in seen:
            continue
        seen.add(key)
        dedup.append(lk)
    return dedup
```

- [ ] **Step 5: 确保测试可导入 —— conftest 顶部加 sys.path**

在 `platform-next/tests/wiki/conftest.py` 顶部加（在 import 之前）：
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # platform-next/
```

- [ ] **Step 6: 运行测试，确认通过**

Run: `cd platform-next && python -m pytest tests/wiki/test_parser.py -v`
Expected: 7 passed。

- [ ] **Step 7: Commit**

```bash
git add platform-next/wiki/parser.py platform-next/tests/wiki/
git commit -m "feat(wiki): front-matter + 链接解析器（关系推断，纯函数 TDD）"
```

---

### Task 3: builder —— 扫树组装 Index（两遍：nodes+body edges / front-matter 派生边）

**Files:**
- Create: `platform-next/wiki/build_wiki_index.py`
- Create: `platform-next/tests/wiki/test_build_index.py`

- [ ] **Step 1: 写失败测试**

```python
# platform-next/tests/wiki/test_build_index.py
from wiki.build_wiki_index import build_index


def test_build_index_basic(sample_assets):
    idx = build_index(sample_assets)
    # 4 个对象 md（命令/配置对象/任务 + 证据）
    assert "command/UDG/20.15.2/ADD-URR.md" in idx.nodes
    assert "configobject/UDG/20.15.2/URR.md" in idx.nodes
    assert "task/UDG/20.15.2/0-00001.md" in idx.nodes
    cmd = idx.nodes["command/UDG/20.15.2/ADD-URR.md"]
    assert cmd.type == "MMLCommand" and cmd.nf == "UDG" and cmd.version == "20.15.2"
    assert ("verb", "ADD") in cmd.group


def test_build_index_id_to_path(sample_assets):
    idx = build_index(sample_assets)
    assert idx.id_to_path["UDG@20.15.2@MMLCommand@ADD URR"] == "command/UDG/20.15.2/ADD-URR.md"


def test_build_index_body_edges_and_reverse(sample_assets):
    idx = build_index(sample_assets)
    cmd = "command/UDG/20.15.2/ADD-URR.md"
    obj = "configobject/UDG/20.15.2/URR.md"
    rels = {(e.dst, e.relation_type, e.resolved) for e in idx.out_edges.get(cmd, ())}
    assert (obj, "operates_on", True) in rels
    # 反链：URR 反引 ADD URR
    assert cmd in idx.reverse.get(obj, ())


def test_build_index_placeholder_unresolved(sample_assets):
    idx = build_index(sample_assets)
    task = "task/UDG/20.15.2/0-00001.md"
    rels = {(e.dst, e.resolved) for e in idx.out_edges.get(task, ())}
    assert ("UDG@20.15.2@ConfigObject@URRGROUP", False) in rels


def test_build_index_frontmatter_derived_edge(sample_assets):
    idx = build_index(sample_assets)
    task = "task/UDG/20.15.2/0-00001.md"
    cmd = "command/UDG/20.15.2/ADD-URR.md"
    rels = {(e.dst, e.relation_type) for e in idx.out_edges.get(task, ())}
    # task.ref -> command（front-matter 派生，与正文"命令"链接去重为 ref_command）
    assert (cmd, "ref_command") in rels


def test_build_index_evidence_node(sample_assets):
    idx = build_index(sample_assets)
    ev = [p for p in idx.nodes if p.startswith("evidence/")]
    assert len(ev) == 1
```

- [ ] **Step 2: 运行确认失败**

Run: `cd platform-next && python -m pytest tests/wiki/test_build_index.py -v`
Expected: FAIL（`build_index` 未定义）。

- [ ] **Step 3: 实现 build_wiki_index.py**

```python
"""扫 assets/ 全量 md，组装 Index（nodes + edges + 反邻接）。

两遍：
  pass1: 逐文件解析 front-matter + 正文链接 → nodes、id_to_path、body edges、占位边
  pass2: front-matter 派生边（task.ref→command、feature.parent_feature_code→parent），经 id_to_path 解析后去重加入
"""
from __future__ import annotations
import posixpath
from collections import defaultdict
from pathlib import Path

import yaml

from wiki.models import Edge, Index, Node
from wiki.parser import extract_links, object_type_of, parse_front_matter, split_front_matter

# type -> 取分组字段的函数（返回 ((field, value), ...) tuple）
_GROUP_FIELDS = {
    "MMLCommand": lambda m: _pairs(m, "category_path", "verb", "object_keyword"),
    "ConfigObject": lambda m: _pairs(m, "object_kind", "object_name"),
    "Feature": lambda m: _pairs(m, "feature_category", "parent_feature_code", "catalog_section"),
    "License": lambda m: _pairs(m, "applicable_nf"),
    "Task": lambda m: _pairs(m, "task_layer", "ref"),
}


def _pairs(m: dict, *keys: str) -> tuple[tuple[str, str], ...]:
    out: list[tuple[str, str]] = []
    for k in keys:
        if k not in m:
            continue
        v = m[k]
        if isinstance(v, list):
            v = "/".join(str(x) for x in v)
        if v in (None, ""):
            continue
        out.append((k, str(v)))
    return tuple(out)


def _first_h1(body: str) -> str:
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
    return ""


def build_index(assets_root: Path) -> Index:
    assets_root = assets_root.resolve()
    nodes: dict[str, Node] = {}
    id_to_path: dict[str, str] = {}
    out_edges: dict[str, list[Edge]] = defaultdict(list)
    reverse: dict[str, list[str]] = defaultdict(list)

    for md_path in sorted(assets_root.rglob("*.md")):
        rel = md_path.relative_to(assets_root).as_posix()
        text = md_path.read_text(encoding="utf-8")
        fm_text, body = split_front_matter(text)
        meta = parse_front_matter(fm_text)
        ntype = str(meta.get("type", _infer_type_from_path(rel)))
        group_fn = _GROUP_FIELDS.get(ntype)
        group = group_fn(meta) if group_fn else ()
        title = _first_h1(body) or str(meta.get("name", ""))
        node = Node(
            path=rel,
            id=str(meta.get("id", "")),
            type=ntype,
            name=str(meta.get("name", title)),
            nf=meta.get("nf"),
            version=meta.get("version"),
            status=str(meta.get("status", "")),
            title=title,
            group=group,
        )
        nodes[rel] = node
        if node.id:
            id_to_path[node.id] = rel

        # 正文 + 占位边
        seen: set[tuple[str, str]] = set()
        for lk in extract_links(body):
            key = (lk.dst, lk.relation_type)
            if key in seen:
                continue
            seen.add(key)
            out_edges[rel].append(Edge(src=rel, dst=lk.dst, relation_type=lk.relation_type, resolved=lk.resolved))
            if lk.resolved:
                reverse[lk.dst].append(rel)

    # pass2: front-matter 派生边（经 id_to_path 解析）
    for rel, node in nodes.items():
        meta_path_pairs: list[tuple[str, str]] = []  # (ref_value, relation_type)
        if node.type == "Task":
            # 重新读 meta 取 ref（轻量：node 未存 raw ref，这里从 group 重建亦可；改用重新解析）
            fm_text, _ = split_front_matter((assets_root / rel).read_text(encoding="utf-8"))
            ref = parse_front_matter(fm_text).get("ref")
            if ref:
                meta_path_pairs.append((ref, "ref_command"))
        if node.type == "Feature":
            fm_text, _ = split_front_matter((assets_root / rel).read_text(encoding="utf-8"))
            parent = parse_front_matter(fm_text).get("parent_feature_code")
            if parent:
                # parent_feature_code 不是完整 id，拼成 Feature id 查 id_to_path
                pid = f"{node.nf}@{node.version}@Feature@{parent}"
                meta_path_pairs.append((pid, "parent"))
        for ref_value, rel_type in meta_path_pairs:
            tgt_path = id_to_path.get(ref_value)
            key = (tgt_path or ref_value, rel_type)
            existing = {(e.dst, e.relation_type) for e in out_edges[rel]}
            if key in existing:
                continue
            if tgt_path:
                out_edges[rel].append(Edge(src=rel, dst=tgt_path, relation_type=rel_type, resolved=True))
                reverse[tgt_path].append(rel)

    return Index(
        nodes=nodes,
        id_to_path=id_to_path,
        out_edges={k: tuple(v) for k, v in out_edges.items()},
        reverse={k: tuple(v) for k, v in reverse.items()},
    )


def _infer_type_from_path(rel: str) -> str:
    top = rel.split("/", 1)[0]
    return {
        "command": "MMLCommand",
        "configobject": "ConfigObject",
        "feature": "Feature",
        "license": "License",
        "task": "Task",
    }.get(top, top.capitalize())
```

- [ ] **Step 4: 运行确认通过**

Run: `cd platform-next && python -m pytest tests/wiki/test_build_index.py -v`
Expected: 6 passed。

- [ ] **Step 5: Commit**

```bash
git add platform-next/wiki/build_wiki_index.py platform-next/tests/wiki/test_build_index.py
git commit -m "feat(wiki): 索引构建器（两遍扫树 + front-matter 派生边 + 反链）"
```

---

### Task 4: builder 序列化 + CLI（写/读 JSON）

**Files:**
- Modify: `platform-next/wiki/build_wiki_index.py`（追加 serialize/deserialize/main）
- Modify: `platform-next/tests/wiki/test_build_index.py`（追加 round-trip 测试）

- [ ] **Step 1: 追加失败测试**

```python
# 追加到 test_build_index.py
import json
from wiki.build_wiki_index import build_index, serialize_index, deserialize_index


def test_serialize_roundtrip(sample_assets, tmp_path):
    idx = build_index(sample_assets)
    out = tmp_path / "idx.json"
    out.write_text(serialize_index(idx), encoding="utf-8")
    idx2 = deserialize_index(out.read_text(encoding="utf-8"))
    assert set(idx2.nodes) == set(idx.nodes)
    assert idx2.id_to_path == idx.id_to_path
```

- [ ] **Step 2: 实现 serialize/deserialize/main（追加到 build_wiki_index.py）**

```python
import json
import sys


def _node_to_dict(n: Node) -> dict:
    return {
        "path": n.path, "id": n.id, "type": n.type, "name": n.name,
        "nf": n.nf, "version": n.version, "status": n.status,
        "title": n.title, "group": [list(p) for p in n.group],
    }


def _edge_to_dict(e: Edge) -> dict:
    return {"from": e.src, "to": e.dst, "relation_type": e.relation_type, "resolved": e.resolved}


def serialize_index(idx: Index) -> str:
    payload = {
        "nodes": {p: _node_to_dict(n) for p, n in idx.nodes.items()},
        "edges": [_edge_to_dict(e) for edges in idx.out_edges.values() for e in edges],
        "reverse": dict(idx.reverse),
        "id_to_path": dict(idx.id_to_path),
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def deserialize_index(text: str) -> Index:
    d = json.loads(text)
    nodes = {p: Node(
        path=n["path"], id=n["id"], type=n["type"], name=n["name"],
        nf=n["nf"], version=n["version"], status=n["status"],
        title=n["title"], group=tuple(tuple(p) for p in n["group"]),
    ) for p, n in d["nodes"].items()}
    out_edges: dict[str, list[Edge]] = defaultdict(list)
    for e in d["edges"]:
        out_edges[e["from"]].append(Edge(src=e["from"], dst=e["to"], relation_type=e["relation_type"], resolved=e["resolved"]))
    return Index(
        nodes=nodes,
        id_to_path=d["id_to_path"],
        out_edges={k: tuple(v) for k, v in out_edges.items()},
        reverse={k: tuple(v) for k, v in d["reverse"].items()},
    )


def main(argv: list[str] | None = None) -> int:
    """CLI: python -m wiki.build_wiki_index <assets_root> <out_json>"""
    argv = argv or sys.argv[1:]
    if len(argv) < 2:
        print("usage: build_wiki_index <assets_root> <out_json>", file=sys.stderr)
        return 2
    assets_root = Path(argv[0])
    out = Path(argv[1])
    idx = build_index(assets_root)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(serialize_index(idx), encoding="utf-8")
    print(f"indexed {len(idx.nodes)} nodes -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 3: 运行测试**

Run: `cd platform-next && python -m pytest tests/wiki/test_build_index.py -v`
Expected: 7 passed。

- [ ] **Step 4: 手动验证 CLI 跑通真实 assets/**

Run: `cd platform-next && python -m wiki.build_wiki_index ../assets wiki/data/wiki_index.json`
Expected: 打印 `indexed NNNNN nodes -> wiki/data/wiki_index.json`（N 应为 2 万+）。

- [ ] **Step 5: 排除生成物 —— 新建 `platform-next/wiki/data/.gitignore`**

```
wiki_index.json
```
并 `touch platform-next/wiki/data/.gitkeep`。

- [ ] **Step 6: Commit**

```bash
git add platform-next/wiki/build_wiki_index.py platform-next/tests/wiki/test_build_index.py platform-next/wiki/data/
git commit -m "feat(wiki): 索引序列化 + CLI（写读 JSON，跑通真实 assets 2万+）"
```

---

## Chunk 2: 后端 service + router + 集成

### Task 5: service —— 载入索引 + 查询方法

**Files:**
- Create: `platform-next/wiki/service.py`
- Create: `platform-next/tests/wiki/test_service.py`

- [ ] **Step 1: 写失败测试**

```python
# platform-next/tests/wiki/test_service.py
from pathlib import Path
from wiki.service import WikiService


def _svc(sample_assets: Path, tmp_path: Path) -> WikiService:
    return WikiService(assets_root=sample_assets, index_path=tmp_path / "idx.json")


def test_categories(sample_assets, tmp_path):
    s = _svc(sample_assets, tmp_path)
    cats = s.categories()
    types = {c["type"] for c in cats}
    assert {"MMLCommand", "ConfigObject", "Task"} <= types


def test_group_command_by_category_path(sample_assets, tmp_path):
    s = _svc(sample_assets, tmp_path)
    groups = s.group("MMLCommand", "UDG", "20.15.2")
    keys = {g["key"] for g in groups}
    assert "用户面服务管理/计费控制" in keys


def test_list_in_bucket(sample_assets, tmp_path):
    s = _svc(sample_assets, tmp_path)
    res = s.list_objs("MMLCommand", "UDG", "20.15.2", group_field="category_path", group_value="用户面服务管理/计费控制")
    assert any(i["path"] == "command/UDG/20.15.2/ADD-URR.md" for i in res["items"])


def test_neighborhood_out_and_reverse(sample_assets, tmp_path):
    s = _svc(sample_assets, tmp_path)
    nb = s.neighborhood("command/UDG/20.15.2/ADD-URR.md")
    paths = {n["path"] for n in nb["nodes"] if n.get("path")}
    # 出向：URR 配置对象、0-00001 任务
    assert "configobject/UDG/20.15.2/URR.md" in paths
    assert "task/UDG/20.15.2/0-00001.md" in paths
    assert nb["center"]["path"] == "command/UDG/20.15.2/ADD-URR.md"


def test_neighborhood_placeholder_node(sample_assets, tmp_path):
    s = _svc(sample_assets, tmp_path)
    nb = s.neighborhood("task/UDG/20.15.2/0-00001.md")
    unresolved = [n for n in nb["nodes"] if not n.get("resolved", True)]
    assert any("URRGROUP" in n["name"] for n in unresolved)


def test_search(sample_assets, tmp_path):
    s = _svc(sample_assets, tmp_path)
    res = s.search("URR")
    assert any(r["path"] == "command/UDG/20.15.2/ADD-URR.md" for r in res)
```

- [ ] **Step 2: 运行确认失败**

Run: `cd platform-next && python -m pytest tests/wiki/test_service.py -v`
Expected: FAIL（`WikiService` 未定义）。

- [ ] **Step 3: 实现 service.py**

```python
"""wiki 查询服务：载入/构建索引到内存，提供 categories/group/list/neighborhood/md/search。

启动时若 index_path 不存在或 stale（mtime < assets 最新 mtime），自动重建。
"""
from __future__ import annotations
from pathlib import Path

from wiki.build_wiki_index import build_index, deserialize_index, serialize_index
from wiki.models import Index
from wiki.parser import object_type_of

# 分组字段（每类一个主字段）
_GROUP_FIELD = {
    "MMLCommand": "category_path",
    "ConfigObject": "object_kind",
    "Feature": "parent_feature_code",
    "License": "applicable_nf",
    "Task": "task_layer",
}


class WikiService:
    def __init__(self, assets_root: Path, index_path: Path) -> None:
        self.assets_root = Path(assets_root).resolve()
        self.index_path = Path(index_path)
        self._index: Index | None = None

    @property
    def index(self) -> Index:
        if self._index is None or self._is_stale():
            self._index = self._load_or_build()
        return self._index

    def _is_stale(self) -> bool:
        if not self.index_path.exists():
            return True
        idx_mtime = self.index_path.stat().st_mtime
        # 取 assets 最新文件 mtime（rglob 较重，仅在没有缓存时触发；命中即短路）
        try:
            newest = max(f.stat().st_mtime for f in self.assets_root.rglob("*.md"))
        except ValueError:
            newest = 0
        return idx_mtime + 1 < newest  # 1s grace，避免刚写完索引即判 stale 冗余重建

    def _load_or_build(self) -> Index:
        if self.index_path.exists() and not self._index is None and not self._is_stale():
            return deserialize_index(self.index_path.read_text(encoding="utf-8"))
        idx = build_index(self.assets_root)
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        self.index_path.write_text(serialize_index(idx), encoding="utf-8")
        return idx

    # ---- 查询 ----

    def categories(self) -> list[dict]:
        agg: dict[str, dict[str, dict[str, int]]] = {}
        for n in self.index.nodes.values():
            if not n.nf or not n.version:
                continue
            agg.setdefault(n.type, {}).setdefault(n.nf, {}).setdefault(n.version, 0)
            agg[n.type][n.nf][n.version] += 1
        return [
            {"type": t, "nfs": [{"nf": nf, "versions": [{"version": v, "count": c for v, c in vers.items()}]}
                                for nf, vers in nfs.items()]}
            for t, nfs in agg.items()
        ]

    def group(self, ntype: str, nf: str, version: str) -> list[dict]:
        field = _GROUP_FIELD.get(ntype, "")
        buckets: dict[str, int] = {}
        for n in self.index.nodes.values():
            if n.type != ntype or n.nf != nf or n.version != version:
                continue
            val = dict(n.group).get(field, "(未分组)")
            buckets[val] = buckets.get(val, 0) + 1
        return [{"key": k, "count": v} for k, v in sorted(buckets.items(), key=lambda x: -x[1])]

    def list_objs(self, ntype: str, nf: str, version: str,
                  group_field: str | None = None, group_value: str | None = None,
                  q: str | None = None, page: int = 1, size: int = 100) -> dict:
        items = []
        for n in self.index.nodes.values():
            if n.type != ntype or n.nf != nf or n.version != version:
                continue
            if group_field and group_value:
                if dict(n.group).get(group_field) != group_value:
                    continue
            if q and q.lower() not in (n.name + n.title + n.id).lower():
                continue
            items.append({"path": n.path, "name": n.name, "id": n.id, "title": n.title})
        items.sort(key=lambda x: x["name"])
        total = len(items)
        start = (page - 1) * size
        return {"items": items[start:start + size], "total": total, "page": page, "size": size}

    def _node_dict(self, path: str | None, obj_id: str | None, resolved: bool) -> dict:
        if path and path in self.index.nodes:
            n = self.index.nodes[path]
            return {"path": n.path, "id": n.id, "type": n.type, "name": n.name,
                    "nf": n.nf, "version": n.version, "title": n.title, "resolved": True}
        return {"path": None, "id": obj_id or "", "type": object_type_of(obj_id or ""),
                "name": (obj_id or "").split("@")[-1], "resolved": resolved}

    def neighborhood(self, path: str, depth: int = 1) -> dict:
        idx = self.index
        center = idx.nodes.get(path)
        if not center:
            return {"center": None, "nodes": [], "edges": []}
        nodes: dict[str, dict] = {path: self._node_dict(path, center.id, True)}
        edges: list[dict] = []
        # 出向
        for e in idx.out_edges.get(path, ()):
            tgt_path = e.dst if e.resolved else None
            nodes.setdefault(e.dst, self._node_dict(tgt_path, e.dst if not e.resolved else idx.nodes.get(e.dst, type("x", (), {"id": ""})).id, e.resolved))
            edges.append({"from": e.src, "to": e.dst, "relation_type": e.relation_type, "resolved": e.resolved})
        # 反链
        for src in idx.reverse.get(path, ()):
            sn = idx.nodes.get(src)
            nodes.setdefault(src, self._node_dict(src, sn.id if sn else "", True))
            # 反链边：从 src 指向 center
            src_edges = {(ee.dst, ee.relation_type) for ee in idx.out_edges.get(src, ())}
            rel = next((r for (d, r) in src_edges if d == path), "related")
            edges.append({"from": src, "to": path, "relation_type": rel, "resolved": True})
        return {
            "center": self._node_dict(path, center.id, True),
            "nodes": list(nodes.values()),
            "edges": edges,
        }

    def md(self, path: str) -> dict | None:
        full = (self.assets_root / path).resolve()
        try:
            full.relative_to(self.assets_root)  # 路径穿越防护
        except ValueError:
            return None
        if not full.is_file() or full.suffix != ".md":
            return None
        n = self.index.nodes.get(path.replace("\\", "/"))
        return {"path": path, "content": full.read_text(encoding="utf-8"),
                "meta": {"type": n.type if n else None, "name": n.name if n else None,
                         "title": n.title if n else None}}

    def search(self, q: str, limit: int = 30) -> list[dict]:
        ql = q.lower()
        out = []
        for n in self.index.nodes.values():
            if ql in (n.name + " " + n.title + " " + n.id).lower():
                out.append({"path": n.path, "type": n.type, "name": n.name, "title": n.title})
                if len(out) >= limit:
                    break
        return out


# 单例（router 用）
_SERVICE: WikiService | None = None


def get_service() -> WikiService:
    global _SERVICE
    if _SERVICE is None:
        from shared.config import get_config
        cfg = get_config().get("wiki", {})
        root = Path(cfg.get("assets_root", "../assets"))
        if not root.is_absolute():
            root = Path(__file__).resolve().parent.parent / root
        idx = Path(__file__).resolve().parent / "data" / "wiki_index.json"
        _SERVICE = WikiService(root, idx)
    return _SERVICE
```

- [ ] **Step 4: 修正 neighborhood 的占位节点构造（简化）**

`neighborhood` 里出向占位节点的构造写得绕，替换出向循环体为更清晰版本：

```python
        for e in idx.out_edges.get(path, ()):
            if e.resolved and e.dst in idx.nodes:
                nodes.setdefault(e.dst, self._node_dict(e.dst, idx.nodes[e.dst].id, True))
            else:
                nodes.setdefault(e.dst, self._node_dict(None, e.dst, e.resolved))
            edges.append({"from": e.src, "to": e.dst, "relation_type": e.relation_type, "resolved": e.resolved})
```

- [ ] **Step 5: 运行确认通过**

Run: `cd platform-next && python -m pytest tests/wiki/test_service.py -v`
Expected: 6 passed。

- [ ] **Step 6: Commit**

```bash
git add platform-next/wiki/service.py platform-next/tests/wiki/test_service.py
git commit -m "feat(wiki): 查询服务（categories/group/list/neighborhood/md/search + 路径穿越防护）"
```

---

### Task 6: router + main.py 集成

**Files:**
- Create: `platform-next/wiki/router.py`
- Create: `platform-next/tests/wiki/test_router.py`
- Modify: `platform-next/main.py`

- [ ] **Step 1: 写失败测试（FastAPI TestClient）**

```python
# platform-next/tests/wiki/test_router.py
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from wiki.router import router
from wiki.service import WikiService


@pytest.fixture
def client(sample_assets, tmp_path, monkeypatch):
    svc = WikiService(sample_assets, tmp_path / "idx.json")
    monkeypatch.setattr("wiki.router.get_service", lambda: svc)
    app = FastAPI()
    app.include_router(router)
    return TestClient(app)


def test_categories_endpoint(client):
    r = client.get("/api/v1/wiki/categories")
    assert r.status_code == 200
    types = {c["type"] for c in r.json()}
    assert "MMLCommand" in types


def test_neighborhood_endpoint(client):
    r = client.get("/api/v1/wiki/neighborhood", params={"path": "command/UDG/20.15.2/ADD-URR.md"})
    assert r.status_code == 200
    data = r.json()
    assert data["center"]["path"] == "command/UDG/20.15.2/ADD-URR.md"


def test_md_endpoint(client):
    r = client.get("/api/v1/wiki/md", params={"path": "command/UDG/20.15.2/ADD-URR.md"})
    assert r.status_code == 200
    assert "ADD URR" in r.json()["content"]


def test_md_traversal_blocked(client):
    r = client.get("/api/v1/wiki/md", params={"path": "../../../etc/passwd"})
    assert r.status_code == 404


def test_md_unknown_returns_404(client):
    r = client.get("/api/v1/wiki/md", params={"path": "nope/missing.md"})
    assert r.status_code == 404
```

- [ ] **Step 2: 运行确认失败**

Run: `cd platform-next && python -m pytest tests/wiki/test_router.py -v`
Expected: FAIL。

- [ ] **Step 3: 实现 router.py**

```python
"""wiki API 路由：/api/v1/wiki/*"""
from fastapi import APIRouter, HTTPException, Query

from wiki.service import get_service

router = APIRouter(prefix="/api/v1/wiki", tags=["wiki"])


@router.get("/categories")
def categories():
    return get_service().categories()


@router.get("/group")
def group(type: str, nf: str, version: str):
    return get_service().group(type, nf, version)


@router.get("/list")
def list_objs(
    type: str, nf: str, version: str,
    group_field: str | None = None, group_value: str | None = None,
    q: str | None = None, page: int = Query(1, ge=1), size: int = Query(100, ge=1, le=500),
):
    return get_service().list_objs(type, nf, version, group_field, group_value, q, page, size)


@router.get("/neighborhood")
def neighborhood(path: str, depth: int = 1):
    nb = get_service().neighborhood(path, depth)
    if nb["center"] is None:
        raise HTTPException(status_code=404, detail="object not found")
    return nb


@router.get("/md")
def md(path: str):
    res = get_service().md(path)
    if res is None:
        raise HTTPException(status_code=404, detail="md not found")
    return res


@router.get("/search")
def search(q: str, limit: int = Query(30, ge=1, le=100)):
    return get_service().search(q, limit)
```

- [ ] **Step 4: 运行确认通过**

Run: `cd platform-next && python -m pytest tests/wiki/test_router.py -v`
Expected: 5 passed。

- [ ] **Step 5: main.py 集成**

在 `platform-next/main.py`：
- import 加 `from wiki.router import router as wiki_router`
- `app.include_router(...)` 区块加 `app.include_router(wiki_router)`

（索引载入是惰性的（service 首次访问触发），lifespan 无需额外动作。）

- [ ] **Step 6: 启动冒烟**

Run: `cd platform-next && python -c "from main import app; print('ok', [r.path for r in app.routes if 'wiki' in getattr(r,'path','')])"`
Expected: 打印 `ok ['/api/v1/wiki/categories', ... ]`（6 条）。

- [ ] **Step 7: Commit**

```bash
git add platform-next/wiki/router.py platform-next/tests/wiki/test_router.py platform-next/main.py
git commit -m "feat(wiki): API 路由 + main.py 集成（6 端点，含路径穿越防护）"
```

---

### Task 7: 跑通真实 assets 全量 + 后端整体回归

- [ ] **Step 1: 删除旧索引（若有）强制重建**

Run: `rm -f platform-next/wiki/data/wiki_index.json`

- [ ] **Step 2: 启动服务触发首建（后台），确认无异常**

Run: `cd platform-next && python main.py` （观察启动日志，后台进程；几秒后 Ctrl-C 或后台跑）
Expected: 启动正常。另开终端验证：`curl -s "http://localhost:8000/api/v1/wiki/categories" | head -c 300` 返回 JSON。

- [ ] **Step 3: 全量后端测试回归**

Run: `cd platform-next && python -m pytest tests/wiki/ -v`
Expected: 全绿。

- [ ] **Step 4: Commit（如有 data/.gitkeep 调整）**

```bash
git add -A platform-next/wiki/data/
git commit -m "chore(wiki): 真实 assets 全量索引回归通过" || echo "nothing to commit"
```

---

## Chunk 3: 前端三栏

> 前端无测试框架。每个 Task 末尾 `npm run build`（vue-tsc 类型检查）必须过 + 浏览器人工验证。
> 复用现有模式：`frontend/src/shared/DocViewer.vue`（md 渲染+链接拦截）、`frontend/src/command_graph/CommandGraph.vue`（vis-network）、`frontend/src/api.ts`（api 工厂）。

### Task 8: 路由 + TopBar tab + wikiApi（骨架可达）

**Files:**
- Create: `frontend/src/wiki/wikiApi.ts`
- Create: `frontend/src/wiki/WikiIndex.vue`（先占位）
- Modify: `frontend/src/router.ts`
- Modify: `frontend/src/shared/TopBar.vue`

- [ ] **Step 1: wikiApi.ts**

```typescript
// frontend/src/wiki/wikiApi.ts
const BASE = '/api/v1/wiki'

async function fetchJson<T>(url: string): Promise<T> {
  const r = await fetch(url)
  if (!r.ok) throw new Error(`${r.status} ${url}`)
  return (await r.json()) as T
}

export interface CategoryNf { nf: string; versions: { version: string; count: number }[] }
export interface Category { type: string; nfs: CategoryNf[] }
export interface GroupBucket { key: string; count: number }
export interface ListItem { path: string; name: string; id: string; title: string }
export interface NbNode {
  path: string | null; id: string; type: string; name: string
  nf?: string; version?: string; title?: string; resolved: boolean
}
export interface NbEdge { from: string; to: string; relation_type: string; resolved: boolean }
export interface Neighborhood { center: NbNode | null; nodes: NbNode[]; edges: NbEdge[] }
export interface MdResp { path: string; content: string; meta: { type?: string; name?: string; title?: string } }

export const wikiApi = {
  categories: () => fetchJson<Category[]>(`${BASE}/categories`),
  group: (type: string, nf: string, version: string) =>
    fetchJson<GroupBucket[]>(`${BASE}/group?type=${type}&nf=${nf}&version=${version}`),
  list: (p: { type: string; nf: string; version: string; group_field?: string; group_value?: string; q?: string; page?: number; size?: number }) => {
    const qs = new URLSearchParams({ type: p.type, nf: p.nf, version: p.version })
    if (p.group_field) qs.set('group_field', p.group_field)
    if (p.group_value) qs.set('group_value', p.group_value)
    if (p.q) qs.set('q', p.q)
    qs.set('page', String(p.page ?? 1)); qs.set('size', String(p.size ?? 100))
    return fetchJson<{ items: ListItem[]; total: number }>(`${BASE}/list?${qs}`)
  },
  neighborhood: (path: string) =>
    fetchJson<Neighborhood>(`${BASE}/neighborhood?path=${encodeURIComponent(path)}`),
  md: (path: string) => fetchJson<MdResp>(`${BASE}/md?path=${encodeURIComponent(path)}`),
  search: (q: string) => fetchJson<ListItem[]>(`${BASE}/search?q=${encodeURIComponent(q)}`),
}
```

- [ ] **Step 2: 占位 WikiIndex.vue**

```vue
<template>
  <div class="wiki-shell">
    <aside class="wiki-left">左树（待建）</aside>
    <section class="wiki-center">中区（待建）</section>
    <aside class="wiki-right">图谱（待建）</aside>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.wiki-shell { display: grid; grid-template-columns: 280px 1fr 1fr; height: calc(100vh - var(--navbar-height)); }
.wiki-left, .wiki-right { border-right: 1px solid var(--border); overflow: auto; padding: 12px; }
.wiki-center { overflow: auto; padding: 16px 24px; }
</style>
```

- [ ] **Step 3: router.ts 加两条路由**

在 `routes` 数组中（`business-graph` 之后）追加：
```typescript
    {
      path: '/graph-overview',
      component: () => import('./wiki/WikiIndex.vue'),
    },
    {
      path: '/graph-overview/a/:path(.*)',
      name: 'graph-overview-asset',
      component: () => import('./wiki/WikiIndex.vue'),
    },
```

- [ ] **Step 4: TopBar.vue 加链接**

在 `<div class="topbar-nav">` 内，`业务图谱` 之后加：
```html
      <router-link to="/graph-overview">图谱总览</router-link>
```

- [ ] **Step 5: 类型检查 + 浏览器冒烟**

Run: `cd platform-next/frontend && npm run build`
Expected: vue-tsc 通过、构建成功。

浏览器：访问 `/graph-overview`，应见三栏占位 + TopBar 出现「图谱总览」。

- [ ] **Step 6: Commit**

```bash
git add platform-next/frontend/src/wiki/ platform-next/frontend/src/router.ts platform-next/frontend/src/shared/TopBar.vue
git commit -m "feat(wiki-ui): 路由 + TopBar tab + api 工厂 + 三栏骨架"
```

---

### Task 9: CategoryTree.vue（左栏分类树，懒加载 + 桶内搜索）

**Files:**
- Create: `frontend/src/wiki/CategoryTree.vue`
- Modify: `frontend/src/wiki/WikiIndex.vue`（挂载 + 选中事件）

- [ ] **Step 1: CategoryTree.vue**

```vue
<template>
  <div class="cat-tree">
    <el-input v-model="searchQ" size="small" placeholder="搜索对象名/id…" clearable
              @keyup.enter="runSearch" @clear="clearSearch" class="cat-search">
      <template #append><el-button @click="runSearch">搜</el-button></template>
    </el-input>

    <el-tree v-if="!searchMode" :data="treeData" :props="treeProps" lazy node-key="key"
             @node-expand="onExpand" :load="loadLazy" highlight-current
             @node-click="onNodeClick" ref="treeRef" />
    <div v-else class="cat-search-result">
      <div v-if="!searchHits.length" class="cat-empty">无匹配</div>
      <div v-for="h in searchHits" :key="h.path" class="cat-hit" @click="$emit('select', h.path)">
        <span class="cat-hit-type">[{{ h.type }}]</span> {{ h.name }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { wikiApi, type Category, type ListItem } from './wikiApi'

const emit = defineEmits<{ (e: 'select', path: string): void }>()

const searchQ = ref('')
const searchMode = ref(false)
const searchHits = ref<ListItem[]>([])
const treeData = ref<any[]>([])
const treeRef = ref<any>(null)
const treeProps = { label: 'label', isLeaf: 'leaf' }

const TYPE_LABEL: Record<string, string> = {
  MMLCommand: '命令', ConfigObject: '配置对象', Feature: '特性',
  License: 'License', Task: '任务', BusinessDomain: '业务层',
}
const GROUP_FIELD: Record<string, string> = {
  MMLCommand: 'category_path', ConfigObject: 'object_kind',
  Feature: 'parent_feature_code', License: 'applicable_nf', Task: 'task_layer',
}

onMounted(async () => {
  const cats = await wikiApi.categories()
  treeData.value = cats.map((c: Category) => ({
    key: `t:${c.type}`, label: `${TYPE_LABEL[c.type] ?? c.type}`, type: 'type',
    raw: c, children: c.nfs.map(n => ({
      key: `n:${c.type}:${n.nf}`, label: n.nf, type: 'nf',
      raw: { type: c.type, nf: n.nf, versions: n.versions }, leaf: false,
    })),
  }))
})

async function loadLazy(node: any, resolve: (data: any[]) => void) {
  const data = node.data?.raw
  // nf -> version 列表
  if (node.data?.type === 'nf') {
    resolve(data.versions.map((v: any) => ({
      key: `v:${data.type}:${data.nf}:${v.version}`, label: v.version, type: 'version',
      raw: { type: data.type, nf: data.nf, version: v.version, count: v.count }, leaf: false,
    })))
    return
  }
  // version -> 分组桶（懒加载调 /group）
  if (node.data?.type === 'version') {
    const buckets = await wikiApi.group(data.type, data.nf, data.version)
    resolve(buckets.map(b => ({
      key: `g:${data.type}:${data.nf}:${data.version}:${b.key}`, label: `${b.key} (${b.count})`,
      type: 'group', raw: { ...data, group_field: GROUP_FIELD[data.type], group_value: b.key }, leaf: false,
    })))
    return
  }
  // group -> 对象叶子（懒加载调 /list）
  if (node.data?.type === 'group') {
    const res = await wikiApi.list({ type: data.type, nf: data.nf, version: data.version,
      group_field: data.group_field, group_value: data.group_value, size: 500 })
    resolve(res.items.map(it => ({ key: `o:${it.path}`, label: it.name, type: 'object', raw: it, leaf: true })))
    return
  }
  resolve([])
}

function onExpand(_n: any, _info: any) {}
function onNodeClick(node: any) { if (node.type === 'object') emit('select', node.raw.path) }

async function runSearch() {
  if (!searchQ.value.trim()) return
  searchMode.value = true
  searchHits.value = await wikiApi.search(searchQ.value.trim())
}
function clearSearch() { searchMode.value = false; searchHits.value = [] }
</script>

<style scoped>
.cat-tree { display: flex; flex-direction: column; gap: 8px; }
.cat-search-result { display: flex; flex-direction: column; gap: 4px; }
.cat-hit { padding: 4px 6px; cursor: pointer; border-radius: 4px; font-size: 13px; }
.cat-hit:hover { background: var(--bg-hover, #f0f5ff); }
.cat-hit-type { color: #7c3aed; font-size: 11px; }
.cat-empty { color: var(--text-tertiary); font-size: 13px; padding: 8px; }
</style>
```

- [ ] **Step 2: WikiIndex.vue 挂载 + 选中跳转**

```vue
<template>
  <div class="wiki-shell">
    <aside class="wiki-left"><CategoryTree @select="go" /></aside>
    <section class="wiki-center">中区（待 Task 10）</section>
    <aside class="wiki-right">图谱（待 Task 11）</aside>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import CategoryTree from './CategoryTree.vue'
const router = useRouter()
function go(path: string) { router.push(`/graph-overview/a/${path}`) }
</script>

<style scoped>
.wiki-shell { display: grid; grid-template-columns: 300px 1fr 1fr; height: calc(100vh - var(--navbar-height)); }
.wiki-left { border-right: 1px solid var(--border); overflow: auto; padding: 10px; }
.wiki-center { overflow: auto; padding: 16px 24px; }
.wiki-right { border-left: 1px solid var(--border); overflow: hidden; padding: 10px; }
</style>
```

- [ ] **Step 3: 类型检查 + 浏览器验证**

Run: `cd platform-next/frontend && npm run build`
浏览器：`/graph-overview` 左树展开 命令→UDG→20.15.2→分组桶→对象，点对象 URL 变为 `/graph-overview/a/command/...`（中区暂占位）。

- [ ] **Step 4: Commit**

```bash
git add platform-next/frontend/src/wiki/CategoryTree.vue platform-next/frontend/src/wiki/WikiIndex.vue
git commit -m "feat(wiki-ui): 左栏分类树（懒加载 + 桶内搜索 + 选中跳转）"
```

---

### Task 10: MdPane.vue（中区，改造 DocViewer 链接拦截 → assets 根路径）

**Files:**
- Create: `frontend/src/wiki/MdPane.vue`
- Modify: `frontend/src/wiki/WikiIndex.vue`（挂载 MdPane + 取数）

> 关键：assets/ 链接已是 assets 根相对（CLAUDE.md §5.5，禁 `../`），无需 DocViewer 的 `..` 解析。直接把 href 当路径 push。

- [ ] **Step 1: MdPane.vue**

```vue
<template>
  <div v-if="loading" v-loading="true" class="md-pane md-pane-loading"></div>
  <div v-else-if="error" class="md-pane md-pane-empty">该页加载失败：{{ error }}</div>
  <div v-else-if="!content" class="md-pane md-pane-empty">
    图谱总览 · 在左侧选择对象，或在任意 md / 图谱节点间点击跳转。
  </div>
  <div v-else class="md-pane md-pane-doc" v-html="rendered" @click="handleClick" ref="docRef"></div>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue'
import MarkdownIt from 'markdown-it'
import DOMPurify from 'dompurify'
import { wikiApi } from './wikiApi'

const props = defineProps<{ path: string | null }>()
const emit = defineEmits<{ (e: 'navigate', path: string): void }>()

const content = ref('')
const meta = ref<{ type?: string; name?: string; title?: string }>({})
const loading = ref(false)
const error = ref('')

const md = new MarkdownIt({ html: true, linkify: true, breaks: true })

const rendered = computed(() => {
  if (!content.value) return ''
  // assets 根相对链接 → 拦截为 #md-ref: 占位；[[ID]] 占位 → 灰 chip
  let src = content.value
  src = src.replace(/\[\[([^\]]+)\]\]/g, (_m, id) =>
    `<span class="md-placeholder" title="未构建：${id}">${id}</span>`)
  src = src.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '[_img_]')  // 简化：暂不渲染图（evidence/无图）
  src = src.replace(/\[([^\]]+)\]\(([^)\s]+?)(?:\s+"[^"]*")?\)/g, (m, text, href) => {
    if (!href.endsWith('.md')) return m
    return `[${text}](#md-ref:${encodeURIComponent(href)})`
  })
  return DOMPurify.sanitize(md.render(src), { ADD_ATTR: ['target'] })
})

async function load() {
  if (!props.path) { content.value = ''; return }
  loading.value = true; error.value = ''
  try {
    const res = await wikiApi.md(props.path)
    content.value = res.content; meta.value = res.meta
  } catch (e: any) {
    content.value = ''; error.value = e.message || '未知错误'
  } finally { loading.value = false }
}

watch(() => props.path, load, { immediate: true })

function handleClick(ev: MouseEvent) {
  const a = (ev.target as HTMLElement).closest('a') as HTMLAnchorElement | null
  if (!a) return
  const href = a.getAttribute('href') || ''
  if (href.startsWith('#md-ref:')) {
    ev.preventDefault()
    emit('navigate', decodeURIComponent(href.substring('#md-ref:'.length)))
  }
}
</script>

<style scoped>
.md-pane { min-height: 200px; }
.md-pane-loading { height: 400px; }
.md-pane-empty { color: var(--text-tertiary); padding: 60px 20px; text-align: center; }
.md-pane-doc :deep(.md-placeholder) { color: #94a3b8; background: #f1f5f9; padding: 0 4px; border-radius: 3px; font-family: monospace; font-size: 0.9em; }
.md-pane-doc :deep(h1) { font-size: 1.5rem; margin: 0 0 12px; }
.md-pane-doc :deep(h2) { font-size: 1.15rem; margin: 20px 0 8px; border-bottom: 1px solid var(--border); padding-bottom: 4px; }
.md-pane-doc :deep(table) { border-collapse: collapse; width: 100%; margin: 8px 0; }
.md-pane-doc :deep(th), .md-pane-doc :deep(td) { border: 1px solid var(--border); padding: 6px 8px; vertical-align: top; }
.md-pane-doc :deep(a) { color: #0891b2; cursor: pointer; }
</style>
```

- [ ] **Step 2: WikiIndex.vue 挂 MdPane + 传当前 path**

把中区改为：
```vue
    <section class="wiki-center">
      <MdPane :path="currentPath" @navigate="go" />
    </section>
```
script 加：
```typescript
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import MdPane from './MdPane.vue'
const route = useRoute()
const currentPath = computed(() => {
  const p = route.params.path
  return Array.isArray(p) ? p.join('/') : (p || null)
})
```
（`go` 已存在。）

- [ ] **Step 3: 类型检查 + 浏览器验证**

Run: `cd platform-next/frontend && npm run build`
浏览器：左树点 `ADD URR` → 中区渲染命令 md；点文中 `[URR](...)` 链接 → URL 变为 configobject/.../URR.md，中区换文；`[[...]]` 显示为灰 chip。

- [ ] **Step 4: Commit**

```bash
git add platform-next/frontend/src/wiki/MdPane.vue platform-next/frontend/src/wiki/WikiIndex.vue
git commit -m "feat(wiki-ui): 中区 md 渲染 + 链接拦截跳转（assets 根路径，占位灰显）"
```

---

### Task 11: NeighborGraph.vue（右栏，改造 CommandGraph vis-network）

**Files:**
- Create: `frontend/src/wiki/NeighborGraph.vue`
- Modify: `frontend/src/wiki/WikiIndex.vue`（挂载）

- [ ] **Step 1: NeighborGraph.vue**

```vue
<template>
  <div class="nb-graph-wrap">
    <div v-if="loading" v-loading="true" class="nb-graph-canvas"></div>
    <div v-else-if="!centerPath" class="nb-empty">选择对象后展示其周围关系</div>
    <div v-else-if="empty" class="nb-empty">该对象无关系</div>
    <div v-show="!loading && centerPath && !empty" ref="containerRef" class="nb-graph-canvas"></div>
    <div class="nb-legend">点节点跳转 · 灰虚=未构建</div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, onBeforeUnmount, nextTick } from 'vue'
import { wikiApi, type NbNode, type NbEdge } from './wikiApi'

const props = defineProps<{ centerPath: string | null }>()
const emit = defineEmits<{ (e: 'navigate', path: string): void }>()

const loading = ref(false); const empty = ref(false)
const containerRef = ref<HTMLDivElement | null>(null)
let network: any = null; let ro: ResizeObserver | null = null

const NODE_COLOR: Record<string, any> = {
  MMLCommand: { bg: '#0891b2', bd: '#0e7490' }, ConfigObject: { bg: '#7c3aed', bd: '#6d28d9' },
  Feature: { bg: '#0d9488', bd: '#0f766e' }, License: { bg: '#ea580c', bd: '#c2410c' },
  Task: { bg: '#db2777', bd: '#be185d' },
}
const EDGE_COLOR: Record<string, string> = {
  operates_on: '#7c3aed', operated_by: '#7c3aed', requires_license: '#ea580c',
  parent: '#475569', child: '#475569', ref_command: '#db2777', has_task: '#db2777',
  evidenced_by: '#94a3b8', relates_to: '#64748b', related: '#cbd5e1',
}

async function load() {
  if (!props.centerPath) { empty.value = false; return }
  loading.value = true
  try {
    const nb = await wikiApi.neighborhood(props.centerPath)
    empty.value = (nb.nodes.length <= 1)
    await nextTick()
    render(nb.nodes, nb.edges, props.centerPath)
  } finally { loading.value = false }
}

function render(nodes: NbNode[], edges: NbEdge[], center: string) {
  if (!containerRef.value) return
  const vis: any = require('vis-network/standalone')  // 见 Step 2 说明，改 ESM import
}

watch(() => props.centerPath, load)
onMounted(() => { if (props.centerPath) load() })
onBeforeUnmount(() => { ro?.disconnect(); network?.destroy() })
</script>

<style scoped>
.nb-graph-wrap { height: 100%; display: flex; flex-direction: column; }
.nb-graph-canvas { flex: 1; min-height: 300px; background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); }
.nb-empty { color: var(--text-tertiary); padding: 60px 12px; text-align: center; font-size: 13px; }
.nb-legend { font-size: 11px; color: var(--text-tertiary); padding: 4px; }
</style>
```

- [ ] **Step 2: 修正 vis-network 导入与 render 实现**

`require` 不适用（ESM 项目）。参考 CommandGraph.vue 用动态 `import`。把 `render` 完整替换为：

```typescript
async function render(nodes: NbNode[], edges: NbEdge[], centerPath: string) {
  if (!containerRef.value) return
  const vis: any = await import('vis-network/standalone')
  const Network = vis.Network; const DataSet: any = vis.DataSet

  const visNodes = nodes.map(n => {
    const c = NODE_COLOR[n.type] || { bg: '#64748b', bd: '#475569' }
    const isCenter = n.path === centerPath
    return {
      id: n.path || n.id,
      label: n.name,
      title: n.id || n.name,
      shape: n.resolved ? 'box' : 'ellipse',
      color: { background: c.bg, border: c.bd, highlight: { background: c.bg, border: c.bd } },
      font: { color: '#fff', size: isCenter ? 14 : 12 },
      borderWidth: isCenter ? 3 : 1,
      dashes: !n.resolved,
      _path: n.path,  // 非_vis 字段，点击时取
    }
  })
  const visEdges = edges.map(e => ({
    from: e.from, to: e.to, arrows: 'to' as const,
    color: { color: EDGE_COLOR[e.relation_type] || '#cbd5e1' },
    label: e.relation_type, font: { size: 10, color: '#4b5563', strokeWidth: 3, strokeColor: '#fff', align: 'top' as const },
    smooth: { enabled: true, type: 'cubicBezier', forceDirection: 'none', roundness: 0.5 },
  }))

  network?.destroy()
  network = new Network(containerRef.value, { nodes: new DataSet(visNodes), edges: new DataSet(visEdges) }, {
    layout: { improvedLayout: true },
    physics: { enabled: true, barnesHut: { gravitationalConstant: -3000, centralGravity: 0.3, springLength: 80, springConstant: 0.04, damping: 0.4 }, stabilization: { iterations: 120, fit: true } },
    interaction: { dragNodes: true, dragView: true, zoomView: true, hover: true, tooltipDelay: 120 },
  })
  network.on('click', (params: any) => {
    const nodeId = params.nodes?.[0]
    if (nodeId == null) return
    const node = visNodes.find(n => n.id === nodeId)
    if (node && node._path) emit('navigate', node._path)  // 未解析节点无 path，不跳转
  })
  ro?.disconnect()
  if (typeof ResizeObserver !== 'undefined' && containerRef.value) {
    ro = new ResizeObserver(() => network?.redraw()); ro.observe(containerRef.value)
  }
}
```
并把 Step 1 模板里的 `render(nb.nodes, nb.edges, props.centerPath)` 保留（render 现在是 async，可 fire-and-forget）。删除 Step 1 中那个占位的 `render` stub。

- [ ] **Step 3: WikiIndex.vue 挂 NeighborGraph**

右栏改为：
```vue
    <aside class="wiki-right">
      <NeighborGraph :center-path="currentPath" @navigate="go" />
    </aside>
```
script 加 `import NeighborGraph from './NeighborGraph.vue'`。

- [ ] **Step 4: 类型检查 + 浏览器验证**

Run: `cd platform-next/frontend && npm run build`
浏览器：选中 `ADD URR` → 右栏以 ADD URR 为中心画 1 跳图（URR 紫菱形、0-00001 粉、边带类型标签）；点节点 → 跳转，图重画。

- [ ] **Step 5: Commit**

```bash
git add platform-next/frontend/src/wiki/NeighborGraph.vue platform-next/frontend/src/wiki/WikiIndex.vue
git commit -m "feat(wiki-ui): 右栏 1 跳邻域图谱（vis-network，节点跳转重画）"
```

---

### Task 12: 历史面包屑 + 空态/节点过多兜底 + 整体打磨

**Files:**
- Modify: `frontend/src/wiki/WikiIndex.vue`

- [ ] **Step 1: 加历史面包屑**

在 shell 顶部加一行（grid 改为带 header）。把之前 Task 9–11 里的 `go()` 替换为下面三个职责清晰的函数：**前进跳转入栈、面包屑回跳截断、URL 落地种子**。

```vue
<template>
  <div class="wiki-page">
    <div class="wiki-crumb">
      <span v-for="(h, i) in history" :key="i" class="wiki-crumb-item"
            :class="{ active: i === history.length - 1 }" @click="backTo(i)">
        {{ labelOf(h) }}<span v-if="i < history.length - 1"> ›</span>
      </span>
    </div>
    <div class="wiki-shell">
      <aside class="wiki-left"><CategoryTree @select="select" /></aside>
      <section class="wiki-center"><MdPane :path="currentPath" @navigate="select" /></section>
      <aside class="wiki-right"><NeighborGraph :center-path="currentPath" @navigate="select" /></aside>
    </div>
  </div>
</template>
```
script（`currentPath` 已在 Task 10 定义；`router` 已在 Task 9 引入）：
```typescript
import { ref, watch } from 'vue'
const history = ref<string[]>([])
function labelOf(p: string) { return decodeURIComponent(p).split('/').pop()?.replace(/\.md$/, '') || p }
function pushRoute(path: string) { router.push(`/graph-overview/a/${path}`) }
function select(path: string) {           // 前进跳转（左树/md 链接/图谱节点）
  history.value.push(path)
  pushRoute(path)
}
function backTo(index: number) {           // 面包屑回跳：截断历史到该处再跳
  history.value = history.value.slice(0, index + 1)
  pushRoute(history.value[index])
}
// 经 URL 直接落地（刷新/分享链接）时，若历史为空，用当前 path 做种子（避免 watch 重复入栈）
watch(currentPath, (p) => {
  if (p && history.value.length === 0) history.value = [p]
}, { immediate: true })
```
> 设计要点：历史栈只在 `select`（前进）和 `backTo`（截断）里显式维护；**不用 watch 把路由变化回灌进历史**（那会导致回跳时重复入栈）。浏览器前进/后退由 URL 驱动，与会话面包屑解耦。

样式追加：
```css
.wiki-page { display: flex; flex-direction: column; height: calc(100vh - var(--navbar-height)); }
.wiki-crumb { padding: 6px 16px; border-bottom: 1px solid var(--border); font-size: 13px; color: var(--text-tertiary); min-height: 30px; }
.wiki-crumb-item { cursor: pointer; }
.wiki-crumb-item.active { color: var(--text-primary); font-weight: 600; cursor: default; }
.wiki-shell { flex: 1; display: grid; grid-template-columns: 300px 1fr 1fr; min-height: 0; }
```
（`.wiki-shell` 的 `height` 改为 `flex:1; min-height:0`，让面包屑占顶。）

- [ ] **Step 2: 类型检查 + 全量浏览器验证（执行 spec §7 的 e2e 清单 1–10）**

Run: `cd platform-next/frontend && npm run build`
浏览器逐条核对：
1. `/graph-overview` 三栏 + 面包屑空。
2. 左树点命令 → 中区 md + 右栏图谱。
3. 中区点 `[URR](...)` → URL 变、中区换 URR、右栏重画以 URR 为中心。
4. 右栏点节点 → 同 3 效果。
5. 浏览器后退 → 回上一对象。
6. 面包屑点回跳。
7. `[[ID]]` 灰 chip（如任务 md）。
8. evidence 链接可打开。
9. business 类别：当前 P4 未建（0 节点），`/categories` 不返回该类、左树不显示——属预期（spec §6 的"待建"占位待 P4 有节点后自然出现，本次不硬编码空槽）。
10. 左树搜索框命中跳转。

- [ ] **Step 3: Commit**

```bash
git add platform-next/frontend/src/wiki/WikiIndex.vue
git commit -m "feat(wiki-ui): 历史面包屑回跳 + 整体打磨（e2e 清单通过）"
```

---

### Task 13: 收尾 —— README 说明 + 全量回归

- [ ] **Step 1: 全量后端 + 前端构建回归**

Run:
```bash
cd platform-next && python -m pytest tests/wiki/ -v
cd frontend && npm run build
```
Expected: pytest 全绿；vue-tsc + vite build 成功。

- [ ] **Step 2: 在 `platform-next/docs/` 加一页简短说明（可选）**

新建 `platform-next/docs/wiki-overview.md`：一段话说明「图谱总览」tab 用途 + 如何重建索引（`python -m wiki.build_wiki_index ../assets wiki/data/wiki_index.json`）。

- [ ] **Step 3: 最终 Commit**

```bash
git add platform-next/docs/wiki-overview.md
git commit -m "docs(wiki): 图谱总览使用说明" || echo "skipped"
```

---

## 验收（对照 spec §10）
- 「图谱总览」tab 可进，三栏布局正确。
- 任选 md：中区渲染 + 右栏 1 跳图谱（出向+反链、边按类型上色）。
- md 链接 / 图谱节点 / 左树叶子 / 搜索 四入口跳转一致，跳转后中区+右栏同步。
- URL 驱动：前进/后退/分享可用；面包屑回跳可用。
- `[[ID]]` 占位、evidence、空 business 按 spec §6 处理。
- 后端 pytest 全绿；路径穿越被拒。

## 风险与回退
- 索引首建 2 万+ 文件数秒；前端首屏左树 `/categories` 仅骨架，懒加载避免一次性拉全量。
- 关系类型推断覆盖不全 → builder 不阻断（未知小节归 `related`），后续按 Lint 迭代补 `_HEADING_RULES`。
- 出问题时回退单个 Task 的 commit（每 Task 独立提交）。
