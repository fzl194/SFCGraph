# Phase 1 参考文件：需求理解与图谱匹配

## ⚠ 阶段执行约束（必须遵守）

**本文件仅用于 Phase 1。执行本文件内容前必须满足以下前置条件，否则 STOP：**

1. **现网脚本必须已验证存在**：必须已通过 GATE-1（用户提供路径）和 GATE-2（用工具验证文件存在）。如果现网脚本未验证，**STOP**，要求用户提供现网配置脚本文件路径。
2. **本阶段完成后必须 STOP**：执行完 §1~§3 后，**必须将匹配结果展示给用户并停止执行**，等待用户在 Phase 2（GATE-3）确认。不得自动进入参数收集或配置生成。
3. **禁止在本阶段生成任何 MML 配置命令**：本阶段只做场景匹配和现网分析，不生成配置。

---

> 本文件定义 Phase 1 的 pipeline 要求、输出模板和操作规则（带宽控制场景专属）。
> 业务知识（决策点定义、配置对象体系、场景关键词）由 Agent 从图谱和知识库动态加载。

---

## 1. Pipeline 步骤

### Step 1: 场景识别

**操作**：从用户需求中提取带宽控制相关关键词，匹配到业务图谱的 NetworkScenario。

**必须加载**：
- `three-layer-graph/01-business-graph.md` — 读取 NetworkScenario (NS-BW-01) 和 ConfigurationSolution (CS-BW-01~07) 定义
- `kb/01-BWM控制体系.md` + `kb/03-核心术语定义.md` — 理解用户提到的带宽控制术语

**场景关键词样例**（匹配到 NS-BW-01）：
- 控制机制：限速、整形、令牌桶、CAR、Shaping、降速、门控、阻断
- 控制维度：按业务、按用户等级、按套餐配额、按应用、按位置区域、按小区负荷
- 带宽参数：CIR/PIR/CBS/PBS、RATE/QUEDEPTH、MBR/GBR、VolumeThreshold
- 典型场景：FUP超量降速、P2P限速、视频GBR保证、ADC应用带宽、漫游限速、拥塞动态限速

**输出**：匹配到的场景 ID、方案 ID（CS-BW-01~07 之一或组合）。

**规则**：
- 7 个方案闭包按控制机制划分，见 `01-business-graph.md` §2：CS-BW-01 SA-BWM / CS-BW-02 FUP降速 / CS-BW-03 GBR保证 / CS-BW-04 ADC动态带宽 / CS-BW-05 小区负荷 / CS-BW-06 位置区域 / CS-BW-07 无线优化标记
- 如同时涉及计费（差异化计费/配额计费动作）或访问限制（URL过滤/重定向阻断），提醒用户本 SOP 仅处理带宽控制部分
- 匹配不到时，向用户确认是否属于带宽控制场景

### Step 2: 网元与决策点解析

**操作**：从用户描述中提取决策点答案，缺失时追问。

**必须加载**：
- `01-business-graph.md` — 读取 DecisionPoint (DP-BW-01~08) 的完整定义、选项和影响
  - DP-BW-01 控制机制选择 → 决定 CS 闭包与 BWMCONTROLLER.CTRLTYPE 或 QOSPROP 路径
  - DP-BW-02 控制粒度 → 决定 BWMRULETYPE（SUBSCRIBER_SPECIFIC / GROUP_SPECIFIC / GLOBAL）和 URR 绑定方式
  - DP-BW-03 规则类型 → 决定配置路径（动态/预定义/本地）和三网元一致性要求；定向业务必须用预定义
  - DP-BW-04 接口代际 → 决定参数体系（QCI/MBR vs 5QI/Session-AMBR）；Gx FUP 需额外配 UMCH
  - DP-BW-05 BWM控制类型 → 决定 BWMCONTROLLER 参数模式（CIR/PIR/CBS/PBS vs RATE/QUEDEPTH）
  - DP-BW-06 FUP累计粒度 → 决定 URR 的 Monitoring-Level（SESSION_LEVEL vs PCC_RULE_LEVEL）
  - DP-BW-07 应用识别需求 → 决定规则类型与 SA 依赖
  - DP-BW-08 产品面分工 → 决定配置入口（UDG执行面 / UNC控制面 / 双产品协作）

**规则**：
- 缺少决策信息时**必须追问**，追问时引用图谱中各选项的含义和影响
- DP-BW-08（产品面分工）无法判断时，BWM 场景默认双产品协作（UDG+UNC），GBR/QoS 可仅 UDG 触发上报

### Step 3: 现网配置解析

**操作**：按对象类型分批提取带宽控制相关命令，构建结构化对象清单。

**必须加载**：
- `04-command-graph.md` — 读取 ConfigObject 定义（29 个），理解 BWM 三级控制层次和依赖关系

**现网脚本分三轮扫描**：

第1轮 UDG(UDG)侧 — BWM 独有体系 + 基础门控：
```
Pattern: ^(ADD|SET|MOD|RMV) +(LICENSESWITCH|BANDWIDTHMNG|REFRESHSRV|SIGNATUREDB|PARSERDB|SRVCOMMONPARA|BWMSERVICE|BWMCONTROLLER|BWMUSERGROUP|BWMRULE|BWMRULEGLOBAL|BCSRVLEVELPLY|CATEGORYPROP|APNBINDBWMUSRG)
```

第2轮 UDG(UDG)侧 — 通用流过滤/PCC/QoS/FUP/ADC（与计费场景共享族）：
```
Pattern: ^(ADD|SET|MOD|RMV) +(FLOWFILTER|FLOWFILTERGRP|FILTER|L7FILTER|FLTBINDFLOWF|PROTBINDFLOWF|SNSSAI|RULE|RULEBINDING|USERPROFILE|USRPROFGROUP|UPBINDUPG|APNUSRPROFG|PCCPOLICYGRP|URR|URRGROUP|QOSPROP|ADCPARA|APNOSLELBWMSW|APNIDLETIME|APNDEACTQFPLCY|APNREPORTATTR)
```

第3轮 UNC(SMF)侧（当 DP-BW-08 包含 UNC 时）：
```
# 系统级与 PCRF 管理
Pattern: ^(ADD|SET|MOD) +(LICENSESWITCH|PCCFUNC|APNPCCFUNC|PCCFAILACTION|PCCTIMER|POLICYMODE|PCCTEMPLATE|PCRF|PCRFGROUP|PCRFBINDGRP|DFTGLBPCRFGRP|N7RCVATTRCTRL|N7SNDATTRCTRL)
# 业务级规则/模板/URR/QoS
Pattern: ^(ADD|SET|MOD) +(RULE|USERPROFILE|RULEBINDING|USRPROFGROUP|UPBINDUPG|APNUSRPROFG|PCCPOLICYGRP|URR|URRGROUP|QOSPROP|FLOWFILTER|ADCPARA|APNIDLETIME|APNREPORTATTR)
```

第4轮结构化：将提取结果按 ConfigObject 分类存储。

**注意**：
- 用 Bash 工具调 grep 命令按 pattern 搜索（不用 Grep 工具、不用 Read），不全量读取（现网脚本通常数万至数十万行）
- 提取后告知用户："已从现网脚本中提取 {n} 条带宽控制相关命令（总计 {total} 行）"
- BWM 独有族（BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE 等）是带宽场景与计费场景现网区分的关键标志

### Step 4: 差异分析

**操作**：对每个 ConfigObject 判断执行类型。

| 执行类型 | 判断条件 | 生成动作 |
|----------|----------|----------|
| 复用(reuse) | 现网存在同名同参数对象 | 不生成命令，直接引用 |
| 修改(modify) | 现网存在同名对象但参数需变更 | 生成 MOD 命令 |
| 新建(create) | 现网无此对象 | 生成 ADD 命令 |
| 删除(delete) | 方案不再需要的对象 | 生成 RMV 命令（先解绑上层） |

---

## 2. 输出格式模板

```markdown
## 匹配结果

**场景**: {NS-BW-01 带宽控制场景}
**方案**: {CS-BW-01~07 之一或组合}

**决策点**:
- DP-BW-01 控制机制: {CAR限速 / Shaping整形 / GBR保证 / FUP降速 / 门控阻断}
- DP-BW-02 控制粒度: {会话级 / 业务级 / 用户组级 / 全局级}
- DP-BW-03 规则类型: {动态 / 预定义 / 本地}
- DP-BW-04 接口代际: {Gx(4G) / N7(5G)}
- DP-BW-05 BWM控制类型: {CAR-CIR保障 / CAR-PIR限速 / SHAPING整形}
- DP-BW-06 FUP累计粒度: {会话级 / 业务级}（仅 FUP 方案）
- DP-BW-07 应用识别需求: {需L7→预定义 / 仅L3L4→动态}
- DP-BW-08 产品面分工: {UDG / UNC / 双产品协作}

**现网分析**:
- 现有 BWMSERVICE / BWMCONTROLLER / BWMUSERGROUP / BWMRULE: {列表}
- 现有 RULE(POLICYTYPE=BWM/PCC/QOS/ADC): {列表}
- 现有 URR/URRGROUP/PCCPOLICYGRP: {列表}（FUP 场景）
- 现有 QOSPROP: {列表}（GBR 场景）
- 现有 ADCPARA: {列表}（ADC 场景）
- 可复用对象: {列表}

**任务编排**:
{按顺序列出需要执行的 ConfigTask，引用 03-task-layer.md 中的 task_id（T-001~T-008 通用 + T-101~T-603 专属）}
```

---

## 3. 注意事项

- 现网脚本通常数万至数十万行，**严禁全量读取**，必须按 pattern 分批提取
- 对象分类时参考 `04-command-graph.md` §2 ConfigObject 的层次关系（底层过滤 → BWM三级体系 / 策略动作 → 策略组合 → 规则汇聚）
- 差异分析时加载 `05-cross-layer-mapping.md` 确认跨层映射关系，避免遗漏依赖（如 BWMRULE 同时引用 BWMSERVICE 和 BWMCONTROLLER）
- POLICYTYPE 是带宽场景 RULE 的关键分支标识（BWM/PCC/QOS/ADC），现网扫描时需区分
