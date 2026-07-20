# scripts/ — 构建管线

> 原始产品文档 → 三层图谱资产的脚本链。本规范包的执行工具。

---

## 核心认知

本规范的**输入起点是原始产品文档**（华为 HDX/HWICS 归档），不是已导出的 md。
因此脚本链从"产品文档导出"开始，**不是**从中间态（output/ 或 jsonl）开始。

---

## 管线全貌（5 阶段）

| 阶段 | 脚本 | 输入 → 输出 | 状态 |
|---|---|---|---|
| **0 导出** | `product_doc_md_exporter_optimized.py` | HDX/HWICS 归档 → `output/` md + 映射表 | ✅ 已纳入 |
| **1 命令图构建** | （原 `CommandGraph/build_all.py`） | output/ md → 命令/配置对象 jsonl | ⬜ 待纳入（随命令层） |
| **2 特性图构建** | （原 `FeatureGraph/build_all.py`） | output/ md → 特性/license jsonl | ⬜ 待纳入（随特性层） |
| **3 wiki 编译** | （原 `assets/scripts/compile_*.py`） | jsonl → typed wiki md | ⬜ 待纳入（随各层） |
| **4 核查** | （原 `assets/scripts/lint_*.py`） | wiki md → 问题报告 | ⬜ 待纳入（随核查流程） |

---

## 纳入原则

1. **随层纳入**：每个脚本随它服务的对象类型一起纳入（命令层脚本随命令层、特性层随特性层）。
2. **唯一源（目标）**：纳入默认移入本目录，本目录成为唯一源。**过渡期可保留原位置副本**（不破坏现有流程），待规范包验证为唯一源后再删原副本（防漂移）。
3. **引用同步**：纳入后，原位置的引用更新指向本目录。

---

## 阶段 0：产品文档导出（已纳入）

| 项 | 值 |
|---|---|
| 脚本 | `product_doc_md_exporter_optimized.py`（1328 行） |
| 输入 | 华为 HDX/HWICS 归档（`.hwics` / `.hdx`，HTML 文档打包格式） |
| 输出 | Markdown 文件树 + `html_to_md_mapping.json`（HTML→MD 路径映射） |
| 依赖 | `chardet`、`beautifulsoup4` |
| 入口函数 | `main(hdx_file)` 归档→md；`main_from_extracted(extracted_dir, output_dir)` 已解压→md；`main2(input_dir, output_dir)` 纯 HTML 批量→md |
| 纳入方式 | 复制（根目录原文件保留，过渡期双存，待规范包验证为唯一源后删根目录副本） |

> 脚本的完整 CLI 契约、与阶段 1（命令图构建）的衔接细节，**随命令层共创时补完**。
