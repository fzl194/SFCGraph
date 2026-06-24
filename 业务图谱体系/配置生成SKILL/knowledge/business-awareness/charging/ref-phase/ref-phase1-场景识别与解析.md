# Phase 1 参考文件：需求理解与图谱匹配

## ⚠ 阶段执行约束（必须遵守）

**本文件仅用于 Phase 1。执行本文件内容前必须满足以下前置条件，否则 STOP：**

1. **现网脚本必须已验证存在**：必须已通过 GATE-1（用户提供路径）和 GATE-2（用工具验证文件存在）。如果现网脚本未验证，**STOP**，要求用户提供现网配置脚本文件路径。
2. **本阶段完成后必须 STOP**：执行完 §1~§3 后，**必须将匹配结果展示给用户并停止执行**，等待用户在 Phase 2（GATE-3）确认。不得自动进入参数收集或配置生成。
3. **禁止在本阶段生成任何 MML 配置命令**：本阶段只做场景匹配和现网分析，不生成配置。

---

> 本文件定义 Phase 1 的 pipeline 要求、输出模板和操作规则。
> 业务知识（决策点定义、配置对象体系、场景关键词）由 Agent 从图谱和知识库动态加载。

---

## 1. Pipeline 步骤

### Step 1: 场景识别

**操作**：从用户需求中提取计费相关关键词，匹配到业务图谱的 NetworkScenario。

**必须加载**：
- `01-business-graph.md` — 读取 NetworkScenario (NS-01) 和 ConfigurationSolution (CS-xx) 定义
- `kb/01-计费系统架构.md` + `kb/03-核心术语定义.md` — 理解用户提到的计费方式术语

**输出**：匹配到的场景 ID 和方案 ID。

**规则**：
- 如果同时涉及其他场景（如带宽控制），提醒用户本 SOP 仅处理计费部分
- 匹配不到时，向用户确认是否属于计费场景

### Step 2: 网元与决策点解析

**操作**：从用户描述中提取决策点答案，缺失时追问。

**必须加载**：
- `01-business-graph.md` — 读取 DecisionPoint (DP-CH-01~08) 的完整定义、选项和影响
  - DP-CH-01: 计费方式 → 影响 URR.USAGERPTMODE
  - DP-CH-02: 配置网元 → 决定生成哪套 MML 命令
  - DP-CH-03: 匹配层次 → 决定需要哪些过滤对象
  - DP-CH-04: 配额耗尽动作 → 决定是否需要 PCCACTIONPROP
  - DP-CH-05~08: 粒度/计量/兜底/一致性 → 按需解析

**规则**：
- 缺少决策信息时**必须追问**，追问时引用图谱中各选项的含义和影响
- DP-CH-02（配置网元）无法判断时默认 UPF+SMF

### Step 3: 现网配置解析

**操作**：按对象类型分批提取计费相关命令，构建结构化对象清单。

**必须加载**：
- `04-command-graph.md` — 读取 ConfigObject 定义，理解对象层次和依赖关系

**现网脚本分三轮扫描**：

第1轮 UPF(UDG)侧：
```
Pattern: ^(ADD|SET|MOD|RMV) +(URR|URRGROUP|PCCPOLICYGRP|PCCACTIONPROP|RULE|RULEBINDING|URRGRPBINDING|USERPROFILE|FLOWFILTER|FLOWFILTERGRP|FLTBINDFLOWF|PROTBINDFLOWF|FILTER|L7FILTER|IPLIST|REFRESHSRV)
```

第2轮 SMF(UNC)侧（当 DP-CH-02 包含 SMF 时）：
```
# 系统级
Pattern: ^(ADD|SET|MOD) +(PCCFUNC|APNPCCFUNC|CHGMODE|APNCHGMODE|CHARGECHAR|TNFINS|TNFGRP|TNFBINDGRP|SELECTCHFGBYCC|GLBDFTCHFGROUP|OCS|OCSGROUP|CCT|SELECTCCTBYCC|DCCTEMPLATE|PDUTRIGGER|RGTRIGGER)
# 业务级
Pattern: ^(ADD|SET|MOD) +(URR|URRGROUP|PCCPOLICYGRP|RULE|RULEBINDING|URRGRPBINDING|USERPROFILE)
```

第3轮结构化：将提取结果按 ConfigObject 分类存储。

**注意**：
- 用 Bash 工具调 grep 命令按 pattern 搜索（不用 Grep 工具、不用 Read），不全量读取
- 提取后告知用户："已从现网脚本中提取 {n} 条计费相关命令（总计 {total} 行）"

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

**场景**: {NS-01 计费场景}
**方案**: {CS-xx 方案名称}

**决策点**:
- DP-CH-01 计费方式: {答案}
- DP-CH-02 配置网元: {答案}
- DP-CH-03 匹配层次: {答案}
- DP-CH-04 配额耗尽动作: {答案}
- {DP-CH-05~08 按实际情况补充}

**现网分析**:
- 现有 UserProfile: {列表}
- 现有 RULE: {列表}
- 现有 URR/URRGROUP/PCCPOLICYGRP: {列表}
- 可复用对象: {列表}

**任务编排**:
{按顺序列出需要执行的 Task，引用 03-task-layer.md 中的 ConfigTask ID}
```

---

## 3. 注意事项

- 现网脚本通常数万至数十万行，**严禁全量读取**，必须按 pattern 分批提取
- 对象分类时参考 `04-command-graph.md` 中 ConfigObject 的层次关系（底层→中间→策略→顶层）
- 差异分析时加载 `05-cross-layer-mapping.md` 确认跨层映射关系，避免遗漏依赖
