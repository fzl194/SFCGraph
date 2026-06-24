# Phase 1 参考文件：APN 开通场景识别与现网解析

## ⚠ 阶段执行约束（必须遵守）

**本文件仅用于 Phase 1。执行本文件内容前必须满足以下前置条件，否则 STOP：**

1. **现网脚本必须已验证存在**：必须已通过 GATE-1（用户提供路径）和 GATE-2（用工具验证文件存在）。如果现网脚本未验证，**STOP**，要求用户提供现网配置脚本文件路径。
2. **本阶段完成后必须 STOP**：执行完 §1~§3 后，**必须将匹配结果展示给用户并停止执行**，等待用户在 Phase 2（GATE-3）确认。不得自动进入参数收集或配置生成。
3. **禁止在本阶段生成任何 MML 配置命令**：本阶段只做场景匹配和现网分析，不生成配置。

---

> 本文件定义 APN 开通场景 Phase 1 的 pipeline 要求、输出模板和操作规则。
> 业务知识（决策点定义、配置对象体系、场景关键词）由 Agent 从图谱和知识库动态加载。
> **APN 是单场景**：NS-APN-01 APN 开通（不分子场景）；地址分配/鉴权/接入方式/地址类型是场景内 4 维度决策，对应 ConfigurationSolution CS-APN-01~09。

---

## 0. Phase 0 业务域识别（前置）

Phase 0 识别业务域为 **APN 接入（接入与会话管理，BD-APN-01）**，加载本目录 `apn/apn-provisioning/`。

**APN 业务域关键词**（命中任一即识别）：
- 地址分配、IP 地址池、POOL/SECTION/POOLGROUP/ADDRPOOL
- APN/DNN 开通、PDU/PDN 会话建立
- Radius 鉴权接入、AAA 二次鉴权、ACCESSMODE
- GRE/IPSec/L2TP/MPLS 隧道接入
- IPv4v6 双栈、IPv6 Prefix Delegation
- UPF 选择、SMF 本地池、基于位置/SMF/APN 分配

**边界**（相邻场景，不在 APN 域内，提醒用户另行处理）：
- 计费场景（BD-CH-01）：URR 三件套、差异化计费
- 带宽控制场景（BD-BW-01）：BWM 限速、FUP 降速
- 访问限制场景：URL 过滤、重定向阻断

---

## 1. Pipeline 步骤

### Step 1: 场景与方案识别

**操作**：从用户需求中提取 APN 4 维度关键词，匹配到 ConfigurationSolution CS-APN-01~09。

**必须加载**：
- `three-layer-graph/01-business-graph.md` — 读取 NS-APN-01 与 CS-APN-01~09 定义
- `APN配置树.md` — 读取配置树三大类（地址分配/鉴权计费/接入方式）的实例化规则
- `APN意图澄清知识库.md` — 理解用户业务语言到配置维度的映射
- `kb/01-APN配置总览与决策维度.md` — 理解 4 维度（地址分配×鉴权×接入方式×地址类型）

**4 维度决策点**（NS-APN-01 归属，详见 `01-business-graph.md` §3）：
- `DP-APN-ADDR-MODE` 地址分配方式 → 决定 POOLTYPE（LOCAL/UDM/SMF/EXTERNAL）、POOLGRPMAP 映射粒度、C-U 决策执行分离
- `DP-APN-ADDR-GRANULARITY` 地址分配粒度 → 决定三级优先级规则字符串（`APN-{0|1}&LOCATION-{0|1}&SMF-{0|1}`）
- `DP-APN-ADDR-TYPE` 地址类型 → 决定 SECTION 配置（V4STARTIP/V6PREFIXSTART）、License 触发（IPv6→LKV3G5V6PB01；双栈→LKV3G5VDSA01；PD→LKV3G5P6PD01）
- `DP-APN-AUTH-MODE` 鉴权方式 → 决定是否调用 AAA（仅 TRANS_AUTH/NON_TRANS 强依赖 Radius）
- `DP-APN-ACCESS-MODE` 接入方式 → 决定隧道封装类型（直连/NAT/IPSec/GRE/MPLS/L2TP/GRE-over-IPSec）

**9 方案快速匹配**（详见 `01-business-graph.md` §2.1~2.9）：

| 方案 | 典型描述 | 地址分配 | 鉴权 | 地址类型 | 接入方式 |
|------|---------|---------|------|---------|---------|
| CS-APN-01 | 工厂工控访问内网 | UDM 静态 | NON_TRANS | IPv4 | IPSec |
| CS-APN-02 | 智慧农业传感器上报 | UPF-APN 动态 | TRANS_NON_AUTH | IPv4 | NAT/直连 |
| CS-APN-03 | 家庭 CPE 宽带 | UPF-SMF 动态 | TRANS_NON_AUTH | IPv4v6 双栈 | NAT/直连 |
| CS-APN-04 | VoLTE 语音 | SMF 本地动态 | TRANS_NON_AUTH | IPv4v6 双栈 | 直连 |
| CS-APN-05 | 企业 AAA 二次鉴权 | RADIUS 下发 | NON_TRANS | IPv4 | GRE/直连 |
| CS-APN-06 | 传统企业 DHCP 迁移 | DHCP 代理 | TRANS_NON_AUTH | IPv4 | 直连 |
| CS-APN-07 | 企业 L2TP VPN | LNS (L2TP) | NON_TRANS | IPv4v6 双栈 | L2TP |
| CS-APN-08 | 区域化运营管理 | UPF-LOCATION 动态 | TRANS_NON_AUTH | IPv4 | 直连 |
| CS-APN-09 | 企业双栈加密接入 | UPF-APN 动态 | TRANS_NON_AUTH | IPv4v6 双栈 | IPSec |

**规则**：
- 缺少决策信息时**必须追问**，追问时引用配置树/意图澄清知识库中的业务场景引导问题
- 无法精确匹配单一方案时，按维度组合自行拼装，并明确告知用户哪些 CS 部分被采用
- 同时涉及计费/带宽控制时，提醒用户本 SOP 仅处理 APN 开通部分

### Step 2: 决策点解析

**操作**：从用户描述中提取 5 个核心决策点答案，缺失时按 `APN意图澄清知识库.md` 场景化追问。

**必须加载**：
- `01-business-graph.md` §3 DecisionPoint — 读取 DP-APN-* 完整 option_set 与 impact_summary
- `APN意图澄清知识库.md` — 用业务语言提问（"设备的 IP 是怎么分配的？"而非"选 UPF/SMF/UDM 分配"）

**规则**：
- 缺少决策信息时**必须追问**，每次只问一个问题，渐进式澄清
- `DP-APN-ADDR-MODE` 无法判断时默认 UPF-SMF 动态（CS-APN-03 家庭宽带场景）
- `DP-APN-AUTH-MODE` 无法判断时默认 TRANS_NON_AUTH（透明接入免鉴权）
- `DP-APN-ACCESS-MODE` 无法判断时默认直连（无隧道）
- 位置/双栈/Radius/L2TP 等需 License 的维度，识别到时必须追问 License 是否已购（见 `kb/02-License门控.md`）

### Step 3: 现网配置解析（Bash grep 分批扫描）

**操作**：按对象类型分批提取 APN 相关命令，构建结构化对象清单。

**必须加载**：
- `04-command-graph.md` — 读取 ConfigObject 定义，理解 APN 对象层次和依赖关系（§2.1~2.13）

**现网脚本按命令类型分批扫描**（每次 grep 一个命令类型，**用 Bash 工具调 grep，不用 Grep 工具、不用 Read**）：

**第 1 轮：UDG（UPF）侧 APN/地址池/地址分配规则**

```bash
# APN 实例（跨域共用挂载点）
grep -nE "^(ADD|SET|MOD|RMV|LST) +APN[ :]" {现网脚本}
# APN 地址分配属性（U+C 共用命令名）
grep -nE "^SET +APNADDRESSATTR" {现网脚本}
# UDG 地址池（POOLTYPE=LOCAL）
grep -nE "^(ADD|MOD|RMV|LST) +POOL[ :]" {现网脚本}
# 地址段
grep -nE "^(ADD|MOD|RMV) +SECTION[ :]" {现网脚本}
# 地址池组 + 绑定 + 映射
grep -nE "^(ADD|MOD|RMV) +POOLGROUP[ :]" {现网脚本}
grep -nE "^(ADD|MOD|RMV) +POOLBINDGROUP[ :]" {现网脚本}
grep -nE "^(ADD|MOD|RMV) +POOLGRPMAP[ :]" {现网脚本}
# 地址分配规则（全局 + APN 级）
grep -nE "^SET +IPALLOCRULE" {现网脚本}
grep -nE "^SET +APNIPALLOCRULE" {现网脚本}
# SMF NodeID + 全局开关
grep -nE "^(ADD|MOD) +CPNODEID[ :]" {现网脚本}
grep -nE "^SET +IPALLOCBYSMFGLBSW" {现网脚本}
grep -nE "^SET +IPALLOCBYLOCGLBSW" {现网脚本}
```

**第 2 轮：UDG 侧 VPN/接口/路由/隧道（按接入方式维度按需扫描）**

```bash
# VPN 实例与地址族（IPv6/双栈必扫）
grep -nE "^(ADD|MOD) +(VPNINST|L3VPNINST|VPNINSTAF|IPBINDVPN)[ :]" {现网脚本}
# 接口与 IP
grep -nE "^(ADD|MOD) +(INTERFACE|LOGICINF|IFIPV4ADDRESS|IFIPV6ADDRESS)[ :]" {现网脚本}
# 静态路由 + OSPF
grep -nE "^(ADD|MOD) +(SRROUTE|SRROUTE6|OSPF|OSPFAREA|OSPFNETWORK|OSPFIMPORTROUTE|OSPFV3)[ :]" {现网脚本}
# GRE 隧道（接入方式 = GRE / 静态冗余）
grep -nE "^(ADD|MOD|RMV) +GRETUNNEL[ :]" {现网脚本}
# IPSec 隧道（接入方式 = IPSec）
grep -nE "^(ADD|MOD) +(ACLGROUPIPSEC|ACLRULEADV4IPSEC|IPSECPROPOSALIPSEC|IKEPROPOSAL|IKEPEER|IPSECPOLICY|IPSECINTFCFGIPSEC)[ :]" {现网脚本}
# L2TP（接入方式 = L2TP）
grep -nE "^(ADD|SET|MOD) +(APNL2TPATTR|L2TPGROUP|L2TPLNSINFO|L2TPCLIENTIP|L2TPRDSCLIENT|GLOBALL2TP|PPPCFG|L2TPN4KEY)[ :]" {现网脚本}
# 接入控制 U 面 QoS
grep -nE "^SET +APNQOSATTR" {现网脚本}
# License 开关
grep -nE "^SET +LICENSESWITCH" {现网脚本}
```

**第 3 轮：UNC（SMF）侧（C 面决策）**

```bash
# UNC 地址池（POOLTYPE=UDM，★前缀 ADDRPOOL，与 UDG POOL 分离）
grep -nE "^(ADD|MOD|RMV) +ADDRPOOL[ :]" {现网脚本}
grep -nE "^(ADD|MOD|RMV) +(ADDRPOOLGRP|POOLBINDGRP|POOLBINDAPN|POOLGRPMAP)[ :]" {现网脚本}
# UPF 节点 + NF 实例 + 选择 11 件套（仅 UPF 选择维度扫描）
grep -nE "^(ADD|MOD) +(UPNODE|PNFPROFILE|PNFDNN|PNFNS|PNFDNAI|UPFBINDGRP)[ :]" {现网脚本}
# Radius 三件套 + 二次鉴权（鉴权 = TRANS_AUTH/NON_TRANS 时扫描）
grep -nE "^(ADD|SET|MOD) +(APNAUTHATTR|RDSSVRGRP|RDSSVR|APNRDSSVRGRP|APNRDSCLIENTIP|APNRDSACCTCTRL|APNRADIUSATTR|FHBYPASS)[ :]" {现网脚本}
grep -nE "^(ADD|SET|MOD) +(UPLIST4RDS|CPGTPUADDR|RDSUPFCTRL|UPFRDSSVR|UPFRDSCLIENTIP|NETWORKINSTVPNMAP)[ :]" {现网脚本}
# UNC L2TP C 面决策（L2TP 场景扫描，★仅 2 参数）
grep -nE "^SET +APNL2TPCTRL" {现网脚本}
grep -nE "^SET +L2TPKEY" {现网脚本}
# 别名 APN / DHCP / AKA / ARD（按需）
grep -nE "^(ADD|MOD) +(APNALIAS|ALIASAPN|AREADNS)[ :]" {现网脚本}
grep -nE "^(ADD|MOD) +(GBAUTHCIPH|IUAUTHCIPH|S1USRSECPARA|NGUSRSECPARA|GBARD|IUARD|S1ARD|NGMMSUBDATA)[ :]" {现网脚本}
```

**第 4 轮：结构化**。将提取结果按 ConfigObject 分类存储，告知用户：
"已从现网脚本中提取 {n} 条 APN 相关命令（UDG {n1} + UNC {n2}，总计 {total} 行扫描）"

### Step 4: 差异分析

**操作**：对每个 ConfigObject 判断执行类型。

| 执行类型 | 判断条件 | 生成动作 |
|----------|----------|----------|
| 复用(reuse) | 现网存在同名同参数对象 | 不生成命令，直接引用 |
| 修改(modify) | 现网存在同名对象但参数需变更 | 生成 MOD/SET 命令 |
| 新建(create) | 现网无此对象 | 生成 ADD 命令 |
| 删除(delete) | 方案不再需要的对象 | 生成 RMV 命令（先解绑上层引用） |

**差异分析重点维度**（APN 特有）：
- **地址池体系**：UDG POOL vs UNC ADDRPOOL 分离识别（CR-APN-01），POOLTYPE 取值差异（CR-APN-04）
- **APN 跨域共用挂载点**：APN 同时被地址分配/鉴权/L2TP/QoS/多PDN 引用，修改 APN 必须评估影响范围
- **L2TP 不对称**：UDG APNL2TPATTR（10+ 参数）vs UNC APNL2TPCTRL（2 参数），不可混用（CR-APN-02）
- **L2TP 密钥跨侧一致**：UDG L2TPN4KEY vs UNC L2TPKEY 必须相同（CR-APN-03）

---

## 2. 输出格式模板

```markdown
## 匹配结果

**业务域**: BD-APN-01 接入与会话管理
**场景**: {NS-APN-01 APN 开通场景}
**方案**: {CS-APN-xx 方案名称}（或自行拼装的维度组合说明）

**决策点**:
- DP-APN-ADDR-MODE 地址分配方式: {UDM静态/UPF-APN动态/UPF-LOCATION动态/UPF-SMF动态/SMF本地/RADIUS下发/DHCP代理/LNS}
- DP-APN-ADDR-GRANULARITY 地址分配粒度: {APN-1&LOC-0&SMF-0 等}
- DP-APN-ADDR-TYPE 地址类型: {IPv4/IPv6/IPv4v6 双栈}
- DP-APN-AUTH-MODE 鉴权方式: {TRANS_NON_AUTH/TRANS_AUTH/NON_TRANS/LOC_AUTH}
- DP-APN-ACCESS-MODE 接入方式: {直连/NAT/IPSec/GRE/MPLS/L2TP/GRE-over-IPSec}

**License 触发**（如适用）:
- {LKV3G5V6PB01 / LKV3G5VDSA01 / LKV3G5P6PD01 / LKV3G5LBAA01 / LKV3G5L2TP01}

**现网分析**:
- 现有 APN: {列表}
- 现有 POOL (UDG) / ADDRPOOL (UNC): {列表}
- 现有 POOLGROUP/ADDRPOOLGRP + POOLGRPMAP: {列表}
- 现有 Radius 服务器组 (RDSSVRGRP): {列表}（鉴权场景）
- 现有 GRETUNNEL / IPSECPOLICY / L2TPGROUP: {列表}（隧道场景）
- 可复用对象: {列表}

**任务编排**:
{按顺序列出需要执行的 ConfigTask，引用 `03-task-layer.md` 的 Task ID（T-001~T-007 通用 / T-002~T-005 地址分配 / T-101~T-109 双栈 / T-201~T-208 L2TP / T-301~T-310 Radius / T-601~T-608 隧道 等）}
```

---

## 3. 注意事项

- 现网脚本通常数万至数十万行，**严禁全量读取**，必须按命令类型分批用 Bash grep 提取
- **每次 grep 只搜一个命令类型**（ADD POOL / ADD SECTION / SET APNAUTHATTR 分开搜），避免单次结果过大
- 对象分类时参考 `04-command-graph.md` §2 ConfigObject 层次关系
- 差异分析时加载 `05-cross-layer-mapping.md` 确认跨层映射，避免遗漏依赖（如 Radius 级联链、L2TP C-U 不对称）
- **APN 是跨域共用挂载点**：APN 同时被地址分配、鉴权、L2TP、QoS、多 PDN 引用，修改前必须全面扫描引用（见 `04-command-graph.md` §3.1 contains 边）
- License 维度必须前置确认：基于位置（LKV3G5LBAA01）/ 双栈（LKV3G5VDSA01）/ IPv6 承载（LKV3G5V6PB01）/ PD（LKV3G5P6PD01）/ L2TP（LKV3G5L2TP01，仅 UDG）/ IPSec 等
- **U+C 不对称识别**：POOL↔ADDRPOOL、APNL2TPATTR↔APNL2TPCTRL、L2TPN4KEY↔L2TPKEY 三组不对称对象，现网扫描时按侧分别归类
