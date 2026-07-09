# UPF网元对接三层图谱 · 第5层：跨层映射关系总表

> **文件定位**：`three-layer-graph/05-cross-layer-mapping.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §12 跨层映射
> **作用**：汇总 CS↔Feature/Task、Feature↔Task、Task↔Command/Object、DP↔Task 的所有跨层边
> **合规要求**：严格避免 §13 禁止关系，前端主导航链路固定为 `CS → Feature → Task → Command`

---

## 0. 跨层映射总览

| 跨层边类型 | 数量 | 方向 | 说明 |
|-----------|------|------|------|
| CS `uses_feature` | 8 | 业务层→特性层 | 5方案映射到8个目录原生特性 |
| CS `uses_task`（方案闭包级） | 5 | 业务层→任务层 | 仅作方案闭包声明，不作为前端主导航 |
| Feature `decomposes_to` ConfigTask | 14 | 特性层→任务层 | 特性向任务展开 |
| ConfigTask `invokes` MMLCommand | 11组 | 任务层→命令层 | Task调用的命令集合 |
| ConfigTask `targets` SemanticObject/ConfigObject | 10组 | 任务层→对象层 | Task操作的对象 |
| DP `selects` / `sets_value_pattern` | 7 | 业务层→任务/参数模式 | 决策点选择路径或参数模式 |

> **前端消费约束**：
> 1. 方案下钻优先走 `CS uses_feature`
> 2. 特性下钻优先走 `Feature decomposes_to ConfigTask`
> 3. 任务下钻优先走 `ConfigTask invokes MMLCommand`
> 4. `CS uses_task` 仅作为方案闭包级辅助映射，不替代主链

---

## 1. CS → Feature 映射（uses_feature，8条）

> 来源：`01-business-graph.md` §2 + §8.2

| CS | uses_feature | Feature角色 |
|----|-------------|------------|
| `CS-ND-01 架构与基础就绪` | `ND-FEAT-01 架构认知与角色判定` | 核心：开局角色与接口认知 |
| `CS-ND-01 架构与基础就绪` | `ND-FEAT-02 License与基础数据就绪` | 核心：开局前置基础闭环 |
| `CS-ND-02 网管与安全接入` | `ND-FEAT-03 网管纳管与安全授权` | 核心：纳管与安全入口 |
| `CS-ND-03 控制面与用户面对接` | `ND-FEAT-04 控制面对接` | 核心：N4控制面入口 |
| `CS-ND-03 控制面与用户面对接` | `ND-FEAT-05 用户面接口对接` | 核心：业务接口承载 |
| `CS-ND-03 控制面与用户面对接` | `ND-FEAT-06 会话接入数据` | 核心：会话接入闭环 |
| `CS-ND-04 路由组网实施` | `ND-FEAT-07 路由组网实施` | 核心：路由实施主特性 |
| `CS-ND-05 实例验证与整网调测` | `ND-FEAT-08 实例与整网调测` | 核心：实例模板与验收 |

---

## 2. CS → ConfigTask 映射（uses_task，方案闭包级，5条）

> 每方案一个主 Task 集，按方案闭包粒度聚合。
> **注**：本节仅用于声明式闭包映射。前端下钻主链仍应优先使用 §1 `CS → Feature` 再走 §3 `Feature → ConfigTask`。

| CS | uses_task（主Task集） | 说明 |
|----|---------------------|------|
| `CS-ND-01 架构与基础就绪` | `T-ND-01`, `T-ND-02`, `T-ND-03` | 架构认知 + License + 基础数据 |
| `CS-ND-02 网管与安全接入` | `T-ND-04`, `T-ND-05` | 安全前置 + 纳管 |
| `CS-ND-03 控制面与用户面对接` | `T-ND-06`, `T-ND-07`, `T-ND-08`, `T-ND-09` | N4 + 用户面 + Nupf/切片 + 会话接入 |
| `CS-ND-04 路由组网实施` | `T-ND-10`, `T-ND-11`, `T-ND-12`, `T-ND-13` | VPN/外联口 + 协议 + 增强 + 自动化 |
| `CS-ND-05 实例验证与整网调测` | `T-ND-14` | 实例映射与调测 |

---

## 3. Feature → ConfigTask 映射（decomposes_to，14条）

| Feature | decomposes_to | Task集 | 说明 |
|---------|---------------|--------|------|
| `ND-FEAT-01 架构认知与角色判定` | `T-ND-01` | `T-ND-01` | 角色、参考点、接口抽象前置 |
| `ND-FEAT-02 License与基础数据就绪` | `T-ND-02`, `T-ND-03` | `T-ND-02~03` | License与基础参数闭环 |
| `ND-FEAT-03 网管纳管与安全授权` | `T-ND-04`, `T-ND-05` | `T-ND-04~05` | 安全授权与纳管闭环 |
| `ND-FEAT-04 控制面对接` | `T-ND-06` | `T-ND-06` | N4控制面接口 |
| `ND-FEAT-05 用户面接口对接` | `T-ND-07`, `T-ND-08` | `T-ND-07~08` | 业务接口 + Nupf/切片 |
| `ND-FEAT-06 会话接入数据` | `T-ND-09` | `T-ND-09` | APN/地址池/分配规则 |
| `ND-FEAT-07 路由组网实施` | `T-ND-10`, `T-ND-11`, `T-ND-12`, `T-ND-13` | `T-ND-10~13` | 路由实施完整链 |
| `ND-FEAT-08 实例与整网调测` | `T-ND-14` | `T-ND-14` | 实例与验收链 |

---

## 4. ConfigTask → MMLCommand 映射（invokes，11组核心映射）

| ConfigTask | invokes | MMLCommand | 说明 |
|-----------|---------|-----------|------|
| `T-ND-02` | `invokes` | `DSP RVKLICINFO` | License激活确认 |
| `T-ND-03` | `invokes` | `SET NTP`, `MOD ME`, `SET OMIP`, `SET SIGDSCP`, `SET UDPCHECKSUM`, `SET SRVCOMMONPARA`, `SET QOSCAR`, `SET IPV6FRAGPLCY`, `SET CPTEIDUALLOC`, `SET TZ`, `SET ANTIFRAUD`, `SET FWDPARA`, `SET HEADENGLBPARA`, `SET MSFAULTALARM`, `SET FABRICMTU`, `MOD INTERFACE`, `SET IFIPV6ENABLE` | 基础数据与MTU |
| `T-ND-04` | `invokes` | `SET SECAUTH`, `ADD USRSECAUTH`, `ADD SECAUTHMEM`, `SET NEWCERTSWITCH` | 安全授权前置 |
| `T-ND-05` | `invokes` | `LST ME` | 纳管校验 |
| `T-ND-06` | `invokes` | `ADD VPNINST`, `ADD LOGICINF`, `SET UPINFO` | N4控制面接口 |
| `T-ND-07` | `invokes` | `ADD VPNINST`, `ADD LOGICINF` | Sa/Sc/Pa/S11-U/SGi/N6 |
| `T-ND-08` | `invokes` | `ADD SNSSAIUPINTF`, `ADD LOGICIP`, `ADD HTTPLEGRP`, `ADD HTTPLE`, `ADD SBIAPLE`, `SET HTTPCONF` | Nupf与切片接口 |
| `T-ND-09` | `invokes` | `ADD APN`, `SET APNSGLPASS`, `ADD POOL`, `ADD SECTION`, `ADD POOLGROUP`, `ADD POOLBINDGROUP`, `ADD POOLGRPMAP`, `SET IPALLOCRULE` | 会话接入数据 |
| `T-ND-10` | `invokes` | `ADD L3VPNINST`, `ADD VPNINSTAF`, `MOD VPNINSTAF`, `ADD VPNTARGET`, `ADD IPBINDVPN` | VPN与外联口基础 |
| `T-ND-11` | `invokes` | `ADD OSPF`, `ADD OSPFAREA`, `ADD OSPFNETWORK`, `ADD OSPFINTERFACE`, `ADD OSPFIMPORTROUTE`, `ADD OSPFV3`, `ADD OSPFV3AREA`, `ADD OSPFV3INTERFACE`, `ADD OSPFV3IMPORTROUTE`, `SET BGP`, `ADD BGPVRF`, `ADD BGPVRFAF`, `ADD BGPPEER`, `ADD BGPPEERAF`, `ADD IMPORTROUTE`, `ADD NETWORKROUTE`, `ADD SRROUTE`, `ADD SRROUTE6` | 路由协议链 |
| `T-ND-12` | `invokes` | `SET BFD`, `ADD BFDSESSION`, `ADD GRETUNNEL`, `MOD GRETUNNEL`, `SET MPLSSITE`, `ADD MPLSIF`, `SET DHCP6CLIENTDUID` | BFD与隧道增强 |
| `T-ND-13` | `invokes` | `LST AUTOCONFIG`, `DSP OPSASSISTSTATE`, `SET AUTOCONFIG`, `ADD AUTOSCALINGETHTRUNK`, `ADD AUTOSCALINGSERVICE`, `MOD AUTOSCALINGSERVICE`, `ADD AUTOSCALINGBFD`, `ADD AUTOSCALINGSRBFD`, `ADD AUTOSCALINGSRROUTE`, `ADD AUTOSCALINGBGPLF`, `ADD AUTOSCALINGIPREACH`, `ADD AUTOSCALINGMPLS`, `ADD NPDIRECTCONNECTPORT` | 自动部署与级联口 |
| `T-ND-14` | `invokes` | `LST LOGICINF`, `LST VPNINST`, `LST APN`, `LST OSPF`, `LST BGPPEER`, `DSP BGPPEERINFO`, `DSP ROUTE`, `DSP ROUTE6`, `DSP SRROUTE`, `DSP OSPFROUTING`, `DSP OSPFPEER`, `DSP BFDSESSION`, `DSP IFSTATUS`, `DSP SESSIONINFO`, `NGPING`, `PING`, `SRVPING`, `SRVTRACERT`, `DSP SERVICERUSTATE`, `EXP MML` | 实例验证与整网调测 |

---

## 5. ConfigTask → SemanticObject/ConfigObject 映射（targets）

| ConfigTask | targets SemanticObject | targets ConfigObject |
|-----------|------------------------|---------------------|
| `T-ND-01` | `SO-ND-01`, `SO-ND-02` | — |
| `T-ND-02` | `SO-ND-03` | `LicenseState` |
| `T-ND-03` | `SO-ND-04`, `SO-ND-05`, `SO-ND-07`, `SO-ND-08` | `NTPSource`, `NetworkElement`, `OMIP`, `GlobalParameter`, `MTUConfig` |
| `T-ND-04` | `SO-ND-06` | `SecurityAuth` |
| `T-ND-05` | `SO-ND-09`, `SO-ND-10`, `SO-ND-11` | `NorthboundUser`, `SNMPUser`, `NetworkMgmtAdapter`, `ManagedNE` |
| `T-ND-06` | `SO-ND-12` | `VPNInstance`, `LogicInterface`, `UPFIdentity` |
| `T-ND-07` | `SO-ND-13` | `VPNInstance`, `LogicInterface` |
| `T-ND-08` | `SO-ND-14`, `SO-ND-13` | `SNSSAIBinding`, `LogicIP`, `HttpLeGroup`, `HttpLe`, `SbiApLe` |
| `T-ND-09` | `SO-ND-15`, `SO-ND-16`, `SO-ND-17` | `APN`, `AddressPool`, `AddressSection`, `PoolGroup`, `PoolBindGroup`, `PoolGroupMap`, `IPAllocRule` |
| `T-ND-10` | `SO-ND-18`, `SO-ND-19` | `L3VPNInstance`, `VPNTarget` |
| `T-ND-11` | `SO-ND-20`, `SO-ND-21`, `SO-ND-22` | `OSPFDomain`, `BGPDomain`, `StaticRoute` |
| `T-ND-12` | `SO-ND-23`, `SO-ND-24` | `BFDSession`, `TunnelOverlay` |
| `T-ND-13` | `SO-ND-18` | `AutoDeployTemplate`, `DirectConnectPort` |
| `T-ND-14` | `SO-ND-25` | `AcceptanceResult` |

---

## 6. DecisionPoint 跨层影响（selects / sets_value_pattern）

| DP | 关系 | 目标 | 说明 |
|----|------|------|------|
| `DP-ND-01 UDG部署角色` | `selects` | `ND-FEAT-04` / `ND-FEAT-05` | 角色不同决定接口集合裁剪 |
| `DP-ND-05 是否需要Nupf` | `selects` | `T-ND-08` | 决定是否进入 Nupf/切片任务 |
| `DP-ND-07 地址分配主体` | `sets_value_pattern` | `IPAllocRule.MODE` | `LOCAL` 或 `EXTERNAL` |
| `DP-ND-09 SDN与否` | `selects` | `T-ND-11` / `T-ND-12` | 限制协议链和 BFD 模式 |
| `DP-ND-10 部署方式` | `selects` | `T-ND-13` | 自动或手工部署 |
| `DP-ND-12 路由协议` | `sets_value_pattern` | `RoutingProtocolFamily` | OSPF/OSPFv3/BGP/静态/MPLS VPN |
| `DP-ND-15 典型实例模板` | `selects` | `T-ND-14` | 选择实例模板进入调测链 |

---

## 7. 端到端链路验证（3条完整路径）

### 7.1 路径A：基础就绪与纳管端到端

```
[业务] BD-ND 网元对接
  → NS-ND-UPF UPF网元对接
    → CS-ND-01 架构与基础就绪
      → ND-FEAT-01 架构认知与角色判定
      → ND-FEAT-02 License与基础数据就绪

[任务] ND-FEAT-02 decomposes_to
  → T-ND-02 加载License
  → T-ND-03 配置基础数据与MTU

[命令] T-ND-03 invokes
  → SET NTP / MOD ME / SET OMIP / SET FABRICMTU

[延伸] CS-ND-02 网管与安全接入
  → ND-FEAT-03 网管纳管与安全授权
  → T-ND-04 配置二次授权与证书开关
  → T-ND-05 配置网管纳管
  → LST ME
```

### 7.2 路径B：控制面到会话接入端到端

```
[业务] CS-ND-03 控制面与用户面对接
  → ND-FEAT-04 控制面对接
  → ND-FEAT-05 用户面接口对接
  → ND-FEAT-06 会话接入数据

[任务]
  ND-FEAT-04 → T-ND-06 配置N4控制面接口
  ND-FEAT-05 → T-ND-07 配置业务用户面接口
  ND-FEAT-05 → T-ND-08 配置Nupf与切片接口
  ND-FEAT-06 → T-ND-09 配置会话接入数据

[命令]
  T-ND-06 → ADD VPNINST / ADD LOGICINF / SET UPINFO
  T-ND-09 → ADD APN / ADD POOL / ADD SECTION / SET IPALLOCRULE
```

### 7.3 路径C：路由实施到调测端到端

```
[业务] CS-ND-04 路由组网实施
  → ND-FEAT-07 路由组网实施
  → T-ND-10 配置VPN与外联口基础
  → T-ND-11 配置路由协议
  → T-ND-12 配置BFD与隧道叠加
  → T-ND-13 配置自动部署或级联口

[命令]
  T-ND-10 → ADD L3VPNINST / ADD VPNINSTAF / ADD VPNTARGET
  T-ND-11 → ADD OSPF* / SET BGP / ADD BGP* / ADD SRROUTE*
  T-ND-12 → SET BFD / ADD BFDSESSION / ADD GRETUNNEL / SET MPLSSITE
  T-ND-13 → SET AUTOCONFIG / ADD AUTOSCALING* / ADD NPDIRECTCONNECTPORT

[验收]
  CS-ND-05 实例验证与整网调测
  → ND-FEAT-08 实例与整网调测
  → T-ND-14 典型实例映射与整网调测
  → DSP SESSIONINFO / NGPING / DSP BGPPEERINFO
```

---

## 8. 一致性说明

| 校验项 | 结果 |
|--------|------|
| 方案下钻主链为 `CS → Feature` | ✅ |
| 特性下钻主链为 `Feature → Task` | ✅ |
| 任务下钻主链为 `Task → Command` | ✅ |
| `CS → Task` 仅保留为辅助闭包 | ✅ |
| 未建立 `CS → Command` 禁止关系 | ✅ |
| 未建立 `Feature → Command` 禁止关系 | ✅ |

---

> 本文件服务前端主导航链路：`方案 → 特性 → 任务 → 命令`。如前端仍直接从方案落到任务，应优先检查消费方是否错误读取了 §2 `CS uses_task`，而不是 §1 和 §3 的主链映射。
