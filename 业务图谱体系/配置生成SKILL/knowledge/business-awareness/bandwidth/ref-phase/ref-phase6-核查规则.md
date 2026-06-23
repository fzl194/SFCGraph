# Phase 6 参考文件：配置核查（图谱规则·本地降级）

> **定位变更**（配置生成 SKILL）：真实配置核查调 `knowledge/common/AI-MML核查流程.md`（coremaster configcheck 接口，内网执行）。本文档的图谱核查规则（BR-BW / CR-BW / TR-BW）承担两个角色：
> 1. **Phase 5 配置生成时的内置约束** — 生成命令时即遵守，避免核查返工
> 2. **非内网环境的静态核查降级** — 作为 `AI-MML核查流程.md §6` 的规则来源
>
> 内网部署优先调 AI MML 核查接口；非内网用本规则做静态核查。

---

## ⚠ 阶段执行约束（必须遵守）

**本文件仅用于 Phase 6。执行本文件内容前必须满足以下前置条件，否则 STOP：**

1. **必须有 Phase 5 生成的配置脚本**：必须有已生成的 MML 配置脚本。如果没有，**STOP**，回到 Phase 5 先生成配置。
2. **核查完成后必须 STOP**：核查通过后，**必须将核查报告和配置脚本展示给用户并停止执行**，等待用户在 GATE-5 确认。不得直接交付给用户。

---

> 本文件定义 Phase 6 的 pipeline 要求、SKILL特有的操作安全检查和输出模板（带宽控制场景专属）。
> 业务规则核查（图谱规则、配置依赖、知识库规则、跨网元一致性）由 Agent 从图谱动态加载执行。

---

## 1. Pipeline 步骤

### Step 1: 加载核查规则

**必须加载**：
- `01-business-graph.md` §4 — 读取 BusinessRule (BR-BW-01~06)，逐条核查
- `04-command-graph.md` §4 — 读取 CommandRule (CR-BW-01~05)，逐条核查
- `03-task-layer.md` §8 — 读取 TaskRule (TR-BW-01~06)，逐条核查
- `../业务感知域规则.md` — 域共享规则（REFRESHSRV 时序、RULE PRIORITY、三网元一致、SA 前置），逐条核查
- `kb/02-CAR限速参数.md` + `kb/05-FUP配额降速.md` + `kb/06-GBR带宽保证.md` — 知识库级约束（按方案加载）

> **核查依据必须是图谱中定义的规则实例（BR-BW-xx / CR-BW-xx / TR-BW-xx），不可凭记忆。**

### Step 2: 执行图谱规则核查

逐条检查加载的 BusinessRule / CommandRule / TaskRule，记录通过/违反项。

**BusinessRule (BR-BW，6 条)**：
| 规则 ID | 规则名 | 核查要点 | 严重级别 |
|---------|--------|---------|---------|
| BR-BW-01 | 预定义规则三网元一致性 | 动态 PCC 场景 RULENAME+参数+FlowFilter 在 PCF/SMF/UPF 三处完全一致 | critical |
| BR-BW-02 | 超额降速优先级覆盖 | FUP 降速规则 PRIORITY 最高且 FlowFilter 完全覆盖原规则 | critical |
| BR-BW-03 | BWM与PCC独立匹配 | BWM 规则与 PCC 规则可叠加，不可误删其一 | warning |
| BR-BW-04 | RULENAME跨策略类型不冲突 | 同产品内 PCC 与 QOS 的 RULENAME 不能同名 | critical |
| BR-BW-05 | REFRESHSRV最后执行 | UDG 侧 SET REFRESHSRV 必须在所有策略配置之后，约 60 秒生效 | info |
| BR-BW-06 | License前置门控 | 对应特性 License 必须开启（UDG/UNC 独立编号体系） | critical |

**CommandRule (CR-BW，5 条)**：
| 规则 ID | 规则名 | 核查要点 | 严重级别 |
|---------|--------|---------|---------|
| CR-BW-01 | RULENAME跨POLICYTYPE不冲突 | PCC 类型 RULENAME 与 QOS 类型 RULENAME 不能相同；BWM 与 CHARGING 可同名 | critical |
| CR-BW-02 | BWMCONTROLLER CTRLTYPE决定参数集 | CAR 用 CIR/PIR/CBS/PBS，SHAPING 用 RATE/QUEDEPTH，两者互斥 | critical |
| CR-BW-03 | CAR与Shaping不可同对象叠加 | 同一 BWMSERVICE 不能同时绑 CAR 和 Shaping 控制器 | warning |
| CR-BW-04 | REFRESHSRV后60秒生效 | REFRESHSRV 必须最后执行，PROTBINDFLOWF 定时器约 60 秒 | info |
| CR-BW-05 | 预定义规则名全网唯一 | 动态 PCC 场景 RULENAME 三处一致；ADC 场景 FLOWFILTERNAME/appid 三处一致 | critical |

**TaskRule (TR-BW，6 条)**：
| 规则 ID | 规则名 | 核查要点 | 严重级别 |
|---------|--------|---------|---------|
| TR-BW-01 | REFRESHSRV时序约束 | SET REFRESHSRV 在所有 BWM/FILTER/策略配置之后 | critical |
| TR-BW-02 | BWMSERVICE→BWMCONTROLLER前置 | 先 ADD BWMSERVICE 再 ADD BWMCONTROLLER，BWMRULE 引用两者 | critical |
| TR-BW-03 | URR→URRGROUP→PCCPOLICYGRP三件套链 | FUP 三件套按序配置，断裂则 FUP 不生效 | critical |
| TR-BW-04 | QoS URR模式校验 | QoS 保证 URR.USAGERPTMODE=QOS；FUP 为 ONLINE/MONITORINGKEY；不可混用 | critical |
| TR-BW-05 | ADC三策略组完整性 | ADC 必须配 Normal/Start/Stop 三策略组 | warning |
| TR-BW-06 | 预定义规则全网一致性前置 | 预定义 RULENAME 在 PCF/SMF/UPF 三侧同名同参；PCC 与 QOS RULENAME 不同名 | critical |

### Step 3: 执行 SKILL 独有的操作安全检查

以下检查项不在图谱中，由本 SKILL 独有提供：

| 核查项 | 规则 | 严重级别 |
|--------|------|---------|
| 同名冲突 | 新增 BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE/RULE 名是否与现网同名 | HIGH |
| 参数覆写 | SET/MOD 命令是否覆盖了现网仍在使用的参数（特别是 BWMCONTROLLER 的 CIR/PIR、QOSPROP 的 GBR） | HIGH |
| 共享对象影响 | 修改被多个 BWMRULE 引用的 BWMCONTROLLER 时，是否评估影响范围 | HIGH |
| 删除安全 | RMV 命令是否先解绑了上层引用（如 RMV BWMCONTROLLER 前先 RMV 引用它的 BWMRULE） | CRITICAL |
| 三色动作合理性 | GREENACT/YELLOWACT/REDACT 组合是否符合业务价值（低价值不应全 PASS） | MEDIUM |

### Step 4: 跨网元一致性核查（仅 DP-BW-08 包含 UDG+UNC 时）

**必须加载**：
- `../业务感知域规则.md §2` — 跨网元一致性（业务感知特有）
- `04-command-graph.md` CommandRule CR-BW-05（预定义规则名全网唯一） — 逐条核查
- `01-business-graph.md` BusinessRule BR-BW-01（预定义规则三网元一致性） — 逐条核查

**重点核查项**（均为 CRITICAL）：
- RULENAME 在 PCF/SMF/UPF 三处完全一致
- ADC 场景 FLOWFILTERNAME/appid 三处一致
- 双产品共用参数（URRID、VOLUMETHRESHOLD）UDG ↔ UNC 一致
- POLICYNAME 跨策略类型（PCC/BWM/QOS/ADC）不冲突

### Step 5: 循环修正

- 发现问题 → **自动修正**并告知用户修正内容
- 无法自动修正 → **暂停并要求用户决策**
- 修正后重新从 Step 2 执行，直到全部通过

---

## 2. 输出格式模板

```markdown
## 核查报告

### 核查结果: {通过 / 已修正}

| 维度 | 规则来源 | 检查项数 | 通过 | 修正 | 待确认 |
|------|---------|---------|------|------|--------|
| BusinessRule | 01-business-graph.md §4 | {n} | {n} | {n} | {n} |
| CommandRule | 04-command-graph.md §4 | {n} | {n} | {n} | {n} |
| TaskRule | 03-task-layer.md §8 | {n} | {n} | {n} | {n} |
| 域共享规则 | ../业务感知域规则.md | {n} | {n} | {n} | {n} |
| 操作安全 | ref-phase6 §1.3 | {n} | {n} | {n} | {n} |

### 修正日志
1. [{规则ID}] {问题描述} → {修正动作}
2. ...
```

---

## 3. 注意事项

- 每条违反项必须标注对应的规则 ID（BR-BW-xx / CR-BW-xx / TR-BW-xx），不可笼统描述
- 图谱规则是业务准确性的保障，必须从图谱原文加载执行，不可省略或简化
- 操作安全检查（§1.3）是图谱未覆盖的生产环境保护，同样不可跳过
- 跨网元一致性检查中，RULENAME/FLOWFILTERNAME 一致性均为 CRITICAL 级别，任一不一致都必须修正
- 带宽场景与计费场景共享 RULE/USERPROFILE/PCCPOLICYGRP/FLOWFILTER/URR 等对象族，修改时需评估对计费场景的连带影响
