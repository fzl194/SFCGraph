# Phase 5 参考文件：配置生成

> 本文件定义 Phase 5 的 pipeline 要求、输出模板和排序规则。
> 业务知识（参数映射、特殊场景处理规则、参数语义）由 Agent 从图谱和知识库动态加载。

---

## 1. Pipeline 步骤

### Step 1: 加载配置规则

**必须加载**：
- `04-command-graph.md` — 读取 MMLCommand 定义和 CommandParameter，确认参数枚举值
- `04-command-graph.md` — 读取 CommandRule (CR-CH-01~14)，了解命令级约束
- `kb/13-计费三件套配置.md` — 三件套参数组合规则
- `kb/12-融合计费配置全景.md` — 融合/在线/离线场景差异

**当 DP-CH-02 包含 SMF 时额外加载**：
- `kb/18-SMF侧对象体系与协同约束.md` — SMF侧命令模板和参数差异

### Step 2: 按模板生成命令

根据 DP-CH-02（配置网元）决定生成范围。

### Step 3: 按排序规则排列命令

### Step 4: 自检

**必须加载**：
- `01-business-graph.md` — 读取 BusinessRule，确认业务约束已满足
- `04-command-graph.md` — 读取 CommandRule，确认命令级约束已满足

---

## 2. UPF(UDG)侧输出模板

每条业务按依赖顺序生成，使用以下模板结构：

```mml
!-- 1. 底层过滤条件 (如需新建)
ADD FILTER:FILTERNAME="{filter_name}", ...;
ADD L7FILTER:L7FILTERNAME="{l7_name}", ...;  (仅L7 URL场景)

!-- 2. 流过滤器与绑定
ADD FLOWFILTER:FLOWFILTERNAME="{ff_name}";
ADD FLTBINDFLOWF:FLOWFILTERNAME="{ff_name}",FILTERNAME="{filter_name}";
ADD PROTBINDFLOWF:FLOWFILTERNAME="{ff_name}", ...;  (仅L7场景)

!-- 3. 计费三件套
ADD URR:URRNAME="{urr_name}", ...;
ADD URRGROUP:URRGROUPNAME="{urrg_name}", ...;
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="{ppg_name}", ...;

!-- 4. 规则
ADD RULE:RULENAME="{rule_name}", ...;
```

> **参数值必须从 `04-command-graph.md` 的 CommandParameter 定义中获取枚举值和格式要求，禁止凭记忆填写。**

---

## 3. SMF(UNC)侧输出模板

当 DP-CH-02 包含 SMF 时，额外生成：

```mml
!-- 系统级前置（已配置则跳过）
SET PCCFUNC:...;
SET CHGMODE:...;

!-- 业务级三件套
ADD URR:URRNAME="{smf_urr}", ...;  (注意: SMF侧有 OFFCOMPOUNDTYPE/ONLCOMPOUNDTYPE 特有参数)
ADD URRGROUP:URRGROUPNAME="{smf_urrg}", ...;
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="{smf_ppg}", ...;

!-- 规则与绑定
ADD RULE:RULENAME="{rule_name}", ...;
ADD RULEBINDING:...;
```

> **SMF侧参数差异必须从`kb/18-SMF侧对象体系与协同约束.md`确认，两侧共用参数必须一致。**

---

## 4. 排序规则

### UPF(UDG)侧（严格顺序）

```
1.  FILTER / L7FILTER               (底层)
2.  FLOWFILTER                       (中间)
3.  FLTBINDFLOWF / PROTBINDFLOWF     (绑定)
4.  URR / PCCACTIONPROP              (策略动作)
5.  URRGROUP / PCCPOLICYGRP          (策略组合)
6.  RULE                              (汇聚)
7.  USERPROFILE                       (容器, 仅新建时)
8.  URRGRPBINDING                     (默认计费组绑定)
9.  RULEBINDING                       (规则绑定)
10. REFRESHSRV                        (刷新生效, 必须最后)
```

### SMF(UNC)侧

```
1. 系统级命令（仅检查，已存在则跳过）
2. 业务级三件套 + 规则 + 绑定
3. 无 REFRESHSRV
```

> **详细依赖链请加载 `03-task-layer.md` 的 command_order 关系确认。**

---

## 5. 配置决策指南

以下场景需要 Agent 从图谱/知识库获取业务规则后做出实现决策：

### OR 条件：FLOWFILTERGRP vs 多 RULE

| 方案 | 适用场景 |
|------|---------|
| FLOWFILTERGRP | 多个条件执行**完全相同**的动作 |
| 多 RULE | 需要不同优先级或后续可能分化 |

**默认**：使用 FLOWFILTERGRP（更简洁）。

### 兜底规则

| 机制 | 命令 | 触发条件 |
|------|------|---------|
| 默认URR组 | SET URRGRPBINDING:DFTURRGRPNAME | 流量未命中任何 RULE |
| 显式兜底RULE | ADD RULE(FILTER=ANY, 低PRIORITY) | 流量命中兜底 RULE |

> **规则**：两者应指向同一计费组。详细约束加载 `01-business-graph.md` BusinessRule BR-CH-06 确认。

### URL 匹配协议绑定

当用户提到"访问某网站"时，HTTP 和 HTTPS 都需要绑定：
```mml
ADD PROTBINDFLOWF:FLOWFILTERNAME="ff_xxx",PROTOCOLNAME="http",L7FILTERNAME="l7_xxx";
ADD PROTBINDFLOWF:FLOWFILTERNAME="ff_xxx",PROTOCOLNAME="https",L7FILTERNAME="l7_xxx";
```

### 融合计费

UPF侧创建**两个独立 URR**（一个OFFLINE一个ONLINE），放入同一 URRGROUP。

> **详细参数组合规则必须加载 `kb/12-融合计费配置全景.md` 确认。**

---

## 6. 注意事项

- 每个参数的枚举值必须从 `04-command-graph.md` CommandParameter 获取，不可自行推断
- 融合/在线/离线的参数差异很大，必须加载`kb/` 对应章节文件确认
- 排序错误会导致配置失败，REFRESHSRV 必须在最后（仅UPF侧）
- 三件套（URR→URRGROUP→PCCPOLICYGRP）每条业务独立，不可跨业务复用
- 两侧共用参数（URRID、RG、RULENAME、USERPROFILENAME）必须一致
