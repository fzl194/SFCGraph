# Phase 3 参考文件：APN 参数收集

## ⚠ 阶段执行约束（必须遵守）

**本文件仅用于 Phase 3。执行本文件内容前必须满足以下前置条件，否则 STOP：**

1. **用户必须已确认方案**：必须已通过 GATE-1（用户在 Phase 2 明确确认了匹配结果）。如果用户未确认方案，**STOP**，回到 Phase 2 等待用户确认。
2. **本阶段完成后必须 STOP**：执行完 §1~§5 后，**必须生成并展示 `xxxLLD.md` 后停止执行**，等待用户在 Phase 4（GATE-2）确认。`LLD` 就是 markdown 形式的规划数据表，不再拆成第二份同义文档。不得自动进入配置生成。
3. **禁止在本阶段生成任何 MML 配置命令**：本阶段只收集和推断参数，不生成配置。

---

> 本文件定义 APN 开通场景 Phase 3 的 pipeline 要求、输出模板和操作规则。
> 业务知识（参数语义、默认值、推导规则）由 Agent 从图谱和知识库动态加载。

---

## 1. Pipeline 步骤

### Step 1: 从需求和现网中推断参数

**操作**：尽可能从以下来源自动推断参数值：
- 用户需求描述（APN/DNN 名、地址段范围、鉴权方式、隧道对端 IP 等）
- 现网配置（VPN 命名规律、地址池前缀、已有 Radius 服务器组）
- 业务图谱中的方案示例（`01-business-graph.md` §9 端到端方案链路）
- 知识库中的默认值与取值范围

**必须加载**：
- `kb/03-地址池体系参数.md` — POOL/SECTION/POOLGROUP/POOLGRPMAP 参数语义
- `kb/04-地址分配规则与三级优先级.md` — IPALLOCRULE 规则字符串推导
- `04-command-graph.md` §5 — 读取 CommandParameter 定义，确认参数枚举值和约束

**APN 特有推断规则**（现网命名规律）：
- 如果现网 POOL 命名为 `pool_apn1_v4`，则新 POOL 建议用相同前缀 `pool_{apn}_{v4|v6}`
- 如果现网 VPNINST 命名为 `vpn1`，则双栈 IPv6 VPN 建议 `vpn1_v6` 或现网规律
- 如果现网 RDSSVRGRP 已存在可复用，无需重复创建（Radius 三件套跨 APN 共享）
- 地址段范围参考现网同类 POOL 的 V4STARTIP/V4ENDIP 网段规律

### Step 2: 按维度收集参数

**操作**：按 APN 4 维度（地址分配/鉴权/接入方式/地址类型）分别收集参数。

**必须加载**：
- `04-command-graph.md` §2 ConfigObject + §5 核心命令参数表 — 确认参数枚举值
- `01-business-graph.md` §3 DecisionPoint — 确认 DP-APN-* option_set

### Step 3: 地址池三级规则参数（独立分析，必须用户确认）

**操作**：基于 `DP-APN-ADDR-GRANULARITY` 决策，推导 `IPALLOCRULE` 三级规则字符串。

**必须加载**：
- `kb/04-地址分配规则与三级优先级.md` — FIRSTRULE/SECONDRULE/THIRDRULE 规则字符串组合

**规则字符串格式**（★严格格式，从 `04-command-graph.md` CR-APN-05 / `feature/GWFD-010105` §4.3.4 确认）：
```
{APN-{0|1}}&{LOCATION-{0|1}}&{SMF-{0|1}}
```
- 单维度：`APN-1&LOCATION-0&SMF-0`（基于 APN）/ `APN-0&LOCATION-0&SMF-1`（基于 SMF）/ `APN-0&LOCATION-1&SMF-0`（基于位置）
- 双维度回退：FIRSTRULE=`APN-1&LOCATION-0&SMF-1`（SMF+APN），SECONDRULE=`APN-0&LOCATION-0&SMF-1`（SMF 兜底）

### Step 4: License 参数（必须独立确认）

**操作**：根据 4 维度决策，列出所有触发的 License。

**必须加载**：
- `kb/02-License门控.md` — License 编号、适用特性、产品侧（UDG/UNC 不对称）
- `feature/{特性}.md` §0 元数据 `license_required` 字段 — **禁止凭记忆填写**

**APN 关键 License 触发矩阵**：

| 触发维度 | License | 适用产品侧 |
|---------|---------|-----------|
| IPv6 承载（DP-APN-ADDR-TYPE=IPv6/双栈） | LKV3G5V6PB01 | UDG |
| IPv4v6 双栈（DP-APN-ADDR-TYPE=双栈） | LKV3G5VDSA01 | UDG（使能 GWFD-010105 的 IPv4v6 取值） |
| IPv6 Prefix Delegation（V6PREFIXLENGTH<64） | LKV3G5P6PD01 | UDG |
| 基于位置地址分配（DP-APN-ADDR-MODE=UPF-LOCATION） | LKV3G5LBAA01 | UDG |
| L2TP VPN（DP-APN-ACCESS-MODE=L2TP） | LKV3G5L2TP01 | ★仅 UDG（UNC 侧 WSFD-104410 无 License，BR-APN-L2TP-CU-ASYM） |

### Step 5: 全局参数与跨侧一致参数

**操作**：列出 U+C 共用参数、APN 跨域共用挂载点参数、全局开关参数。

**必须加载**：
- `kb/05-U+C不对称与跨侧一致性.md` — POOL↔ADDRPOOL、APNL2TPATTR↔APNL2TPCTRL、L2TPN4KEY↔L2TPKEY 跨侧一致约束

---

## 2. 输出格式模板

### APN 主参数表

```markdown
### APN: {APN/DNN 名}

| 参数项 | UDG(UPF)侧 | UNC(SMF)侧 | 来源 | 状态 |
|--------|-----------|-----------|------|------|
| **基础** | | | | |
| APN/DNN 名 | {值} | **必须与 UDG 一致** | 需求 | 已知/待确认 |
| HASVPN | ENABLE/DISABLE | — | 推断 | 已知 |
| VPNINSTANCE | {vpn 名} | — | 现网/需求 | 已知/待确认 |
| HASVPNIPV6（双栈） | ENABLE/DISABLE | — | DP-APN-ADDR-TYPE | 已知 |
| VPNINSTANCEIPV6（双栈） | {vpn_v6 名} | — | 推断 | 待确认 |
| **地址分配** | | | | |
| SUPPORTIPV4 | ENABLE/DISABLE | ENABLE/DISABLE | DP-APN-ADDR-TYPE | 已知 |
| SUPPORTIPV6 | ENABLE/DISABLE | ENABLE/DISABLE | DP-APN-ADDR-TYPE | 已知 |
| IGNOREV4POOLID（RADIUS 子方式） | DISABLE | — | DP-APN-ADDR-MODE | 已知 |
| 地址池名 | {POOL 名} | {ADDRPOOL 名，仅 UDM 静态} | 推断 | 待确认 |
| POOLTYPE | **LOCAL**（必选） | **UDM**（仅静态签约） | CR-APN-01/04 | 已知 |
| 地址段 V4STARTIP/V4ENDIP | {x.x.x.1 - x.x.x.10} | — | 需求 | **待提供** |
| V6PREFIXSTART/V6PREFIXLENGTH（IPv6） | {值}/{64 或 <64} | — | 需求 | 待确认 |
| FIRSTRULE | {规则字符串} | {规则字符串} | DP-APN-ADDR-GRANULARITY | 已知 |
| **鉴权**（仅鉴权维度） | | | | |
| ACCESSMODE | — | {TRANS_NON_AUTH/TRANS_AUTH/NON_TRANS/LOC_AUTH} | DP-APN-AUTH-MODE | 已知 |
| COMMONUSERNAME/PASS（TRANS_AUTH） | — | {值} | 需求 | **待提供** |
| Radius 服务器组 | — | {RDSSVRGRP 名，可复用现网} | 现网/需求 | 待确认 |
| **接入方式**（仅隧道维度） | | | | |
| GRETUNNEL TNLNAME/SRCIFNAME/DSTIPADDR（GRE） | {值} | — | 需求 | **待提供** |
| IPSECPOLICY/IKEPEER/ACL（IPSec） | {值} | {值}（对称部署） | 需求 | **待提供** |
| APNL2TPATTR 10+ 参数（L2TP U 面） | {值} | — | 需求 | 待确认 |
| APNL2TPCTRL APN/L2TPSWITCH（L2TP C 面） | — | {值} | 推断 | 已知 |
| **并发限制**（可选） | | | | |
| APNACTNUM PDNNUM/IPV4ADDRNUM/IPV6ADDRNUM | — | {值} | 需求 | 待确认 |
```

### License 触发表

```markdown
### License 清单

| License 编号 | 触发维度 | 适用产品侧 | 现网状态 | 状态 |
|-------------|---------|-----------|---------|------|
| LKV3G5VDSA01 | 双栈 | UDG | 已购/未购 | 已知/待确认 |
| ... | ... | ... | ... | ... |
```

### 跨侧一致参数表（U+C 同时配置时必填）

```markdown
### 跨侧一致（CRITICAL）

| 参数项 | UDG 值 | UNC 值 | 一致性 |
|--------|--------|--------|--------|
| APN/DNN 名 | {值} | {值} | 必须一致 |
| L2TPN4KEY / L2TPKEY 密钥（L2TP 场景） | {KEY} | {KEY} | **必须相同**（CR-APN-03） |
| VPNINSTANCE（若两侧都配 VPN） | {值} | {值} | 必须一致 |
| SUPPORTIPV4/SUPPORTIPV6 | {值} | {值} | 必须一致 |
```

---

## 3. 地址池三级规则分析流程（必须独立执行，必须用户确认）

> **核心规则**：地址分配粒度由 `DP-APN-ADDR-GRANULARITY` 决定，对应规则字符串组合。

### 步骤

1. 确认地址分配方式（DP-APN-ADDR-MODE）和粒度（DP-APN-ADDR-GRANULARITY）
2. 从现网提取已有 `SET IPALLOCRULE` / `SET APNIPALLOCRULE`，分析现网规则组合规律
3. 根据用户描述的分配优先级需求，推导三级规则字符串
4. 输出分析表
5. **STOP。将分析表展示给用户，等待用户确认规则字符串。**

### STOP 条件

**完成分析表后必须 STOP，输出分析表并明确要求用户确认。在用户确认之前：**
- **禁止**生成 SET IPALLOCRULE / SET APNIPALLOCRULE 命令
- **禁止**进入 Phase 5 配置生成

### 输出格式

```
## 地址池三级规则分析

**分配方式**: {UPF-APN动态 / UPF-SMF动态 / UPF-LOCATION动态 / ...}
**分配粒度**: {DP-APN-ADDR-GRANULARITY 取值}

**规则字符串推导**:
- FIRSTRULE: {APN-1&LOCATION-0&SMF-0}（基于 APN）
- SECONDRULE: {DISABLE / 规则字符串}（兜底维度）
- THIRDRULE: {DISABLE / 规则字符串}

**现网已有规则**（参考）:
| MAPPINGNAME | APN | POOLGROUPNAME | 现网规则 |
|-------------|-----|---------------|---------|
| ... | ... | ... | ... |

**请确认三级规则字符串设置是否合理。如需调整（如启用兜底回退）请告知。**
```

### 禁止事项

- **禁止**自行假设规则字符串格式，必须严格按 `APN-{0|1}&LOCATION-{0|1}&SMF-{0|1}` 三段式
- **禁止**在用户未确认规则前生成 SET IPALLOCRULE 命令

---

## 4. 注意事项

- 参数表中每个字段都应标注"来源"（需求/现网/推断/图谱/知识库）和"状态"（已知/待确认/待提供）
- **POOLTYPE 跨侧差异**是 APN 最易错点：UDG 必须 LOCAL，UNC 仅 UDM（CR-APN-04），两侧同名参数取值集不同
- **双栈 License 串联**：IPv6 承载（LKV3G5V6PB01）→ 双栈（LKV3G5VDSA01）→ PD（LKV3G5P6PD01），前级必须先激活（BR-APN-IPV6-CASCADE）
- **V6PREFIXLENGTH 分水岭**：=64 为普通 IPv6 单栈；<64 切换 PD 模式（CR-APN-05 / TR-APN-04）
- **L2TP C-U 不对称**：U 侧 APNL2TPATTR 10+ 参数 vs C 侧 APNL2TPCTRL 2 参数，参数集不匹配会导致隧道建链失败（CR-APN-02）
- **L2TP 密钥跨侧一致**：UDG SET L2TPN4KEY 与 UNC SET L2TPKEY 的 KEY 必须相同（CR-APN-03）
- **Radius 级联链**：Radius 功能（011306）→ 鉴权接入（011305）→ 二次鉴权（108007），前级必须先激活（BR-APN-RADIUS-CASCADE）
- **ACCESSMODE 与 Radius 依赖**：仅 TRANS_AUTH/NON_TRANS 强依赖 Radius 功能；TRANS_NON_AUTH/LOC_AUTH 不调用 Radius（TR-APN-02）
- **LOC_AUTH 不支持 PPP 用户**（BR-APN-LOC-AUTH-NO-PPP）
- 遇到不确定的参数语义，加载 `04-command-graph.md` §5 核心命令参数表确认，禁止凭记忆填写枚举值
