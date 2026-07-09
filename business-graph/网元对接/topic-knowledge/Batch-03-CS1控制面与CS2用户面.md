# Batch-03: CS-1控制面(N4↔SMF) + CS-2用户面(接口+会话接入)
> 批次03 | 对接面 CS-1控制面 + CS-2用户面 | 文件数9 | 核心度★★★★★
> 子场景：UPF网元对接（UDG扮演 UPF / PGW-U / SGW-U 融合角色）
> 文档前缀：`output/UDG_Product_Documentation_CH_20.15.2/网络部署/初始配置/UDG初始配置与调测/组网对接配置/`

## 1. 概述

本批次覆盖 UPF 网元对接的**核心对接面**：
- **CS-1 控制面**：UDG（UPF）与 SMF/SGW-C/PGW-C 之间通过 **N4（N4/Sxa/Sxb）接口**建立信令连接，这是 UPF 的**唯一必备接口**，承载 PFCP 会话管理信令。
- **CS-2 用户面**：UDG 与外部网元之间的各类数据面接口（Sa/N3/S1-U ↔ RAN；Sc/N9c/S5-S ↔ I-UPF；Pa/N9a/S5-P ↔ ULCL/ePDG/SGSN；S11-U ↔ MME；SGi/N6 外联口；Nupf ↔ NWDAF），以及**会话接入数据**（APN/DNN + 地址池 + 地址分配规则），使用户完成激活流程接入 PDN/DN 网络。

CS-1 与 CS-2 通过 **PFCP 会话**联动：N4 接口建立后，SMF 通过 N4 下发 PDR/FAR/QER 等规则，驱动用户面接口的数据转发。CS-2 的会话接入数据（APN、地址池）则定义了"用户接入哪个网络、用什么IP"，是 N4 会话的**业务侧输入**。

| 对接面 | 核心对象 | 关键MML命令 | 来源文档 |
|--------|----------|-------------|----------|
| CS-1 控制面 | N4if（N4/Sxa/Sxb 合一抽象接口）、UPF标识(UPINFO) | ADD VPNINST / ADD LOGICINF / SET UPINFO | 配置N4接口数据_68634162.md |
| CS-2 用户面-接入侧 | Saif/N3if/S1-uif（接 RAN） | ADD LOGICINF + SLICEATTRSW/ADD SNSSAIUPINTF | 配置Sa_N3_S1-U接口数据_68634192.md |
| CS-2 用户面-中间侧 | Scif/N9cif/S5-Sif（接 PSA UPF/PGW-U） | ADD VPNINST / ADD LOGICINF | 配置Sc_N9c_S5-S_S8-S接口数据_68634165.md |
| CS-2 用户面-锚点侧 | Paif（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U 合一）（接 ULCL/ePDG/SGSN） | ADD VPNINST / ADD LOGICINF | 配置Pa接口数据_68634202.md |
| CS-2 用户面-NB-IoT | S11-uif（接 MME） | ADD VPNINST / ADD LOGICINF | 配置S11-U接口数据_83013474.md |
| CS-2 用户面-DN外联 | SGi/N6（物理外联口，无需逻辑接口） | 无（外联口在路由配置） | 配置SGi_N6接口数据_36261585.md |
| CS-2 用户面-服务化 | Nupf（接 NWDAF，HTTP/SBI） | ADD LOGICIP / ADD HTTPLEGRP / ADD HTTPLE / ADD SBIAPLE / SET HTTPCONF | 配置Nupf接口数据_64469713.md |
| CS-2 会话接入 | APN/DNN、地址池POOL、地址段SECTION、地址池组POOLGROUP、地址池绑定POOLBINDGROUP、地址池组映射POOLGRPMAP、分配规则IPALLOCRULE | ADD APN / ADD POOL / ADD SECTION / ADD POOLGROUP / ADD POOLBINDGROUP / ADD POOLGRPMAP / SET IPALLOCRULE / SET APNSGLPASS | 配置会话接入数据_68634166.md |

文档关系：`配置业务接口数据_68634146.md`（总览）按 UDG 部署位置（边缘/锚点/融合）索引到 7 类接口子文档；会话接入 `配置会话接入数据_68634166.md` 独立成篇，与接口配置共同构成"用户接入"完整闭环。

---

## 2. 核心知识点

### KP-01: UDG 部署位置 → 业务接口组合矩阵
- **内容**：UDG 根据部署位置（边缘/锚点/融合）承担不同 UPF 角色，决定对外接口集。组网场景简化矩阵如下（来自总览表1）：

| 部署位置 | 5G形态 | 4G形态 | 必配接口 | 协议接口说明 |
|----------|--------|--------|----------|--------------|
| **边缘位置** | ULCL UPF / BP UPF / I-UPF | SGW-U | Sa/N3/S1-U + Sc/N9c/S5-S/S8-S + N4(N4/Sxa/Sxb) | 接 RAN + 接 PSA + 控制面 |
| **锚点位置** | PSA UPF | PGW-U | Pa(N9a/S5-P/S8-P/Gn-U/Gp-U) + N4(N4/Sxa/Sxb) | 接 I-UPF/ePDG/SGSN + 控制面 |
| **融合位置** | ULCL/BP/I-UPF + PSA UPF | SGW-U + PGW-U | Sa + Sc + Pa(N9a/S5-P/S8-P) + N4 | 全套用户面接口 + 控制面 |

  **关键约束（IP网段隔离）**：逻辑接口（N3/N4/N9/S1-U/Sa/Sc/Pa 等）的 IP **不能**和外联口 IP 在同一网段，也**不能**和对端的物理接口 IP 在同一网段。
- **来源**：配置业务接口数据_68634146.md（表1 + 说明）
- **核心度**：★★★★★（CS-1/CS-2 的部署决策依据）
- **关联特性**：GWFD-010234 Single IP（N4/Pa 强制合一抽象接口）
- **关联命令**：无（决策层）
- **关联配置对象**：UDG 部署位置（决定后续 ADD LOGICINF 的接口组合）
- **对接面**：CS-5 全局（决定 CS-1/CS-2 接口集）

### KP-02: CS-1 控制面 — N4（N4/Sxa/Sxb）接口配置
- **内容**：N4 接口是 UPF 与 SMF/SGW-C/PGW-C 之间的**信令路径**，承载 PFCP 协议（遵循 3GPP TS 29.244）。N4 是 UPF 的**唯一必备接口**。

  **强制合一抽象接口**：考虑到 4G/5G 互操作时移动锚点不变，SMF+PGW-C 融合部署时 N4、Sxa、Sxb 接口使用**相同协议**，因此 UDG 上**只支持使用合一抽象接口 N4if**，不支持独立配置 Sxa、Sxb 接口。

  **必备前提条件**：
  - 已完成组网路由配置
  - 已阅读 GWFD-010234 Single IP 特性
  - SMF/PGW-C 要求 UPF 必须配 N9 才能作为主锚点激活时，还需配置 Paif（见 KP-06）
  - 配置 N4 后，UDG 上**至少需存在一个数据面逻辑接口IP**（Paif/Scif/Saif/N3if/S1-uif/S11-uif 之一），否则 SMF↔UPF N4 偶联异常

  **MML 配置命令（原样保留）**：
  ```
  # 步骤1：配置N4接口所属VPN实例（必须与对应外联口VPN一致）
  ADD VPNINST: VPNINSTANCE="VPN_Signaling";

  # 步骤2：配置N4（N4/Sxa/Sxb）合一抽象逻辑接口
  # 注意：N4接口名称唯一，固定为 N4if1/0/0
  ADD LOGICINF: NAME="N4if1/0/0", IPVERSION=IPV4, IPV4ADDRESS1="10.1.6.1", IPV4MASK1="255.255.255.255", VPNINSTANCE="VPN_Signaling";

  # 步骤3：配置UPF标识（HostName全网唯一，不配则偶联失败）
  SET UPINFO: HOSTNAME="UP_001";
  ```
  （双栈组网：IPVERSION=IPVER_ALL，分别配 IPv4 和 IPv6 地址）

  **验证方法**：
  ```
  # 查询逻辑接口
  LST LOGICINF;
  # 业务Ping调测UDG→SMF/SGW-C/PGW-C（IPv4）
  SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="N4if1/0/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.6.1", DSTIPV4ADDR="10.2.6.1";
  # 业务Tracert定位故障
  SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="N4if1/0/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.6.1", DSTIPV4ADDR="10.2.6.1";
  # 检查路由
  DSP ROUTE / DSP ROUTE6;
  ```

  **一个UPF对接多个SMF场景**：需额外配置 **GWFD-020161 CU Full Mesh** 特性并申请相关 License。

- **来源**：配置N4(N4_Sxa_Sxb)接口数据_68634162.md
- **核心度**：★★★★★（UPF 唯一必备接口）
- **关联特性**：GWFD-010234 Single IP、GWFD-020161 CU Full Mesh
- **关联命令**：ADD VPNINST、ADD LOGICINF、SET UPINFO、LST LOGICINF、SRVPING、SRVTRACERT、DSP ROUTE、DSP ROUTE6
- **关联配置对象**：VPN实例(VPN_Signaling)、N4if逻辑接口、UPF标识(HostName)
- **对接面**：CS-1 控制面

### KP-03: CS-2 用户面-接入侧 — Sa/N3/S1-U 接口配置（接 RAN）
- **内容**：Sa/N3/S1-U 接口是 UDG（边缘 UPF/SGW-U）与无线 (R)AN 侧 eNodeB/gNodeB 之间的**数据路径**。

  **配置灵活性**：N3、S1-U 接口**可独立配置，也可使用抽象接口 Sa 合一配置**（推荐合一）。两种方式**互斥**：已配独立接口再配抽象接口系统会失败，反之亦然。

  **网络切片绑定**：
  - Saif1/1/0 / N3if1/1/0 不能和网络切片绑定（独立切片场景）
  - 通过 `SLICEATTRSW=ENABLE` 标记接口绑定切片属性
  - 配置独立切片接口后还需通过 `ADD SNSSAIUPINTF` 命令将网络切片和接口绑定

  **接口编号规则**：最后一位数字取值 0~31。中心云上下行入不转板场景还需规划 1/Y/0 接口（Y=2~64，每个 ISU POD 一个逻辑接口 IP），与 1/1/0 绑定相同 VPN。

  **MML 配置命令（原样保留）**：
  ```
  # 步骤1：配置VPN实例
  ADD VPNINST: VPNINSTANCE="VPN_Access";   # 不绑切片
  ADD VPNINST: VPNINSTANCE="VPN_Access_001"; # 绑切片

  # 步骤2A：配置抽象接口 Sa（推荐）— 不绑切片
  ADD LOGICINF:NAME="Saif1/1/0",IPVERSION=IPV4,IPV4ADDRESS1="10.1.1.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="VPN_Access",SLICEATTRSW=DISABLE;
  # 配置抽象接口 Sa — 绑切片
  ADD LOGICINF:NAME="Saif1/1/1",IPVERSION=IPV4,IPV4ADDRESS1="10.1.1.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="VPN_Access_001",SLICEATTRSW=ENABLE;

  # 步骤2B：配置独立接口 N3（不推荐，与Sa互斥）
  ADD LOGICINF:NAME="N3if1/1/0",IPVERSION=IPV4,IPV4ADDRESS1="10.1.1.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="VPN_Access",SLICEATTRSW=DISABLE;

  # 步骤2C：配置独立接口 S1-U（4G）
  ADD LOGICINF:NAME="s1-uif1/1/0",IPVERSION=IPV4,IPV4ADDRESS1="10.1.2.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="VPN_Access";

  # 切片绑定（独立切片接口后追加）
  ADD SNSSAIUPINTF: ...;  # 将网络切片和 Saif/N3if 接口绑定
  ```

  **验证**：SRVPING（DST=eNodeB/gNodeB）、SRVTRACERT、DSP ROUTE。

- **来源**：配置Sa_N3_S1-U接口数据_68634192.md
- **核心度**：★★★★★（边缘 UPF 必备）
- **关联特性**：GWFD-010234 Single IP
- **关联命令**：ADD VPNINST、ADD LOGICINF（含 SLICEATTRSW）、ADD SNSSAIUPINTF、LST LOGICINF、SRVPING、SRVTRACERT、DSP ROUTE、DSP ROUTE6
- **关联配置对象**：Saif/N3if/S1-uif 逻辑接口、切片属性开关、网络切片绑定关系
- **对接面**：CS-2 用户面（边缘 UPF 接入侧）

### KP-04: CS-2 用户面-中间侧 — Sc/N9c/S5-S/S8-S 接口配置（接 PSA UPF/PGW-U）
- **内容**：Sc/N9c/S5-S/S8-S 接口是 UDG（边缘 ULCL/BP/I-UPF/SGW-U）与 PSA UPF/PGW-U 之间的**数据路径**。

  **配置灵活性**：N9c、S5/S8-S 接口**可独立配置，也可使用抽象接口 Sc 合一配置**（推荐合一）。两种方式互斥（同 Sa）。

  **MML 配置命令（原样保留）**：
  ```
  # 步骤1：配置VPN实例
  ADD VPNINST: VPNINSTANCE="VPN_Sc";

  # 步骤2：配置Sc/N9c/S5-S/S8-S逻辑接口
  ADD LOGICINF:NAME="Scif1/1/0",IPVERSION=IPV4,IPV4ADDRESS1="10.1.1.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="VPN_Sc";
  ```

  **中心云上下行入不转板场景**：除 1/1/0（或 1/1/X，X=1~31）外，还需规划 1/Y/0（Y=2~64，每 ISU POD 一个 IP），与 1/1/0 同 VPN。

  **验证**：SRVPING（DST=PSA UPF/PGW-U）。

- **来源**：配置Sc_N9c_S5-S_S8-S接口数据_68634165.md
- **核心度**：★★★★（边缘 UPF 接 PSA 锚点必备）
- **关联特性**：GWFD-010234 Single IP
- **关联命令**：ADD VPNINST、ADD LOGICINF、LST LOGICINF、SRVPING、SRVTRACERT、DSP ROUTE、DSP ROUTE6
- **关联配置对象**：Scif/N9cif/S5-Sif 逻辑接口
- **对接面**：CS-2 用户面（边缘 UPF 中间侧）

### KP-05: CS-2 用户面-锚点侧 — Pa(N9a/S5-P/S8-P/S2b/Gn-U/Gp-U) 接口配置（接 ULCL/ePDG/SGSN）
- **内容**：Pa 接口是 UDG（PSA UPF/PGW-U）与 ULCL UPF/BP UPF/I-UPF/SGW-U/ePDG/SGSN 之间的**数据路径**，承载多种协议（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U）。

  **强制合一抽象接口**：考虑到 4G/5G 互操作时数据锚点不变，PSA UPF+PGW-U 融合部署时 N9a、S5-P/S8-P 接口地址**必须相同**，因此 UDG 上**只支持使用合一抽象接口 Paif**，不支持独立配置 N9a、S5-P/S8-P、S2b、Gn-U、Gp-U 接口。

  **多接口规划**：需要用不同 IP 与 ULCL/BP/I-UPF/SGW-U/ePDG/SGSN 建立逻辑连接时，规划多个 Paif 接口，编号 Paif1/1/N（N=0~31）。

  **Direct Tunnel 特殊场景**：部署 Direct Tunnel 且用 BGP over 静态路由方案生成 PGW-U→RNC 路由时，若 PGW-U 到 RNC、到 Gn 网络**同 VPN**，但 DCGW 到 RNC、到 Gn 网络**不同 VPN**，则需在 PGW-U 上配置到 DCGW 和 RNC 互通 VPN 对应的 BGP IP 的路由，但**不配置该路由对应的默认路由**。

  **MML 配置命令（原样保留）**：
  ```
  # 步骤1：配置VPN实例
  ADD VPNINST: VPNINSTANCE="VPN_Pa";

  # 步骤2：配置Pa逻辑接口
  ADD LOGICINF:NAME="Paif1/1/0",IPVERSION=IPV4,IPV4ADDRESS1="10.1.3.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="VPN_Pa";
  ```

  **验证**：SRVPING（DST=ULCL/BP/I-UPF/SGW-U/ePDG）。

- **来源**：配置Pa(N9a_S5-P_S8-P_S2b_Gn-U_Gp-U)接口数据_68634202.md
- **核心度**：★★★★★（锚点 UPF 必备，承载多协议合一）
- **关联特性**：GWFD-010234 Single IP
- **关联命令**：ADD VPNINST、ADD LOGICINF、LST LOGICINF、SRVPING、SRVTRACERT、DSP ROUTE、DSP ROUTE6
- **关联配置对象**：Paif 逻辑接口（强制合一，Paif1/1/N）
- **对接面**：CS-2 用户面（锚点 UPF 对外数据面）

### KP-06: CS-2 用户面-NB-IoT — S11-U 接口配置（接 MME）
- **内容**：S11-U 接口是 UDG 扮演 SGW-U 时与 MME 之间的数据路径，**仅出现在 NB-IoT 解决方案**场景。

  **MML 配置命令（原样保留）**：
  ```
  # 步骤1：配置VPN实例
  ADD VPNINST: VPNINSTANCE="VPN_NBIoT";

  # 步骤2：配置S11-U逻辑接口
  ADD LOGICINF:NAME="S11-uif1/1/0",IPVERSION=IPV4,IPV4ADDRESS1="10.1.1.22",IPV4MASK1="255.255.255.255",VPNINSTANCE="VPN_NBIoT";
  ```

  **验证**：SRVPING（DST=MME）。

  **注**：S11-U 是独立接口（非抽象接口合一），接口编号最后一位 0~31。

- **来源**：配置S11-U接口数据_83013474.md
- **核心度**：★★★（仅 NB-IoT 场景）
- **关联特性**：无
- **关联命令**：ADD VPNINST、ADD LOGICINF、LST LOGICINF、SRVPING、SRVTRACERT、DSP ROUTE、DSP ROUTE6
- **关联配置对象**：S11-uif 逻辑接口
- **对接面**：CS-2 用户面（NB-IoT 专用）

### KP-07: CS-2 用户面-DN外联 — SGi/N6 接口（物理外联口，无逻辑接口）
- **内容**：与 PDN/DN/IMS 互通的 SGi/N6 接口**使用物理外联口实现，无需配置逻辑接口**。外联口配置参见"组网路由配置_75096802.md"。

  **DN-AAA 互通两种方案**（DN-AAA 部署在企业园区，SMF 需经 UPF 连接 DN-AAA 时）：

  | 方案 | 实现方式 | 关键约束 |
  |------|----------|----------|
  | **方案A：N6 接口直连** | UPF 通过 N6 接口与企业园区 DN-AAA 互通 | N6 对应外联口的 VPN 必须**与 SMF 通过 Network Instance 信元携带的 VPN 相同**；UPF 需将 SMF 下发的 UE IP 作为静态用户地址发布下行路由；SMF 上该地址不允许对外发布路由 |
  | **方案B：N4 专用会话隧道** | UPF 通过 N4 接口专用会话（RoleType=N4U_Tunnel）和 SMF 互通 | UPF 根据 SMF 指示创建 Radius 消息专用 N4 会话，基于该会话的 GTP-U 隧道转发 SMF↔DN-AAA 消息；**N4 专用会话不占用基本功能 License** |

- **来源**：配置SGi_N6接口数据_36261585.md
- **核心度**：★★★★（锚点 UPF 对 DN 必备，但配置归路由侧）
- **关联特性**：无（外联口在 CS-4 路由对接面）
- **关联命令**：无（外联口配置见组网路由配置）
- **关联配置对象**：物理外联口（Gi/SGi/N6）、N4 专用会话（RoleType=N4U_Tunnel，方案B）
- **对接面**：CS-2 用户面（与 CS-4 路由对接面边界）

### KP-08: CS-2 用户面-服务化 — Nupf 接口配置（接 NWDAF，HTTP/SBI）
- **内容**：Nupf 接口是 UPF 与 NWDAF 之间的**服务化接口**（HTTP/HTTPS），承载 SBI 通信。仅在 UPF 与 NWDAF 对接场景需要配置。

  **配置三件套**：逻辑IP（ADD LOGICIP）→ HTTP本端实体组（ADD HTTPLEGRP）→ HTTP本端实体（ADD HTTPLE，含 SERVER/CLIENT 角色）→ 服务化接口本端实体（ADD SBIAPLE）。

  **前置条件**：必须先完成 **SSU 服务** 和 **SBIM 服务** 安装（基于 VNF LCM 安装 UDG 非 SDN 模式下的可选服务）。

  **角色与NF类型**：UPF 既可作为 HTTP Server（端口 80，可选 TLS），也可作为 HTTP Client；本端 NF 类型固定为 **NFTypeUPF**。

  **MML 配置命令（原样保留）**：
  ```
  # 步骤1：增加Nupf接口IP地址（IPv4 + IPv6 各一组：server/client）
  ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.1.20.1", VPNINSTNAME="VRF_Nupf", DESC="UPF_server";
  ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.1.20.2", VPNINSTNAME="VRF_Nupf", DESC="UPF_client";
  ADD LOGICIP: IPVERSION=IPv6, LOGICIPV6="FC00::10:1:20:1", VPNINSTNAME="VRF_Nupf", DESC="UPF_server";
  ADD LOGICIP: IPVERSION=IPv6, LOGICIPV6="FC00::10:1:20:2", VPNINSTNAME="VRF_Nupf", DESC="UPF_client";

  # 步骤2：配置HTTP本端实体组
  ADD HTTPLEGRP: INDEX=1, DESC="UPF";

  # 步骤3：配置HTTP本端实体（UPF作为Server - IPv4/IPv6）
  ADD HTTPLE: INDEX=1, HTTPLEGRPIDX=1, LETYPE=SERVER, PORT=80, TLSFLG=NO, IPTYPE=IPv4, IPV4="10.1.20.1", VPNNAME="VRF_Nupf", DESC="UPF_server";
  ADD HTTPLE: INDEX=11, HTTPLEGRPIDX=1, LETYPE=SERVER, PORT=80, TLSFLG=NO, IPTYPE=IPv6, IPV6="FC00::10:1:20:1", VPNNAME="VRF_Nupf", DESC="UPF_server";
  # UPF作为Client - IPv4/IPv6
  ADD HTTPLE: INDEX=2, HTTPLEGRPIDX=1, LETYPE=CLIENT, IPTYPE=IPv4, IPV4="10.1.20.2", VPNNAME="VRF_Nupf", DESC="UPF_client";
  ADD HTTPLE: INDEX=12, HTTPLEGRPIDX=1, LETYPE=CLIENT, IPTYPE=IPv6, IPV6="FC00::10:1:20:2", VPNNAME="VRF_Nupf", DESC="UPF_client";

  # 步骤4：配置UPF使用的HTTP本端实体组（NF类型固定NFTypeUPF）
  ADD SBIAPLE: INDEX=1, HTTPLEGRPIDX=1, NFTYPE=NFTypeUPF, DESCRIPTION="UPF";

  # 步骤5：设置HTTP属性
  SET HTTPCONF: INITLINKINTVL=500, LINKAGINGTIME=120;
  ```

  **索引规则**：HTTPLE 本端实体索引 VNF 内不能重复；1~2 是 IPv4 的索引，11~12 是 IPv6 的索引。

  **验证**：
  ```
  NGPING: IPTYPE=IPv4, VPNNAME="VRF_Nupf", SRCIPV4ADDR="10.1.20.1", DSTIPV4ADDR="NWDAF的Nupf接口IP";
  PING:IPVERSION=IPv4,VPNNAME="VRF_Nupf",SOURCEIPV4ADDRESS="UPF Nupf对应的外联口IP",DESTIPV4ADDRESS="NWDAF Nupf逻辑接口对应的外联口IP";
  ```

- **来源**：配置Nupf接口数据_64469713.md
- **核心度**：★★★（仅 NWDAF 对接场景，非通用）
- **关联特性**：无（独立服务化对接，需 SSU+SBIM 服务）
- **关联命令**：ADD LOGICIP、ADD HTTPLEGRP、ADD HTTPLE、ADD SBIAPLE、SET HTTPCONF、NGPING、PING
- **关联配置对象**：逻辑IP（VRF_Nupf）、HTTP本端实体组、HTTP本端实体（SERVER/CLIENT）、服务化接口本端实体（NFTYPE=NFTypeUPF）
- **对接面**：CS-2 用户面（服务化对接，特殊子类）

### KP-09: CS-2 会话接入核心 — APN/DNN 实例配置
- **内容**：APN/DNN 实例定义"用户接入哪个网络"。UDG 本端配置的 APN/DNN 必须**与 C 面（SMF/SGW-C/PGW-C）一致**（全网规划）。

  **关键约束**：业务 APN 绑定的 VPN 必须**与 UDG 到 PDN/DN 互通的外联口绑定的 VPN 一致**。

  **MML 配置命令（原样保留）**：
  ```
  # 步骤1：配置APN所属VPN实例
  ADD VPNINST: VPNINSTANCE="VPN_Internet";

  # 步骤2：配置APN实例（绑定VPN）
  ADD APN:APN="apn-op",HASVPN=ENABLE,VPNINSTANCE="VPN_Internet";

  # 步骤3：设置APN单通检测（特殊业务如NB-IoT抄表仅上行流量时设DISABLE）
  SET APNSGLPASS:APN="apn-op",SWITCH=PF_ACT_ENABLE;
  ```

  **APN 单通检测**：指定 APN 的用户存在上下行数据时开启（PF_ACT_ENABLE）；只存在单向上行/下行业务（如 NB-IoT 抄表）时关闭（PF_ACT_DISABLE）。

- **来源**：配置会话接入数据_68634166.md（步骤1~3）
- **核心度**：★★★★★（用户接入入口）
- **关联特性**：GWFD-010105 用户面地址分配、GWFD-020421 基于位置的地址分配
- **关联命令**：ADD VPNINST、ADD APN、SET APNSGLPASS、LST APN、LST VPNINST
- **关联配置对象**：APN/DNN 实例（绑定 VPN）、APN 单通检测开关
- **对接面**：CS-2 会话接入

### KP-10: CS-2 会话接入地址池 — 地址分配三件套（POOL / SECTION / POOLGROUP）
- **内容**：UE IP 地址分配通过"地址池→地址段→地址池组"三层结构实现。地址池类型分两种：

  | 地址池类型 | POOLTYPE | 适用场景 | 是否需要地址分配规则 |
  |------------|----------|----------|----------------------|
  | **本地地址池** | LOCAL | UDG 作为主锚点且给 UE 分配 IP | 是（需配置完整POOLGROUP+POOLGRPMAP+IPALLOCRULE） |
  | **外地址池** | EXTERNAL | 辅锚点/ULCL/外部NF（如UDM）给UE分配IP | 否（仅需POOL+SECTION，可选CHECKIPVALID校验） |

  **关键约束（VPN 三一致）**：
  - 用户激活使用的 APN 绑定的 VPN
  - 地址池绑定的 VPN
  - 与 PDN/DN 连接的 Gi/SGi/N6 接口的外联口绑定的 VPN
  三者必须**一致**。

  **本地地址池场景 MML（原样保留，UDG 作为主锚点给 UE 分配地址）**：
  ```
  # a. 配置LOCAL类型地址池
  ADD POOL:POOLNAME="testpool",POOLTYPE=LOCAL,HASVPN=ENABLE,VPNINSTANCE="VPN_Internet";

  # b. 配置地址段（普通场景）
  ADD SECTION:POOLNAME="testpool",SECTIONNUM=1,IPVERSION=IPV4,V4STARTIP="10.10.1.1",V4ENDIP="10.10.1.254";
  # b'. 入不转板场景需追加 MASK 参数
  ADD SECTION:POOLNAME="testpool",SECTIONNUM=1,IPVERSION=IPV4,V4STARTIP="10.10.1.1",V4ENDIP="10.10.1.254",mask=5;

  # c. 配置地址池组（使能优先级算法）
  ADD POOLGROUP:POOLGRPNAME="poolgroup1",IPV4ALLOCPRIALG=ENABLE,IPV6ALLOCPRIALG=ENABLE;

  # d. 地址池绑定到地址池组（设优先级，同类地址池间比较）
  ADD POOLBINDGROUP:POOLGROUPNAME="poolgroup1",POOLNAME="testpool",PRIORITY=10;

  # e. APN/DNN与地址池组映射（决定APN下用户用哪个地址池组）
  ADD POOLGRPMAP:MAPPINGNAME="mapping1",APN="apn-op",POOLGROUPNAME="poolgroup1";
  ```

  **外部分配地址场景 MML（辅锚点/ULCL/外部NF分配）**：
  ```
  # a. 配置EXTERNAL类型地址池（CHECKIPVALID=ENABLE时需校验IP合法性）
  ADD POOL:POOLNAME="testpool",POOLTYPE=EXTERNAL,IPVERSION=IPV4,CHECKIPVALID=ENABLE,HASVPN=ENABLE,VPNINSTANCE="VPN_Internet",IMSSW=DISABLE,REDUNDFUNC=ENABLE;

  # b. 配置地址段（同上，入不转板场景需MASK）
  ADD SECTION:POOLNAME="testpool",SECTIONNUM=1,IPVERSION=IPV4,V4STARTIP="10.10.1.1",V4ENDIP="10.10.1.254";
  # c~e 同本地场景
  ```

  **入不转板特殊约束**：开启上下行入不转板或下行入不转板功能时，POOLTYPE 必须 LOCAL，且 SECTION 必须规划 MASK 参数。

  **验证**：LST APN、LST POOLGRPMAP、LST POOLBINDGROUP、LST POOL、LST SECTION，配合 SRVPING（SRCIPTYPE=POOL）。

- **来源**：配置会话接入数据_68634166.md（步骤4~5）
- **核心度**：★★★★★（用户 IP 分配核心机制）
- **关联特性**：GWFD-010105 用户面地址分配、GWFD-020421 基于位置的地址分配
- **关联命令**：ADD POOL、ADD SECTION、ADD POOLGROUP、ADD POOLBINDGROUP、ADD POOLGRPMAP、LST POOL、LST SECTION、LST POOLGROUP、LST POOLBINDGROUP、LST POOLGRPMAP
- **关联配置对象**：地址池(POOL)、地址段(SECTION)、地址池组(POOLGROUP)、地址池绑定(POOLBINDGROUP)、APN↔地址池组映射(POOLGRPMAP)
- **对接面**：CS-2 会话接入（地址分配层）

### KP-11: CS-2 会话接入分配规则 — SET IPALLOCRULE 三级地址分配规则
- **内容**：地址分配规则决定 UPF 在多维度（APN、位置、SMF）下如何选择地址池组。规则分三级，**默认仅第一级使能**：

  | 级别 | 规则维度组合（样例） | 默认开关 |
  |------|----------------------|----------|
  | 第一级规则 | `APN-1&LOCATION-0&SMF-0` | **ENABLE（默认使能）** |
  | 第二级规则 | （按需配置） | DISABLE（默认不使能） |
  | 第三级规则 | （按需配置） | DISABLE（默认不使能） |

  **规则组合语法**：`维度-权重&维度-权重&维度-权重`，权重数字决定该维度在选地址池组时的优先级。

  **MML 配置命令（原样保留，默认配置）**：
  ```
  SET IPALLOCRULE:FIRSTRULESW=ENABLE,FIRSTRULE=APN-1&LOCATION-0&SMF-0,SECONDRULESW=DISABLE,THIRDRULESW=DISABLE;
  ```

  **分配方式选择指引**：
  - 基于 APN/DNN 分配（默认，本文档主流程）
  - 基于 SMF 分配、基于位置分配：详见 GWFD-010105 用户面地址分配、GWFD-020421 基于位置的地址分配特性文档

- **来源**：配置会话接入数据_68634166.md（步骤4.f）
- **核心度**：★★★★（多维度地址分配决策）
- **关联特性**：GWFD-010105 用户面地址分配、GWFD-020421 基于位置的地址分配
- **关联命令**：SET IPALLOCRULE
- **关联配置对象**：地址分配规则（三级 FIRSTRULE/SECONDRULE/THIRDRULE）
- **对接面**：CS-2 会话接入（地址分配决策层）

### KP-12: CS-2 会话接入下行路由 — 动态/静态路由发布用户下行路由
- **内容**：用户下行路由发布（让网络知道如何将下行流量路由到 UE）有三种方式：

  | 路由方式 | 实现机制 | 配置位置 |
  |----------|----------|----------|
  | **OSPF/OSPFv3 动态路由** | 外联口配置 `ADD OSPFIMPORTROUTE`/`ADD OSPFV3IMPORTROUTE`，PROTOCOL=wlr | UDG 本端 |
  | **BGP over 静态路由** | 外联口配置 `ADD IMPORTROUTE`，PROTOCOL=wlr | UDG 本端 |
  | **纯静态路由** | 在对端设备上配置到用户的下行路由（目的地址/掩码对应 UE IP 网段，下一跳是每个 ISU/IPU VM 的外联口 IP） | 对端设备 |

  **wlr 协议标识**：表示"网络侧路由（用户路由）"，OSPF/OSPFv3/BGP over 静态路由方案中均通过 PROTOCOL=wlr 标识用户下行路由的动态发布。

- **来源**：配置会话接入数据_68634166.md（步骤6 + 验证）
- **核心度**：★★★（路由层补充，与 CS-4 路由对接面交界）
- **关联特性**：无（路由协议层）
- **关联命令**：ADD OSPFIMPORTROUTE、ADD OSPFV3IMPORTROUTE、ADD IMPORTROUTE（均 PROTOCOL=wlr）、DSP ROUTE、DSP ROUTE6、SRVPING（SRCIPTYPE=POOL）、SRVTRACERT、DSP SESSIONINFO
- **关联配置对象**：用户下行路由（wlr 协议标识）
- **对接面**：CS-2 会话接入 + CS-4 路由（边界）

---

## 3. 关键发现

### 3.1 接口配置共性（七类接口高度同构）
所有逻辑接口配置遵循**同一套命令范式**：`ADD VPNINST → ADD LOGICINF`，关键参数同为 NAME/IPVERSION/IPV4ADDRESS1/IPV4MASK1(固定 255.255.255.255)/VPNINSTANCE。验证手段统一为 LST LOGICINF + SRVPING + SRVTRACERT + DSP ROUTE/DSP ROUTE6。**VPN 一致性是跨接口的硬约束**：逻辑接口 VPN 必须与对应外联口 VPN 相同。

### 3.2 接口配置的强制合一 vs 可选合一
| 接口 | 配置方式 | 原因 |
|------|----------|------|
| **N4if**（N4/Sxa/Sxb） | **强制合一** | 4G/5G互操作时 N4/Sxa/Sxb 协议相同（TS 29.244） |
| **Paif**（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U） | **强制合一** | 4G/5G互操作时数据锚点不变，N9a/S5-P/S8-P 地址必须相同 |
| **Saif**（Sa/N3/S1-U） | **可选合一**（推荐合一，与独立互斥） | 抽象接口与独立接口二选一 |
| **Scif**（Sc/N9c/S5-S/S8-S） | **可选合一**（推荐合一，与独立互斥） | 同上 |
| **S11-uif** | **独立接口**（无抽象合一） | NB-IoT 专用 |
| **SGi/N6** | **无逻辑接口**（物理外联口） | 与 PDN/DN/IMS 互通走外联口 |
| **Nupf** | **服务化接口**（非 LOGICINF，用 LOGICIP+HTTPLE+SBIAPLE） | HTTP/SBI 协议，需 SSU+SBIM 服务 |

### 3.3 N4 必备性的落地约束
N4 接口是 UPF **唯一必备接口**，但单独配置 N4 不足以建立偶联——必须**至少存在一个数据面逻辑接口 IP**（Paif/Scif/Saif/N3if/S1-uif/S11-uif 任一）。SMF 要求 UPF 配 N9 才能作为主锚点激活时，Paif 成为附加必备项。一个 UPF 对接多个 SMF 需额外配置 GWFD-020161 CU Full Mesh 特性并申请 License。

### 3.4 会话接入三件套关系（APN-地址池-分配规则）
用户激活接入 PDN/DN 的完整闭环由三层构成：
1. **APN/DNN 层**（ADD APN）：定义"接入哪个网络"，绑定 VPN（必须与外联口 VPN 一致）
2. **地址池层**（POOL→SECTION→POOLGROUP→POOLBINDGROUP→POOLGRPMAP）：定义"用什么 IP"，POOLGRPMAP 将 APN 映射到地址池组
3. **分配规则层**（SET IPALLOCRULE）：定义"多维度下如何选地址池组"，默认第一级 APN 维度使能

**关键决策**：UDG 作为主锚点且给 UE 分配 IP → LOCAL 地址池 + 完整三件套；UDG 作为辅锚点/ULCL 或外部 NF 分配 → EXTERNAL 地址池 + 仅 POOL/SECTION（可选 CHECKIPVALID 校验）。

### 3.5 VPN 一致性的"四统一"原则
UPF 全局 VPN 一致性要求覆盖四类对象：
- 业务 APN 绑定的 VPN
- 地址池绑定的 VPN
- Gi/SGi/N6 外联口绑定的 VPN
- 各业务逻辑接口（N4if/Saif/Scif/Paif 等）绑定的 VPN（必须与对应外联口 VPN 一致）

### 3.6 切片绑定是接入侧特有能力
仅 Saif/N3if 支持 `SLICEATTRSW` 参数和 `ADD SNSSAIUPINTF` 切片绑定关系配置。其他接口（N4if/Scif/Paif/S11-uif）不涉及切片绑定。绑切片前若 SLICEATTRSW=DISABLE，接口会被当作非切片接口使用，可能导致 PDU Session 建立失败。

### 3.7 入不转板场景的特殊参数规划
中心云上下行入不转板或下行入不转板场景对接口和地址段都有特殊要求：
- 业务接口（Saif/Scif/Paif）：除 1/1/0 外需规划 1/Y/0（Y=2~64，每 ISU POD 一个 IP），同 VPN
- 地址池：POOLTYPE 必须 LOCAL，SECTION 必须规划 MASK 参数

---

## 4. 对接面与决策点归纳（★供第1层业务图谱）

### 4.1 CS-1 控制面对接方案要素
| 要素 | 取值/规则 | 来源KP |
|------|-----------|--------|
| N4 接口类型 | 强制合一抽象接口 N4if（不支持独立 Sxa/Sxb） | KP-02 |
| N4 接口名称 | 固定 N4if1/0/0（唯一） | KP-02 |
| N4 对端网元 | SMF / SGW-C / PGW-C（融合部署） | KP-02 |
| N4 协议 | PFCP（3GPP TS 29.244） | KP-02 |
| UPF 标识 | SET UPINFO HOSTNAME 全网唯一 | KP-02 |
| N4 偶联前提 | UDG 上至少存在一个数据面逻辑接口 IP | KP-02 |
| 多 SMF 对接 | 需 GWFD-020161 CU Full Mesh 特性 + License | KP-02 |

### 4.2 CS-2 用户面对接方案要素（按部署位置）
| UDG 角色 | 必配用户面接口 | 对端网元 | 协议接口 |
|----------|----------------|----------|----------|
| **边缘 ULCL/BP/I-UPF / SGW-U** | Saif(或N3if/S1-uif) + Scif(或N9cif/S5-Sif) | (R)AN + PSA UPF/PGW-U | Sa/N3/S1-U + Sc/N9c/S5-S |
| **锚点 PSA UPF / PGW-U** | Paif + (SGi/N6外联口) | ULCL/ePDG/SGSN + DN/PDN | Pa(N9a/S5-P/S8-P/S2b/Gn-U/Gp-U) + SGi/N6 |
| **融合 UPF+PGW-U(+SGW-U)** | Saif + Scif + Paif + (SGi/N6) | 全套 | Sa+Sc+Pa+SGi/N6 |
| **NB-IoT SGW-U** | S11-uif（附加） | MME | S11-U |
| **NWDAF 对接** | Nupf（附加） | NWDAF | HTTP/SBI |

### 4.3 决策点（DP）归纳

**DP-01: UPF 角色 → 用户面接口组合**
- 输入：UDG 部署位置（边缘/锚点/融合）+ UPF 角色（ULCL/BP/I-UPF/PSA/SGW-U/PGW-U）
- 输出：必配接口集（见 4.2 表）
- 决策依据：KP-01 部署位置矩阵

**DP-02: 双栈 / 单栈地址规划**
- 输入：组网类型（IPv4 / IPv6 / IPv4v6 双栈）
- 输出：ADD LOGICINF 的 IPVERSION（IPV4 / IPV6 / IPVER_ALL）
- 决策依据：所有接口 KP 共同约束（双栈需分别配 IPv4 和 IPv6 地址）

**DP-03: 抽象接口合一 vs 独立接口（仅 Sa/Sc）**
- 输入：Sa/Sc 接口是否合一
- 输出：使用 Saif/Scif 抽象接口 或 N3if/S1-uif/N9cif/S5-Sif 独立接口（互斥）
- 决策依据：KP-03/KP-04（推荐合一，简化配置）

**DP-04: 接入侧切片绑定**
- 输入：是否启用网络切片 + 切片是否独占逻辑接口
- 输出：SLICEATTRSW=ENABLE/DISABLE + ADD SNSSAIUPINTF 绑定关系
- 决策依据：KP-03（仅 Saif/N3if 支持）

**DP-05: 地址分配主体（UDG本地 vs 外部NF）**
- 输入：UDG 是否作为主锚点 + 是否由 UDG 给 UE 分配 IP
- 输出：POOLTYPE=LOCAL（本地，需完整三件套） 或 POOLTYPE=EXTERNAL（外部，仅 POOL+SECTION）
- 决策依据：KP-10 地址池类型表

**DP-06: 地址分配维度（APN/SMF/位置）**
- 输入：业务场景（基于APN/基于SMF/基于位置）
- 输出：SET IPALLOCRULE 三级规则组合（默认 APN-1&LOCATION-0&SMF-0）
- 决策依据：KP-11（默认第一级 APN 维度使能）

**DP-07: 用户下行路由发布方式**
- 输入：UDG↔PDN/DN 路由方案（OSPF/OSPFv3/BGP over 静态/纯静态）
- 输出：ADD OSPFIMPORTROUTE / ADD OSPFV3IMPORTROUTE / ADD IMPORTROUTE（PROTOCOL=wlr） 或 对端静态路由
- 决策依据：KP-12 下行路由三种方式表

**DP-08: DN-AAA 互通方案（仅园区 DN-AAA 场景）**
- 输入：SMF 是否需经 UPF 连接企业园区 DN-AAA
- 输出：方案A（N6 直连，VPN 与 SMF Network Instance 一致） 或 方案B（N4 专用会话 RoleType=N4U_Tunnel，不占 License）
- 决策依据：KP-07 DN-AAA 互通两种方案表

---

## 附录: 本批次 MML 命令清单（Stage4 命令层输入）

### A.1 接口配置类命令
| 命令 | 用途 | 适用接口 |
|------|------|----------|
| ADD VPNINST | 增加 VPN 实例 | 所有接口（VPN_Signaling/VPN_Access/VPN_Sc/VPN_Pa/VPN_NBIoT/VRF_Nupf/VPN_Internet） |
| ADD LOGICINF | 增加逻辑接口 | N4if/Saif/N3if/S1-uif/Scif/N9cif/S5-Sif/Paif/S11-uif |
| ADD LOGICIP | 增加逻辑 IP（服务化） | Nupf |
| ADD SNSSAIUPINTF | 网络切片与逻辑接口绑定 | Saif/N3if（仅接入侧） |
| SET UPINFO | 设置 UPF 标识（HostName） | N4（控制面必备） |

### A.2 会话接入类命令
| 命令 | 用途 |
|------|------|
| ADD APN | 添加 APN/DNN 配置（绑定 VPN） |
| SET APNSGLPASS | 设置 APN 单通检测开关 |
| ADD POOL | 添加地址池（LOCAL/EXTERNAL） |
| ADD SECTION | 添加地址池 IP 地址段 |
| ADD POOLGROUP | 添加地址池组 |
| ADD POOLBINDGROUP | 地址池绑定到地址池组 |
| ADD POOLGRPMAP | APN/DNN 与地址池组映射 |
| SET IPALLOCRULE | 设置地址分配规则（三级） |

### A.3 HTTP/SBI 服务化类命令（仅 Nupf）
| 命令 | 用途 |
|------|------|
| ADD HTTPLEGRP | 增加 HTTP 本端实体组 |
| ADD HTTPLE | 增加 HTTP 本端实体（SERVER/CLIENT） |
| ADD SBIAPLE | 增加服务化接口本端实体（NFTYPE=NFTypeUPF） |
| SET HTTPCONF | 设置 HTTP 属性 |

### A.4 路由发布类命令（与 CS-4 路由对接面交界）
| 命令 | 用途 |
|------|------|
| ADD OSPFIMPORTROUTE | OSPF 动态路由发布用户下行路由（PROTOCOL=wlr） |
| ADD OSPFV3IMPORTROUTE | OSPFv3 动态路由发布（IPv6，PROTOCOL=wlr） |
| ADD IMPORTROUTE | BGP over 静态路由发布（PROTOCOL=wlr） |

### A.5 验证/查询类命令
| 命令 | 用途 |
|------|------|
| LST LOGICINF | 查询逻辑接口 |
| LST VPNINST | 查询 VPN 实例 |
| LST APN | 查询 APN 配置 |
| LST POOL / LST SECTION / LST POOLGROUP / LST POOLBINDGROUP / LST POOLGRPMAP | 地址池体系查询 |
| DSP SESSIONINFO | 显示用户上下文（探测源 IP 选择） |
| SRVPING | 业务 Ping（SRCIPTYPE=LOGICINF/POOL） |
| SRVTRACERT | 业务 Tracert |
| NGPING | 服务化接口 Ping（Nupf） |
| PING | 物理 Ping（Nupf 外联口） |
| DSP ROUTE / DSP ROUTE6 | IPv4/IPv6 路由表查询 |
| EXP MML | 导出 MML 配置文件（故障收集） |
