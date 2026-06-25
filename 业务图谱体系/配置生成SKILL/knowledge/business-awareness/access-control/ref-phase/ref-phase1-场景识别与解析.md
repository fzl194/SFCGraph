# Phase 1 参考文件：需求理解与图谱匹配

## ⚠ 阶段执行约束（必须遵守）

**本文件仅用于 Phase 1。执行本文件内容前必须满足以下前置条件，否则 STOP：**

1. **现网脚本必须已验证存在**：必须已通过 GATE-A（用户提供路径）和 GATE-B（用工具验证文件存在）。如果现网脚本未验证，**STOP**，要求用户提供现网配置脚本文件路径。
2. **本阶段完成后必须 STOP**：执行完 §1~§3 后，**必须将匹配结果展示给用户并停止执行**，等待用户在 Phase 2（GATE-1）确认。不得自动进入参数收集或配置生成。
3. **禁止在本阶段生成任何 MML 配置命令**：本阶段只做场景匹配和现网分析，不生成配置。

---

> 本文件定义 Phase 1 的 pipeline 要求、输出模板和操作规则（访问限制场景专属）。
> 业务知识（9 方案闭包、8 决策点、双轨道+五子轨机制）由 Agent 从图谱和知识库动态加载。
> 域共享规则（REFRESHSRV 时序、跨网元一致性、优先级、SA 前置）见 `../业务感知域规则.md`，本文件不复述。

---

## 1. Pipeline 步骤

### Step 1: 场景识别

**操作**：从用户需求中提取访问限制相关关键词，匹配到业务图谱的 NetworkScenario。

**必须加载**：
- `../../访问限制场景/three-layer-graph/01-business-graph.md` — 读取 NetworkScenario (NS-AC-01) 和 ConfigurationSolution (CS-AC-01~09) 定义
- `../kb/01-访问限制动作体系与双轨道.md` + `../kb/03-核心术语定义.md` — 理解用户提到的动作术语（阻塞 / 头增强 / 重定向 / URL 过滤）

**访问限制关键词 → 方案闭包映射**：

| 用户关键词 | 匹配方案 | 动作轨道 |
|-----------|---------|---------|
| 阻塞 / 禁止访问 / 丢弃 / 黑名单（PCC 体系） | CS-AC-01 PCC 阻塞 | 轨道 A（PCC/ADC） |
| 头增强 / 插入 MSISDN / 插入 IMSI / 业务认证 / WAP 网关 | CS-AC-02 头增强 | 轨道 A（HEADEN） |
| HTTP 重定向 / 301/302/303 / 错误码跳转 | CS-AC-03 HTTP 重定向 | 轨道 A（SMARTREDIRECT） |
| DNS 纠错 / 域名解析失败 / NXDOMAIN / 纠错页 | CS-AC-04 DNS 重定向 | 轨道 A（SMARTREDIRECT） |
| Portal / captive / 业务订购页 / 广告推送 | CS-AC-05 Portal | 轨道 A（PCC + IPFarm） |
| WebProxy / 透明代理 / HTTPS 重定向 / 网络加速 | CS-AC-05 WebProxy | 轨道 A（WEBPROXY） |
| URL 过滤 / 家长控制 / 内容分类 / BLOCK/PERMIT / ICAP | CS-AC-06 URL 过滤 | 轨道 B（CFTEMPLATE.ACTION） |
| SAR / 区域漫游限制 / ODB / 欠费禁用 / 接入控制 | CS-AC-07 接入控制 | UNC 侧（USRLOCATION） |
| 配额耗尽 / 套餐耗尽 / 充值页 / RedirectInformation | CS-AC-08 配额耗尽重定向 | 轨道 A（PCC + PCF 决策） |
| 漫游引导 / 出国签约 / PRA / 区域引导订购 | CS-AC-09 区域引导重定向 | 轨道 A（PCC + 位置触发） |

**规则**：
- 如果同时涉及其他场景（如计费、带宽控制），提醒用户本 SOP 仅处理访问限制部分；并发表明可叠加执行（规则匹配类型独立原则，BR-AC-02）
- **关键判断点**：用户说"放行白名单"→ 必须走 CS-AC-06 URL 过滤（轨道 B 独有 PERMIT，BR-AC-10），轨道 A 无法显式 PERMIT
- 匹配不到时，向用户确认是否属于访问限制场景

### Step 2: 网元与决策点解析

**操作**：从用户描述中提取决策点答案，缺失时追问。

**必须加载**：
- `01-business-graph.md` — 读取 DecisionPoint (DP-AC-01~08) 的完整定义、选项和影响

| 决策点 | 问题 | 影响对象 |
|--------|------|---------|
| DP-AC-01 动作类型 | DISCARD / HEADEN / REDIRECT / PERMIT | 决定 CS 闭包与 RULE.POLICYTYPE 或 CFTEMPLATE.ACTION 路径 |
| DP-AC-02 规则类型 | 动态 / 预定义 / 本地 | 决定三网元一致性要求；URL 过滤必选预定义 |
| **★ DP-AC-03 动作轨道** | 轨道 A（PCC 体系） vs 轨道 B（URL 过滤体系） | 决定 ConfigObject 体系（RULE vs CFTEMPLATE）、动作指定方式（隐式 vs 显式）、外部依赖（可选 PCRF vs 必需 ICAP）、是否支持 PERMIT |
| DP-AC-04 网元范围 | UPF 执行 / SMF 翻译 / AMF 接入控制 / 锚点模式 | 决定规则生效范围 |
| DP-AC-05 匹配层次 | L3/L4 / L7 / DNS / ADC 应用 | 决定 Filter 类型（FILTER/L7FILTER/EXTENDEDFILTER） |
| DP-AC-06 重定向目标 | 充值页 / Portal / Proxy / 第三方 / Platform | 决定重定向特性选择（仅 REDIRECT 类方案） |
| DP-AC-07 协议支持 | HTTP1.x / HTTPS / RTSP / 任意 TCP / DNS | 决定特性选择；**加密协议仅 WebProxy 可处理** |
| DP-AC-08 PCF 容灾 | 回落本地 PCC / 会话失败 / DNN 混合 | 决定访问限制策略可靠性 |

**规则**：
- 缺少决策信息时**必须追问**，追问时引用图谱中各选项的含义和影响
- DP-AC-03 是访问限制场景的核心路由决策，必须明确（轨道 A 还是 B），否则无法选 ConfigObject 体系
- DP-AC-04 无法判断时默认 UPF（UDG 侧执行）；UNC 侧位置触发仅在本地 PCC 场景需要（TR-AC-08）

### Step 3: 现网配置解析

**操作**：按对象类型分批提取访问限制相关命令，构建结构化对象清单。

**必须加载**：
- `../../访问限制场景/three-layer-graph/04-command-graph.md` — 读取 ConfigObject（41 个）定义与依赖关系，理解双轨道对象体系

**现网脚本分四轮扫描**（访问限制独有对象族远多于计费，必须分四轮）：

第 1 轮 UDG 侧 — 通用骨架与流过滤链：
```
Pattern: ^(ADD|SET|MOD|RMV) +(LICENSESWITCH|REFRESHSRV|SIGNATUREDB|PARSERDB|FILTER|FLOWFILTER|FLOWFILTERGRP|FLTBINDFLOWF|PROTBINDFLOWF|L7FILTER|CATEGORYPROP)
```

第 2 轮 UDG 侧 — 双轨道动作对象族（访问限制独有，按子轨分组）：
```
# 轨道 A 动作对象
Pattern: ^(ADD|SET|MOD|RMV) +(RULE|USERPROFILE|RULEBINDING|PCCPOLICYGRP|URR|URRGROUP|ADCPARA|HEADEN|BASE64|EXTENDEDFILTER|ERRORCODE|WELLKNOWNPORT)
# 轨道 A SMARTREDIRECT 子轨
Pattern: ^(ADD|SET|MOD|RMV) +(SMARTHTTPREDIR|REDIRAPPENDINFO|DNSOVERWRITING)
# 轨道 A WEBPROXY 子轨
Pattern: ^(ADD|SET|MOD|RMV) +(IPFARMGLOBAL|IPFARM|IPFARMSERVER|LOGICINF|BLACKLISTRULE|APN)
# 轨道 B URL 过滤 ICAP 互通前置
Pattern: ^(ADD|SET|MOD|RMV) +(VPNINST|ICAPSERVER|ICAPLOCALINFO|ICAPSVRGRP|ICAPSVRBINDISG|CFSRVMODE)
# 轨道 B URL 过滤内容过滤业务
Pattern: ^(ADD|SET|MOD|RMV) +(APNCFFUNC|CFPROFILE|CFTEMPLATE|APNCFTEMPLATE|CFPROFBINDCFT|CONTCATEGROUP|CONTCATEGBIND|CFCACHEPARA|GLBCFFUNC|CFWHITEURLLST|CFIPWHITELIST|CFPFSPECACTION)
```

第 3 轮 UNC 侧（当 DP-AC-04 包含 SMF/AMF 时）：
```
# PCC 骨架与 PCRF 管理
Pattern: ^(ADD|SET|MOD) +(LICENSESWITCH|PCCFUNC|PCCFAILACTION|POLICYMODE|N7RCVATTRCTRL|N7SNDATTRCTRL|FHBYPASS|PCRF|PCRFGROUP|PCRFBINDGRP|DFTGLBPCRFGRP)
# 规则模板绑定链
Pattern: ^(ADD|SET|MOD) +(RULE|USERPROFILE|RULEBINDING|USRPROFGROUP|UPBINDUPG|APNUSRPROFG)
# 接入控制触发（UNC 侧独有）
Pattern: ^(ADD|SET|MOD) +(USRLOCATION|USRLOCATIONGRP)
```

第 4 轮结构化：将提取结果按双轨道 ConfigObject 分类存储。

**关键分类规则（双轨道判定，CR-AC-02 / TR-AC-03）**：
- **轨道 A 对象**：RULE + POLICYTYPE∈{ADC,PCC,HEADEN,SMARTREDIRECT,WEBPROXY}；动作对象 = POLICYNAME 指向（PCCPOLICYGRP / HEADEN / SMARTHTTPREDIR / DNSOVERWRITING / IPFARM）
- **轨道 B 对象**：CFTEMPLATE / CONTCATEGBIND（含 ACTION=BLOCK/PERMIT/REDIRECT）；RULE 用 POLICYTYPE=PCC 仅作匹配触发，**动作不走 PCCPOLICYGRP**
- 同一现网可能双轨并存（CR-AC-14），需分别归类

**注意**：
- 用 Bash 工具调 grep 命令按 pattern 搜索（不用 Grep 工具、不用 Read），不全量读取
- 提取后告知用户："已从现网脚本中提取 {n} 条访问限制相关命令（总计 {total} 行），其中轨道 A {a} 条、轨道 B {b} 条、UNC 侧 {u} 条"

### Step 4: 差异分析

**操作**：对每个 ConfigObject 判断执行类型。

| 执行类型 | 判断条件 | 生成动作 |
|----------|----------|----------|
| 复用(reuse) | 现网存在同名同参数对象 | 不生成命令，直接引用 |
| 修改(modify) | 现网存在同名对象但参数需变更 | 生成 MOD 命令（注意 UNC 侧 MOD UPBINDUPG 用于位置触发绑定） |
| 新建(create) | 现网无此对象 | 生成 ADD 命令 |
| 删除(delete) | 方案不再需要的对象 | 生成 RMV 命令（先解绑上层） |

---

## 2. 输出格式模板

```markdown
## 匹配结果

**场景**: {NS-AC-01 访问限制场景}
**方案**: {CS-AC-xx 方案名称}
**★ 动作轨道**: {轨道 A PCC 体系 / 轨道 B URL 过滤体系 / 双轨并存}

**决策点**:
- DP-AC-01 动作类型: {答案}
- DP-AC-02 规则类型: {答案}
- DP-AC-03 动作轨道: {答案}
- DP-AC-04 网元范围: {答案}
- DP-AC-05 匹配层次: {答案}
- DP-AC-06 重定向目标: {答案，仅 REDIRECT 类}
- DP-AC-07 协议支持: {答案}
- DP-AC-08 PCF 容灾: {答案，仅动态 PCC}

**现网分析**:
- 现有 UserProfile / RULE / PCCPOLICYGRP: {列表}
- 现有轨道 A 动作对象（HEADEN/SMARTHTTPREDIR/DNSOVERWRITING/IPFARM/ADCPARA）: {列表}
- 现有轨道 B 动作对象（CFTEMPLATE/CONTCATEGBIND + ICAP 系列）: {列表}
- 现有 UNC 侧位置对象（USRLOCATION/USRLOCATIONGRP）: {列表}
- 可复用对象: {列表}

**任务编排**:
{按顺序列出需要执行的 Task，引用 03-task-layer.md 中的 ConfigTask ID（T-001~T-008 generic + T-AC-101~T-AC-109 独有）}
```

---

## 3. 注意事项

- 现网脚本通常数万至数十万行，**严禁全量读取**，必须按 pattern 分批提取
- 对象分类时参考 `04-command-graph.md` §3 ConfigObject 关系边（双轨道五子轨层次：通用结构 9 + 轨道 A 各子轨 + 轨道 B URL 过滤 + 接入控制 + 协议盲区互斥）
- **双轨道判定是本场景核心**：必须先识别每个 RULE/CFTEMPLATE 属于轨道 A 还是 B，再归类（CR-AC-02、TR-AC-03）
- 差异分析时加载 `05-cross-layer-mapping.md` 确认跨层映射关系，避免遗漏依赖（特别是 ICAP 互通前置链与 PCC 计费属性链）
- UNC 侧位置触发对象仅本地 PCC 场景需要配置（动态 PCC 场景跳过，TR-AC-08）
