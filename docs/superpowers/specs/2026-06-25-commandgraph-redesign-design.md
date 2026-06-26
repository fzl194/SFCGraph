# 命令图谱重构设计（CommandGraph）

- **日期**：2026-06-25
- **范围**：仅命令图谱（business / feature 图谱不动）
- **状态**：设计待评审

## 1. 背景与动机

命令图谱的**抽取能力已验证可用**（MMLCommand、CommandParameter 两个对象跑通），但整条链路存在四类痛点：

| 痛点 | 现状证据 |
|---|---|
| 2.1 网元/版本资产未隔离 | 产物平铺为 `data/output/mml_commands_{udg,unc}.jsonl`，仅靠文件名后缀区分；网元/版本靠命令行参数 `--nf --version` 手工传入，无配置化 |
| 2.2 流水线断点、缺主入口 | 4 个脚本（`md_reader`→`build_mmlcommand`→`enrich_mmlcommand`→`build_commandparameter`）必须手工逐个跑，顺序靠人记，参数多处重复 |
| 2.3 前端缺三级导航 | `CommandList.vue` 是带筛选器的平铺表格，无统计面板/网元卡片/版本卡片 |
| 2.4 设计态+前后端过度定制化 | 章节映射、派生正则、CSV 列名、绝对路径全硬编码；`service.py:16-18` 无视 `config.yaml` 直接硬编码路径与两个文件名；字段命名 `product`/`nf`/`ne` 三套混用 |

## 2. 已锁定决策

| 决策项 | 结论 |
|---|---|
| 范围 | 只命令图谱 |
| 隔离模型 | 网元目录 → 版本目录 → 资产 |
| 资产布局 | 每对象一个 JSONL |
| 一键入口 | 单根 `pipeline.yaml` + `build_all.py [nf] [version]` |
| 字段管理 | 混合：基本信息固定 core / 章节字段进 `sections.yaml` / 派生字段进 `extractors/` 注册函数 |
| 前端导航 | 统计面板 → 网元卡片 → 版本卡片 → 命令列表；版本内搜索 + 面包屑 |
| 字段命名 | **统一用现有 JSON 字段名 `nf`**（数据字段不动；API/前端 `product`→`nf`） |
| 新目录 | 新建干净目录 `CommandGraph/`（设计态 only）；platform-next 后端/前端就地重构读 `CommandGraph/assets` |
| 落地路径 | A 分层自底向上（Phase1 数据层 → Phase2 后端 → Phase3 前端），每层独立可验收 |
| 关键约束 | 抽取逻辑已验证可用 → **只重构组织方式，保留已验证的抽取代码** |

## 3. Phase 1：数据层重构（新建 `CommandGraph/`）

### 3.1 新目录结构

```
SFCGraph/
├── CommandGraph/                       ← 新建：干净的设计态
│   ├── pipeline.yaml                   ← 唯一配置入口
│   ├── build_all.py                    ← 一键编排入口
│   ├── builder/
│   │   ├── core/
│   │   │   └── identity.py             ← 基本信息推导（nf/version/command_id/verb/object_keyword/status）
│   │   ├── sections.yaml               ← 章节标题→字段名（从旧 md_reader.py:19-35 _SECTION_TO_FIELD 搬出）
│   │   ├── extractors/                 ← 派生字段注册制（从旧 enrich_mmlcommand.py 的 10 个函数搬出）
│   │   │   ├── registry.py             ← 注册表 + 统一调用
│   │   │   ├── command_category.py
│   │   │   ├── applicable_nf.py
│   │   │   ├── is_dangerous.py
│   │   │   └── ...（每个派生字段一个文件）
│   │   ├── steps/                      ← 流水线步骤（保留已验证逻辑）
│   │   │   ├── mmlcommand.py           ← 复用 build_mmlcommand + md_reader（改读 sections.yaml）
│   │   │   ├── enrich.py               ← 遍历 extractors registry 跑所有派生字段
│   │   │   ├── parameter.py            ← 复用 build_commandparameter（路径改读 pipeline.yaml）
│   │   │   └── ...                     ← 后续叠加：config_object.py / command_rule.py
│   │   └── constants.py                ← 路径/魔数集中（去掉 D:/mywork 绝对路径、-2 魔数）
│   └── data/
│       └── assets/                     ← 隔离产物（替代旧 data/output 平铺）
│           ├── UDG/20.15.2/{mml_commands,command_parameters,command_has_parameter,parameter_depends_on}.jsonl
│           └── UNC/20.15.2/mml_commands.jsonl
├── command-graph/                      ← 旧，保留参考，验证后删
└── platform-next/command_graph/        ← 后端/前端就地重构（见 Phase 2/3）
```

**复用/参考关系**：从旧 `command-graph/builder/` 拷贝 `md_reader.py`、`build_mmlcommand.py`、`enrich_mmlcommand.py`、`build_commandparameter.py` 的核心逻辑到新结构，重新组织而非重写。

### 3.2 `pipeline.yaml` 形态

```yaml
assets_root: data/assets
project_root: ..                         # source 相对它计算（替代写死的 D:/mywork）
ne:
  UDG:
    20.15.2:
      source: output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令
      steps: [mmlcommand, enrich, parameter]
      parameter_csv: data/kgdata/UDG_命令参数.csv   # 可选，parameter 步骤才用
  UNC:
    20.15.2:
      source: output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令
      steps: [mmlcommand, enrich]
```

源 MD 仍在根级 `output/` 下不动；`project_root: ..` 指向 `SFCGraph/` 根。

### 3.3 `build_all.py` 编排

```
python build_all.py                # 全量
python build_all.py UDG            # 单网元（所有版本）
python build_all.py UDG 20.15.2    # 单版本
```

- 读 `pipeline.yaml` → 按 `(nf, version)` 迭代 → 依序跑 `steps` → 写 `assets/{nf}/{version}/`
- 强制步骤顺序（先 `mmlcommand` 才能 `enrich`/`parameter`），缺前置自动报错
- 单个 `(nf, version, step)` 失败不影响其他网元，错误明确指到三元组
- 幂等：`enrich` 可重算覆盖（沿用现有机制）

### 3.4 字段可变性落地（混合模式）

- **基本信息**：固定在 `core/identity.py`（nf/version/command_id/command_name/command_name_zh/verb/object_keyword/status/source_evidence_ids/category_path）
- **章节字段**：`sections.yaml` 声明"MD 章节标题→字段名"映射（含别名与前缀匹配，沿用 `md_reader.map_section` 逻辑）；加减章节字段只改 YAML
- **派生字段**：每个派生字段一个 `extractors/*.py`，在 `registry.py` 注册；`enrich` 步骤遍历 registry 调用全部已注册 extractor（每个返回 immutable 新 dict）。加减派生字段 = 加一个文件 + 注册一行
- **新增对象类型**（ConfigObject/CommandRule 等）：加 `steps/xxx.py` + `pipeline.yaml` 的 `steps` 列表加一项；产物自动落对应 jsonl

## 4. Phase 2：后端重构（`platform-next/command_graph/`）

### 4.1 数据加载去硬编码（核心）

- `service.py` 从 `config.yaml` 读 `command_graph.assets_root`（新指向 `../CommandGraph/data/assets`），**删除**第 16-18 行硬编码的 `command-graph/data/output` 与第 25-28 行写死的两个文件名
- 启动时**扫描** `assets_root/{nf}/{version}/*.jsonl`：自动发现所有网元、版本、对象类型；新增网元/版本/对象 = 丢文件 + 重启即识别，不改代码
- 内存按 `(nf, version, object_type)` 索引；MMLCommand、CommandParameter、关系边分类型加载
- **修复反模式**：当前 `config.yaml` 已有 `command_graph.data_dir` 但 `service.py` 完全无视它——这次把配置真正用起来

### 4.2 统一字段命名（`product` → `nf`）

全链路统一用 `nf`（数据字段名保持不变）：

- `router.py` 所有端点的 `product` 参数 → `nf`
- `service.py` 内部 `product` 变量 → `nf`；删除 `_slim` 里 `nf→product` 的映射（`service.py:68`）
- `/stats` 返回 `by_nf`（替代 `by_product`）

### 4.3 API 调整（6 端点保留，参数/返回优化）

| 端点 | 改动 |
|---|---|
| `GET /stats` | 返回**嵌套结构**直接驱动 L1+L2：`{total, total_parameters, nes:[{name, command_count, parameter_count, versions:[{version, command_count, parameter_count}]}]}` |
| `GET /commands` | `product`→`nf`；`nf + version + search + page + size` |
| `GET /command` | `product`→`nf`；`nf + command_name + version` |
| `GET /command-md` | `product`→`nf` |
| `GET /doc-content`、`/file` | 路径走 config 的 `doc_root`，契约不变 |

### 4.4 配置

```yaml
# platform-next/config.yaml
command_graph:
  assets_root: "../CommandGraph/data/assets"   # 新（替代被忽略的 data_dir）
  doc_root: ".."                                # 保留
```

## 5. Phase 3：前端重构（`platform-next/frontend/src/command_graph/`）

### 5.1 路由重构为漏斗

```
/command-graph                              CommandIndex（壳 + 面包屑 + router-view）
  ├── ''                                    → CommandOverview    L1 统计面板 + 网元卡片
  ├── ':nf'                                 → CommandVersions    L2 该网元的版本卡片
  └── ':nf/:version'                        → CommandList        L3 命令列表（版本内搜索）
/command-graph/:nf/:version/:commandName    → CommandDetail      详情（双栏，已动态）
```

### 5.2 组件新增/改造

| 组件 | 动作 | 说明 |
|---|---|---|
| **CommandOverview.vue** | 新建（L1） | 调 `/stats`，渲染统计数字（总命令/网元数/版本数/参数数）+ 网元卡片网格（网元名/版本数/命令数）；点卡 → `/:nf` |
| **CommandVersions.vue** | 新建（L2） | 从 `/stats` 嵌套结构取选中网元的版本卡片（版本号/命令数/参数数）；点卡 → `/:nf/:version` |
| **CommandList.vue** | 改造（L3） | **删掉**顶部 product/version 筛选器（范围已被路由固定），**保留**搜索框（版本内）；调 `/commands?nf=&version=`；点行 → 详情 |
| **CommandDetail.vue** | 小改 | 路由 param `product`→`nf`、补 `:version`；双栏动态展示**不动** |
| **CommandIndex.vue** | 小改 | 加面包屑（统计 > {nf} > {version}），`router-view` 留子路由 |

### 5.3 命名统一（`product` → `nf`）

- 路由 param `product` → `nf`
- `api.ts`：`command(product,…)` → `command(nf,…)`，参数键用 `nf`；`commandMd` 同理
- `CommandList.vue`：`filters.product` → `filters.nf`，`stats.by_product` → `stats.by_nf`

### 5.4 字段动态展示（保留现状，不回退）

- **CommandDetail** 的 `sections` 动态遍历 + LABEL_MAP 装饰（`CommandDetail.vue:130-139`）满足"所有字段不藏、加字段自动出现"——**保持不动**
- **CommandList** 列表保留"基本信息列"（命令/中文名/版本/分类/功能），全字段交给详情
- DocViewer / 原始文档右栏：契约不变（`api-base="command-graph"`，后端 `/doc-content`、`/file` 不动）

## 6. 迁移、测试与上线节奏

### 6.1 数据迁移与对比验证

- 新 pipeline 跑一遍 UDG/UNC → 生成 `CommandGraph/data/assets/{UDG,UNC}/20.15.2/*.jsonl`
- **对比验收**：新 assets 的命令数、各派生字段非空率，与旧 `data/output/mml_commands_{udg,unc}.jsonl` 逐一核对（`enrich` 步骤本身已打印非空率）
- 旧 `command-graph/` 保留至 Phase 2 后端验证通过后再清理

### 6.2 跨 Phase 的 API 兼容（保证每层独立可验收）

- **Phase 2**：后端 `nf` 为主参数，**`product` 作为兼容别名**同时接受；旧前端继续可用
- **Phase 3**：前端全面切 `nf`
- **收尾**：删除 `product` 别名

### 6.3 测试策略

| 层 | 测试 |
|---|---|
| 设计态 | 保留 `tests/test_build_commandparameter.py`；新增 pipeline 编排单测（选性执行 / 步骤顺序校验 / 单步失败隔离）、extractors registry 单测（注册即被 enrich 调用） |
| 后端 | service 单测：扫描 assets/ 发现 nf/version/object、stats 嵌套结构、nf+version 过滤、版本内搜索（小型 assets fixture） |
| 前端 | 漏斗路由可点通（L1→L2→L3→详情）、面包屑回退、版本内搜索 |

### 6.4 上线节奏（每个 Phase 可独立验收）

1. **Phase 1**：建 `CommandGraph/` 设计态 → 跑出 assets → 对比验证 ✅
2. **Phase 2**：后端切 assets/ + 去硬编码 + stats 嵌套 + `nf`（带 `product` 别名）→ 旧前端仍跑 ✅
3. **Phase 3**：前端漏斗 + 面包屑 + 版本内搜索 + 切 `nf` → 删别名 ✅

## 7. 不在本次范围

- business_graph / feature_graph 模块（每层图谱结构不同，本次不统一抽象）
- 命令图谱新对象类型的实际抽取（ConfigObject / CommandRule）——架构留好扩展点，具体抽取后续叠加
- 网元实例维度（如 UDG-01）、环境隔离（dev/test/prod）、版本演进链

## 8. 风险与缓解

| 风险 | 缓解 |
|---|---|
| 重构破坏已验证的抽取逻辑 | 只搬不改：拷贝原函数到新结构，对比验证命令数与字段非空率一致才算通过 |
| Phase 2 命名改动打断旧前端 | `product` 兼容别名，Phase 3 完成后才移除 |
| `sections.yaml` 别名/前缀匹配行为漂移 | 直接移植 `md_reader.map_section` 的精确+前缀两段逻辑，配单测覆盖脏数据标题 |
| 派生 extractor 注册遗漏 | registry 单测：断言每个已注册 extractor 被 `enrich` 调用且返回 immutable dict |
