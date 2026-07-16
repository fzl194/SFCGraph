# 图谱资产管理平台 v1 Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 一个独立平台：导入 md 资产包 → 按 frontmatter 自动归类合并进唯一统一资产库 → 通用解析（对象 + `## 边` wikilink 边 + 版本解析）→ 读 API（单对象/单跳）→ 三栏只读前端 → 可导出。

**Architecture:** Python FastAPI 单例 service + 内存索引（复用 platform-next 读模式）；纯文件目录统一资产库（遵循"三层图谱构建规范/command"约定）；Vue3+TS 三栏只读前端。资产格式以 command 规范为权威：ID 版本无关 3 段（NF）/ 2 段（跨 NF），版本只在目录与 frontmatter，边 = `## 边` wikilink。

**Tech Stack:** 后端 Python 3.11 + FastAPI + uvicorn + PyYAML + python-multipart + pytest；前端 Vue3 + TypeScript + Vite + Element Plus + vis-network + markdown-it + DOMPurify。

**Spec：** `docs/superpowers/specs/2026-07-16-graph-asset-platform-design.md`（r6，权威）。

---

## 全局约定（每个任务都要遵守）

1. **工作目录**：在 `D:\mywork\KnowledgeBase\SFCGraph`（master 分支，直接提交，不开分支）。
2. **⚠️ GIT 陷阱（极重要）**：仓库里 `三层图谱构建规范/scripts/product_doc_md_exporter_optimized.py` 长期处于 git 暂存态（`A`）。**任何不带路径限定的 `git commit` 都会把它夹带进提交**。提交时**只能**：
   - `git add graph-asset-platform/<具体文件>`（只 add 平台目录下的文件），然后 `git commit -m "..." -- graph-asset-platform/`；或
   - `git commit -m "..." -- <精确路径>`
   - **绝不要** `git add -A` / `git add .` / `git commit -am`。
3. **TDD**：先写失败测试 → 跑（红）→ 最小实现 → 跑（绿）→ 提交。
4. **小步提交**：每个任务结束 commit 一次；提交信息用 `<type>: <描述>`（feat/fix/test/docs/chore）。
5. **不耦合业务**：平台代码不得出现 charging/bandwidth/SFCGraph 等具体业务名（spec §14.6 验收）。
6. **数据目录**：`<data>` 默认 `./platform-data/`（平台自管，加进 `.gitignore`，不进仓库）。

---

## File Structure（锁定分解）

```
graph-asset-platform/
  README.md
  .gitignore                         # platform-data/, __pycache__, node_modules, dist
  backend/
    pyproject.toml                   # 依赖：fastapi uvicorn pyyaml python-multipart；dev: pytest httpx
    app/
      __init__.py
      main.py                        # FastAPI app + lifespan + 挂 router + 静态托管前端 dist
      config.py                      # DATA_DIR、默认注册表路径
      default_registry.yaml          # 内置对象类型注册表（§6.3）
      models.py                      # Object / Edge dataclass
      registry.py                    # 类型注册表加载 + bundle types/ 合并
      logical_id.py                  # id 解析（3段/2段）+ 段数判定
      classify.py                    # id+frontmatter → 标准路径 + 文件名（=逻辑ID）
      md_parser.py                   # md → frontmatter + body + ##边 段
      edges.py                       # ##边 wikilink 解析 + 解析器管线
      version.py                     # 版本解析：网元最新（语义化排序）
      store.py                       # 统一资产库读写（<data>/assets/）
      index.py                       # 内存索引：nodes_by_(id,version)、邻接表、versions[] 聚合
      bundle.py                      # import(解压→归类→合并) / export(快照→zip)
      routers/
        __init__.py
        assets.py                    # POST /import, GET /export, /imports, /stats
        objects.py                   # /objects, /objects/{id}, /neighbors, /md, /subgraph
    tests/
      __init__.py
      conftest.py                    # fixtures：tmp_data_dir（sample_bundle fixture 见 Task 5.1）
      test_logical_id.py
      test_classify.py
      test_md_parser.py
      test_edges.py
      test_version.py
      test_registry.py
      test_store.py
      test_index.py
      test_bundle.py
      test_api_assets.py
      test_api_objects.py
      fixtures/
        sample_bundle/               # 极小样例资产（command/configobject/feature/business 各几个）
  frontend/
    package.json
    vite.config.ts
    tsconfig.json
    index.html
    src/
      main.ts
      App.vue
      router.ts
      api.ts
      views/BrowserView.vue
      components/TopBar.vue
      components/VersionSelector.vue
      components/ObjectIndex.vue
      components/MdPane.vue
      components/NeighborGraph.vue
```

**职责边界**：`logical_id`/`classify`/`md_parser`/`edges`/`version` 是纯函数核心（无 IO，易测）；`store`/`index`/`bundle` 是数据层；`routers` 是 API 薄层；前端独立。文件按职责分，不按技术层堆叠。

---

## Chunk 1: 后端核心纯逻辑（models / logical_id / classify / md_parser / edges / version / registry）

目标：把 spec 里最易错的部分（ID 段数、归类规则、`## 边` 解析、版本解析、类型注册表）做成纯函数 + 单元测试。这一块无 IO，TDD 最有效。

### Task 1.1: 项目脚手架 + 配置

**Files:**
- Create: `graph-asset-platform/.gitignore`
- Create: `graph-asset-platform/backend/pyproject.toml`
- Create: `graph-asset-platform/backend/app/__init__.py`
- Create: `graph-asset-platform/backend/app/config.py`
- Create: `graph-asset-platform/backend/tests/__init__.py`
- Create: `graph-asset-platform/backend/tests/conftest.py`

- [ ] **Step 1: 建目录与 .gitignore**

`graph-asset-platform/.gitignore`:
```
platform-data/
__pycache__/
*.pyc
node_modules/
dist/
.vite/
```

- [ ] **Step 2: pyproject.toml**

`graph-asset-platform/backend/pyproject.toml`:
```toml
[project]
name = "graph-asset-platform-backend"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["fastapi", "uvicorn[standard]", "pyyaml", "python-multipart"]

[project.optional-dependencies]
dev = ["pytest", "httpx"]

[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]
```

- [ ] **Step 3: config.py**

`graph-asset-platform/backend/app/config.py`:
```python
from pathlib import Path

# 资产库根（可被环境变量覆盖）。默认 ./platform-data/assets
DATA_DIR = Path(__file__).resolve().parents[2] / "platform-data"
ASSETS_DIR = DATA_DIR / "assets"
DEFAULT_REGISTRY_PATH = Path(__file__).resolve().parent / "default_registry.yaml"
```

- [ ] **Step 4: 空 conftest.py（占位，后续 Task 加 fixture）**

`graph-asset-platform/backend/tests/conftest.py`:
```python
import pytest
```

- [ ] **Step 5: 验证 pytest 可跑**

Run（在 `graph-asset-platform/backend/`）: `python -m pytest -q`（安装依赖：`pip install -e ".[dev]"`）
Expected: `no tests ran`（无报错即可）。

- [ ] **Step 6: Commit**

```bash
git add graph-asset-platform/.gitignore graph-asset-platform/backend
git commit -m "feat(platform): 后端脚手架(pyproject/config/目录)" -- graph-asset-platform/
```

### Task 1.2: models（Object / Edge dataclass）

**Files:**
- Create: `graph-asset-platform/backend/app/models.py`
- Test: `graph-asset-platform/backend/tests/test_models.py`

- [ ] **Step 1: 写测试**

`tests/test_models.py`:
```python
from app.models import Object, Edge

def test_object_minimum():
    o = Object(id="UDG@MMLCommand@ADD URR", type="MMLCommand", layer="Command",
               scope="nf", nf="UDG", version="20.15.2", versions=["20.15.2"],
               frontmatter={"id": "UDG@MMLCommand@ADD URR"}, body_md="x", raw_md="x", source_path="Command/UDG/20.15.2/UDG@MMLCommand@ADD URR.md")
    assert o.id == "UDG@MMLCommand@ADD URR"
    assert o.scope == "nf"

def test_edge():
    e = Edge(from_id="UDG@MMLCommand@ADD URR", from_version="20.15.2",
             relation="操作配置对象", to="UDG@ConfigObject@URR")
    assert e.to == "UDG@ConfigObject@URR"
```

- [ ] **Step 2: 跑测试（红）**

Run: `python -m pytest tests/test_models.py -q`
Expected: FAIL（ModuleNotFoundError / 名未定义）。

- [ ] **Step 3: 实现 models.py**

`app/models.py`:
```python
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Object:
    id: str                       # 版本无关逻辑ID（NF 3段 / 跨NF 2段）
    type: str
    layer: str                    # Command/ConfigObject/.../Business
    scope: str                    # "nf" | "cross"
    version: Optional[str]        # 本实例版本（NF有；cross 为 None）
    versions: list[str]           # 该 id 全部兄弟版本
    frontmatter: dict
    body_md: str                  # 去 frontmatter 与 ## 边
    raw_md: str                   # 原始全文
    source_path: str              # 资产库内相对路径
    nf: Optional[str] = None
    domain: Optional[str] = None
    scenario: Optional[str] = None

@dataclass
class Edge:
    from_id: str                  # 源节点版本无关 id
    from_version: Optional[str]   # 源节点版本（NF有；cross None）
    relation: Optional[str]
    to: str                       # 目标版本无关 id（wikilink，不带版本）
```

- [ ] **Step 4: 跑测试（绿）**

Run: `python -m pytest tests/test_models.py -q`
Expected: PASS。

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/models.py graph-asset-platform/backend/tests/test_models.py
git commit -m "feat(platform): Object/Edge 数据模型" -- graph-asset-platform/
```

### Task 1.3: logical_id（id 段数 + 解析）

**Files:**
- Create: `app/logical_id.py`
- Test: `tests/test_logical_id.py`

规则（spec §5.3）：NF 隔离类 3 段 `{nf}@{Type}@{local}`；跨 NF 类 2 段 `{Type}@{semantic}`。

- [ ] **Step 1: 写测试**

`tests/test_logical_id.py`:
```python
from app.logical_id import split_id, segment_count, is_nf_scoped

def test_nf_3seg():
    assert split_id("UDG@MMLCommand@ADD URR") == ("UDG", "MMLCommand", "ADD URR")
    assert segment_count("UDG@MMLCommand@ADD URR") == 3
    assert is_nf_scoped("UDG@MMLCommand@ADD URR") is True

def test_cross_2seg():
    assert split_id("NetworkScenario@charging") == (None, "NetworkScenario", "charging")
    assert segment_count("NetworkScenario@charging") == 2
    assert is_nf_scoped("NetworkScenario@charging") is False

def test_command_name_keeps_space():
    nf, typ, local = split_id("UDG@MMLCommand@ACT LICCTL")
    assert local == "ACT LICCTL"   # 空格保留，@ 不在 local 内
```

- [ ] **Step 2: 跑（红）** — Run: `python -m pytest tests/test_logical_id.py -q` → FAIL。

- [ ] **Step 3: 实现**

`app/logical_id.py`:
```python
def segment_count(id_: str) -> int:
    return id_.count("@") + 1

def is_nf_scoped(id_: str) -> bool:
    return segment_count(id_) == 3

def split_id(id_: str):
    """3段→(nf,type,local)；2段→(None,type,semantic)。local/semantic 内含空格原样保留。"""
    parts = id_.split("@")
    if len(parts) == 3:
        return parts[0], parts[1], parts[2]
    if len(parts) == 2:
        return None, parts[0], parts[1]
    raise ValueError(f"非法逻辑ID（非2/3段）: {id_!r}")
```

- [ ] **Step 4: 跑（绿）** — Run: `python -m pytest tests/test_logical_id.py -q` → PASS。

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/logical_id.py graph-asset-platform/backend/tests/test_logical_id.py
git commit -m "feat(platform): 逻辑ID段数解析(3段NF/2段跨NF)" -- graph-asset-platform/
```

### Task 1.4: 类型注册表（default_registry.yaml + registry.py）

**Files:**
- Create: `app/default_registry.yaml`
- Create: `app/registry.py`
- Test: `tests/test_registry.py`

注册表对齐 spec §6.3。每类型：layer/scope/id_segments/path_fields/frontmatter_required。

- [ ] **Step 1: default_registry.yaml**

`app/default_registry.yaml`:
```yaml
object_types:
  MMLCommand:
    layer: Command
    scope: nf
    id_segments: 3
    frontmatter_required: [id, type, name, nf, version, source, status]
  ConfigObject:
    layer: ConfigObject
    scope: nf
    id_segments: 3
    frontmatter_required: [id, type, name, nf, version, object_kind, source, status]
  Feature:
    layer: Feature
    scope: nf
    id_segments: 3
    frontmatter_required: [id, type, nf, version]
  License:
    layer: License
    scope: nf
    id_segments: 3
    frontmatter_required: [id, type, nf, version]
  Task:
    layer: Task
    scope: nf
    id_segments: 3
    frontmatter_required: [id, type, nf, version]
  BusinessDomain:
    layer: Business
    scope: cross
    id_segments: 2
    path_fields: [domain]
    frontmatter_required: [id, type, domain]
  NetworkScenario:
    layer: Business
    scope: cross
    id_segments: 2
    path_fields: [domain, scenario]
    frontmatter_required: [id, type, domain, scenario]
  ConfigurationSolution:
    layer: Business
    scope: cross
    id_segments: 2
    path_fields: [domain, scenario]
    frontmatter_required: [id, type, domain, scenario]
```

- [ ] **Step 2: 写测试**

`tests/test_registry.py`:
```python
from app.registry import Registry
from app.config import DEFAULT_REGISTRY_PATH

def test_load_default():
    r = Registry.load_default()
    assert r.get("MMLCommand")["layer"] == "Command"
    assert r.get("MMLCommand")["scope"] == "nf"
    assert r.get("NetworkScenario")["path_fields"] == ["domain", "scenario"]

def test_layer_of_type():
    r = Registry.load_default()
    assert r.layer_of("MMLCommand") == "Command"
    assert r.layer_of("ConfigurationSolution") == "Business"

def test_merge_extension_overrides():
    r = Registry.load_default()
    r.merge_extensions({"MMLCommand": {"layer": "Command", "scope": "nf", "id_segments": 3, "frontmatter_required": ["id"]})
    # 覆盖默认，不报错
    assert r.get("MMLCommand")["frontmatter_required"] == ["id"]

def test_unknown_type():
    r = Registry.load_default()
    assert r.get("Nope") is None
```

- [ ] **Step 3: 跑（红）** — `python -m pytest tests/test_registry.py -q` → FAIL。

- [ ] **Step 4: 实现 registry.py**

`app/registry.py`:
```python
import yaml
from pathlib import Path
from typing import Optional

class Registry:
    def __init__(self, types: dict):
        self._t = types  # {TypeName: {layer,scope,...}}

    @classmethod
    def load_default(cls, path: Optional[Path] = None) -> "Registry":
        from app.config import DEFAULT_REGISTRY_PATH
        path = path or DEFAULT_REGISTRY_PATH
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        return cls(data.get("object_types", {}))

    def get(self, type_name: str) -> Optional[dict]:
        return self._t.get(type_name)

    def layer_of(self, type_name: str) -> Optional[str]:
        e = self.get(type_name)
        return e["layer"] if e else None

    def merge_extensions(self, ext: dict) -> list:
        """bundle 扩展覆盖默认；返回告警列表。"""
        warnings = []
        for name, spec in (ext or {}).items():
            if name in self._t:
                warnings.append(f"类型 {name} 被 bundle 扩展覆盖")
            self._t[name] = spec
        return warnings

    def known(self, type_name: str) -> bool:
        return type_name in self._t
```

- [ ] **Step 5: 跑（绿）** — PASS。

- [ ] **Step 6: Commit**

```bash
git add graph-asset-platform/backend/app/default_registry.yaml graph-asset-platform/backend/app/registry.py graph-asset-platform/backend/tests/test_registry.py
git commit -m "feat(platform): 对象类型注册表(默认+可扩展)" -- graph-asset-platform/
```

### Task 1.5: classify（id+frontmatter → 路径 + 文件名）

**Files:**
- Create: `app/classify.py`
- Test: `tests/test_classify.py`

规则（spec §5.4）：文件名 = 逻辑ID（`{id}.md`）；NF 类路径 `{Layer}/{nf}/{version}/`（nf 从 id 段0、version 从 frontmatter）；跨 NF 类路径由 frontmatter `domain`/`scenario`（path_fields）。

- [ ] **Step 1: 写测试**

`tests/test_classify.py`:
```python
from app.classify import classify
from app.registry import Registry

R = Registry.load_default()

def test_nf_command():
    rel, fname = classify("UDG@MMLCommand@ADD URR", R, {"version": "20.15.2"})
    assert fname == "UDG@MMLCommand@ADD URR.md"
    assert rel == "Command/UDG/20.15.2"

def test_nf_configobject():
    rel, fname = classify("UDG@ConfigObject@URR", R, {"version": "20.15.2"})
    assert rel == "ConfigObject/UDG/20.15.2"
    assert fname == "UDG@ConfigObject@URR.md"

def test_business_domain():
    rel, fname = classify("BusinessDomain@charging", R, {"domain": "business-awareness"})
    assert rel == "Business/business-awareness"
    assert fname == "BusinessDomain@charging.md"

def test_business_scenario():
    rel, fname = classify("NetworkScenario@charging", R, {"domain": "business-awareness", "scenario": "charging"})
    assert rel == "Business/business-awareness/charging"

def test_business_solution():
    rel, fname = classify("ConfigurationSolution@charging-online", R, {"domain": "business-awareness", "scenario": "charging"})
    assert rel == "Business/business-awareness/charging"
    assert fname == "ConfigurationSolution@charging-online.md"

def test_missing_version_raises():
    import pytest
    with pytest.raises(ValueError):
        classify("UDG@MMLCommand@ADD URR", R, {})  # NF 类缺 version
```

- [ ] **Step 2: 跑（红）**。

- [ ] **Step 3: 实现 classify.py**

`app/classify.py`:
```python
from .logical_id import split_id, segment_count
from .registry import Registry

def classify(id_: str, registry: Registry, frontmatter: dict) -> tuple[str, str]:
    """返回 (相对目录, 文件名)。文件名恒为 {id}.md（= 版本无关逻辑ID）。"""
    nf, typ, _local = split_id(id_)
    entry = registry.get(typ)
    if entry is None:
        raise ValueError(f"未知类型 {typ!r}（id={id_!r}）")
    filename = f"{id_}.md"
    if entry["scope"] == "nf":
        version = frontmatter.get("version")
        if not version:
            raise ValueError(f"NF 类 {typ} 缺 frontmatter.version（id={id_!r}）")
        # nf 以 id 段0 为准（权威），frontmatter.nf 仅校验
        layer = entry["layer"]
        return f"{layer}/{nf}/{version}", filename
    # cross
    layer = entry["layer"]
    parts = [layer]
    for field in entry.get("path_fields", []):
        v = frontmatter.get(field)
        if not v:
            raise ValueError(f"跨NF类 {typ} 缺 frontmatter.{field}（id={id_!r}）")
        parts.append(v)
    return "/".join(parts), filename
```

- [ ] **Step 4: 跑（绿）**。

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/classify.py graph-asset-platform/backend/tests/test_classify.py
git commit -m "feat(platform): 资产归类器(id+frontmatter→路径+文件名)" -- graph-asset-platform/
```

### Task 1.6: md_parser（frontmatter + body + ## 边 三段切分）

**Files:**
- Create: `app/md_parser.py`
- Test: `tests/test_md_parser.py`

切分：YAML frontmatter（`---` 围栏）→ body（正文）→ 底部 `## 边` 章节（如有）。

- [ ] **Step 1: 写测试**

`tests/test_md_parser.py`:
```python
from app.md_parser import parse_md

MD = """---
id: UDG@MMLCommand@ADD URR
type: MMLCommand
nf: UDG
version: 20.15.2
---
# ADD URR
正文行。

## 边
- 操作配置对象: [[UDG@ConfigObject@URR]]
- 参见: [[UDG@MMLCommand@MOD URR]]
"""

def test_frontmatter():
    fm, body, edge_section = parse_md(MD)
    assert fm["id"] == "UDG@MMLCommand@ADD URR"
    assert fm["type"] == "MMLCommand"

def test_body_strips_edge_section():
    fm, body, edge_section = parse_md(MD)
    assert "# ADD URR" in body
    assert "## 边" not in body          # body 不含边章节
    assert "操作配置对象" in edge_section  # 边章节单独切出

def test_no_edges():
    md = "---\nid: X@T@y\ntype: T\n---\n正文\n"
    fm, body, edge_section = parse_md(md)
    assert edge_section == ""
```

- [ ] **Step 2: 跑（红）**。

- [ ] **Step 3: 实现 md_parser.py**

`app/md_parser.py`:
```python
import yaml
import re

_FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.S)
_EDGE_HEADER_RE = re.compile(r"\n##\s*边\s*\n", re.M)

def parse_md(text: str) -> tuple[dict, str, str]:
    """→ (frontmatter_dict, body_md, edge_section_text)。无 frontmatter→空dict；无##边→''。"""
    fm: dict = {}
    body = text
    m = _FM_RE.match(text)
    if m:
        fm = yaml.safe_load(m.group(1)) or {}
        body = m.group(2)
    # 切出 ## 边 章节（取该标题到文末）
    em = _EDGE_HEADER_RE.search("\n" + body)
    edge_section = ""
    if em:
        # em.start() 指向 "\n## 边\n" 的开头 \n（body 前补了一个 \n）
        cut = em.start()  # 相对 prefixed body
        edge_section = ("\n" + body)[cut:].lstrip("\n")
        body = ("\n" + body)[:cut].rstrip("\n")
    return fm, body, edge_section
```

> 说明：`## 边` 视为 body 末尾的专章，从该标题到文末整段切给 edge_section；body 保留正文。

- [ ] **Step 4: 跑（绿）**（可能需微调正则；确保 body/edge 切分正确）。

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/md_parser.py graph-asset-platform/backend/tests/test_md_parser.py
git commit -m "feat(platform): md三段解析器(frontmatter+正文+##边)" -- graph-asset-platform/
```

### Task 1.7: edges（## 边 wikilink 解析）

**Files:**
- Create: `app/edges.py`
- Test: `tests/test_edges.py`

格式（spec §6.2）：`- {relation}: [[{to_id}]]`，to_id 版本无关。

- [ ] **Step 1: 写测试**

`tests/test_edges.py`:
```python
from app.edges import parse_edges, Edge

SEC = """## 边
- 操作配置对象: [[UDG@ConfigObject@URR]]
- 参见: [[UDG@MMLCommand@MOD URR]]
- 无关系冒号的行（不是边）
"""

def test_parse_two_edges():
    es = parse_edges(SEC, from_id="UDG@MMLCommand@ADD URR", from_version="20.15.2")
    assert len(es) == 2
    assert es[0].relation == "操作配置对象"
    assert es[0].to == "UDG@ConfigObject@URR"
    assert es[1].relation == "参见"
    assert es[1].to == "UDG@MMLCommand@MOD URR"

def test_empty():
    assert parse_edges("", "a@T@b", "1.0") == []
    assert parse_edges("## 边\n（暂无）", "a@T@b", "1.0") == []

def test_dedup():
    s = "## 边\n- r: [[X@T@y]]\n- r: [[X@T@y]]\n"
    assert len(parse_edges(s, "a@T@b", "1.0")) == 1
```

- [ ] **Step 2: 跑（红）**。

- [ ] **Step 3: 实现 edges.py**

`app/edges.py`:
```python
import re
from .models import Edge
from typing import Optional

# - {relation}: [[ {to_id} ]]
_LINE_RE = re.compile(r"^\s*-\s*(?P<rel>[^:]+?):\s*\[\[(?P<to>[^\]]+)\]\]\s*$", re.M)

def parse_edges(edge_section: str, from_id: str, from_version: Optional[str]) -> list[Edge]:
    if not edge_section:
        return []
    seen = set()
    out = []
    for m in _LINE_RE.finditer(edge_section):
        rel = m.group("rel").strip()
        to = m.group("to").strip()
        key = (from_id, rel, to)
        if key in seen:
            continue
        seen.add(key)
        out.append(Edge(from_id=from_id, from_version=from_version, relation=rel, to=to))
    return out
```

- [ ] **Step 4: 跑（绿）**。

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/edges.py graph-asset-platform/backend/tests/test_edges.py
git commit -m "feat(platform): ##边 wikilink 边解析器" -- graph-asset-platform/
```

### Task 1.8: version（网元最新版本，语义化排序）

**Files:**
- Create: `app/version.py`
- Test: `tests/test_version.py`

规则（spec §6.4）：默认版本 = 该网元最新版本，按点分段数值比较（避免 `20.9.10 > 20.15.2` 的字符串陷阱）。

- [ ] **Step 1: 写测试**

`tests/test_version.py`:
```python
from app.version import latest_version

def test_simple():
    assert latest_version(["20.15.2", "20.15.1"]) == "20.15.2"

def test_semantic_not_string():
    # 字符串排序会错把 20.9.10 排到 20.15.2 之后；语义化必须 20.15.2 更新
    assert latest_version(["20.9.10", "20.15.2"]) == "20.15.2"

def test_three_segments():
    assert latest_version(["20.15.2", "20.16.0", "20.15.10"]) == "20.16.0"

def test_non_numeric_fallback():
    # 非纯数字段退化为字符串比较
    assert latest_version(["r1", "r2"]) == "r2"

def test_empty():
    assert latest_version([]) is None
```

- [ ] **Step 2: 跑（红）**。

- [ ] **Step 3: 实现 version.py**

`app/version.py`:
```python
from functools import cmp_to_key

def _ver_key(v: str):
    parts = v.split(".")
    keyed = []
    for p in parts:
        if p.isdigit():
            keyed.append((0, int(p)))       # 数值优先
        else:
            keyed.append((1, p))            # 非数字退化为字符串
    return keyed

def _cmp(a: str, b: str) -> int:
    ka, kb = _ver_key(a), _ver_key(b)
    # 长度对齐：短的补 (0,0) 视为更小
    n = max(len(ka), len(kb))
    ka += [(0, 0)] * (n - len(ka))
    kb += [(0, 0)] * (n - len(kb))
    return (ka > kb) - (ka < kb)

def latest_version(versions: list[str]):
    """返回最新版本（语义化点分段数值比较，非数字退化为字符串）。空→None。"""
    if not versions:
        return None
    return sorted(versions, key=cmp_to_key(_cmp))[-1]
```

- [ ] **Step 4: 跑（绿）**。

- [ ] **Step 5: 全量跑 + Commit**

Run: `python -m pytest -q` → 全绿。
```bash
git add graph-asset-platform/backend/app/version.py graph-asset-platform/backend/tests/test_version.py
git commit -m "feat(platform): 版本解析(网元最新, 语义化排序)" -- graph-asset-platform/
```

**Chunk 1 完成**：核心纯逻辑（models/logical_id/registry/classify/md_parser/edges/version）全部 TDD 通过，无业务耦合。派发 plan-document-reviewer 审 Chunk 1（见文末 Plan Review Loop）。

---

## Chunk 2: 数据层（store / index / bundle 导入导出）

目标：把核心逻辑组装成"统一资产库读写 + 内存索引 + 导入合并 + 导出"。

### Task 2.1: store（统一资产库读写）

**Files:**
- Create: `app/store.py`
- Test: `tests/test_store.py`

职责：在 `<data>/assets/` 下按相对路径读写 md；列出所有 md 文件。

- [ ] **Step 1: 写测试**（用 tmp_path fixture 做 `<data>`）

`tests/conftest.py` 增加：
```python
import pytest
from pathlib import Path

@pytest.fixture
def tmp_data_dir(tmp_path, monkeypatch):
    data = tmp_path / "platform-data"
    assets = data / "assets"
    assets.mkdir(parents=True)
    import app.config as config
    monkeypatch.setattr(config, "DATA_DIR", data)
    monkeypatch.setattr(config, "ASSETS_DIR", assets)
    return assets
```

`tests/test_store.py`:
```python
from app.store import Store

def test_write_and_read(tmp_data_dir):
    s = Store(tmp_data_dir)
    s.write("Command/UDG/20.15.2/UDG@MMLCommand@ADD URR.md", "---\nid: x\n---\nbody\n")
    assert "body" in s.read("Command/UDG/20.15.2/UDG@MMLCommand@ADD URR.md")

def test_list_all_md(tmp_data_dir):
    s = Store(tmp_data_dir)
    s.write("Command/UDG/20.15.2/a.md", "x")
    s.write("Business/d/BusinessDomain@d.md", "y")
    md_files = s.list_md()
    assert len(md_files) == 2

def test_exists(tmp_data_dir):
    s = Store(tmp_data_dir)
    s.write("Command/UDG/20.15.2/a.md", "x")
    assert s.exists("Command/UDG/20.15.2/a.md")
    assert not s.exists("nope.md")
```

- [ ] **Step 2: 跑（红）**。

- [ ] **Step 3: 实现 store.py**

`app/store.py`:
```python
from pathlib import Path

class Store:
    def __init__(self, assets_dir: Path):
        self.root = Path(assets_dir)
        self.root.mkdir(parents=True, exist_ok=True)

    def _resolve(self, rel: str) -> Path:
        p = (self.root / rel).resolve()
        # 防路径穿越
        if self.root.resolve() not in p.parents and p != self.root.resolve():
            raise ValueError(f"非法路径: {rel}")
        return p

    def write(self, rel: str, text: str) -> None:
        p = self._resolve(rel)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def read(self, rel: str) -> str:
        return self._resolve(rel).read_text(encoding="utf-8")

    def exists(self, rel: str) -> bool:
        return self._resolve(rel).exists()

    def list_md(self) -> list[str]:
        return [str(p.relative_to(self.root)).replace("\\", "/")
                for p in self.root.rglob("*.md")]
```

- [ ] **Step 4: 跑（绿）**。

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/store.py graph-asset-platform/backend/tests/test_store.py graph-asset-platform/backend/tests/conftest.py
git commit -m "feat(platform): 统一资产库存储(读写+列举+路径穿越防护)" -- graph-asset-platform/
```

### Task 2.2: index（内存索引：节点 + 邻接 + versions 聚合 + 版本解析）

**Files:**
- Create: `app/index.py`
- Test: `tests/test_index.py`

职责：遍历 store 所有 md → 解析为 Object 节点（一个 md = 一个 (id,version) 节点）→ 按 id 聚合 versions[] → 解析 `## 边` → 建 `out_edges[(id,version)]` / `in_edges`；提供 latest_version_per_nf、resolve_target(to_id, version=None)。

- [ ] **Step 1: 写测试**（构造 2 个 command + 1 configobject，跨版本）

`tests/test_index.py`:
```python
from app.store import Store
from app.index import Index
from app.registry import Registry

def _cmd(store, id_, version, body_edges=""):
    nf, typ, _ = id_.split("@")
    md = f"---\nid: {id_}\ntype: MMLCommand\nnf: {nf}\nversion: {version}\n---\n# {id_}\n{body_edges}"
    store.write(f"Command/{nf}/{version}/{id_}.md", md)

def test_nodes_and_versions(tmp_data_dir):
    s = Store(tmp_data_dir)
    _cmd(s, "UDG@MMLCommand@ADD URR", "20.15.2")
    _cmd(s, "UDG@MMLCommand@ADD URR", "20.16.0")   # 同 id 两版本
    idx = Index.build(s, Registry.load_default())
    # 两个节点
    assert idx.node("UDG@MMLCommand@ADD URR", "20.15.2") is not None
    assert idx.node("UDG@MMLCommand@ADD URR", "20.16.0") is not None
    # versions 聚合
    vs = idx.versions_of("UDG@MMLCommand@ADD URR")
    assert set(vs) == {"20.15.2", "20.16.0"}

def test_latest_version(tmp_data_dir):
    s = Store(tmp_data_dir)
    _cmd(s, "UDG@MMLCommand@ADD URR", "20.9.10")
    _cmd(s, "UDG@MMLCommand@ADD URR", "20.15.2")
    idx = Index.build(s, Registry.load_default())
    assert idx.latest_version_of_nf("UDG") == "20.15.2"

def test_default_resolves_latest(tmp_data_dir):
    s = Store(tmp_data_dir)
    _cmd(s, "UDG@MMLCommand@ADD URR", "20.15.2")
    _cmd(s, "UDG@MMLCommand@ADD URR", "20.16.0")
    idx = Index.build(s, Registry.load_default())
    # 不指定版本 → 最新
    n = idx.resolve_node("UDG@MMLCommand@ADD URR", version=None)
    assert n.version == "20.16.0"

def test_default_when_id_only_at_old_version(tmp_data_dir):
    # UDG 有更新版本(OTHER@20.16.0)，但 ADD URR 只在 20.15.2 → 默认不 404，落到最新现存 20.15.2
    s = Store(tmp_data_dir)
    _cmd(s, "UDG@MMLCommand@ADD URR", "20.15.2")
    _cmd(s, "UDG@MMLCommand@OTHER", "20.16.0")
    idx = Index.build(s, Registry.load_default())
    n = idx.resolve_node("UDG@MMLCommand@ADD URR", version=None)
    assert n is not None and n.version == "20.15.2"

def test_edges_and_inedges(tmp_data_dir):
    s = Store(tmp_data_dir)
    edges_md = "## 边\n- 操作配置对象: [[UDG@ConfigObject@URR]]\n"
    _cmd(s, "UDG@MMLCommand@ADD URR", "20.15.2", edges_md)
    # configobject
    s.write("ConfigObject/UDG/20.15.2/UDG@ConfigObject@URR.md",
            "---\nid: UDG@ConfigObject@URR\ntype: ConfigObject\nnf: UDG\nversion: 20.15.2\n---\nx\n")
    idx = Index.build(s, Registry.load_default())
    out = idx.out_edges("UDG@MMLCommand@ADD URR", "20.15.2")
    assert any(e.to == "UDG@ConfigObject@URR" for e in out)
    # 反链（版本无关，按 id）
    back = idx.in_edges("UDG@ConfigObject@URR")
    assert any(e.from_id == "UDG@MMLCommand@ADD URR" for e in back)

def test_dangling_edge_warning(tmp_data_dir):
    s = Store(tmp_data_dir)
    _cmd(s, "UDG@MMLCommand@ADD URR", "20.15.2", "## 边\n- 参见: [[UDG@MMLCommand@NOPE]]\n")
    idx = Index.build(s, Registry.load_default())
    assert idx.has_dangling()   # 目标不存在 → 悬空
```

- [ ] **Step 2: 跑（红）**。

- [ ] **Step 3: 实现 index.py**

`app/index.py`:
```python
from pathlib import Path
from .store import Store
from .registry import Registry
from .md_parser import parse_md
from .edges import parse_edges
from .logical_id import split_id
from .models import Object, Edge
from .version import latest_version
from collections import defaultdict
from typing import Optional

class Index:
    def __init__(self):
        self.nodes = {}                       # (id,version) -> Object
        self.versions: dict[str, list[str]] = {}   # id -> [versions]
        self.out: dict[tuple, list[Edge]] = defaultdict(list)
        self.dangling = False

    @classmethod
    def build(cls, store: Store, registry: Registry) -> "Index":
        idx = cls()
        # 第1趟：建节点 + 聚合 versions + 收集原始边
        raw_edges = []   # (from_id, from_version, Edge)
        for rel in store.list_md():
            try:
                text = store.read(rel)
                fm, body, edge_sec = parse_md(text)
            except Exception:
                continue
            id_ = fm.get("id"); typ = fm.get("type")
            if not id_ or not typ or not registry.known(typ):
                continue
            nf, _, _ = split_id(id_)
            version = fm.get("version")
            obj = Object(id=id_, type=typ, layer=registry.layer_of(typ),
                         scope=registry.get(typ)["scope"], version=version, versions=[],
                         frontmatter=fm, body_md=body, raw_md=text, source_path=rel,
                         nf=nf, domain=fm.get("domain"), scenario=fm.get("scenario"))
            key = (id_, version)
            idx.nodes[key] = obj
            idx.versions.setdefault(id_, [])
            if version not in idx.versions[id_]:
                idx.versions[id_].append(version)
            for e in parse_edges(edge_sec, from_id=id_, from_version=version):
                raw_edges.append((id_, version, e))
                idx.out[key].append(e)
        # 聚合 versions 到节点
        for key, obj in idx.nodes.items():
            obj.versions = sorted(idx.versions[obj.id])
        # 第2趟：悬空检测（to_id 完全不存在 → 悬空边）
        for (fid, fver), edges in idx.out.items():
            for e in edges:
                if e.to not in idx.versions:
                    idx.dangling = True
        return idx

    def node(self, id_: str, version: str) -> Optional[Object]:
        return self.nodes.get((id_, version))

    def versions_of(self, id_: str) -> list[str]:
        return self.versions.get(id_, [])

    def latest_version_of_nf(self, nf: str) -> Optional[str]:
        # 取该 nf 所有版本
        vs = {v for (i, v) in self.nodes.keys() if self.nodes[(i, v)].nf == nf}
        return latest_version(list(vs)) if vs else None

    def latest_version_of_id(self, id_: str) -> Optional[str]:
        return latest_version(self.versions_of(id_))

    def resolve_node(self, id_: str, version: Optional[str]) -> Optional[Object]:
        """指定版本优先(不存在→None→API 404)；否则该 id 最新现存版本(≈网元最新; id 仅存旧版本则落到旧版本,不404)。"""
        if version:
            return self.node(id_, version)   # 指定但不存在 → None
        v = self.latest_version_of_id(id_)
        return self.node(id_, v) if v else None

    def out_edges(self, id_: str, version: str) -> list[Edge]:
        return self.out.get((id_, version), [])

    def in_edges(self, to_id: str) -> list[Edge]:
        # 反链：边是版本无关引用，按 to_id 收集（与查看哪个版本节点无关）
        return [e for edges in self.out.values() for e in edges if e.to == to_id]

    def has_dangling(self) -> bool:
        return self.dangling
```

> 注意：`in_edges` 这里用"to_id 最新版本"近似匹配；若需精确反链按指定版本，可在 build 时按 (to_id)→(to_default_version) 预算反链表。Plan 评审时确认粒度。

- [ ] **Step 4: 跑（绿）**。

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/index.py graph-asset-platform/backend/tests/test_index.py
git commit -m "feat(platform): 内存索引(节点+版本聚合+邻接+版本解析)" -- graph-asset-platform/
```

### Task 2.3: bundle 导入（解压 → 归类 → 合并）

**Files:**
- Create: `app/bundle.py`（import 部分）
- Test: `tests/test_bundle.py`

职责：`POST /import` 的核心：解压 zip → 先扫 `types/` 合并注册表 → 逐 md 解析 frontmatter → classify → 写入 store（同 id 同版本=更新）→ 统计 added/updated + 告警 → 重建索引。

- [ ] **Step 1: 写测试**（构造内存 zip）

`tests/test_bundle.py`:
```python
import io, zipfile
from app.bundle import import_bundle, BundleResult
from app.store import Store
from app.index import Index
from app.registry import Registry

def _zip(files: dict) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for name, content in files.items():
            z.writestr(name, content)
    return buf.getvalue()

CMD = "---\nid: UDG@MMLCommand@ADD URR\ntype: MMLCommand\nnf: UDG\nversion: 20.15.2\n---\n# x\n"
CFG = "---\nid: UDG@ConfigObject@URR\ntype: ConfigObject\nnf: UDG\nversion: 20.15.2\n---\n# y\n"

def test_import_classifies_and_writes(tmp_data_dir):
    store = Store(tmp_data_dir)
    data = _zip({"随便/flat.md": CMD, "ConfigObject/UDG/20.15.2/URR.md": CFG})
    res = import_bundle(data, store, Registry.load_default())
    assert res.added == 2 and res.updated == 0
    assert store.exists("Command/UDG/20.15.2/UDG@MMLCommand@ADD URR.md")
    assert store.exists("ConfigObject/UDG/20.15.2/UDG@ConfigObject@URR.md")

def test_import_update_same_id_version(tmp_data_dir):
    store = Store(tmp_data_dir)
    import_bundle(_zip({"a.md": CMD}), store, Registry.load_default())
    res2 = import_bundle(_zip({"b.md": CMD}), store, Registry.load_default())  # 同 id+version
    assert res2.updated == 1 and res2.added == 0

def test_import_skips_invalid(tmp_data_dir):
    store = Store(tmp_data_dir)
    bad = "---\ntype: MMLCommand\n---\nno id\n"   # 缺 id
    res = import_bundle(_zip({"bad.md": bad, "good.md": CMD}), store, Registry.load_default())
    assert res.added == 1
    assert any("bad.md" in w for w in res.warnings)
```

- [ ] **Step 2: 跑（红）**。

- [ ] **Step 3: 实现 bundle.py（import 部分）**

`app/bundle.py`:
```python
import zipfile, io, yaml
from dataclasses import dataclass, field
from pathlib import Path
from .store import Store
from .registry import Registry
from .md_parser import parse_md
from .classify import classify

@dataclass
class BundleResult:
    added: int = 0
    updated: int = 0
    skipped: int = 0
    warnings: list[str] = field(default_factory=list)

def import_bundle(zip_bytes: bytes, store: Store, registry: Registry) -> BundleResult:
    res = BundleResult()
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
        names = z.namelist()
        # 1. 先扫 types/*.yaml 合并注册表
        for n in names:
            if n.startswith("types/") and n.endswith(".yaml"):
                spec = yaml.safe_load(z.read(n)) or {}
                res.warnings.extend(registry.merge_extensions({Path(n).stem: spec}))
        # 2. 逐 md 归类合并
        for n in names:
            if not n.endswith(".md"):
                continue
            text = z.read(n).decode("utf-8")
            try:
                fm, _body, _edges = parse_md(text)
            except Exception as ex:
                res.warnings.append(f"{n}: 解析失败 {ex}"); res.skipped += 1; continue
            id_ = fm.get("id"); typ = fm.get("type")
            if not id_ or not typ:
                res.warnings.append(f"{n}: 缺 id/type"); res.skipped += 1; continue
            if not registry.known(typ):
                res.warnings.append(f"{n}: 未知类型 {typ}"); res.skipped += 1; continue
            try:
                rel, fname = classify(id_, registry, fm)
            except ValueError as ex:
                res.warnings.append(f"{n}: {ex}"); res.skipped += 1; continue
            target = f"{rel}/{fname}"
            if store.exists(target):
                res.updated += 1
            else:
                res.added += 1
            store.write(target, text)
    return res
```

- [ ] **Step 4: 跑（绿）**。

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/bundle.py graph-asset-platform/backend/tests/test_bundle.py
git commit -m "feat(platform): bundle导入(解压→归类→合并, added/updated统计)" -- graph-asset-platform/
```

### Task 2.4: bundle 导出（快照 → zip，可过滤）

**Files:**
- Modify: `app/bundle.py`（加 export_bundle）
- Test: `tests/test_bundle.py`（加导出测试）

- [ ] **Step 1: 加测试**

追加到 `tests/test_bundle.py`:
```python
from app.bundle import export_bundle

def test_export_roundtrip(tmp_data_dir):
    store = Store(tmp_data_dir)
    import_bundle(_zip({"a.md": CMD, "b.md": CFG}), store, Registry.load_default())
    zbytes = export_bundle(store)
    with zipfile.ZipFile(io.BytesIO(zbytes)) as z:
        names = z.namelist()
    assert "Command/UDG/20.15.2/UDG@MMLCommand@ADD URR.md" in names
    assert "ConfigObject/UDG/20.15.2/UDG@ConfigObject@URR.md" in names

def test_export_filter_nf(tmp_data_dir):
    store = Store(tmp_data_dir)
    import_bundle(_zip({"a.md": CMD}), store, Registry.load_default())
    zbytes = export_bundle(store, nf="UNC")   # UDG 不在结果
    with zipfile.ZipFile(io.BytesIO(zbytes)) as z:
        assert all("UDG" not in n for n in z.namelist())
```

- [ ] **Step 2: 跑（红）**。

- [ ] **Step 3: 实现 export_bundle**

追加到 `app/bundle.py`:
```python
def export_bundle(store: Store, nf: str | None = None, version: str | None = None,
                  domain: str | None = None, scenario: str | None = None) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in store.list_md():
            parts = rel.split("/")
            # 粗粒度过滤：layer/nf/version/... 或 Business/domain/scenario/...
            if nf and (len(parts) < 3 or parts[1] != nf):
                continue
            if version and (len(parts) < 3 or parts[2] != version):
                continue
            if domain and not (parts[0] == "Business" and len(parts) > 1 and parts[1] == domain):
                continue
            if scenario and not (parts[0] == "Business" and len(parts) > 2 and parts[2] == scenario):
                continue
            z.writestr(rel, store.read(rel))
    return buf.getvalue()
```

- [ ] **Step 4: 跑（绿）**。

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/bundle.py graph-asset-platform/backend/tests/test_bundle.py
git commit -m "feat(platform): bundle导出(快照zip, 可按nf/version/domain过滤)" -- graph-asset-platform/
```

**Chunk 2 完成**：store/index/import/export 可独立测，数据层打通。派发 plan-document-reviewer 审 Chunk 2。

---

## Chunk 3: FastAPI 读 API + 上传

目标：把 store/index/bundle 暴露为 HTTP API（spec §8）。单例 service：启动时建索引；`/import` 后重建。

### Task 3.1: service 单例 + main.py

**Files:**
- Create: `app/service.py`
- Create: `app/main.py`

- [ ] **Step 1: service.py（持有 store/registry/index，启动建索引，import 后重建）**

`app/service.py`:
```python
from pathlib import Path
from .config import ASSETS_DIR, DEFAULT_REGISTRY_PATH
from .store import Store
from .registry import Registry
from .index import Index
from .bundle import import_bundle

class Service:
    def __init__(self):
        self.store = Store(ASSETS_DIR)
        self.registry = Registry.load_default()
        self.index = Index.build(self.store, self.registry)

    def rebuild(self):
        self.index = Index.build(self.store, self.registry)

_service: Service | None = None

def get_service() -> Service:
    global _service
    if _service is None:
        _service = Service()
    return _service
```

- [ ] **Step 2: main.py（FastAPI + lifespan + CORS + 静态托管前端 dist）**

`app/main.py`:
```python
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .service import get_service
from .routers import assets as assets_router, objects as objects_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    get_service()  # 启动预热建索引
    yield

app = FastAPI(title="Graph Asset Platform", version="0.1.0", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.include_router(assets_router.router, prefix="/api/v1")
app.include_router(objects_router.router, prefix="/api/v1")

# 前端静态托管（dist 存在后构建）
_dist = Path(__file__).resolve().parents[2] / "frontend" / "dist"
if _dist.exists():
    app.mount("/", StaticFiles(directory=_dist, html=True), name="spa")
```

- [ ] **Step 3: 空 routers 包**

`app/routers/__init__.py`: 空。（冒烟测试由 Task 3.2 的 `/stats` 测试覆盖，不单独建 smoke 文件。）

- [ ] **Step 4: Commit 骨架**

```bash
git add graph-asset-platform/backend/app/service.py graph-asset-platform/backend/app/main.py graph-asset-platform/backend/app/routers
git commit -m "feat(platform): FastAPI service单例+main骨架" -- graph-asset-platform/
```

### Task 3.2: assets router（/import /export /imports /stats）

**Files:**
- Create: `app/routers/assets.py`
- Test: `tests/test_api_assets.py`

- [ ] **Step 1: 写测试**

`tests/test_api_assets.py`:
```python
import io, zipfile
from fastapi.testclient import TestClient
from app.main import app

CMD = "---\nid: UDG@MMLCommand@ADD URR\ntype: MMLCommand\nnf: UDG\nversion: 20.15.2\n---\n# x\n"

def _zip(files):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for n, c in files.items():
            z.writestr(n, c)
    buf.seek(0)
    return ("bundle.zip", buf, "application/zip")

def test_import_and_stats(tmp_data_dir, monkeypatch):
    # 让 service 用 tmp_data_dir
    import app.service as svc
    from app.store import Store
    from app.registry import Registry
    from app.index import Index
    # 重置单例到 tmp
    s = svc.Service.__new__(svc.Service)
    s.store = Store(tmp_data_dir); s.registry = Registry.load_default(); s.index = Index.build(s.store, s.registry)
    monkeypatch.setattr(svc, "_service", s)
    with TestClient(app) as c:
        r = c.post("/api/v1/import", files={"file": _zip({"a.md": CMD})})
        assert r.status_code == 200
        body = r.json()
        assert body["added"] == 1
        r2 = c.get("/api/v1/stats")
        assert r2.status_code == 200
        assert r2.json()["object_counts_by_type"]["MMLCommand"] == 1

def test_export(tmp_data_dir, monkeypatch):
    import app.service as svc
    from app.store import Store
    from app.registry import Registry
    from app.index import Index
    s = svc.Service.__new__(svc.Service)
    s.store = Store(tmp_data_dir); s.registry = Registry.load_default(); s.index = Index.build(s.store, s.registry)
    monkeypatch.setattr(svc, "_service", s)
    with TestClient(app) as c:
        c.post("/api/v1/import", files={"file": _zip({"a.md": CMD})})
        r = c.get("/api/v1/export")
        assert r.status_code == 200
        assert r.headers["content-type"].startswith("application/zip")
```

> 注：测试用 monkeypatch 把 service 单例指向 tmp_data_dir，避免污染真实 platform-data。

- [ ] **Step 2: 跑（红）**。

- [ ] **Step 3: 实现 routers/assets.py**

`app/routers/assets.py`:
```python
import json
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, Query
from fastapi.responses import StreamingResponse, PlainTextResponse
import io
from ..service import get_service
from ..config import DATA_DIR
from ..bundle import import_bundle, export_bundle

router = APIRouter()
_LOG = DATA_DIR / "_imports.log"

@router.post("/import")
async def do_import(file: UploadFile = File(...)):
    data = await file.read()
    svc = get_service()
    res = import_bundle(data, svc.store, svc.registry)
    svc.rebuild()
    _LOG.parent.mkdir(parents=True, exist_ok=True)
    with _LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"added": res.added, "updated": res.updated, "warnings_n": len(res.warnings)}, ensure_ascii=False) + "\n")
    return {"added": res.added, "updated": res.updated, "skipped": res.skipped, "warnings": res.warnings, "counts": _counts(svc)}

@router.get("/imports")
def imports_log():
    if not _LOG.exists():
        return []
    return [json.loads(l) for l in _LOG.read_text(encoding="utf-8").splitlines() if l.strip()]

@router.get("/export")
def do_export(nf: str | None = None, version: str | None = None, domain: str | None = None, scenario: str | None = None):
    svc = get_service()
    z = export_bundle(svc.store, nf=nf, version=version, domain=domain, scenario=scenario)
    return StreamingResponse(io.BytesIO(z), media_type="application/zip",
                             headers={"Content-Disposition": "attachment; filename=assets.zip"})

@router.get("/stats")
def stats():
    svc = get_service()
    return {"object_counts_by_type": _counts(svc), "edge_count": _edge_count(svc),
            "nfs": sorted(svc.index.nfs()), "versions_per_nf": svc.index.versions_per_nf()}

def _counts(svc):
    from collections import Counter
    c = Counter()
    for obj in svc.index.nodes.values():
        c[obj.type] += 1
    return dict(c)

def _edge_count(svc):
    return sum(len(v) for v in svc.index.out.values())
```

> 需在 `Index` 补两个小方法：`nfs()`（返回所有 nf 集合）、`versions_per_nf()`（nf→版本集合）。Task 2.2 的 index.py 末尾补：
```python
    def nfs(self):
        return {o.nf for o in self.nodes.values() if o.nf}
    def versions_per_nf(self):
        from collections import defaultdict
        m = defaultdict(set)
        for o in self.nodes.values():
            if o.nf and o.version:
                m[o.nf].add(o.version)
        return {k: sorted(v) for k, v in m.items()}
```

- [ ] **Step 4: 跑（绿）**。

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/routers/assets.py graph-asset-platform/backend/app/index.py graph-asset-platform/backend/tests/test_api_assets.py
git commit -m "feat(platform): /import /export /imports /stats API" -- graph-asset-platform/
```

### Task 3.3: objects router（/objects, /objects/{id}, /neighbors, /md, /subgraph）

**Files:**
- Create: `app/routers/objects.py`
- Test: `tests/test_api_objects.py`

- [ ] **Step 1: 写测试**

`tests/test_api_objects.py`:
```python
import io, zipfile
from fastapi.testclient import TestClient
from app.main import app
from app.store import Store
from app.registry import Registry
from app.index import Index
import app.service as svc

CMD_EDGES = "---\nid: UDG@MMLCommand@ADD URR\ntype: MMLCommand\nnf: UDG\nversion: 20.15.2\n---\n# x\n## 边\n- 操作配置对象: [[UDG@ConfigObject@URR]]\n"
CFG = "---\nid: UDG@ConfigObject@URR\ntype: ConfigObject\nnf: UDG\nversion: 20.15.2\n---\n# y\n"

def _setup(tmp_data_dir, monkeypatch, files):
    s = svc.Service.__new__(svc.Service)
    s.store = Store(tmp_data_dir); s.registry = Registry.load_default(); s.index = Index.build(s.store, s.registry)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for n, c in files.items(): z.writestr(n, c)
    from app.bundle import import_bundle
    import_bundle(buf.getvalue(), s.store, s.registry)
    s.index = Index.build(s.store, s.registry)
    monkeypatch.setattr(svc, "_service", s)

def test_list_objects(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES, "b.md": CFG})
    with TestClient(app) as c:
        r = c.get("/api/v1/objects", params={"type": "MMLCommand"})
        assert r.status_code == 200
        rows = r.json()
        assert any(o["id"] == "UDG@MMLCommand@ADD URR" for o in rows)

def test_get_object_default_latest(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES})
    with TestClient(app) as c:
        r = c.get("/api/v1/objects/UDG@MMLCommand@ADD URR")  # 不带版本
        assert r.status_code == 200
        assert r.json()["version"] == "20.15.2"

def test_neighbors(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES, "b.md": CFG})
    with TestClient(app) as c:
        r = c.get("/api/v1/objects/UDG@MMLCommand@ADD URR/neighbors", params={"hops": 1})
        assert r.status_code == 200
        out = r.json()["out"]
        assert any(e["to"] == "UDG@ConfigObject@URR" for e in out)

def test_md_raw(tmp_data_dir, monkeypatch):
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES})
    with TestClient(app) as c:
        r = c.get("/api/v1/objects/UDG@MMLCommand@ADD URR/md")
        assert r.status_code == 200
        assert "ADD URR" in r.text
```

- [ ] **Step 2: 跑（红）**。

- [ ] **Step 3: 实现 routers/objects.py**

`app/routers/objects.py`:
```python
from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import PlainTextResponse
from ..service import get_service

router = APIRouter()

@router.get("/objects")
def list_objects(type: str | None = None, q: str | None = None,
                 nf: str | None = None, domain: str | None = None,
                 page: int = 1, size: int = 50):
    idx = get_service().index
    seen = {}
    for (id_, ver), obj in idx.nodes.items():
        if id_ in seen:
            seen[id_]["versions"] = idx.versions_of(id_); continue
        if type and obj.type != type: continue
        if nf and obj.nf != nf: continue
        if domain and obj.domain != domain: continue
        if q and q.lower() not in id_.lower() and q.lower() not in obj.frontmatter.get("name", "").lower(): continue
        seen[id_] = {"id": id_, "type": obj.type, "nf": obj.nf, "domain": obj.domain,
                     "name": obj.frontmatter.get("name"), "versions": idx.versions_of(id_)}
    rows = list(seen.values())
    start = (page - 1) * size
    return rows[start:start + size]

def _resolve(id_: str, version: str | None):
    idx = get_service().index
    obj = idx.resolve_node(id_, version)
    if obj is None:
        raise HTTPException(404, f"对象不存在: {id_}" + (f"（无版本 {version}）" if version else ""))
    return obj

@router.get("/objects/{id_}")
def get_object(id_: str, version: str | None = None):
    obj = _resolve(id_, version)
    idx = get_service().index
    return {**_dump(obj), "versions": idx.versions_of(obj.id), "out_edges": [_dump_edge(e) for e in idx.out_edges(obj.id, obj.version)]}

@router.get("/objects/{id_}/neighbors")
def neighbors(id_: str, hops: int = 1, version: str | None = None):
    obj = _resolve(id_, version)
    idx = get_service().index
    out = [_dump_edge(e) for e in idx.out_edges(obj.id, obj.version)]
    back = [_dump_edge(e) for e in idx.in_edges(obj.id)]
    return {"center": _dump(obj), "out": out, "in": back}

@router.get("/objects/{id_}/md", response_class=PlainTextResponse)
def get_md(id_: str, version: str | None = None):
    return _resolve(id_, version).raw_md

@router.get("/subgraph")
def subgraph(center: str, hops: int = 1, type: str | None = None, version: str | None = None):
    idx = get_service().index
    start = _resolve(center, version)
    visited, nodes, edges = set(), [], []
    frontier = [(start.id, start.version)]
    for _ in range(hops):
        nxt = []
        for (cid, cver) in frontier:
            if (cid, cver) in visited: continue
            visited.add((cid, cver))
            n = idx.node(cid, cver)
            if n: nodes.append(_dump(n))
            for e in idx.out_edges(cid, cver):
                edges.append(_dump_edge(e))
                tv = version or idx.latest_version_of_id(e.to)
                if tv and (e.to, tv) not in visited:
                    nxt.append((e.to, tv))
        frontier = nxt
    return {"nodes": nodes, "edges": edges}

def _dump(o): return {"id": o.id, "type": o.type, "layer": o.layer, "scope": o.scope,
                      "nf": o.nf, "version": o.version, "domain": o.domain, "scenario": o.scenario,
                      "frontmatter": o.frontmatter, "body_md": o.body_md, "source_path": o.source_path}
def _dump_edge(e): return {"from": e.from_id, "from_version": e.from_version, "relation": e.relation, "to": e.to}
```

- [ ] **Step 4: 跑（绿）**。

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/routers/objects.py graph-asset-platform/backend/tests/test_api_objects.py
git commit -m "feat(platform): /objects /objects/{id} /neighbors /md /subgraph API" -- graph-asset-platform/
```

**Chunk 3 完成**：后端 API 全通。派发 plan-document-reviewer 审 Chunk 3。

---

## Chunk 4: 前端（三栏只读浏览器 + 版本选择器）

目标：Vue3+TS 三栏（左索引/中md/右节点图）+ 顶栏（导入导出+版本选择器）。复用 platform-next 的 UI 风格与依赖（Element Plus / vis-network / markdown-it / DOMPurify），但**只建一个 Browser 视图**，不照搬其项目特定 tab。

### Task 4.1: 前端脚手架

**Files:**
- Create: `graph-asset-platform/frontend/package.json`, `vite.config.ts`, `tsconfig.json`, `index.html`
- Create: `src/main.ts`, `src/App.vue`, `src/router.ts`

- [ ] **Step 1: package.json**

```json
{
  "name": "graph-asset-platform-frontend",
  "version": "0.1.0",
  "scripts": {
    "dev": "vite",
    "build": "vue-tsc --noEmit && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "^3.5.0",
    "vue-router": "^4.5.0",
    "element-plus": "^2.9.0",
    "vis-network": "^9.1.0",
    "markdown-it": "^14.0.0",
    "dompurify": "^3.0.0"
  },
  "devDependencies": {
    "vite": "^6.1.0",
    "@vitejs/plugin-vue": "^5.0.0",
    "typescript": "^5.7.0",
    "vue-tsc": "^2.0.0"
  }
}
```

- [ ] **Step 2: vite.config.ts（dev 代理 /api/v1 → 后端 8000）**

```ts
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
export default defineConfig({
  plugins: [vue()],
  server: { proxy: { '/api': 'http://localhost:8000' } },
  build: { outDir: 'dist' },
})
```

- [ ] **Step 3: index.html / main.ts / App.vue / router.ts**（标准 Vue3 入口；router 单路由 `/` → BrowserView；URL 同步 `/o/{id}?version=`）。

- [ ] **Step 4: 安装 + 构建**

Run（`graph-asset-platform/frontend/`）: `npm install && npm run build`
Expected: `dist/` 产出，无 TS 报错。

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/frontend/package.json graph-asset-platform/frontend/vite.config.ts graph-asset-platform/frontend/tsconfig.json graph-asset-platform/frontend/index.html graph-asset-platform/frontend/src
git commit -m "feat(platform): 前端脚手架(Vue3+TS+Vite)" -- graph-asset-platform/
```

### Task 4.2: api client

**Files:** `src/api.ts`

- [ ] 实现 api.ts（全部 fetch `/api/v1/...`；id 经 `encodeURIComponent`，`@`→`%40`、空格→`%20`）：

```ts
const BASE = '/api/v1'
const qs = (p: Record<string, string | undefined>) =>
  '?' + Object.entries(p).filter(([, v]) => v).map(([k, v]) => `${k}=${encodeURIComponent(v!)}`).join('&')

export const listObjects = (p: { type?: string; q?: string; nf?: string; domain?: string; page?: number; size?: number }) =>
  fetch(`${BASE}/objects${qs(p as any)}`).then(r => r.json())
export const getObject = (id: string, version?: string) =>
  fetch(`${BASE}/objects/${encodeURIComponent(id)}${qs({ version })}`).then(r => r.json())
export const neighbors = (id: string, version?: string) =>
  fetch(`${BASE}/objects/${encodeURIComponent(id)}/neighbors${qs({ version })}`).then(r => r.json())
export const getMd = (id: string, version?: string) =>
  fetch(`${BASE}/objects/${encodeURIComponent(id)}/md${qs({ version })}`).then(r => r.text())
export const stats = () => fetch(`${BASE}/stats`).then(r => r.json())
export const importBundle = (file: File) => {
  const fd = new FormData(); fd.append('file', file)
  return fetch(`${BASE}/import`, { method: 'POST', body: fd }).then(r => r.json())
}
export const exportUrl = (f: { nf?: string; version?: string; domain?: string; scenario?: string }) =>
  `${BASE}/export${qs(f as any)}`
```

- [ ] Commit。

### Task 4.3: 三个 pane 组件 + 顶栏

**Files:** `components/ObjectIndex.vue`, `MdPane.vue`, `NeighborGraph.vue`, `VersionSelector.vue`, `TopBar.vue`, `views/BrowserView.vue`

- [ ] **ObjectIndex**：调 `listObjects`，按 `type` 分组（el-tree / 折叠），显示计数；搜索框（`q`）；点击 → emit `select(id)`。
- [ ] **MdPane**：props `id, version`；调 `getObject` + `getMd`；markdown-it 渲染 + DOMPurify（`v-html`）；顶部 type/nf/version badge。
- [ ] **NeighborGraph**：props `id, version`；调 `neighbors`；vis-network 渲染单跳（中心+邻居），邻居点击 → emit `select(id)`；下方邻居清单。
- [ ] **VersionSelector**：调 `stats` 拿 `nfs` + `versions_per_nf`；每 nf 一个下拉（默认=最新）；emit `version(nf, ver)` → 驱动 `?version=`。
- [ ] **TopBar**：导入（el-upload → `importBundle`，成功后刷新）、导出（跳 `exportUrl`）、统计概览、嵌 VersionSelector。
- [ ] **BrowserView**：组合三栏 + 顶栏；URL 同步 `?o={id}&version={v}`。
- [ ] 每个组件写一个最小 vitest 快照或交互测试（可选；v1 以 `npm run build` 通过为底线）。
- [ ] Commit（可合并一个）：
```bash
git add graph-asset-platform/frontend/src
git commit -m "feat(platform): 三栏只读浏览器+版本选择器" -- graph-asset-platform/
```

**Chunk 4 完成**：前端三栏可跑。派发 plan-document-reviewer 审 Chunk 4。

---

## Chunk 5: 样例 bundle + 端到端 + README + 收尾

### Task 5.1: 样例 bundle fixture

**Files:** `backend/tests/fixtures/sample_bundle/`（command/configobject/feature/business 各 2-3 个 md，含 `## 边` wikilink，覆盖跨版本与跨 NF）

- [ ] 用 command 规范的 frontmatter + `## 边` 手写覆盖矩阵（~12 md）：
  - 命令：`UDG@MMLCommand@ADD URR`（双版本 20.15.2 + 20.16.0）、`UDG@MMLCommand@MOD URR`；
  - 配置对象：`UDG@ConfigObject@URR`；ADD URR 的 `## 边` 含 `- 操作配置对象: [[UDG@ConfigObject@URR]]`、`- 参见: [[UDG@MMLCommand@MOD URR]]`；
  - 特性：`UDG@Feature@GWFD-000101`；
  - 业务树：`BusinessDomain@demo`（domain=demo）、`NetworkScenario@charging`（domain=demo,scenario=charging）、`ConfigurationSolution@charging-online`；NS 的 `## 边` 含 `- 方案: [[ConfigurationSolution@charging-online]]`；
  - 悬空边：某命令 `## 边` 含 `- 参见: [[UDG@MMLCommand@NOPE]]`（验证悬空检测）。
- [ ] 在 conftest.py 加 `sample_bundle` fixture（返回该目录路径或 zip 字节）。
- [ ] 写 e2e 测试：import sample_bundle → 校验 stats 计数、单对象、neighbors（含反链）、版本切换（默认最新现存 + `?version=` 指定/不存在→404）、悬空告警。
- [ ] Commit。

### Task 5.2: README + 启动说明

**Files:** `graph-asset-platform/README.md`

- [ ] 写：定位、与 assets/ 解耦、资产格式（引用 spec）、启动（`pip install -e ".[dev]"`、`npm install && npm run build`、`uvicorn app.main:app`）、API 速查、提交注意（git 陷阱）。
- [ ] Commit。

### Task 5.3: 验收清单核对（对照 spec §14）

- [ ] 逐条核对 spec §14 的 7 条验收标准，跑全量 `pytest -q` + 前端 `npm run build` + 手动 import sample_bundle 浏览。
- [ ] 确认无业务名硬编码（grep charging/bandwidth/SFCGraph 在 `graph-asset-platform/`）。
- [ ] Commit（如有修复）。

**Chunk 5 完成** → 派发 plan-document-reviewer 审 Chunk 5 → 全 plan 审通过 → 执行交接（subagent-driven-development）。

---

## Plan Review Loop

每完成一个 Chunk，派发 plan-document-reviewer 子代理（见 skill 的 plan-document-reviewer-prompt.md），提供：该 chunk 内容 + spec 路径 `docs/superpowers/specs/2026-07-16-graph-asset-platform-design.md`。❌ Issues Found → 修 → 再审，直到 ✅ Approved 再进下一 chunk。超过 5 轮上报人工。

## Execution Handoff

Plan 完成并保存到 `docs/superpowers/plans/2026-07-16-graph-asset-platform.md` 后：

> "Plan complete and saved to `docs/superpowers/plans/2026-07-16-graph-asset-platform.md`. Ready to execute?"

本 harness 有 subagents → **使用 superpowers:subagent-driven-development**（每 task 一个 fresh subagent + 两阶段 review）执行。
