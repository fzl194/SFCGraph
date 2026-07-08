# index · assets/ 内容目录

> **Agent 每次 Compile/Ingest 必须更新本文件。** Query 时先读这里定位。
> 顶层只导航到**层 / {nf}/{version} 局部 index**——具体对象清单在各局部 index（避免单文件膨胀）。
> 规则见 `CLAUDE.md` §6/§8。

---

## 业务层（BusinessDomain / NetworkScenario / ConfigurationSolution）
<!-- 跨产品两段式 ID，不带 nf@version。P4 待建。 -->
<!-- 例：- [ConfigurationSolution@charging-converged](business/business-awareness/charging/ConfigurationSolution@charging-converged.md) -->

_未建（P4 LLM 凝练 + 人审）_

---

## 特性层（Feature / License）

- 特性（Feature）· UDG/20.15.2 → [局部 index](feature/UDG/20.15.2/index.md)（313 节点）
- 特性（Feature）· UNC/20.15.2 → [局部 index](feature/UNC/20.15.2/index.md)（629 节点）
- License 控制项 · UDG/20.15.2 → [局部 index](license/UDG/20.15.2/index.md)（187 节点）
- License 控制项 · UNC/20.15.2 → [局部 index](license/UNC/20.15.2/index.md)（448 节点）

---

## 命令层（MMLCommand / ConfigObject，参数内聚）

- 命令（MMLCommand）· UDG/20.15.2 → [局部 index](command/UDG/20.15.2/index.md)
- 命令（MMLCommand）· UNC/20.15.2 → [局部 index](command/UNC/20.15.2/index.md)
- 配置对象（ConfigObject）· UDG/20.15.2 → [局部 index](configobject/UDG/20.15.2/index.md)
- 配置对象（ConfigObject）· UNC/20.15.2 → [局部 index](configobject/UNC/20.15.2/index.md)

---

## 任务层（Task，rule+决策点内嵌）

_未建（P5 LLM 凝练 + 人审；建后回填命令 md 的 `[[Task ID]]` 占位）_

---

## Skill

_未建（P6 切换：拷入 SOP + knowledge，服务化取包）_

---

## Schema（各对象类型 typed 模板）

- 三层图谱定义（自包含拷贝）→ [schema/三层图谱定义.md](schema/三层图谱定义.md)
- 特性层对象与关系定义（开发期源）→ `../FeatureGraph/特性层对象与关系定义.md`（只读，不进 assets 运行时）

---

## Compile 器（scripts/）

- [compile_commands.py](scripts/compile_commands.py) — 命令层纯投影
- [compile_configobjects.py](scripts/compile_configobjects.py) — ConfigObject 反向枢纽
- [compile_features.py](scripts/compile_features.py) — 特性层纯投影
- [compile_licenses.py](scripts/compile_licenses.py) — License 纯投影（反向链 Feature）
