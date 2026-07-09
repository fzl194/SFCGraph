# 跨主题分析 cross-topic-analysis
> EV-CA-02 | 7批次主题知识横向归纳 | ★第1层业务图谱数据源（主体层）
> 业务域=网元对接，子场景=UPF网元对接（UDG 扮演 UPF/PGW-U/SGW-U 融合角色，对接 N4/N3/N9/N6）
> 输入：`topic-knowledge/Batch-01~07`（共60个源文档）
> 输出消费者：`three-layer-graph/01-business-graph.md`（第1层 CS/DP/SO/BR）、`03-task-layer.md`（第3层 Task 编排）、`04-command-layer.md`（第4层 ConfigObject/MMLCommand）
> 编制日期：2026-06-29

---

## 1. 概述（对接场景特殊性：方案/流程驱动，CS 按对接面组织）

UPF 网元对接是**对接类场景**，其主体不是"业务能力配置"，而是"**如何把 UDG 这一虚拟网元接入运营商网络并打通端到端会话**"。这决定了本场景的三层图谱结构与计费/带宽/访问限制等"业务配置类场景"有本质差异：

| 维度 | 业务配置类（计费/带宽） | 对接类（UPF 网元对接，本场景） |
|------|----------------------|------------------------------|
| CS 组织方式 | 按业务能力（基础/计费/带宽/限制） | **按对接面**（CS-1控制面 / CS-2用户面 / CS-3网管 / CS-4路由 / CS-5基础就绪） |
| 主体对象 | 业务规则、URR/PCC/RULE 配置块 | **对接方案闭包（CS）+ 组网模式决策点（DP）** |
| 特性（Feature）角色 | 业务能力的载体（直接配置对象） | **引用支撑**（为对接方案提供能力，如 GWFD-010234 Single IP 支撑接口抽象） |
| 决策复杂度 | 单一业务路径 | **多维组网矩阵**（硬件×SDN×IP版本×路由协议×部署方式） |
| 第3层 Task 主线 | 业务开通流程 | **开局流程**（CS-5→CS-3→CS-1→CS-2→CS-4→FirstCall 调测） |

**5个对接面 CS 的定位**（对应 §6 的5个方案闭包）：

| 对接面 | 全称 | 对接对象 | 核心对象 | 复杂度 |
|--------|------|----------|----------|--------|
| **CS-1** | 控制面对接 | SMF/SGW-C/PGW-C | N4if（N4/Sxa/Sxb 强制合一） | ★★★ 唯一必备接口 |
| **CS-2** | 用户面对接 | (R)AN / I-UPF / ULCL / DN | Saif/Scif/Paif + 会话接入三件套 | ★★★★ 接口+会话双层 |
| **CS-3** | 网管对接 | U2020/MAE | 北向用户/SNMP/网元14参数 | ★★ 5步闭包 |
| **CS-4** | 路由对接 | DC-GW/PE/EOR/Server Leaf | VPN+路由协议+外联口+自动部署 | ★★★★★ 最大最复杂 |
| **CS-5** | 基础就绪 | — | License+NTP+网元身份+公共参数+MTU | ★★★ 全局前置 |

**端到端开局链路**（详见 §9）：
```
CS-5基础就绪 → CS-3网管 → CS-1控制面N4 → CS-2用户面 → CS-4路由 → 调测FirstCall
```

---

## 2. 主题分类与知识地图

### 2.1 对接面 CS-1~CS-5 × 初始配置流程 知识地图

| 批次 | 主要对接面 | 知识点 KP | 输入文档数 |
|------|-----------|----------|-----------|
| Batch-01 | CS-5 架构认知+License | KP-01~11（双模部署/参考点/接口映射表/接口命名/License双路径） | 8 |
| Batch-02 | CS-5 基础数据+CS-3 网管 | KP-01~06（NTP/网元身份/二次授权/公共参数11项/MTU三层/网管5步） | 6 |
| Batch-03 | CS-1 控制面+CS-2 用户面 | KP-01~12（N4配置/7类接口/会话接入三件套/地址分配规则） | 9 |
| Batch-04 | CS-4 非SDN无NP卡自动部署 | KP-01~11（自动部署模板/6种路由方案/IPsec/GRE/MPLS VPN） | 14 |
| Batch-05 | CS-4 非SDN手动+网络加速卡 | KP-01~12（手动vs自动差异/级联口NP100/NP121/加速卡专属路由） | 16 |
| Batch-06 | CS-4 NP卡直连PE+SDN | KP-01~09（NP卡级联口/SDN架构/SDN DHCP+单臂BFD） | 17 |
| Batch-07 | 典型实例+整网调测 | KP-01~08（7个组网组合实例/FirstCall 4阶段29步） | 8 |

### 2.2 知识维度交叉矩阵

```
              CS-5基础  CS-3网管  CS-1控制面  CS-2用户面  CS-4路由
架构认知        ★★★★★     —        ★★★★       ★★★★       ★★★
License         ★★★★      —         —          —          —
基础数据        ★★★★★    ★★★       —          —         ★★★(MTU)
接口配置         —        —        ★★★★★     ★★★★★      ★★(外联口)
会话接入         —        —         —         ★★★★★       ★
路由协议         —        —         —          ★(下行路由) ★★★★★
自动部署         —        —         —          —         ★★★★★
SDN/NP/加速卡    —        —         —          —         ★★★★★
端到端调测       —        —         ★(N4偶联)  ★(逻辑接口) ★★★★★(路由负荷分担)
```

---

## 3. 共性机制分析（→第1层 SemanticObject / 第4层 ConfigObject）

### 3.1 接口配置范式：ADD VPNINST → ADD LOGICINF（统一掩码，VPN四统一）

CS-1/CS-2 全部业务逻辑接口遵循**同一套命令范式**（Batch-03 §3.1）：

```
ADD VPNINST: VPNINSTANCE="<VPN_业务面>";           # 步骤1：VPN实例
ADD LOGICINF: NAME="<接口名>", IPVERSION=<IPV4|IPV6|IPVER_ALL>,
              IPV4ADDRESS1="<IP>", IPV4MASK1="255.255.255.255",   # ★掩码固定 /32
              VPNINSTANCE="<VPN_业务面>", [SLICEATTRSW=<ENABLE|DISABLE>];  # 步骤2：逻辑接口
```

**核心共性约束**（→ BusinessRule BR-VPN-4UNIFY）：
- **掩码统一**：所有逻辑接口 IPV4MASK1 固定 `255.255.255.255`（/32 主机路由）
- **VPN 四统一**（Batch-03 §3.5）：业务 APN 绑定 VPN、地址池绑定 VPN、Gi/SGi/N6 外联口绑定 VPN、各业务逻辑接口绑定 VPN —— 四者必须一致
- **网段隔离**（Batch-03 KP-01）：逻辑接口 IP **不能**与外联口 IP 同网段，也**不能**与对端物理接口 IP 同网段

**接口名规范**（→ SO_InterfaceName）：
| 接口类型 | 配置方式 | 命名规则 |
|----------|----------|----------|
| Saif（Sa/N3/S1-U 合一） | 可选合一（推荐） | `Saif1/1/0`（最后位 0~31） |
| Scif（Sc/N9c/S5-S/S8-S 合一） | 可选合一（推荐） | `Scif1/1/0` |
| Paif（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U 合一） | **强制合一** | `Paif1/1/N`（N=0~31） |
| N4if（N4/Sxa/Sxb 合一） | **强制合一** | `N4if1/0/0`（唯一） |
| S11-uif | 独立（无抽象） | `S11-uif1/1/0` |
| SGi/N6/Gi | 无逻辑接口（物理外联口） | — |

### 3.2 路由对接 5 层共性结构（→ CS-4 方案骨架）

所有 6 种路由方案 + 3 种隧道（IPsec/GRE/MPLS VPN）遵循统一配置层次（Batch-04 §3.1）：

```
[层1 VPN实例]    ADD L3VPNINST + ADD VPNINSTAF (ipv4uni / ipv6uni)
[层2 全局使能]   SET BFD:BFDENABLE=TRUE [+SET BGP / +SET MPLSSITE]
[层3 路由协议]   OSPF/OSPFv3：进程+区域+引入路由(+NSSA时Loopback)
                 静态：静态路由模板+BFD模板
                 BGP：VPN实例+地址族+对等体+引入路由(依赖IGP)
[层4 外联口]    自动部署：ADD AUTOSCALINGSERVICE (OSPF方案带OSPFENABLE)
                 手动部署：MOD INTERFACE→ADD INTERFACE→ADD IPBINDVPN→ADD ETHSUBIF→ADD IFIPV4/V6ADDRESS
[层5 开关驱动]   自动：关→配模板→开，必须 DSP OPSASSISTSTATE 确认 Ready
                 手动：无开关，逐条下发
```

### 3.3 自动部署模板族（→ ConfigObject AutoScalingTemplate）

8 个 AUTOSCALING 模板命令构成自动部署的配置对象族（Batch-04 KP-01）：

| 模板命令 | 用途 | 适用场景 |
|---------|------|---------|
| `ADD AUTOSCALINGETHTRUNK` | SR-IOV bonding Eth-trunk 模板 | bonding 组网（VNICLIST 两个 MAC 相同且 ID 连续） |
| `ADD AUTOSCALINGSERVICE` | ★外联口自动部署主模板 | 所有自动部署场景 |
| `ADD AUTOSCALINGBFD` | BFD 会话模板（单臂 echo） | 静态路由/SDN/网络加速卡场景 |
| `ADD AUTOSCALINGSRBFD` | 静态路由动态 BFD 模板（双向） | 静态路由双向检测场景 |
| `ADD AUTOSCALINGSRROUTE` | 静态路由模板 | 静态路由/BGP over 静态场景 |
| `ADD AUTOSCALINGBGPLF` | BGP 入不转板策略模板 | BGP over 静态 + 入不转板场景 |
| `ADD AUTOSCALINGIPREACH` | RU 可达性检测模板 | 入不转板配套 |
| `ADD AUTOSCALINGMPLS` | MPLS 接口自动化模板 | MPLS VPN 自动部署场景 |

**`ADD AUTOSCALINGSERVICE` 关键参数差异**（→ variant_dimensions）：

| 参数 | 非SDN自动(USER_CONFIG) | SDN自动 | 网络加速卡 |
|------|----------------------|---------|----------|
| IPALLOCTYPE4/6 | `USER_CONFIG` | **`DHCP`** | `USER_CONFIG` |
| NEXTHOPALLOCTYPE4/6 | `CONFIG` | **`DHCP`** | `CONFIG` |
| AUTOCFGIFTYPE | VNIC / ETHTRUNK | VNIC / ETHTRUNK | **ETHTRUNK（强制）** |
| OSPFENABLE | 支持（OSPF 方案） | **不支持** | **不支持（仅静态基础）** |

### 3.4 会话接入三件套（→ SO_SessionAccess）

用户激活接入 PDN/DN 的完整闭环（Batch-03 §3.4）由三层构成：

```
[层1 APN/DNN]   ADD APN:APN="<apn>", HASVPN=ENABLE, VPNINSTANCE="<VPN_业务>"
                  ↓ POOLGRPMAP 映射
[层2 地址池]    ADD POOL(LOCAL|EXTERNAL) → ADD SECTION → ADD POOLGROUP
                  → ADD POOLBINDGROUP → ADD POOLGRPMAP(APN↔POOLGROUP)
[层3 分配规则]  SET IPALLOCRULE:FIRSTRULESW=ENABLE,
                  FIRSTRULE=APN-1&LOCATION-0&SMF-0  # 默认 APN 维度使能
```

**地址池类型决策**（→ DP-CS2-05）：
- `LOCAL`：UDG 作主锚点 + UDG 给 UE 分配 IP（需完整三件套）
- `EXTERNAL`：辅锚点/ULCL/外部 NF（如 UDM）分配 IP（仅 POOL+SECTION，可选 CHECKIPVALID）

### 3.5 高危命令二次授权机制（→ SO_SecurityAuth）

13 类 UDG 默认二次授权命令清单（Batch-02 KP-03），开局自动化脚本必须先 `SET SECAUTH:STATUS=ON` + `ADD USRSECAUTH` 才能避免高危 MML（SET OMIP / MOD VIRTUALIP / SET FWDPARA / IPsec 系列）弹窗阻塞。

---

## 4. 配置差异对比（→第4层 CommandParameter）

### 4.1 SDN vs 非SDN 差异矩阵（★CS-4 核心差异，Batch-06 F-1）

| 维度 | 非SDN（自动/手动/NP卡/加速卡） | SDN |
|------|------------------------------|-----|
| 路由协议支持 | OSPF / 静态 / BGP over OSPF·静态 / MPLS VPN | **仅 BGP over 静态路由 / BGP MPLS VPN**（不支持 OSPF） |
| 外联口 IP 获取 | 静态规划 `ADD IFIPV4ADDRESS` | **DHCP 动态获取**（`IPALLOCTYPE4/6=DHCP`） |
| 下一跳获取 | 静态 IP | **DHCP**（`NEXTHOPALLOCTYPE4/6=DHCP`） |
| BFD 模式 | 双向 BFD + 单臂 Echo（可选） | **强制单臂 BFD Echo**（`ONEARMECHO=TRUE`） |
| BFD 目的地址 | 网关接口 IP（DC-GW/PE） | **Leaf 节点 IP**（VNF↔Server Leaf 直连检测） |
| BGP 对等体对象 | PE / DC-GW | **DC-GW**（经 Leaf/Spine 中转） |
| IPv6 前置 | 默认 | **`SET DHCP6CLIENTDUID:DUIDTYPE=MAC_PLUS_VLAN`** 必配 |
| 外联口 IPv6 地址模式 | 默认 | **`ADDRMODE=NETWOKSEGMENT_MODE`**（强制） |
| `SET IFIPV6ENABLE` 参数 | 默认 | **`AUTOLINKLOCAL=TRUE`** 必设 |
| `ADD SRROUTE` 参数 | 默认 | **`DHCPENABLE=TRUE`** 必设 |
| 控制器协同 | 无 | SDN 控制器统一纳管 DC-GW/Spine/Leaf |
| VPN 命名前缀 | `VPN_*` | `VRF_*` |
| 描述文件 | VNFD | VNFD + **NSD**（新增） |
| 部署组件 | VNFM | **NFVO**（直接部署 VNF） |

### 4.2 自动 vs 手动部署差异（Batch-04 §3.5 / Batch-05 KP-01）

| 配置层 | 自动部署 | 手动部署 |
|--------|---------|---------|
| 外联口/子接口/VLAN/IP/VPN | `ADD AUTOSCALINGSERVICE`（1 模板） | 逐条：MOD INTERFACE→ADD INTERFACE→ADD IPBINDVPN→ADD ETHSUBIF→ADD IFIPV4/V6ADDRESS |
| BFD 会话 | `ADD AUTOSCALINGBFD`（模板） | `ADD BFDSESSION`（逐条，含 LOCALDISCR/REMOTEDISCR） |
| 静态路由 | `ADD AUTOSCALINGSRROUTE`（模板） | `ADD SRROUTE`（逐条，SESSIONNAME 绑定 BFD） |
| **MPLS 接口** | **`ADD AUTOSCALINGMPLS`**（VM 扩容自动适配） | **`ADD MPLSIF`**（逐个，扩容需手工补） |
| OSPF/BGP 协议层 | **与手动完全一致** | 与自动完全一致 |
| 自动化开关 | SET AUTOCONFIG:SWITCHFLAG 控制 | 不涉及 |

**核心结论**：协议层（OSPF/BGP/MPLS VPN 的 VPN 实例/对等体/地址族/RT/LDP 等）命令在手动与自动部署中**完全一致**；差异集中在**外联口基础设施层**和 **MPLS 接口层**。

### 4.3 硬件类型差异（无NP卡 / NP卡直连PE / 网络加速卡直连DC-GW）

| 维度 | 无NP卡标卡 | NP卡直连PE | 网络加速卡直连DC-GW |
|------|----------|----------|-------------------|
| 物理口命名 | `Ethernet66/0/X` | `100GE66/0/9`(NP100) / `400GE·200GE66/0/9`(NP121) | `100GE·400GE·200GE X/0/X` |
| 自动部署 | ✅ 推荐 | ❌ 不支持 | ✅（强制 SR-IOV bonding + LACP） |
| SDN 组网 | ✅ | ❌ | ❌ |
| OSPF 支持 | ✅ | ✅ | ✅ |
| BGP over 静态 | ✅ | ✅ | ✅（**仅此一种路由**，不支持 OSPF） |
| Eth-trunk 模式 | Manual（可选） | — | **Lacp 强制（passive），DC-GW 必须 active** |
| BFD 模式 | 双向/单臂可选 | 双向/单臂 | **强制单臂 Echo** |
| bonding 必要性 | 可选 | — | **强制** |
| 级联口命令 | 无 | `ADD NPDIRECTCONNECTPORT`（NP100 多框级联） | `ADD NPDIRECTCONNECTPORT`（NP100 多框级联） |
| 级联口型号 | — | NP100 有 P3/P4；NP121 无 | NP100 有 P3/P4；NP121 无 |

### 4.4 IPv4 vs IPv6 vs IPv4v6 双栈差异（→ variant_dimensions IPVersion）

| 维度 | IPv4 | IPv6 | IPv4v6 双栈 |
|------|------|------|------------|
| VPN 地址族 | `ipv4uni` | `ipv6uni` | **两个地址族都要配** |
| OSPF 进程 | `ADD OSPF`（SCHEMAROUID） | `ADD OSPFV3`（ROUTERID, DETECTMULINTV） | 分别配 |
| OSPF NSSA 区域 | 需配 Loopback（自动选 FA） | 不需配 Loopback | 分别配 |
| 外联口掩码 | `MASKLEN=25`（典型） | `MASKLEN=121`（典型） | 分别配 |
| 静态路由前缀 | `PREFIX4` / `NEXTHOP4` | `PREFIX6` / `NEXTHOP6` | 分别配 |
| Loopback | /32 | /128（需先 `SET IFIPV6ENABLE`） | 同接口配 IPv4+IPv6 |
| BGP 对等体 | `ADDRESSTYPE=ipv4` | `ADDRESSTYPE=ipv6` | 各一套 |
| 逻辑接口 IPVERSION | `IPV4` | `IPV6` | **`IPVER_ALL`** |
| APN | `HASVPN=ENABLE` | `HASVPNIPV6=ENABLE` | 两者都 ENABLE |
| 地址段 SECTION | V4STARTIP/V4ENDIP | V6PREFIXSTART/END/LENGTH=64 | SECTIONNUM=1(v4)+2(v6) |
| Eth-trunk 硬件模板 | 1 个 | 1 个 | **1 个（硬件层共享）** |
| SDN DHCPv6 前置 | 不需要 | `SET DHCP6CLIENTDUID` 必配 | 必配 |
| SDN 外联口 IPv6 模式 | — | `ADDRMODE=NETWOKSEGMENT_MODE` | 必配 |
| BGP ROUTERID | 实例级 | **与 IPv4 共用一个 ROUTERID** | 删除 IPv4 地址族前必须查记录 ROUTERID 并用 `MOD BGPVRF` 补回 |

---

## 5. 依赖关系与协同（→ BusinessRule）

### 5.1 N4 必备性原则（→ BR-N4-MANDATORY）

- **规则**：UPF 对接时 **N4 是唯一必配接口**，其余接口按 UPF 角色（PSA/ULCL/BP/I-UPF）和位置动态确认（Batch-01 KP-07）
- **附加约束**（Batch-03 §3.3）：N4 单独配置不足以建立偶联，UDG 上**至少需存在一个数据面逻辑接口 IP**（Paif/Scif/Saif/N3if/S1-uif/S11-uif 任一）
- **多 SMF 对接**：需额外配置 `GWFD-020161 CU Full Mesh` 特性并申请 License
- **位置决定接口集**（Batch-01 §3.5）：
  - ULCL + 本地 PSA 共建：N3+N4+N9c+N9a+N6 五接口
  - 拆分 ULCL UPF：N3+N4+N9c
  - 拆分 PSA UPF：N4+N9a+N6

### 5.2 Paif/N4if 强制合一（→ BR-INTERFACE-FORCE-MERGE）

- **规则**：因 4G/5G 互操作时移动锚点不变、协议相同，**Paif 和 N4if 不支持独立配置**，只能使用合一抽象接口（Batch-01 KP-06）
  - N4if：N4/Sxa/Sxb 强制合一（TS 29.244 协议相同）
  - Paif：N9a/S5-P/S8-P/S2b/Gn-U/Gp-U 强制合一（数据锚点不变，地址必须相同）
- **对比**：Saif（Sa/N3/S1-U）和 Scif（Sc/N9c/S5-S/S8-S）**可选合一**，与独立配置互斥

### 5.3 VPN 四统一原则（→ BR-VPN-4UNIFY，§3.1）

业务 APN 绑定 VPN、地址池绑定 VPN、Gi/SGi/N6 外联口绑定 VPN、各业务逻辑接口绑定 VPN —— **四者必须一致**。

### 5.4 接口↔路由↔会话接入协同（→ BR-CROSS-DOMAIN）

- **接口→路由**：逻辑接口绑定 VPN 必须与对应外联口 VPN 一致（路由侧规划）
- **会话接入→路由**：用户下行路由发布（wlr 协议标识）依赖路由协议承载
- **N4→数据面接口**：N4 偶联成功需数据面逻辑接口存在
- **Saif 合一→跨域协同**：UDG 用 Saif 抽象接口（N3 与 S1-U IP 合一）时，若无线侧 NG-U 与 S1-U IP 也合一，无线侧要求两者配在**同一用户面 EPGROUP**（跨设备协同约束）

### 5.5 MTU 层级约束（→ BR-MTU-HIERARCHY，Batch-02 KP-05）

- **层级**：网卡 MTU ≥ Fabric MTU > 主接口 MTU ≥ 子接口 MTU（建议子接口与主接口一致）
- **对齐**：外联口 MTU 必须与直连下一跳网关（DCGW/路由器）一致，默认 1500
- **IPv6 分片联动**：`SET IPV6FRAGPLCY:INNERIPV6FRAGPLCY` 初始值 `TOOBIG_PKTDROP` 在 MTU 偏小时丢包，业务稳定需改 `OUTERFRAG`
- **Eth-trunk 特殊**：不修改成员接口 MTU；成员接口加入 Eth-trunk 前修改 MTU 会导致添加失败
- **模板同步**：仅修改接口 MTU 不同步 `MOD AUTOSCALINGSERVICE` 会触发告警 **ALM-232398849**

### 5.6 CS-5 → CS-3 回流约束（→ BR-FLOAT-IP-RECONNECT，Batch-02 发现1）

修改浮动 IP（`SET OMIP`）会**中断网管和 VNFM 连接**，必须重对接网管（CS-3 完整5步重跑）。`SET OMIP` 本身是默认二次授权命令，需先完成二次授权配置。

### 5.7 网管对接密码三元组（→ BR-CS3-PASSWORD-TRIPLE，Batch-02 发现4）

CS-3 网管对接 3 类帐号中，**后两类有严格初次对接密码约束**：
- 北向对接用户：**必须重置密码**
- SNMP 用户：**必须重置共享认证密钥和共享加密密钥，且两者不能相同**
- 任何一项不满足，对接直接失败（开局最常见对接失败原因）

### 5.8 BGP 依赖关系（→ BR-BGP-DEPENDENCY）

- BGP **自身无自动部署**，依赖 OSPF/静态路由的 IGP 自动部署基础
- BGP **自身不能发现路由**，必须 `ADD IMPORTROUTE:IMPORTPROTOCOL=wlr` 引入
- BGP 需专用 Loopback 接口（与 IGP 外联口同 VPN），建立 eBGP 邻居（`EBGPMAXHOP=10`）
- DC-GW 双活网关/M-LAG 场景**只支持 BGP over 静态路由+BFD 单臂 echo，不支持 OSPF**

### 5.9 MPLS VPN 独特性（→ BR-MPLS-VPN-PUBLIC，Batch-04 §3.6）

- 外联口 VPN 固定 `_public_`（不绑业务 VPN）
- **不配置 IPv6 外联口**（MP-EBGP 用 IPv4 eBGP 传 IPv6 私网路由）
- Loopback 接口**不绑 VPN**（用公网 BGP 传私网路由）
- **必须配 VRFRD**（路由标识），不同 VPN 实例不能重复
- MP-EBGP 开关 = `ADD BGPVRFAF:VRFNAME="_public_", AFTYPE=ipv4vpn`
- 标签节省组合：VPN 侧 `VRFLABELMODE=perInstance` + BGP 侧 `APPLYLABELMODE=perNexthop`

### 5.10 自动部署开关操作规范（→ BR-AUTOCONFIG-SWITCH）

```
LST AUTOCONFIG → DSP OPSASSISTSTATE(确保 autoscaling_autoconfig.py 为 Ready)
   → SET AUTOCONFIG:SWITCHFLAG=FALSE（关）
   → 配置所有 AUTOSCALING* 模板
   → SET AUTOCONFIG:SWITCHFLAG=TRUE（开）
   → DSP OPSASSISTSTATE(确认 Ready 后再做其他操作)
```

---

## 6. ★与 UPF 网元对接核心关联（→ 第1层 CS 方案闭包 + DP 决策点，主体层数据源）

> 本节是 `01-business-graph.md` 的直接输入。每个 CS 方案闭包明确：**方案要素 / uses_feature(引用 EV-FK) / uses_task / 决策点 DP / 业务规则 BR / 语义对象 SO**。

### 6.1 CS-1 控制面对接方案闭包（N4 ↔ SMF/SGW-C/PGW-C）

**方案要素**：
| 要素 | 取值/规则 | 来源 |
|------|----------|------|
| N4 接口类型 | **强制合一抽象接口 N4if**（不支持独立 Sxa/Sxb） | B3-KP-02 |
| N4 接口名称 | 固定 `N4if1/0/0`（唯一） | B3-KP-02 |
| N4 对端网元 | SMF / SGW-C / PGW-C（融合部署） | B3-KP-02 |
| N4 协议 | PFCP（3GPP TS 29.244） | B3-KP-02 |
| UPF 标识 | `SET UPINFO:HOSTNAME` 全网唯一 | B3-KP-02 |
| N4 偶联前提 | UDG 上至少存在一个数据面逻辑接口 IP | B3-KP-02 |
| 多 SMF 对接 | 需 GWFD-020161 CU Full Mesh 特性 + License | B3-KP-02 |
| VPN 实例 | `VPN_Signaling`（与对应外联口 VPN 一致） | B7-KP-01 |

**uses_feature**（引用 EV-FK）：
- `GWFD-010234 Single IP`（接口抽象合一能力）
- `GWFD-020161 CU Full Mesh`（一个 UPF 对接多个 SMF 场景，需 License）
- `GWFD-010105 用户面地址分配`（N4 会话与地址分配联动）

**uses_task**（→ 第3层 Task）：
- T-CS1-01 配置 N4 VPN 实例（`ADD VPNINST:VPNINSTANCE="VPN_Signaling"`）
- T-CS1-02 配置 N4if 合一逻辑接口（`ADD LOGICINF:NAME="N4if1/0/0",...`）
- T-CS1-03 配置 UPF 标识（`SET UPINFO:HOSTNAME`）
- T-CS1-04 N4 偶联验证（`SRVPING` / `SRVTRACERT` / `DSP ROUTE`）

**决策点 DP**：
| DP ID | 决策点 | 选项 | 影响 |
|-------|--------|------|------|
| DP-CS1-01 | IP 版本 | IPv4 / IPv6 / IPv4v6 双栈 | IPVERSION 取值（IPV4/IPV6/IPVER_ALL） |
| DP-CS1-02 | 多 SMF 对接 | 单 SMF（默认）/ 多 SMF | 是否启用 GWFD-020161 + License |

**业务规则 BR**：BR-N4-MANDATORY（§5.1）、BR-INTERFACE-FORCE-MERGE（§5.2）、BR-VPN-4UNIFY（§5.3）

**语义对象 SO**：
- `SO_N4Interface`（N4if1/0/0，强制合一抽象）
- `SO_VPN_Signaling`（VPN 实例）
- `SO_UPFIdentity`（HostName 全网唯一）
- `SO_PFCPSession`（PFCP 会话，承载 PDR/FAR/QER 规则下发）

---

### 6.2 CS-2 用户面对接方案闭包（N3/N9/N6 接口 + 会话接入）

**方案要素**（按 UDG 部署位置 → 接口组合，Batch-03 §4.2）：
| UDG 角色 | 必配用户面接口 | 对端网元 | 协议接口 |
|----------|---------------|----------|----------|
| **边缘 ULCL/BP/I-UPF / SGW-U** | Saif(或N3if/S1-uif) + Scif(或N9cif/S5-Sif) | (R)AN + PSA UPF/PGW-U | Sa/N3/S1-U + Sc/N9c/S5-S |
| **锚点 PSA UPF / PGW-U** | Paif + (SGi/N6 外联口) | ULCL/ePDG/SGSN + DN/PDN | Pa(N9a/S5-P/S8-P/S2b/Gn-U/Gp-U) + SGi/N6 |
| **融合 UPF+PGW-U(+SGW-U)** | Saif + Scif + Paif + (SGi/N6) | 全套 | Sa+Sc+Pa+SGi/N6 |
| **NB-IoT SGW-U** | S11-uif（附加） | MME | S11-U |
| **NWDAF 对接** | Nupf（附加） | NWDAF | HTTP/SBI（需 SSU+SBIM 服务） |

**会话接入子要素**：
| 要素 | 取值/规则 | 来源 |
|------|----------|------|
| APN/DNN 实例 | UDG 本端与 C 面（SMF/SGW-C/PGW-C）一致 | B3-KP-09 |
| 地址池类型 | LOCAL（UDG 主锚点分配 IP）/ EXTERNAL（外部 NF 分配） | B3-KP-10 |
| 地址分配规则 | 三级（默认仅第一级 APN 维度使能） | B3-KP-11 |
| 切片绑定 | 仅 Saif/N3if 支持 `SLICEATTRSW` + `ADD SNSSAIUPINTF` | B3-KP-03 |
| DN-AAA 互通 | 方案A N6 直连 / 方案B N4 专用会话（不占 License） | B3-KP-07 |

**uses_feature**：
- `GWFD-010234 Single IP`（接口抽象合一）
- `GWFD-010105 用户面地址分配`
- `GWFD-020421 基于位置的地址分配`
- `IPFD-010001 接口管理`（接口配置基础）

**uses_task**：
- T-CS2-01 配置业务面 VPN 实例（VPN_Access/VPN_Sc/VPN_Pa/VPN_Internet）
- T-CS2-02 配置接入侧接口（Saif 或 N3if/S1-uif，含切片绑定）
- T-CS2-03 配置中间侧接口（Scif 或 N9cif/S5-Sif）
- T-CS2-04 配置锚点侧接口（Paif 强制合一）
- T-CS2-05 配置会话接入 APN/DNN
- T-CS2-06 配置地址池三件套（POOL→SECTION→POOLGROUP→POOLBINDGROUP→POOLGRPMAP）
- T-CS2-07 配置地址分配规则（SET IPALLOCRULE）
- T-CS2-08（按需）配置 Nupf 服务化接口（ADD LOGICIP+HTTPLEGRP+HTTPLE+SBIAPLE）

**决策点 DP**：
| DP ID | 决策点 | 选项 |
|-------|--------|------|
| DP-CS2-01 | UPF 角色 → 接口组合 | 边缘/锚点/融合/NB-IoT/NWDAF |
| DP-CS2-02 | IP 版本 | IPv4 / IPv6 / 双栈 |
| DP-CS2-03 | Sa/Sc 合一 vs 独立 | Saif/Scif（推荐合一）或 N3if/S1-uif/N9cif/S5-Sif（互斥） |
| DP-CS2-04 | 接入侧切片绑定 | SLICEATTRSW=ENABLE + ADD SNSSAIUPINTF |
| DP-CS2-05 | 地址分配主体 | LOCAL（UDG 分配）/ EXTERNAL（外部 NF 分配） |
| DP-CS2-06 | 地址分配维度 | APN / SMF / 位置（默认 APN） |
| DP-CS2-07 | 用户下行路由发布 | OSPF/OSPFv3 动态 / BGP over 静态 / 纯静态（PROTOCOL=wlr） |
| DP-CS2-08 | DN-AAA 互通 | 方案A N6 直连 / 方案B N4 专用会话 |

**业务规则 BR**：BR-INTERFACE-FORCE-MERGE（Paif 强制合一）、BR-VPN-4UNIFY、BR-CROSS-DOMAIN（§5.4）

**语义对象 SO**：
- `SO_AccessInterface`（Saif/N3if/S1-uif）
- `SO_CoreInterface`（Scif/N9cif/S5-Sif）
- `SO_AnchorInterface`（Paif 强制合一）
- `SO_ExternalInterface`（SGi/N6 物理外联口）
- `SO_NupfInterface`（服务化接口，HTTP/SBI）
- `SO_APN_DNN`（接入点实例）
- `SO_AddressPool / SO_AddressSection / SO_PoolGroup / SO_PoolBinding / SO_PoolGroupMap`（地址池五件套）
- `SO_IPAllocRule`（三级地址分配规则）

---

### 6.3 CS-3 网管对接方案闭包

**方案要素**（5 步闭包，Batch-02 KP-06）：
| 要素 | 取值/规则 | 来源 |
|------|----------|------|
| 前置帐号准备 | 网管用户 + 北向对接用户（必须重置密码）+ SNMP 用户（必须重置共享认证/加密密钥且不相同） | B2-KP-06 |
| 北向对接用户密码 | 初次对接必须重置 | B2-KP-06 |
| SNMP 共享密钥 | OM Portal "系统 > SNMP管理 > 重置共享密钥" | B2-KP-06 |
| 网管适配层安装 | 华为支持网站下载版本配套软件 → 网管侧安装 | B2-KP-06 |
| 创建网元 14 项参数 | 名称/IP（外网浮动IP）/TLS连接/OSS认证（证书/匿名）/emscomm账号+密码/SNMPV3/v3User/端口8000/SHA512+AES256（推荐） | B2-KP-06 |
| 证书场景 | LiteCA 自动更新 5 前置；4 类证书场景不支持自动更新 | B2-KP-06 |
| EMS 归属检查 | VNF LCM 独立部署时在 "VNFM-EMS管理" 检查 | B2-KP-06 |
| 验证 | U2020/MAE 执行 `LST ME` 成功 | B2-KP-06 |

**uses_feature**：
- `NPFD-010000 操作维护功能`（OM Portal 北向/SNMP/证书属操作维护范畴）
- `NPFD-010014 支持NTP功能`（间接关联，CS-5 基础）

**uses_task**：
- T-CS3-01 重置北向对接用户密码
- T-CS3-02 重置 SNMP 用户共享认证/加密密钥
- T-CS3-03 安装网管适配层
- T-CS3-04 创建 UDG 网元（14 项参数）
- T-CS3-05（仅 VNF LCM 独立部署）检查 VNF 已添加到所属 EMS
- T-CS3-06 验证 LST ME 执行成功

**决策点 DP**：
| DP ID | 决策点 | 选项 |
|-------|--------|------|
| DP-CS3-01 | 认证模式 × 协议版本 × 加密协议 | OSS：证书/匿名；协议：SNMPV3（推荐）；授权：SHA512（推荐）/SHA（不安全告警ALM-136750）；加密：AES256（推荐） |
| DP-CS3-02 | VNF LCM 部署形态 × 适配层时序 | 独立+已装+选EMS=跳过；独立+未装+选EMS=仅装适配层；合设=完整5步 |
| DP-CS3-03 | 证书更新路径 | LiteCA 自动（5前置）/ 手动（4类证书场景） |

**业务规则 BR**：BR-CS3-PASSWORD-TRIPLE（§5.7）、BR-FLOAT-IP-RECONNECT（§5.6）

**语义对象 SO**：
- `SO_NorthboundUser`（北向对接用户）
- `SO_SNMPUser`（SNMP 用户）
- `SO_NetworkMgmtAdapter`（网管适配层）
- `SO_ManagedNE`（网管侧创建的网元，14 参数）
- `SO_EMSAssociation`（EMS 归属关系）

---

### 6.4 CS-4 路由对接方案闭包（★最大，含组网模式决策树）

**方案要素**（一个完整的 CS-4 闭包由以下要素组合决定，Batch-04 §4.1）：
- **VPN 实例**：业务隔离（VPN_Access / VRF_Internet / VRF_PDNx / `_public_`）
- **路由协议**：OSPF / OSPFv3 / 静态 / BGP（依赖 IGP）
- **BFD 探测**：双向 BFD / 单臂 echo（BFD Echo）
- **外联口形态**：子接口（推荐）/ 主接口；SR-IOV bonding / 非 bonding
- **IP 版本**：IPv4 / IPv6 / IPv4v6 双栈
- **隧道叠加**：无 / IPsec / GRE / MPLS VPN
- **部署方式**：自动部署（推荐）/ 手动部署

#### ★组网模式 DP 决策树（CS-4 核心，5 维矩阵）

```
根决策（DP-CS4-ROOT）：硬件类型 × 组网架构 × 部署方式
│
├─ DP-CS4-01 硬件类型
│   ├─ A. 无NP卡标卡（Ethernet66/0/X）→ 自动/手动均可，全路由协议支持
│   ├─ B. NP卡直连PE → ★不支持自动部署、★不支持SDN；全路由协议支持（手动）
│   └─ C. 网络加速卡直连DC-GW
│       ├─ C1. NP100（100GE，有级联口P3/P4）→ 自动部署；仅BGP over静态+BFD单臂Echo
│       └─ C2. NP121（400GE/200GE自适应，无级联）→ 自动部署；仅BGP over静态+BFD单臂Echo
│
├─ DP-CS4-02 组网架构（SDN vs 非SDN）
│   ├─ A. 非SDN
│   │   ├─ A1. 三层/二层架构（DC-GW作L3GW）→ 全路由类型（OSPF/静态/BGP/MPLS）
│   │   └─ A2. 二层/一层架构（DC-GW作L3GW+L2GW）→ 仅静态/BGP over静态（OSPF产生环路，禁用）
│   └─ B. SDN（Leaf-Spine + NFVO + SDN控制器）
│       ├─ ★不支持OSPF
│       ├─ ★外联口IP DHCP动态获取
│       ├─ ★强制单臂BFD Echo（DEST=Leaf IP）
│       └─ ★仅 BGP over 静态路由 / BGP MPLS VPN
│
├─ DP-CS4-03 部署方式
│   ├─ A. 自动部署（推荐）
│   │   ├─ 适用：无NP卡或NP卡直连TOR；SDN；网络加速卡
│   │   ├─ 命令：AUTOSCALING* 模板族 + SET AUTOCONFIG 开关
│   │   └─ ★约束：部署完成后无法自动修改/删除；扩容零人工
│   └─ B. 手动部署
│       ├─ 适用：NP卡直连PE（必须）；自动部署失败补救；手动调测
│       ├─ 命令：逐条 MOD/ADD INTERFACE + ADD MPLSIF（MPLS接口关键差异）
│       └─ ★MPLS场景扩容需手工补 ADD MPLSIF
│
├─ DP-CS4-04 路由协议 × IP 版本（6种基础组合 + 3种隧道）
│   │              IPv4          IPv6          IPv4v6双栈
│   ├─ OSPF/OSPFv3 ✓ KP-02       ✓ KP-05(OSPFv3) 分别配
│   ├─ 静态路由    ✓ KP-03       ✓ KP-06        分别配
│   ├─ BGP over    ✓ KP-04       ✓ KP-07        分别配
│   ├─ IPsec       跨安全域信令/数据（Sxa/Sxb/N4/S1-U/N3）
│   ├─ GRE隧道     PGW-U/UPF↔WAP网关（N6/SGi，基于Loopback）
│   └─ MPLS VPN    UDG作PE对接企业网（OptionB跨域，外联口_public_）
│
├─ DP-CS4-05 BFD 模式
│   ├─ A. 双向BFD（ADD AUTOSCALINGSRBFD 或 ADD BFDSESSION 双臂）→ 非SDN OSPF/静态场景
│   └─ B. 单臂BFD Echo（ADD AUTOSCALINGBFD ONEARMECHO=TRUE 或 ADD BFDSESSION ONEARMECHO=TRUE）
│       → SDN强制 / 网络加速卡强制 / DC-GW双活网关·M-LAG强制
│
├─ DP-CS4-06 外联口形态
│   ├─ A. 子接口（推荐，自动部署主路径）
│   └─ B. 主接口
│   ├─ bonding：非SR-IOV（VNIC）/ SR-IOV bonding（ETHTRUNK，ADD AUTOSCALINGETHTRUNK）
│
└─ DP-CS4-07 隧道叠加（按业务需求）
    ├─ 无 → 基础 6 种方案
    ├─ IPsec → 跨安全域加密
    ├─ GRE → WAP访问PDN/DN
    └─ MPLS VPN → UDG作PE对接企业网（OptionB跨域）
```

**决策矩阵速查**（硬件 × 组网 × 部署，Batch-06 DP-1）：

| 硬件 \ 组网 | 非SDN自动部署 | 非SDN手动部署 | SDN |
|------------|--------------|--------------|-----|
| **无NP卡** | ✅ Batch-04 | ✅ Batch-05 | ✅ Batch-06 |
| **NP卡直连PE** | ❌ 不支持自动 | ✅ Batch-06(KP-03/04) | ❌ 不支持SDN |
| **网络加速卡直连DC-GW** | — | — | ❌ |
| **网络加速卡直连DC-GW（自动）** | ✅ Batch-05(KP-08~11) | — | ❌ |

**uses_feature**（引用 EV-FK）：
- `IPFD-014000 路由功能`（总称）
- `IPFD-014001 OSPF`（含 OSPFv3）
- `IPFD-014002 BGP`
- `IPFD-014003 静态路由`
- `IPFD-012003 BFD`（注：SDN 文档引用旧编号 IPFD-104403，规范为 IPFD-012003）
- `GWFD-020411 MPLS VPN`
- `IPFD-015004 IPsec`
- `GWFD-111201 网络加速卡流量加速单元`（NP100/NP121 推测关联）
- `IPFD-010001 接口管理`（MTU 修改、外联口基础）

**uses_task**（→ 第3层 Task，按部署方式分轨）：

*自动部署轨*（推荐，无NP卡 / SDN / 网络加速卡）：
- T-CS4-A1 配置 VPN 实例与地址族（ADD L3VPNINST + ADD VPNINSTAF）
- T-CS4-A2 全局使能（SET BFD [+SET BGP / +SET MPLSSITE]）
- T-CS4-A3 关闭自动配置开关（SET AUTOCONFIG:SWITCHFLAG=FALSE + DSP OPSASSISTSTATE）
- T-CS4-A4 配置路由协议层（OSPF/OSPFv3/静态/BGP/MPLS VPN 协议命令）
- T-CS4-A5 配置 AUTOSCALING 模板族（ETHTRUNK/SERVICE/BFD/SRROUTE/MPLS）
- T-CS4-A6 打开自动配置开关（SET AUTOCONFIG:SWITCHFLAG=TRUE + DSP OPSASSISTSTATE）
- T-CS4-A7 配置 Loopback 接口（BGP/MPLS 场景，ADD INTERFACE+IPBINDVPN+IFIPV4ADDRESS）

*手动部署轨*（NP卡直连PE / 自动失败补救）：
- T-CS4-M1 配置 VPN 实例与地址族
- T-CS4-M2 全局使能
- T-CS4-M3 手动配置外联口基础设施（MOD INTERFACE→ADD INTERFACE→ADD IPBINDVPN→ADD ETHSUBIF→ADD IFIPV4/V6ADDRESS）
- T-CS4-M4 手动配置 BFD 会话（ADD BFDSESSION，含 LOCALDISCR/REMOTEDISCR）
- T-CS4-M5 配置路由协议层（OSPF/静态/BGP/MPLS VPN）
- T-CS4-M6（MPLS场景）手动 ADD MPLSIF 逐个接口
- T-CS4-M7（NP100多框级联）配置级联口（ADD NPDIRECTCONNECTPORT）

**业务规则 BR**：
- BR-BGP-DEPENDENCY（§5.8，BGP 依赖 IGP + IMPORTROUTE）
- BR-MPLS-VPN-PUBLIC（§5.9，MPLS VPN `_public_` + VRFRD + perInstance/perNexthop）
- BR-AUTOCONFIG-SWITCH（§5.10，开关操作规范）
- BR-MTU-HIERARCHY（§5.5，MTU 层级约束）

**语义对象 SO**：
- `SO_VPNInstance`（L3VPN 实例，含地址族）
- `SO_OSPFProcess / SO_OSPFArea`（OSPF 进程/区域）
- `SO_StaticRoute / SO_BFDRSession`（静态路由 + BFD 会话）
- `SO_BGPInstance / SO_BGPAddressFamily / SO_BGPPeer`（BGP 三件套）
- `SO_MPLSGlobal / SO_MPLSInterface`（MPLS 全局/接口）
- `SO_LoopbackInterface`（Loopback，BGP/MPLS 必备）
- `SO_ExternalInterface`（外联口，子接口/主接口/Eth-trunk）
- `SO_AutoScalingTemplate`（8 个自动部署模板对象）
- `SO_GRETunnel / SO_IPsecSA`（隧道叠加对象）
- `SO_NPCascadePort`（NP卡级联口，NP100 多框级联）
- `SO_NetworkMode`（组网模式，承载 DP-CS4 决策树结果）

---

### 6.5 CS-5 基础就绪方案闭包（License + 基础数据 + 架构认知）

**方案要素**（CS-5 = 开局第1步，全局前置，Batch-01/02）：

| 子要素 | 内容 | 来源 |
|--------|------|------|
| **架构认知** | 双模部署（5G SA / 2/3/4/5G 互操作融合）、UPF 角色分类（PSA/ULCL/BP/I-UPF）、3GPP→UDG 抽象接口映射（Saif/Scif/Paif/N4if）、VNF↔外部互通（vNIC→CSLB→EOR） | B1-KP-01~08 |
| **License 加载** | 双路径：OM Portal（仅网元）/ U2020/MAE（网元 + Service Fabric）；OM Portal 6步 + U2020/MAE 4步；颜色告警（红/黄/白）；ESN 一致性；紧急License 3次/7天 | B1-KP-09~11 |
| **NTP 时间同步** | 双路（OMC + FusionStage），依赖 NPFD-010014 | B2-KP-01 |
| **网元基本信息** | MOD ME 改名 + SET OMIP 改浮动IP/物理IP | B2-KP-02 |
| **高危命令二次授权** | SET SECAUTH + ADD USRSECAUTH + ADD SECAUTHMEM；13 类 UDG 默认清单 | B2-KP-03 |
| **公共参数（11项）** | SIGDSCP / UDPCHECKSUM / SRVCOMMONPARA / QOSCAR / IPV6FRAGPLCY / CPTEIDUALLOC / TZ / ANTIFRAUD / FWDPARA(高危) / HEADENGLBPARA / MSFAULTALARM | B2-KP-04 |
| **MTU 调整** | Fabric/Tunnel/外联口 三层 + AUTOSCALINGSERVICE 模板同步 | B2-KP-05 |

**License 加载决策矩阵**（→ DP-CS5-06）：
| 维度 | OM Portal | U2020/MAE |
|------|-----------|-----------|
| 网元 License | ✅ | ✅ |
| Service Fabric License | ❌ | ✅ |
| 生效方式 | 需激活（上传后"未激活"） | 网元需激活；Service Fabric **上传即生效** |
| 文件格式 | dat(2.0)/xml(3.0) | xml 或 dat |

**架构认知决策矩阵**（→ DP-CS5-01~04）：
| 决策 | 选项 | 影响 |
|------|------|------|
| DP-CS5-01 架构模式 | A. 5G SA 独立 / B. 2/3/4/5G 互操作融合 | 决定 UDG 是否承担 PGW-U/SGW-U，影响全部接口集 |
| DP-CS5-02 UDG 部署形态 | A. UPF独立 / B. UPF+PGW-U / C. UPF+SGW-U+PGW-U | 决定可配置接口范围 |
| DP-CS5-03 UPF 角色 | PSA / ULCL / BP / I-UPF / 多角色共建 | 决定 N3/N9a/N9c/N6 组合 |
| DP-CS5-04 接口抽象策略 | A. 独立接口 / B. 抽象接口合一 | 4G/5G 隔离→独立；融合→抽象；Paif/N4if 强制抽象 |

**uses_feature**：
- `NPFD-010014 支持NTP功能`（属 NPFD-010000 操作维护功能父特性）
- `IPFD-010001 接口管理`（MTU 修改、外联口基础）

**uses_task**：
- T-CS5-01 加载 License（DP-CS5-06 决策路径）
- T-CS5-02 配置 NTP 双路时间同步
- T-CS5-03 修改网元基本信息（MOD ME / SET OMIP，注意触发 CS-3 回流）
- T-CS5-04 配置高危命令二次授权（SET SECAUTH + ADD USRSECAUTH）
- T-CS5-05 配置公共参数 11 项
- T-CS5-06 调整 MTU 三层 + 自动部署模板同步
- T-CS5-07 架构认知确认（决策 DP-CS5-01~04，决定下游接口集）

**决策点 DP**：
| DP ID | 决策点 | 选项 |
|-------|--------|------|
| DP-CS5-01 | 架构模式 | 5G SA 独立 / 2/3/4/5G 互操作融合 |
| DP-CS5-02 | UDG 部署形态 | UPF独立 / UPF+PGW-U / UPF+SGW-U+PGW-U |
| DP-CS5-03 | UPF 角色 | PSA / ULCL / BP / I-UPF / 多角色共建 |
| DP-CS5-04 | 接口抽象策略 | 独立接口 / 抽象接口合一（Paif/N4if 强制抽象） |
| DP-CS5-05 | 路由方案 | IPv4/IPv6 × OSPF/静态/BGP + BFD（6 组合）→ 影响 CS-4 |
| DP-CS5-06 | License 加载路径 | OM Portal（仅网元）/ U2020/MAE（+Service Fabric） |
| DP-CS5-07 | License 文件格式 | dat(2.0) / xml(3.0) |

**业务规则 BR**：
- BR-N4-MANDATORY（§5.1，N4 必备）
- BR-MTU-HIERARCHY（§5.5）
- BR-FLOAT-IP-RECONNECT（§5.6）

**语义对象 SO**：
- `SO_DeploymentForm`（部署形态：UPF独立/UPF+PGW-U/融合）
- `SO_UPFRole`（UPF 角色：PSA/ULCL/BP/I-UPF）
- `SO_AbstractInterface`（抽象接口映射表，5 组）
- `SO_License`（License 文件 + ESN + 控制项 + 状态机）
- `SO_NTPSource`（双路时间源）
- `SO_NetworkElement`（网元身份：MEID/MENAME/OMIP）
- `SO_SecurityAuth`（二次授权用户 + 命令清单）
- `SO_GlobalParameter`（11 项公共参数集）
- `SO_MTUConfig`（Fabric/Tunnel/外联口 三层 MTU）

---

## 7. 关键发现（隐藏关系 / 约束 / 跨域协同）

### 7.1 接口抽象的"强制 vs 可选"二元性
- **强制合一**（Paif/N4if）：因 4G/5G 互操作时协议相同/锚点不变
- **可选合一**（Saif/Scif）：与独立配置互斥，推荐合一简化
- 这是隐藏的硬约束——选错会导致接口配置失败

### 7.2 N4 必备性 ≠ N4 单独可用
N4 是唯一必配接口，但**单独配 N4 无法建立偶联**，必须至少存在一个数据面逻辑接口 IP。这是常见的开局失败原因（Batch-03 §3.3）。

### 7.3 CS-5→CS-3 回流闭环（Batch-02 发现1）
修改浮动 IP（CS-5）会强制回流到 CS-3 重做网管对接（5步），且 SET OMIP 本身是二次授权命令。三者形成串行链：
```
二次授权配置（CS-5 KP-03）→ 修改网元信息（CS-5 KP-02）→ 重对接网管（CS-3）
```

### 7.4 BGP 是"寄生"协议
- 无自动部署（依赖 IGP 自动部署基础）
- 不能发现路由（必须 IMPORTROUTE 引入 wlr）
- 需专用 Loopback（与 IGP 外联口同 VPN）
- 双活网关/M-LAG 场景强制 BGP over 静态+BFD 单臂 echo

### 7.5 MPLS VPN 的"公私分离"特殊架构
- 外联口绑 `_public_`（非业务 VPN）
- Loopback 不绑 VPN
- MP-EBGP 用 IPv4 eBGP 传 IPv6 私网路由（不配 IPv6 外联口）
- VRFRD 必配，perInstance + perNexthop 节省标签

### 7.6 SDN 的"四强制"约束
- 强制 DHCP（外联口 IP + 下一跳）
- 强制单臂 BFD Echo（DEST=Leaf IP）
- 强制 BGP over 静态路由（不支持 OSPF）
- 强制 IPv6 DHCPv6 DUID（`SET DHCP6CLIENTDUID`）

### 7.7 自动部署的"模板不可变"约束
部署完成后**无法自动修改/删除**已部署配置，需手动：关开关→删子接口→改模板→重开开关。这是自动化开局的隐患点。

### 7.8 5 段式开局链路骨架（Batch-07 §3.1）
7 个典型实例都遵循同一开局链路：
```
[段1 全局预处理] → [段2 多对接面路由配置] → [段3 自动部署开关(自动类)] → [段4 业务逻辑接口] → [段5 会话接入]
```
差异仅在每段内的具体命令。

### 7.9 FirstCall 验证的"丢包率三分支"诊断模型
- 0% → 路由 OK
- 100% → 路由异常（按协议类型分支：静态→DSP SRROUTE / OSPF→DSP OSPFROUTING / BGP→LST BGPPEER）
- 非0非100% → 网络拥塞（联系华为）

### 7.10 BFD 特性 ID 勘误（Batch-06 F-5）
SDN 4 份文档引用 `IPFD-104403 BFD特性概述`（旧/别名），规范 ID 为 `IPFD-012003`。第4层 MMLCommand 关联特性时需以 IPFD-012003 为准。

---

## 8. 附录

### 附录 A 场景归并表（典型实例 → 组网模式组合，→ 第1层 CS 实例化）

| 实例 | UDG角色 | 路由协议 | IP版本 | 部署 | SDN | 典型适用场景 | 对应CS-4 DP |
|------|---------|---------|--------|------|-----|------------|-----------|
| 1 | 融合 | OSPF | IPv4 | 自动 | 非SDN | 2/3/4/5G 融合网络主流部署 | DP-CS4-01.A × 02.A1 × 03.A × 04.OSPFv4 |
| 2 | 锚点 | OSPFv3 | IPv6 | 自动 | 非SDN | IPv6 网络独立锚点网关 | DP-CS4-01.A × 02.A1 × 03.A × 04.OSPFv3v6 |
| 3 | 边缘 | 静态路由 | IPv4 | 手动 | 非SDN | 本地分流/边缘桥接 | DP-CS4-01.A × 02.A1 × 03.B × 04.静态v4 |
| 4 | 边缘 | BGP over OSPFv3 | IPv6 | 手动 | 非SDN | 边缘网元需 BGP 路由发布 | DP-CS4-01.A × 02.A1 × 03.B × 04.BGPoverv6 |
| 5 | PGW-U/UPF | BGP over 静态 | IPv4 | 自动 | **SDN** | SDN 数据中心 IPv4 接入 | DP-CS4-01.A × 02.B × 03.A × 04.BGPoverv4 |
| 6 | PGW-U/UPF | BGP over 静态 | IPv6 | 自动 | **SDN** | SDN 数据中心 IPv6 接入 | DP-CS4-01.A × 02.B × 03.A × 04.BGPoverv6 |
| 7 | PGW-U/UPF | BGP over 静态 | IPv4v6 | 自动 | **SDN** | SDN 数据中心双栈（最完整） | DP-CS4-01.A × 02.B × 03.A × 04.BGPover双栈 |

**未覆盖的组合（潜在扩展场景）**：
- NP 卡直连 PE × 任意路由（Batch-06 KP-03/04，无独立实例）
- 网络加速卡直连 DC-GW × BGP over 静态（Batch-05 KP-08~11，无独立实例）
- MPLS VPN × OptionB 跨域（Batch-04 KP-10 / Batch-05 KP-11 / Batch-06 KP-09，无独立实例）

### 附录 B MML 命令全集交叉参考（→ 第4层 MMLCommand + invokes 边）

#### B.1 基础数据类（CS-5）
| 命令 | 用途 | 对接面 |
|------|------|--------|
| MOD ME | 修改网元名称 | CS-5 |
| SET OMIP | 修改浮动IP/物理IP（**高危，二次授权**） | CS-5 |
| LST OMIP / LST ME | 查询 OMIP / 网元 | CS-5 |
| SET SECAUTH / ADD USRSECAUTH / ADD SECAUTHMEM | 二次授权配置 | CS-5 |
| SET SIGDSCP / SET UDPCHECKSUM / SET SRVCOMMONPARA / SET QOSCAR / SET IPV6FRAGPLCY / SET CPTEIDUALLOC / SET TZ / SET ANTIFRAUD / SET FWDPARA(高危) / SET HEADENGLBPARA / SET MSFAULTALARM | 公共参数 11 项 | CS-5 |
| SET FABRICMTU / MOD INTERFACE / SET IFIPV6ENABLE | MTU 三层修改 | CS-5 |
| DSP RVKLICINFO | License 失效码查询 | CS-5 |
| SET NEWCERTSWITCH | 证书开关（LiteCA 前置） | CS-3/CS-5 |

#### B.2 接口配置类（CS-1/CS-2）
| 命令 | 用途 | 对接面 |
|------|------|--------|
| ADD VPNINST | 增加 VPN 实例 | CS-1/CS-2 |
| ADD LOGICINF | 增加逻辑接口（掩码固定 255.255.255.255） | CS-1/CS-2 |
| ADD SNSSAIUPINTF | 网络切片与逻辑接口绑定（仅 Saif/N3if） | CS-2 |
| SET UPINFO | 设置 UPF 标识（HostName） | CS-1 |
| ADD LOGICIP / ADD HTTPLEGRP / ADD HTTPLE / ADD SBIAPLE / SET HTTPCONF | Nupf 服务化接口配置 | CS-2 |

#### B.3 会话接入类（CS-2）
| 命令 | 用途 |
|------|------|
| ADD APN / SET APNSGLPASS | APN/DNN 实例 + 单通检测 |
| ADD POOL / ADD SECTION / ADD POOLGROUP / ADD POOLBINDGROUP / ADD POOLGRPMAP | 地址池五件套 |
| SET IPALLOCRULE | 三级地址分配规则 |

#### B.4 路由协议类（CS-4）
| 命令 | 用途 |
|------|------|
| ADD L3VPNINST / ADD VPNINSTAF / MOD VPNINSTAF / ADD VPNTARGET | L3VPN 实例 + 地址族 + RT |
| ADD IPBINDVPN | 接口绑定 VPN |
| SET BFD | 全局激活 BFD |
| ADD OSPF / ADD OSPFAREA / ADD OSPFNETWORK / ADD OSPFINTERFACE / ADD OSPFIMPORTROUTE | OSPF IPv4 |
| ADD OSPFV3 / ADD OSPFV3AREA / ADD OSPFV3INTERFACE / ADD OSPFV3IMPORTROUTE | OSPF IPv6 |
| ADD BFDSESSION | 手动 BFD 会话（含 LOCALDISCR/REMOTEDISCR/ONEARMECHO） |
| ADD SRROUTE / ADD SRROUTE6 | 手动静态路由 |
| SET BGP / ADD BGPVRF / ADD BGPVRFAF / ADD BGPPEER / ADD BGPPEERAF / ADD IMPORTROUTE / RMV BGPPEERAF | BGP 全套 |
| SET MPLSSITE / ADD MPLSIF | MPLS 全局 + 接口 |
| ADD GRETUNNEL / MOD GRETUNNEL | GRE 隧道 |
| ADD NETWORKROUTE | Loopback 路由引入 BGP |
| ADD NPDIRECTCONNECTPORT / LST NPDIRECTCONNECTPORT / RMV NPDIRECTCONNECTPORT | NP 卡级联口（NP100 多框级联） |
| SET DHCP6CLIENTDUID | SDN IPv6 DHCPv6 前置 |

#### B.5 自动部署模板类（CS-4）
| 命令 | 用途 |
|------|------|
| SET AUTOCONFIG / LST AUTOCONFIG / DSP OPSASSISTSTATE | 自动配置开关 + 助手状态 |
| ADD / RMV / LST / MOD AUTOSCALINGSERVICE | 外联口主模板 |
| ADD / RMV / LST AUTOSCALINGETHTRUNK | SR-IOV bonding Eth-trunk 模板 |
| ADD / RMV / LST AUTOSCALINGBFD | BFD 会话模板（单臂 echo） |
| ADD / RMV / LST AUTOSCALINGSRBFD | 静态路由动态 BFD 模板（双向） |
| ADD / RMV / LST AUTOSCALINGSRROUTE | 静态路由模板 |
| ADD / RMV / LST AUTOSCALINGBGPLF | BGP 入不转板策略模板 |
| ADD / RMV / LST AUTOSCALINGIPREACH | RU 可达性检测模板 |
| ADD / RMV / LST AUTOSCALINGMPLS | MPLS 接口自动化模板 |

#### B.6 验证/查询类
| 命令 | 用途 |
|------|------|
| LST LOGICINF / LST VPNINST / LST APN / LST POOL / LST SECTION / LST POOLGROUP / LST POOLBINDGROUP / LST POOLGRPMAP | 各对象查询 |
| LST INTERFACE / LST IFIPV4ADDRESS / LST IFIPV6ADDRESS / LST IPBINDVPN | 接口查询 |
| LST OSPF / LST OSPFAREA / LST OSPFINTERFACE / LST OSPFNETWORK / LST OSPFIMPORTROUTE | OSPF 查询 |
| LST BGPPEER / DSP BGPPEERINFO / LST BGPVRFAF | BGP 查询 |
| LST FABRICMTU / LST AUTOSCALINGSERVICE / LST AUTOCONFIG | MTU / 自动部署查询 |
| SRVPING / SRVTRACERT | 业务 Ping/Tracert（SRCIPTYPE=LOGICINF/POOL） |
| NGPING | 服务化/网络 Ping（Nupf / 多 ISU 逐个） |
| PING | 物理 Ping |
| DSP ROUTE / DSP ROUTE6 / DSP SRROUTE / DSP OSPFROUTING / DSP OSPFINTERFACE / DSP OSPFPEER / DSP BFDSESSION | 路由/协议状态查询 |
| DSP IFSTATUS | 接口状态（UP/Down） |
| DSP SESSIONINFO | ★FirstCall 成功标志：APN/RoleType/IPv4 PDP/Session时间戳 |
| DSP SERVICERUSTATE | 所有 RU 状态（调测阶段0） |
| DSP OPSASSISTSTATE | 自动部署助手状态（必须 Ready） |
| EXP MML | 导出 MML 配置（兜底故障收集） |

### 附录 C 配置对象复用矩阵（→ 第4层 ConfigObject）

| ConfigObject | CS-1 | CS-2 | CS-3 | CS-4 | CS-5 |
|--------------|------|------|------|------|------|
| VPNInstance | ✅ VPN_Signaling | ✅ VPN_Access/Sc/Pa/Internet | — | ✅ 全部 | — |
| LogicInterface | ✅ N4if | ✅ Saif/Scif/Paif/S11-uif | — | — | — |
| ExternalInterface | — | ✅ SGi/N6 | — | ✅ 外联口/子接口/Eth-trunk | — |
| APN | — | ✅ | — | — | — |
| AddressPool/Section/PoolGroup | — | ✅ | — | — | — |
| LoopbackInterface | — | — | — | ✅ BGP/MPLS 必备 | — |
| OSPFProcess/Area | — | — | — | ✅ | — |
| StaticRoute/BFDSession | — | — | — | ✅ | — |
| BGPInstance/Peer | — | — | — | ✅ | — |
| MPLSGlobal/Interface | — | — | — | ✅ | — |
| AutoScalingTemplate (8种) | — | — | — | ✅ | — |
| GRETunnel/IPsecSA | — | — | — | ✅ | — |
| MTUConfig | — | — | — | ✅ (外联口) | ✅ (Fabric/Tunnel) |
| License | — | — | — | — | ✅ |
| NetworkElement/OMIP | — | — | ✅ (14参数) | — | ✅ |
| SecurityAuth | — | — | — | — | ✅ |
| GlobalParameter (11项) | — | — | — | — | ✅ |
| NPCascadePort | — | — | — | ✅ (NP100) | — |

### 附录 D 端到端配置流程（→ 第3层 TaskCommandOrderEdge）

按 §9 端到端开局链路，每个 CS 的 Task 编排顺序（→ 03-task-layer.md 的 TaskCommandOrderEdge）：

```
[CS-5] T-CS5-01 License → T-CS5-02 NTP → T-CS5-03 网元信息 → T-CS5-04 二次授权
       → T-CS5-05 公共参数 → T-CS5-06 MTU → T-CS5-07 架构认知
   ↓
[CS-3] T-CS3-01 北向密码 → T-CS3-02 SNMP密钥 → T-CS3-03 适配层
       → T-CS3-04 创建网元 → T-CS3-05 EMS检查 → T-CS3-06 LST ME验证
   ↓
[CS-1] T-CS1-01 VPN_Signaling → T-CS1-02 N4if接口 → T-CS1-03 UPINFO → T-CS1-04 SRVPING验证
   ↓
[CS-2] T-CS2-01 业务面VPN → T-CS2-02 接入侧接口 → T-CS2-03 中间侧接口 → T-CS2-04 锚点侧接口
       → T-CS2-05 APN → T-CS2-06 地址池 → T-CS2-07 IPALLOCRULE
   ↓
[CS-4] (按 DP-CS4 决策树分支)
       自动轨: T-CS4-A1 VPN → A2 全局使能 → A3 关开关 → A4 协议层 → A5 AUTOSCALING模板 → A6 开开关 → A7 Loopback
       手动轨: T-CS4-M1 VPN → M2 全局使能 → M3 外联口基础设施 → M4 BFD会话 → M5 协议层 → M6 MPLSIF → M7 级联口
   ↓
[调测] DSP SERVICERUSTATE → NGPING(每ISU) → 路由验证 → 直连路由器PING → FirstCall拨测 → DSP SESSIONINFO
```

---

## 9. 端到端开局链路（→ 第3层 Task 编排 + Stage4 端到端链路验证）

### 9.1 完整开局流程（按对接面 CS × 流程顺序）

```
CS-5 基础就绪（开局第1步，全局前置）
  ├─ License 加载（DP-CS5-06 决策路径）
  ├─ NTP 双路时间同步（OMC + FusionStage）
  ├─ 网元基本信息（MOD ME + SET OMIP，注意触发 CS-3 回流）
  ├─ 高危命令二次授权（SET SECAUTH + 13类清单）
  ├─ 公共参数 11 项（SIGDSCP/UDPCHECKSUM/...）
  ├─ MTU 三层调整 + 自动部署模板同步
  └─ 架构认知确认（DP-CS5-01~04，决定下游接口集）
       ↓
CS-3 网管对接（开局对接调测起点）
  └─ 5步闭包：北向密码 → SNMP密钥 → 适配层 → 创建网元14参数 → EMS检查
       ↓
CS-1 控制面 N4（UPF 唯一必备接口）
  └─ 配置 N4if（强制合一）+ SET UPINFO + SRVPING 验证偶联
       ↓
CS-2 用户面（接口 + 会话接入双层）
  ├─ 接口层：Saif/Scif/Paif + (S11-uif/Nupf 按需)
  └─ 会话接入层：APN → 地址池三件套 → IPALLOCRULE
       ↓
CS-4 路由对接（★最大，按组网模式决策树分支）
  ├─ 自动部署（非SDN无NP卡 / SDN / 网络加速卡）：AUTOSCALING 模板族
  └─ 手动部署（NP卡直连PE / 失败补救）：逐条 MML
       ↓
调测 FirstCall（端到端验证）
  └─ 4阶段29步：RU状态 → UDG→对端路由 → 直连路由器→UDG → FirstCall拨测
```

### 9.2 Stage4 端到端链路验证清单（来自 Batch-07 KP-08）

按以下顺序执行验证，任一阶段失败即按 KP-08 流程分支定位：

1. **RU 就绪**：`DSP SERVICERUSTATE` 全部正常
2. **UDG→对端路由可达**：`NGPING`（每 ISU 逐个）丢包率 0%
3. **路由负荷分担**：`DSP SRROUTE`/`DSP OSPFROUTING`/`LST BGPPEER`+`DSP BGPPEERINFO`(=Established) 验证多路径等开销
4. **直连路由器→UDG 回程**：路由器 PING UDG 逻辑接口 IP 可达 + 路由表多条
5. **UDG 逻辑接口→对端业务 IP**：`NGPING`（源=逻辑接口 IP）丢包率 0%
6. **路由引入正确**：`LST OSPFIMPORTROUTE` 协议分类=wlr
7. **FirstCall 拨测**：测试终端 apn-test 接入 → `DSP SESSIONINFO` APN/RoleType/IPv4 PDP/Session时间戳 4参数正确
8. **数据业务验证**：用户访问 Internet 数据业务正常

### 9.3 FirstCall 验证的关键诊断分支（丢包率三分支）

```
NGPING 丢包率
├─ 0%   → 路由 OK → 进入 FirstCall 拨测
├─ 100% → 路由异常
│        ├─ 静态路由 → DSP SRROUTE（多条等开销 + 不同 ISU = 负荷分担正常）
│        ├─ OSPF     → DSP OSPFROUTING + LST OSPF(VPNINSCAPSIMFLG=TRUE/VIRTUALSYSFLAG=TRUE)
│        │            + LST OSPFAREA(NSSA) + Loopback 配置检查
│        └─ BGP      → LST BGPPEER + DSP BGPPEERINFO(=Established) + PING Loopback↔Peer
└─ 非0非100% → 网络拥塞 → 联系华为技术支持
```

**FirstCall 拨测失败定位**：
- N4 偶联建立失败 → `LST LOGICINF` 检查 Pa 接口 → 缺则补 Pa 逻辑接口
- PGW-U/UPF 无资源 → 检查 UDG 地址池配置（POOL/SECTION）
- 基站同时支持 4G/5G → 需 4G+5G 终端同时拨测

---

## 文档结束

**本文件是 Stage4 第1层业务图谱（01-business-graph.md）的主体层数据源**，核心产出：
- 5 个 CS 方案闭包（§6.1~6.5），每个明确方案要素/uses_feature/uses_task/DP/BR/SO
- CS-4 组网模式决策树（§6.4），5 维矩阵（硬件×SDN×部署×路由×IP版本）
- 10 条 BusinessRule（§5.1~5.10）
- 附录 B/C/D 是第3/4层数据源（MML 命令全集、ConfigObject 复用矩阵、端到端流程）
- §9 端到端开局链路供 03-task-layer.md 的 Task 编排
