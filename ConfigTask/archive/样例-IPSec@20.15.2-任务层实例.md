# IPSec (IPFD-015004) @ UDG 20.15.2 — 任务层实例（多场景同骨架样板）

> 严格按 `ConfigTask/CONFIGTASK_SCHEMA.md` 字段建立。
> 数据来源：`output/.../IP基本特性/IPFD-015004 IPSec功能/特性配置/激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md` 等 9 份变体文档。
> **形态验证**：IPSec 有 9 份"激活"变体文档（普通IPv4/主备/GRE over/IPv6/...），**共享同一 9 步骨架** → **1 个 ConfigTask**，9 个场景由 DecisionPoint 表达（不建 9 个 task）。
> **ID 格式**：`UDG@20.15.2@<ObjectType>@<编号>`；命令/参数引用 `UDG@20.15.2@MMLCommand@...` / `@CommandParameter@...`。每个命令只列关键参数（全量见命令图谱）。

## 对象清单

- **1 ConfigTask**：`@ConfigTask@00001` 建立IPsec隧道
- **2 TaskRule**：`@TaskRule@00001`(双配原则)、`@TaskRule@00002`(PSK必填)
- **1 DecisionPoint**：`@DecisionPoint@00001` 隧道场景选择（9 场景）

---

## 一、ConfigTask 实例

### `@ConfigTask@00001` 建立IPsec隧道

| 字段 | 值 |
|---|---|
| `task_id` | `UDG@20.15.2@ConfigTask@00001` |
| `task_logical_name` | 建立IPsec隧道 |
| `nf` / `version` | UDG / 20.15.2 |
| `raw_steps_text` | 9 步：VNRS侧VPN+隧道口+静态路由 → IPsec侧VPN+隧道口 → 保护数据流(ACL) → IPsec提议 → IKE提议 → IKE对等体 → IPsec策略(策略+绑提议+绑对等体) → 应用策略 → DPD(可选) |
| `task_goal` | 在 VNRS 微服务与 IPsec 微服务间建立 IPsec 隧道，保护指定数据流 |
| `task_summary` | 配置两侧 VPN/隧道口、ACL、IPsec/IKE 提议与对等体、策略并应用到隧道口 |
| `task_category` | 配置 |
| `status` | active |
| `source_evidence_ids` | [`output/.../激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md` 等 9 份] |

**commands（顺序=执行序，9 步骨架，所有场景共享）：**

**步骤1 创建 VNRS 微服务 VPN + IPsec 隧道接口 + 静态路由**
- `UDG@20.15.2@MMLCommand@ADD L3VPNINST` — `VRFNAME` variable/planned
- `UDG@20.15.2@MMLCommand@ADD VPNINSTAF` — `VRFNAME` reference, `AFTYPE` fixed=ipv4uni
- `UDG@20.15.2@MMLCommand@ADD IPBINDVPN` — `IFNAME` variable/planned, `VRFNAME` reference
- `UDG@20.15.2@MMLCommand@ADD IFIPV4ADDRESS` — `IFNAME` reference, `IFIPADDR/SUBNETMASK` variable/planned
- `UDG@20.15.2@MMLCommand@ADD INTERFACE` — `IFNAME` variable/planned, `IFADMINSTATUS` fixed=up（隧道口）
- `UDG@20.15.2@MMLCommand@ADD IPSECINTFCFG` — `INTERFACENAME` reference, `TNLTYPE` fixed=IPSEC
- `UDG@20.15.2@MMLCommand@ADD IPBINDVPN` — `IFNAME` reference, `VRFNAME` reference（隧道口绑 VPN）
- `UDG@20.15.2@MMLCommand@ADD IFIPV4ADDRESS` — 隧道口 IP（双配）
- `UDG@20.15.2@MMLCommand@ADD SRROUTE` — `VRFNAME` reference, `PREFIX/MASKLENGTH/NEXTHOP` variable/planned, `IFNAME` reference

**步骤2 创建 IPsec 微服务 VPN + 隧道接口（与 VNRS 双配）**
- `UDG@20.15.2@MMLCommand@ADD L3VPNINSTIPSEC` — `VRFNAME` variable/planned（**双配**同 VNRS）
- `UDG@20.15.2@MMLCommand@ADD VPNINSTAFIPSEC` — `VRFNAME` reference, `AFTYPE` fixed
- `UDG@20.15.2@MMLCommand@ADD INTERFACEIPSEC` — `IFNAME` variable/planned（**双配**）
- `UDG@20.15.2@MMLCommand@ADD IPBINDVPNIPSEC` — `IFNAME` reference, `VRFNAME` reference（**双配**）
- `UDG@20.15.2@MMLCommand@ADD IFIPV4ADDRESSIPSEC` — `IFNAME` reference, `IFIPADDR` variable/planned（**双配**）

**步骤3 定义保护数据流**
- `UDG@20.15.2@MMLCommand@ADD ACLGROUPIPSEC` — `ACLNAME` variable/planned
- `UDG@20.15.2@MMLCommand@ADD ACLRULEADV4IPSEC` — `ACLNAME` reference, `ACLRULENAME` variable/planned, `ACLACTION` fixed=Permit, `ACLPROTOCOL/ACLSOURCEIP/ACLSRCWILD/ACLDESTIP/ACLDESTWILD` variable/planned, `VRFNAME` reference

**步骤4 IPsec 安全提议**
- `UDG@20.15.2@MMLCommand@ADD IPSECPROPOSALIPSEC` — `PROPOSALNAME` variable/planned, `ESPAUTHALGO/ESPENCRYPTALGO/IPSECPROTOCOL/ENCAPMODE` variable/planned（对端协商）

**步骤5 IKE 安全提议**
- `UDG@20.15.2@MMLCommand@ADD IKEPROPOSAL` — `PROPOSALNUMBER` variable/planned, `AUTHMETHOD` variable/planned（对端协商，default Pre_share）, `AUTHALGORITHM` variable/planned, `DHGROUP` variable/planned（对端协商，不能 None）

**步骤6 IKE 对等体**
- `UDG@20.15.2@MMLCommand@ADD IKEPEER` — `PEERNAME` variable/planned, `PRESHAREDKEY` variable/planned（对端协商，PSK 时必填）, `NATTRAVERSAL` variable/planned, `PROPOSAL` reference, `LOWREMOTEADDR` variable/planned（全网规划）, `INVRFNAME/OUTVRFNAME` reference

**步骤7 IPsec 安全策略（策略 + 绑提议 + 绑对等体）**
- `UDG@20.15.2@MMLCommand@ADD IPSECPOLICY` — `POLICYNAME` variable/planned, `SEQUENCENUMBER` variable/planned, `POLICYMODE/TEMPLATEMODE` variable/planned（对端协商）, `ACLNUMBER` reference（或 ACLNAME）
- `UDG@20.15.2@MMLCommand@ADD PROPATTACHIPSECPROPOSAL` — `POLICYNAME/SEQUENCENUMBER` reference, `IPSECPROPNAME` reference
- `UDG@20.15.2@MMLCommand@ADD ATTACHIKEPEER` — `POLICYNAME/SEQUENCENUMBER` reference, `IKEPEERNAME` reference, `PEERPRIORITY` variable/planned

**步骤8 应用策略到隧道口**
- `UDG@20.15.2@MMLCommand@ADD IPSECINTFCFGIPSEC` — `INTERFACENAME` reference, `TNLTYPE` fixed=IPSEC, `POLICYNAME` reference

**步骤9 DPD（可选）**
- `UDG@20.15.2@MMLCommand@SET IKEGLOBALCONFIG` — `DPDTYPE/DPDINTERVAL/DPDRETRYINTRVL/NATKLI` variable/planned

---

## 二、TaskRule 实例

### `@TaskRule@00001` VNRS 与 IPsec 微服务双配原则

| 字段 | 值 |
|---|---|
| `rule_id` | `UDG@20.15.2@TaskRule@00001` |
| `task_ref` | `UDG@20.15.2@ConfigTask@00001` |
| `rule_name` | VNRS 与 IPsec 微服务双配原则 |
| `rule_type` | `consistency_rule` |
| `rule_logic` | IPsec 协商用到的隧道接口、隧道接口 IP、隧道类型、VPN 必须在 VNRS 微服务与 IPsec 微服务上一对一配置（步骤1 与步骤2 对应命令的 VRFNAME/IFNAME/IFIPADDR 必须一致）；删除时也要同时删两侧，否则业务不通。 |
| `violation_effect` | 业务不通 |
| `severity` | critical |
| `status` | active |
| `source_evidence_ids` | [`output/.../激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md`] |

### `@TaskRule@00002` PSK 认证必须配 PRESHAREDKEY

| 字段 | 值 |
|---|---|
| `rule_id` | `UDG@20.15.2@TaskRule@00002` |
| `task_ref` | `UDG@20.15.2@ConfigTask@00001` |
| `rule_name` | PSK 认证下必须配 PRESHAREDKEY |
| `rule_type` | `conditional_param_rule` |
| `rule_logic` | 当 ADD IKEPROPOSAL.AUTHMETHOD=Pre_share（缺省）时，ADD IKEPEER 必须配置 PRESHAREDKEY 且与对端一致，否则 SA 建立不成功。 |
| `violation_effect` | SA 建立失败 |
| `severity` | critical |
| `status` | active |
| `source_evidence_ids` | [`output/.../激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md`] |

> 单命令约束不入 TaskRule，归 CommandRule：如 `DHGROUP 不能 None`、`对端地址不能地址段`、`ACL 只支持源/目的 IP`、`反掩码 0=精确匹配`。

---

## 三、DecisionPoint 实例（9 场景变体）

### `@DecisionPoint@00001` 隧道场景选择

| 字段 | 值 |
|---|---|
| `decision_id` | `UDG@20.15.2@DecisionPoint@00001` |
| `owner_layer` | task |
| `owner_ref_type` | ConfigTask |
| `owner_ref` | `UDG@20.15.2@ConfigTask@00001` |
| `decision_name` | 隧道场景选择 |
| `decision_question` | 建立哪种 IPsec 隧道场景？（决定步骤内的命令增减/参数取值） |
| `trigger_condition` | 建立IPsec隧道时 |
| `status` | active |
| `source_evidence_ids` | [9 份变体文档] |

**options（每个场景的 impacts 改变骨架内的命令/参数，不另建 task）：**

- `普通IPv4隧道`: impacts = []（基准骨架，无改动）
- `IPv4主备`: impacts = [
    {parameter, `…@ADD IPSECPOLICY:WORKMODE`, sets_value_pattern, =Master_standby},
    {parameter, `…@ADD IPSECPOLICY:AUTOSWITCHBACK`, sets_value_pattern, =Disable},
    {command, `…@MMLCommand@ADD ATTACHIKEPEER`, adds, 出现 2 次（PEERPRIORITY=1/2 绑主备对等体）}]
- `IPv6隧道`: impacts = [
    {command, `…@MMLCommand@ADD IFIPV6ADDRESS`, changes_command_set, 替换 IPv4 地址命令为 IPv6},
    {command, `…@MMLCommand@ADD ACLRULEADV6IPSEC`, changes_command_set, IPv6 ACL}]
- `IPv6主备`: impacts = [IPv6 场景 + 主备参数（同上组合）]
- `GRE over IPsec`: impacts = [
    {command, `…@MMLCommand@ADD GRETUNNEL`, adds, 步骤1 额外建 GRE 隧道}]
- `OSPF over IPsec`: impacts = [
    {command, `…@MMLCommand@ADD OSPF*`, adds, 关联 OSPF 路由配置}]
- `多Sequence`: impacts = [
    {parameter, `…@ADD IPSECPOLICY:SEQUENCENUMBER`, changes_command_set, 多条不同 SEQUENCENUMBER 的策略}]
- `指定本端接口`: impacts = [
    {parameter, `…@ADD IKEPEER:LOCALINTERFACE`, adds, 用指定接口作 IKE 协商本端 IP}]
- `国密IKEv1`: impacts = [
    {parameter, `…@ADD IPSECPROPOSALIPSEC:*ALGO`, sets_value_pattern, 国密算法},
    {parameter, `…@ADD IKEPROPOSAL:IKEVERSION`, sets_value_pattern, =IKEv1}]

---

## 四、关系汇总（存储方向）

| 子对象 | FK 字段 | 父对象 |
|---|---|---|
| TaskRule@00001 / 00002 | `task_ref` | ConfigTask@00001 |
| DecisionPoint@00001 | `owner_ref` | ConfigTask@00001 |

> **本样例验证的关键决策**：9 份"激活"变体文档共享同一 9 步命令骨架 → **建为 1 个 ConfigTask**，9 个场景由 DecisionPoint `隧道场景选择` 的 options 表达（每个 option 用 impacts 增减命令/改参数），**不建 9 个 task、不加 variant_dimensions 字段**（schema §1.11、§6.3）。
> 上层（特性层）：Feature IPFD-015004 `decomposes_to` ConfigTask@00001（单 task 特性）。
