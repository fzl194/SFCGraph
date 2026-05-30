# 业务感知配置生成 SOP（Agent 可执行）

## 1. 定位

本 SOP 是 Agent 执行"业务感知配置生成"的完整工作流指令。

Agent 根据用户的自然语言需求和现网配置文件，经过需求理解、方案路由、差异分析、参数映射、脚本生成与校验六个阶段，输出可直接执行的 MML 配置脚本。

## 2. 知识源

Agent 在执行过程中需要查询以下知识：

| 知识源 | 路径 | 用途 |
|--------|------|------|
| 业务图谱 | `SKILL/业务图谱.md` | 场景识别、方案选择、任务编排、决策点、校验规则 |
| 特性文档 | `SKILL/feature/UDG/UPF/{特性ID}/*.md` | UDG 特性能力与配置说明 |
| 特性文档 | `SKILL/feature/UNC/SMF/{特性ID}/*.md` | UNC 特性能力与配置说明 |
| UDG 命令参考 | `SKILL/command/UDG/{CMD}.md` | UDG MML 命令参数定义与约束 |
| UNC 命令参考 | `SKILL/command/UNC/{CMD}.md` | UNC MML 命令参数定义与约束 |

## 3. 整体流程

```
Phase 1: 需求理解与方案路由
  输入: 用户自然语言需求
  输出: 方案上下文(场景+方案+决策+任务清单)
  ↓
Phase 2: 现网基线导入与差异分析
  输入: 方案上下文 + 用户提供的现网配置文件
  输出: 现网对象清单 + 每个 Task 的执行类型(新建/修改/复用/删除)
  ↓
Phase 3: 数据规划与参数映射
  输入: 差异分析结果 + 用户规划数据(文本/表格/混合)
  输出: 每个 Task 的完整 MML 命令(参数已填充)
  ↓
Phase 4: 配置脚本组装
  输入: 各 Task 的 MML 命令
  输出: 按依赖顺序排列的完整配置脚本
  ↓
Phase 5: 校验脚本生成
  输入: 配置脚本 + 方案上下文中的 verify 任务
  输出: LST/DSP 校验命令 + 预期结果
  ↓
Phase 6: 输出交付
  输出: 配置脚本文件 + 校验脚本文件 + 变更摘要
```

## 4. Phase 1: 需求理解与方案路由

### 4.1 目标

从用户自然语言需求中识别业务场景、选择交付方案、解析决策点、确定工程任务清单。

### 4.2 工作步骤

**Step 1: 场景识别**

从业务图谱的 NetworkScenario 中匹配。判断标准：

| 场景 | 关键词/语义特征 |
|------|----------------|
| NS-01 计费场景 | 计费、收费、费率、单价、免费、配额、额度、在线计费、离线计费、融合计费 |
| NS-02 带宽控制场景 | 限速、保障、整形、带宽、QoS、速率、CIR、PIR、FUP |
| NS-03 访问限制场景 | 阻塞、屏蔽、重定向、拦截、Portal、头增强、防欺诈、黑名单 |
| NS-04 本地分流场景 | 分流、MEC、UL CL、本地DN、边缘、DNAI、PRA、公网私网 |

规则：
- 一条需求可同时匹配多个场景（如"计费+带宽控制"→ NS-01 + NS-02）
- 匹配后加载对应 DS 和 Task 编排顺序

**Step 2: 决策点解析**

沿场景和方案查找 DecisionPoint，从用户描述中提取答案：

| 决策点 | 问题 | 来源 | 答案选项 |
|--------|------|------|----------|
| DP-01 | 计费方式选择 | NS-01 | 离线计费 / 在线计费 / 融合计费 |
| DP-02 | 配额耗尽后动作 | DS-01 | BLOCK / REDIRECT / FORWARD |
| DP-03 | 分流策略来源 | NS-04 | PCF下发 / SMF下发 / PCF经SMF下发 / MPF下发 |
| DP-04 | 分流触发与UPF选择 | DS-04 | 仅主锚点 / 插入UL CL / 插入辅锚点 / UL CL+辅锚点 |
| DP-05 | 访问限制动作选择 | DS-02 | DISCARD / HEADEN / IPREDIR / REDIRECT |

规则：
- 如果用户描述中缺少决策信息，Agent **必须追问**
- 决策答案直接影响后续 Task 选择和参数映射

**Step 3: 任务清单确定**

根据匹配的场景和方案，按业务图谱中的任务编排顺序生成任务列表。

每个方案的 Task 编排顺序（必须严格遵循）：

**DS-01 差异化计费组合方案**：
```
T-PLAN-001 → T-PLAN-002 → T-PLAN-003 → T-PLAN-004 → T-PLAN-005
→ T-EXEC-001 → T-EXEC-002 → T-EXEC-003 → T-EXEC-004 → T-EXEC-005
→ T-EXEC-008 → T-EXEC-010
→ T-VERIFY-001 → T-VERIFY-002 → T-VERIFY-003
```

**DS-02 访问限制组合方案**：
```
T-PLAN-001 → T-PLAN-002 → T-PLAN-003 → T-PLAN-006
→ T-EXEC-002 → T-EXEC-003 → T-EXEC-004 → T-EXEC-006
→ T-EXEC-008 → T-EXEC-010
→ T-VERIFY-004 → T-VERIFY-005
```

**DS-03 带宽控制与QoS编排方案**：
```
T-PLAN-001 → T-PLAN-002 → T-PLAN-003 → T-PLAN-007
→ T-EXEC-002 → T-EXEC-003 → T-EXEC-004 → T-EXEC-007
→ T-EXEC-009 → T-EXEC-008 → T-EXEC-010
→ T-VERIFY-006
```

**DS-04 本地分流与独立计费方案**（规划态）：
```
T-PLAN-001 → T-PLAN-008 → T-PLAN-009
```

多场景组合时：共享 Task（T-PLAN-001/002/003, T-EXEC-002/003/004/008/010）只执行一次。

### 4.3 输出格式

```json
{
  "phase": 1,
  "scenarios": [{"id": "NS-01", "name": "计费场景"}],
  "solutions": [{"id": "DS-01", "name": "差异化计费组合方案"}],
  "decisions": [
    {"id": "DP-01", "question": "计费方式选择", "answer": "离线计费"}
  ],
  "tasks": [
    {"id": "T-PLAN-001", "phase": "plan", "name": "规划生效范围"},
    {"id": "T-EXEC-001", "phase": "execute", "name": "配置IP地址列表", "config_object": "IPLIST"},
    ...
  ],
  "clarification_needed": []
}
```

## 5. Phase 2: 现网基线导入与差异分析

### 5.1 目标

解析现网配置文件，构建现网对象清单，对每个 execute Task 的 ConfigObject 判断新建/修改/复用/删除。

### 5.2 输入

- Phase 1 输出的方案上下文
- 用户提供的现网配置文件（MML 脚本）

### 5.3 工作步骤

**Step 1: 解析现网脚本**

逐条解析 MML 命令，按 ConfigObject 分类归纳：

```
解析规则:
- ADD XXX:... → 新建对象 XXX
- SET XXX:... → 修改对象 XXX
- LST XXX:... → 查询(忽略)
```

按以下 ConfigObject 分类存储：

| 对象层级 | ConfigObject | 依赖关系 |
|----------|-------------|----------|
| 底层 | IPLIST | 无依赖 |
| 底层 | FILTER | 可引用 IPLIST |
| 底层 | L7FILTER | 无依赖 |
| 中间 | FLOWFILTER | 引用 FILTER |
| 中间 | FLOWFILTERGRP | 引用 FLOWFILTER |
| 中间 | FLTBINDFLOWF | 绑定 FILTER→FLOWFILTER |
| 中间 | PROTBINDFLOWF | 绑定 L7FILTER→FLOWFILTER |
| 策略层 | URR | 无依赖 |
| 策略层 | URRGROUP | 引用 URR |
| 策略层 | PCCPOLICYGRP | 引用 URRGROUP / PCCACTIONPROP |
| 策略层 | PCCACTIONPROP | 无依赖 |
| 策略层 | HEADEN | 无依赖 |
| 策略层 | REDIRECT | 无依赖 |
| 策略层 | CATEGORYPROP | 无依赖 |
| 策略层 | BWMSERVICE | 引用 CATEGORYPROP |
| 策略层 | BWMCONTROLLER | 无依赖 |
| 策略层 | BWMUSERGROUP | 无依赖 |
| 策略层 | BWMRULE | 引用 BWMSERVICE + BWMCONTROLLER + BWMUSERGROUP |
| 汇聚层 | RULE | 引用 FLOWFILTER + 策略对象 |
| 汇聚层 | BLACKLISTRULE | 引用 FLOWFILTER |
| 顶层 | USERPROFILE | 无依赖 |
| 顶层 | RULEBINDING | 绑定 RULE→USERPROFILE |
| 顶层 | URRGRPBINDING | 绑定 URRGROUP→USERPROFILE |

**Step 2: 差异分析**

对 Phase 1 确定的每个 execute Task，分析其 ConfigObject 的执行类型：

| 执行类型 | 判断条件 | 生成动作 |
|----------|----------|----------|
| 复用(reuse) | 现网存在同名同参数对象 | 不生成命令，直接引用现网对象名 |
| 修改(modify) | 现网存在同名对象但参数需变更 | 生成 SET/MOD 命令 |
| 新建(create) | 现网无此对象或对象名不同 | 生成 ADD 命令 |
| 删除(delete) | 方案不再需要的现网对象 | 生成 RMV 命令 |

**Step 3: 依赖链分析**

SA 配置对象有严格的依赖链，差异分析按从底向上的顺序进行：

```
依赖链（从底到顶）:
IPLIST → FILTER ─┐
                  ├→ FLOWFILTER → RULE → RULEBINDING → USERPROFILE
L7FILTER ────────┘         ↓
                     PCCPOLICYGRP / BWM链 / 动作链
```

规则：
- 修改上层对象前必须确认底层对象已就位
- 删除对象前必须先解除上层绑定（如先 RMV RULEBINDING 再 RMV RULE）
- 共享对象（被多个 RULE 引用的 FILTER 等）修改时需评估影响范围并提醒用户

### 5.4 输出格式

```json
{
  "phase": 2,
  "baseline_objects": {
    "FILTER": [{"name": "filterA", "params": {"L34PROTOCOL": "ANY"}}],
    "L7FILTER": [{"name": "l7filterA", "params": {"URL": "www.test.com/*"}}],
    ...
  },
  "task_execution_plan": [
    {
      "task_id": "T-EXEC-002",
      "config_object": "FILTER",
      "action": "create",
      "reason": "现网无匹配FILTER",
      "params_to_fill": {"FILTERNAME": "?", "L34PROTOCOL": "ANY"}
    },
    {
      "task_id": "T-EXEC-005",
      "config_object": "URR",
      "action": "modify",
      "existing_name": "urrA",
      "reason": "现网存在urrA，需修改OFFMETERINGTYPE",
      "params_to_change": {"OFFMETERINGTYPE": "FREE"}
    }
  ]
}
```

## 6. Phase 3: 数据规划与参数映射

### 6.1 目标

将用户的规划数据映射为完整的 MML 命令参数。

### 6.2 输入

- Phase 2 的差异分析结果（每个 Task 的执行类型和待填参数）
- 用户的规划数据（自然语言文本、表格、或混合格式）

### 6.3 工作步骤

**Step 1: 解析规划数据**

将用户的规划数据结构化为业务参数表。不论输入格式如何，最终归一化为：

```
业务参数表:
[
  {
    biz_index: 1,
    biz_name: "华为网站计费",
    match_condition: {type: "url", value: "www.huawei.com/*", protocol: "HTTPS"},
    action: {type: "charge", method: "offline", rate_id: 1000},
    priority: 100
  },
  {
    biz_index: 2,
    biz_name: "免费业务",
    match_condition: {type: "protocol", value: "RTSP"},
    action: {type: "charge", method: "offline", metering: "FREE", rate_id: 4000},
    priority: 300
  },
  ...
]
```

**Step 2: 查命令文档**

对每个 Task 涉及的命令，读取对应的命令 MD 获取：
- 必填参数列表
- 选填参数列表
- 参数枚举值约束
- 参数取值范围

查命令文档规则：
- UDG 侧 Task → 查 `SKILL/command/UDG/{CMD}.md`
- UNC 侧 Task → 查 `SKILL/command/UNC/{CMD}.md`
- 一条命令可能涉及多个 CMD（如 T-EXEC-005 涉及 ADD URR, ADD URRGROUP, ADD PCCPOLICYGRP）

**Step 3: 参数映射**

按业务图谱中每个 Task 的命令模板 + 命令文档参数约束，将业务参数填入：

通用映射规则：

| 规划数据字段 | 映射目标 | 映射规则 |
|-------------|---------|----------|
| match_condition.type="url" | T-EXEC-003 ADD L7FILTER | URLTYPE=URL, URL={value} |
| match_condition.type="ip_range" | T-EXEC-001 ADD IPLIST + T-EXEC-002 FILTER | IPV4ADDR+MASKVALUE, SVRIPMODE=IPLIST |
| match_condition.type="protocol" | T-EXEC-002 FILTER 或 PROTBINDFLOWF | L34PROTOCOL={protocol} |
| match_condition.type="any" | T-EXEC-002 FILTER | L34PROTOCOL=ANY |
| match_condition.type="port_range" | T-EXEC-002 FILTER | MSSTARTPORT+MSENDPORT |
| action.type="charge" + method="offline" | T-EXEC-005 ADD URR | USAGERPTMODE=OFFLINE |
| action.type="charge" + metering="FREE" | T-EXEC-005 ADD URR | OFFMETERINGTYPE=FREE |
| action.type="block" | T-EXEC-006 ADD PCCACTIONPROP | 四向GATE=DISCARD |
| action.type="headen" | T-EXEC-006 ADD HEADEN | DATATYPE=MSISDN1, ANTIFRAUD=ENABLE |
| action.type="redirect_url" | T-EXEC-006 ADD REDIRECT | URL={target} |
| action.type="bwm_cir" | T-EXEC-007 ADD BWMCONTROLLER | CTRLTYPE=CAR, CIR={kbps} |
| action.type="bwm_pir" | T-EXEC-007 ADD BWMCONTROLLER | CTRLTYPE=CAR, PIR={kbps} |
| action.type="bwm_shaping" | T-EXEC-007 ADD BWMCONTROLLER | CTRLTYPE=SHAPING, RATE={kbps} |
| priority | T-EXEC-008 ADD RULE | PRIORITY={value} |

**Step 4: 参数校验**

对映射后的命令参数进行校验：
- 必填参数是否都有值
- 枚举参数是否在合法范围内
- 数值参数是否在取值范围内
- 依赖参数是否一致（如 RULE 的 POLICYTYPE 必须与 RULEBINDING 的一致）

缺失参数处理：
1. 查业务图谱中的套餐示例作为参考默认值
2. 标注为"待确认"并说明原因
3. Agent 追问用户

### 6.4 输出格式

```json
{
  "phase": 3,
  "commands": [
    {
      "task_id": "T-EXEC-002",
      "command": "ADD FILTER",
      "params": {"FILTERNAME": "filterA", "L34PROTTYPE": "STRING", "L34PROTOCOL": "ANY"},
      "source": "规划数据-业务1",
      "status": "ready"
    },
    {
      "task_id": "T-EXEC-005",
      "command": "ADD URR",
      "params": {"URRNAME": "urrA", "URRID": 1000, "USAGERPTMODE": "OFFLINE"},
      "source": "规划数据-业务1",
      "status": "ready"
    },
    {
      "task_id": "T-EXEC-005",
      "command": "ADD URR",
      "params": {"URRNAME": "urr?", "URRID": "?", "USAGERPTMODE": "?"},
      "source": "规划数据-业务3",
      "status": "missing_params",
      "missing": ["URRID: 需用户指定费率ID"],
      "suggestion": "参考套餐1: URRID=4000"
    }
  ]
}
```

## 7. Phase 4: 配置脚本组装

### 7.1 目标

将所有命令按依赖顺序组装为完整配置脚本。

### 7.2 工作步骤

**Step 1: 排序**

按 ConfigObject 依赖链从底到顶排列：

```
执行顺序（严格）:
1. IPLIST                    （底层，无依赖）
2. FILTER                    （可引用 IPLIST）
3. L7FILTER                  （无依赖）
4. FLOWFILTER                （引用 FILTER）
5. FLTBINDFLOWF / PROTBINDFLOWF （绑定关系）
6. FLOWFILTERGRP             （组合 FLOWFILTER）
7. URR / PCCACTIONPROP / HEADEN / REDIRECT / CATEGORYPROP （策略动作）
8. URRGROUP / PCCPOLICYGRP / BWMSERVICE / BWMCONTROLLER / BWMUSERGROUP （策略组合）
9. BWMRULE                   （BWM汇聚）
10. BLACKLISTRULE            （例外规则）
11. RULE                     （匹配条件+策略绑定）
12. USERPROFILE              （容器）
13. URRGRPBINDING            （默认计费组绑定）
14. RULEBINDING              （规则绑定到容器）
15. REFRESHSRV               （刷新生效）
```

**Step 2: 命令格式化**

将参数映射结果格式化为标准 MML 命令：

```
格式: CMD OBJTYPE:PARAM1="VALUE1",PARAM2="VALUE2",...;
示例: ADD FILTER:FILTERNAME="filterA",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
```

格式化规则：
- 字符串参数用双引号
- 数值参数不加引号
- 枚举参数不加引号
- 每条命令以分号结尾

**Step 3: 脚本分区**

将配置脚本按功能分区：

```mml
!-- =============================================
!-- 业务感知配置脚本
!-- 方案: {方案名称}
!-- 生成时间: {timestamp}
!-- =============================================

!-- [Phase 1] IP地址列表配置
ADD IPLIST:...;

!-- [Phase 2] 三四层过滤条件配置
ADD FILTER:...;

!-- [Phase 3] 七层过滤条件配置
ADD L7FILTER:...;

!-- [Phase 4] 流过滤器配置与绑定
ADD FLOWFILTER:...;
ADD FLTBINDFLOWF:...;
ADD PROTBINDFLOWF:...;

!-- [Phase 5] 策略动作配置
ADD URR:...;
ADD URRGROUP:...;
ADD PCCPOLICYGRP:...;

!-- [Phase 6] 规则配置
ADD RULE:...;

!-- [Phase 7] UserProfile与绑定
ADD USERPROFILE:...;
SET URRGRPBINDING:...;
ADD RULEBINDING:...;

!-- [Phase 8] 刷新生效
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;
```

### 7.3 输出

- `config_script.mml`：可执行配置脚本

## 8. Phase 5: 校验脚本生成

### 8.1 目标

基于方案中的 verify Task，生成对应的校验命令和预期结果。

### 8.2 工作步骤

**Step 1: 生成校验命令**

根据方案的 verify Task 清单，生成 LST/DSP 查询命令：

| Verify Task | 校验命令 | 预期结果关键字段 |
|-------------|---------|-----------------|
| T-VERIFY-001 | LST LICENSESWITCH | 开关=ENABLE |
| T-VERIFY-002 | LST RULEBINDING → LST RULE → LST FLOWFILTER → LST FILTER (逐层回查) | 各层名称与规划一致 |
| T-VERIFY-003 | LST URR → LST URRGROUP → LST PCCPOLICYGRP (PFCP会话验证需人工操作) | URR ID 一致 |
| T-VERIFY-004 | LST RULEBINDING → LST RULE → LST PCCPOLICYGRP → LST PCCACTIONPROP | 四向GATE=DISCARD |
| T-VERIFY-005 | LST PROTBINDFLOWF → LST L7FILTER → DSP SIGNATUREDB (七层链路) | URL匹配 + 特征库已加载 |
| T-VERIFY-006 | LST BWM全链路 | CIR/PIR/RATE 值与规划一致 |

**Step 2: 格式化校验脚本**

```mml
!-- =============================================
!-- 校验脚本
!-- 方案: {方案名称}
!-- =============================================

!-- T-VERIFY-001: 验证License开关
LST LICENSESWITCH:LICITEM="LKV3G5SABS01";
!-- 预期: 开关=ENABLE

!-- T-VERIFY-002: 配置链逐层回查
LST RULEBINDING:USERPROFILENAME="up_charging";
!-- 预期: 4条RULEBINDING (ruleA/ruleB/ruleC/ruleD)
LST RULE:RULENAME="ruleA",POLICYTYPE=PCC;
!-- 预期: FLOWFILTERNAME="flowfilterA", POLICYNAME="pccgA", PRIORITY=100
...
```

### 8.3 输出

- `verify_script.mml`：校验命令脚本
- `verify_checklist.md`：预期结果清单（供人工核对）

## 9. Phase 6: 输出交付

### 9.1 交付物

| 文件 | 内容 |
|------|------|
| `config_script.mml` | 可执行配置脚本（按依赖顺序排列） |
| `verify_script.mml` | 校验命令脚本 |
| `verify_checklist.md` | 预期结果清单 |
| `change_summary.md` | 变更摘要（新建/修改/复用/删除的对象统计） |

### 9.2 change_summary.md 格式

```markdown
# 配置变更摘要

## 方案信息
- 场景: {NS-01 计费场景}
- 方案: {DS-01 差异化计费组合方案}
- 决策: 离线计费, 配额耗尽后BLOCK

## 变更统计
| 操作类型 | 对象数量 |
|---------|---------|
| 新增(ADD) | 12 |
| 修改(SET/MOD) | 2 |
| 复用(不生成命令) | 3 |
| 删除(RMV) | 0 |

## 新增对象清单
| ConfigObject | 对象名 | 关联Task | 说明 |
|-------------|--------|---------|------|
| FILTER | filterA | T-EXEC-002 | 匹配任意流量 |
| L7FILTER | l7filterA | T-EXEC-003 | URL=www.huawei.com/* |
| ... | ... | ... | ... |

## 复用现网对象清单
| ConfigObject | 对象名 | 复用自Task |
|-------------|--------|-----------|
| FILTER | filter_existing | T-EXEC-002 |

## 注意事项
- {需要人工确认或注意的事项}
```

## 10. 错误处理与异常流程

### 10.1 需求理解失败

如果 Agent 无法将用户需求匹配到任何 NetworkScenario：
- 输出错误信息，说明当前支持的四类场景
- 要求用户补充需求描述或重新表述

### 10.2 参数映射缺失

如果规划数据不完整，无法填充必填参数：
- 标注为"待确认"
- 提供业务图谱中套餐示例的默认值作为建议
- Agent 追问用户

### 10.3 现网配置冲突

如果现网中存在与新增对象同名的对象但参数不同：
- 提醒用户存在命名冲突
- 提供两个选项：修改现网对象 / 使用新名称

### 10.4 依赖链断裂

如果现网中缺少底层依赖对象（如引用的 IPLIST 不存在）：
- 自动补充创建底层对象的 ADD 命令
- 在变更摘要中标注为自动补充

## 11. 多方案组合规则

当用户需求涉及多个场景时：

1. 共享 Task 去重：T-PLAN-001/002/003, T-EXEC-002/003/004/008/010 只执行一次
2. 方案特有 Task 按各自方案编排顺序执行
3. 执行顺序：共享 plan → 方案A plan特有 → 方案B plan特有 → 共享 execute → 方案A execute特有 → 方案B execute特有 → 共享 verify + 方案特有 verify
4. 最终只生成一个 USERPROFILE，所有 RULE 和 BLACKLISTRULE 绑定到同一个 USERPROFILE 下
5. REFRESHSRV 在所有绑定完成后执行一次

组合示例（计费+带宽控制）：

```
T-PLAN-001(共享) → T-PLAN-002(共享) → T-PLAN-003(共享)
→ T-PLAN-004(DS-01) → T-PLAN-005(DS-01) → T-PLAN-007(DS-03)
→ T-EXEC-001(DS-01) → T-EXEC-002(共享) → T-EXEC-003(共享) → T-EXEC-004(共享)
→ T-EXEC-005(DS-01) → T-EXEC-007(DS-03) → T-EXEC-008(共享) → T-EXEC-010(共享)
→ T-VERIFY-001(DS-01) → T-VERIFY-002(共享) → T-VERIFY-003(DS-01) → T-VERIFY-006(DS-03)
```

## 12. Agent 执行约束

1. **严格按依赖顺序执行**：不可跳过底层对象直接配置上层
2. **REFRESHSRV 必须最后执行**：所有配置完成后才刷新
3. **命令文档为参数权威**：参数约束以命令 MD 文档为准
4. **业务图谱为流程权威**：Task 编排顺序以业务图谱为准
5. **动网操作保守原则**：对现网对象的修改必须有明确的用户确认
6. **追问而非猜测**：缺失决策信息或参数时必须追问，不可自行推断必填参数的值
