# 命令图谱：抽取 + 前端展示 规划

## Context

从 MML 产品文档（UDG ~4000+ 文件 + UNC ~500+ 文件）中批量抽取命令和参数，生成结构化数据，然后前端展示。

## 数据源

- **UDG**: `output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/`
- **UNC**: `output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/`
- 每个 md = 一条 MML 命令，格式：命令功能 → 注意事项 → 操作用户权限 → 参数说明（表格） → 使用实例

## Phase 1: 抽取脚本

输出目录: `command-graph/data/`

### Step 1: `step1_scan_commands.py` — 命令扫描
- 扫描全部 md 文件，提取命令基本信息和各章节内容
- 输出: `data/raw_commands.csv`

### Step 2: `step2_extract_params.py` — 参数抽取
- 解析参数说明表格，拆分可选必选/前提条件/取值范围/默认值/配置原则
- 输出: `data/raw_parameters.csv`

### Step 3: `step3_derive_objects.py` — 推导配置对象
- 按 object_keyword 聚合，ADD 命令参数 → 配置对象属性
- 输出: `data/config_objects.csv`, `data/cmd_object_relations.csv`

### Step 4: `step4_extract_deps.py` — 依赖关系
- 同命令/跨命令参数依赖，命令顺序约束
- 输出: `data/param_dependencies.csv`, `data/cmd_ordering.csv`

### Step 5: `step5_extract_rules.py` — 规则抽取
- 从注意事项提取唯一性/数量/删除保护/性能等规则
- 输出: `data/command_rules.csv`

### Step 6: 质量报告
- 输出: `data/extraction_report.md`

## Phase 2: 后端 API

修改 `platform-next/command_graph/router.py`，复用 `platform-next/shared/csv_service.py`

## Phase 3: 前端展示

Vue3 + Element Plus，两个视图：命令视图 + 配置对象视图
