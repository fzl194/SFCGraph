# 命令证据包：ADD L3VPNINST
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md`
> 用该命令的特性数：8

## ② 命令真相（mml_commands.jsonl）
**功能**：该命令用于创建L3VPN实例。

创建VPN可以使用户获得专用虚拟的网络。

专用：VPN网络与底层承载网络之间保持资源独立，即VPN资源不被网络中非该VPN的用户所使用；且VPN能够提供足够的安全保证，确保VPN内部信息不受外部侵扰。

虚拟：VPN用户内部的通信是通过公共网络进行的，而这个公共网络同时也可以被其他非VPN用户使用，VPN用户获得的只是一个逻辑意义上的专网。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为4096。
- 不能增加VPN实例 _public_、__mpp_vpn_inner__、__mpp_vpn_inner_server__。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| VRFNAME | VPN实例名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。 |
| VRFDESCRIPTION | VPN实例描述 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～242。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### IPFD-012001

**md：`IPFD-012001/激活QoS复杂流分类功能（VNRS）_13119479.md`**
- 操作步骤上下文（±2 行原文）：
  L112:
    >     - （可选）配置重定向VPN组：
    >       **[ADD SQOSRDRVPNGROUP](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/重定向VPN组/增加QoS重定向VPN组（ADD SQOSRDRVPNGROUP）_00441265.md)** :VPNGROUPNAME="VPN组名称", BEHAVIORNAME="行为名称";
    >       需要先使用 [**ADD SQOSVPNGROUP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/VPN组/增加VPN组（ADD SQOSVPNGROUP）_00600349.md) 命令添加VPN组，使用 [**ADD L3VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md) 命令添加VPN实例，使用 [**ADD SQOSVPNGROUPMEM**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/VPN组成员/增加VPN组成员（ADD SQOSVPNGROUPMEM）_50280994.md) 命令向VPN组添加VPN成员。
    >     - （可选）配置安全URPF：
    >       **[ADD SQOSURPF](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/流行为安全URPF/增加流行为安全URPF（ADD SQOSURPF）_50280766.md)** :BEHAVIORNAME="流行为名称", URPFTYPE="URPF检查类型", URPFDEFAULT="匹配默认路由";

### IPFD-016000

**md：`IPFD-016000/激活IPsec功能（GRE over IPsec）_78985535.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
- 操作步骤上下文（±2 行原文）：
  L154:
    > 1. 创建VNRS微服务的VPN、IPsec隧道接口和GRE隧道接口。
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 创建GRE本端源接口。
  L223:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 
  L409:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（IPv4 IPsec主备隧道）_88744738.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
- 操作步骤上下文（±2 行原文）：
  L148:
    > 1. 创建VNRS微服务的VPN和IPsec隧道接口，并配置到达目的网络的静态路由。
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
  L210:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 
  L374:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（IPv6 IPsec隧道主备方式）_53998700.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
- 操作步骤上下文（±2 行原文）：
  L149:
    > 1. 创建VNRS微服务的VPN和IPsec隧道接口，并配置到达目的网络的静态路由。
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
  L212:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 
  L404:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（OSPF over IPsec）_90949389.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
- 操作步骤上下文（±2 行原文）：
  L164:
    > 1. 创建VNRS微服务的VPN、IPsec隧道接口和OSPF的loopback口。
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 创建OSPF的loopback口。
  L234:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 
  L436:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（多Sequence的IPsec策略）_78985536.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
- 操作步骤上下文（±2 行原文）：
  L153:
    > 1. 创建VNRS微服务的VPN和IPsec隧道接口，并配置到达目的网络的静态路由。
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
  L215:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 
  L409:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（指定本端接口建立IPsec隧道）_78985537.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
- 操作步骤上下文（±2 行原文）：
  L169:
    > 1. 创建VNRS微服务的VPN和IPsec隧道接口、Loopback接口，并配置静态路由用于IPsec引流。
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
  L229:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 
  L395:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
- 操作步骤上下文（±2 行原文）：
  L143:
    > 1. 创建VNRS微服务的VPN和IPsec隧道接口，并配置到达目的网络的静态路由。
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
  L205:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 
  L359:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（普通IPv6 IPsec隧道）_78985538.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
- 操作步骤上下文（±2 行原文）：
  L141:
    > 1. 创建VNRS微服务的VPN和IPsec隧道接口，并配置到达目的网络的静态路由。
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
  L204:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 
  L372:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（GRE over IPsec）_53928160.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
- 操作步骤上下文（±2 行原文）：
  L156:
    > 1. 创建VNRS微服务的VPN、IPsec隧道接口和GRE隧道接口。
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 创建GRE本端源接口。
  L223:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 
  L415:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（多Sequence的IPsec策略）_03408185.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
- 操作步骤上下文（±2 行原文）：
  L155:
    > 1. 创建VNRS微服务的VPN和IPsec隧道接口，并配置到达目的网络的静态路由。
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
  L215:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 
  L415:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（指定本端接口建立IPsec隧道）_03567841.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
- 操作步骤上下文（±2 行原文）：
  L171:
    > 1. 创建VNRS微服务的VPN和IPsec隧道接口、Loopback接口，并配置静态路由用于IPsec引流。
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
  L229:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 
  L401:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（普通IPv4 IPsec隧道）_03728909.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
- 操作步骤上下文（±2 行原文）：
  L143:
    > 1. 创建VNRS微服务的VPN和IPsec隧道接口，并配置到达目的网络的静态路由。
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
  L203:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 
  L363:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（普通IPv6 IPsec隧道）_53768408.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vrf1";`
  `ADD L3VPNINST:VRFNAME="vrf1";`
- 操作步骤上下文（±2 行原文）：
  L142:
    > 1. 创建VNRS微服务的VPN和IPsec隧道接口，并配置到达目的网络的静态路由。
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
  L203:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 
  L377:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vrf1";
    > ```
    > 

### WSFD-010102

**md：`WSFD-010102/配置到3GPP AAA Server的数据_80511835.md`**
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST: VRFNAME="vpn_3gpp_aaa";`
- 操作步骤上下文（±2 行原文）：
  L74:
    >   [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > 3. 配置L3VPN实例。
    >   **[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)**
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. **可选：**配置S6b接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
  L129:
    > 3. 创建VPN实例。
    >   ```
    >   ADD L3VPNINST: VRFNAME="vpn_3gpp_aaa";
    >   ```
    >   ```

### WSFD-202001

**md：`WSFD-202001/WSFD-202001 CHR功能参考信息_50287964.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**ADD L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    > - [**ADD UCFIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/UCF管理/UCF本地IP/配置UCF报表本地IP资源池（ADD UCFIP）_51253792.md)
    > - [**ADD UCFSVRIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/UCF管理/UCF服务器IP/添加UCF报表服务器的接入点IP地址（ADD UCFSVRIP）_51253793.md)
  L15:
    > - [**ADD UCFIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/UCF管理/UCF本地IP/配置UCF报表本地IP资源池（ADD UCFIP）_51253792.md)
    > - [**ADD UCFSVRIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/UCF管理/UCF服务器IP/添加UCF报表服务器的接入点IP地址（ADD UCFSVRIP）_51253793.md)
    > - [**ADD L3VPNINST**](../../../../../OM参考/命令/UNC机机接口命令/平台机机命令/平台服务管理_031069_1.md)
    > - [**SET NGACCCHRCFG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/CHR管理/NG接入CHR配置/设置NG接入CHR上报策略（SET NGACCCHRCFG）_34945607.md)
    > - [**ADD NGACCCHRPRCTMPL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/CHR管理/NG接入CHR流程控制模板/增加NG接入CHR流程控制模板（ADD NGACCCHRPRCTMPL）_34945602.md)

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - **[SET RDSRSPADDRCHK](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/RADIUS响应消息地址检查/设置全局RADIUS响应消息源IP_端口检查配置（SET RDSRSPADDRCHK）_09896744.md)**
    > - [**ADD UPLIST4RDS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)
    > - [**ADD L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    > - **[**ADD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)

**md：`WSFD-011306/配置到AAA Server的数据（单平面+静态路由+BFD组网）_32044985.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md) | VPN实例名称 (VRFNAME) | vpn_pdn<br>vpn_aaa | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST: VRFNAME ="vpn_pdn";`
  `ADD L3VPNINST: VRFNAME ="vpn_aaa";`
- 操作步骤上下文（±2 行原文）：
  L89:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 创建L3VPN实例。
    >   [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 创建VPN实例。
  L137:
    > 
    > ```
    > ADD L3VPNINST: VRFNAME ="vpn_pdn";
    > ```
    > 
  L147:
    > 
    > ```
    > ADD L3VPNINST: VRFNAME ="vpn_aaa";
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（双平面+OSPF动态路由+BFD组网 ）_31879931.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md) | VPN实例名称 (VRFNAME) | vpn_pdn | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST:VRFNAME="vpn_pdn";`
- 操作步骤上下文（±2 行原文）：
  L91:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 创建L3VPN实例。
    >   [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 创建VPN实例。
  L137:
    > 
    > ```
    > ADD L3VPNINST:VRFNAME="vpn_pdn";
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（带内组网GRE VPN）_32723577.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md) | VPN实例名称 (VRFNAME) | vpn_enterprise<br>vpn_tunnel | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST: VRFNAME ="vpn_enterprise";`
  `ADD L3VPNINST: VRFNAME ="vpn_tunnel";`
- 操作步骤上下文（±2 行原文）：
  L106:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 创建L3VPN实例。
    >   [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 创建GRE隧道。
  L169:
    > 
    > ```
    > ADD L3VPNINST: VRFNAME ="vpn_enterprise";
    > ```
    > 
  L177:
    > 
    > ```
    > ADD L3VPNINST: VRFNAME ="vpn_tunnel";
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（带外组网GRE VPN）_32050904.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md) | VPN实例名称 (VRFNAME) | vpn_enterprise<br>vpn_tunnel<br>vpn_aaa | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST: VRFNAME ="vpn_enterprise";`
  `ADD L3VPNINST: VRFNAME ="vpn_tunnel";`
  `ADD L3VPNINST: VRFNAME ="vpn_aaa";`
- 操作步骤上下文（±2 行原文）：
  L106:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 创建L3VPN实例。
    >   [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 创建GRE隧道。
  L170:
    > 
    > ```
    > ADD L3VPNINST: VRFNAME ="vpn_enterprise";
    > ```
    > 
  L178:
    > 
    > ```
    > ADD L3VPNINST: VRFNAME ="vpn_tunnel";
    > ```
    > 

### WSFD-104004

**md：`WSFD-104004/WSFD-104004 IPv6前缀代理参考信息_76459529.md`**
- 操作步骤上下文（±2 行原文）：
  L15:
    > - [**RMV VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/删除VPN实例（RMV VPNINST）_09651424.md)
    > - [**LST VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)
    > - **[**ADD L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)**
    > - **[**RMV L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/删除L3VPN实例（RMV L3VPNINST）_50120962.md)**
    > - **[**MOD L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/修改L3VPN实例（MOD L3VPNINST）_00840733.md)**

**md：`WSFD-104004/激活IPv6前缀代理_76459527.md`**
- 数据规划表（该命令的参数行）：
  | **[**ADD L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)** | VPN实例名称（VRFNAME） | vpn1 | 本端规划 | 配置L3VPN实例。 |
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST: VRFNAME="vpn1";`
- 操作步骤上下文（±2 行原文）：
  L50:
    >       [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    >     b. 使能IPv6地址族。
    >       **[**ADD L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)**
    >       **[**ADD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    >     c. 配置路由标识符。
  L87:
    > ADD VPNINST
    > : VPNINSTANCE="vpn1";
    > ADD L3VPNINST: VRFNAME="vpn1";
    > ADD VPNINSTAF: VRFNAME="vpn1", AFTYPE=ipv6uni;
    > MOD VPNINSTAF: VRFNAME="vpn1", AFTYPE=ipv6uni, VRFRD="65512:2";

### WSFD-011201

**md：`WSFD-011201/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md`**
- 数据规划表（该命令的参数行）：
  | **ADD L3VPNINST** | VPN实例名称（VRFNAME） | vpn_ga | 本端规划 | 创建L3VPN实例 |
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST: VRFNAME="vpn_ga";`
- 操作步骤上下文（±2 行原文）：
  L63:
    > 1. 参考 **《UNC产品手册》：UNC初始配置与调测->** **组网路由配置->** **配置VNF侧IP路由数据（非SDN）->** **手动部署** **->** **配置静态路由+BFD组网（IPv4）** 配置对应的组网。
    > 2. 创建L3VPN实例。
    >   **ADD L3VPNINST**
    > 3. 创建VPN实例。
    >   **ADD VPNINST**
  L120:
    > 2. 创建L3VPN实例。
    >   ```
    >   ADD L3VPNINST: VRFNAME="vpn_ga";
    >   ADD VPNINSTAF:VRFNAME="vpn_ga", AFTYPE=ipv4uni;
    >   MOD VPNINSTAF:VRFNAME="vpn_ga", AFTYPE=ipv4uni, VRFRD="1050:1";

### WSFD-109001

**md：`WSFD-109001/配置到OCS的数据(静态路由+BFD组网)_95923542.md`**
- 数据规划表（该命令的参数行）：
  | **ADD L3VPNINST** | VPN实例名称（VRFNAME） | vpn_gy | 本端规划 | 创建L3VPN实例。 |
- 任务示例脚本（该命令行）：
  `ADD L3VPNINST: VRFNAME="vpn_gy";`
- 操作步骤上下文（±2 行原文）：
  L83:
    >   **ADD VPNINST**
    > 3. 创建L3VPN实例。
    >   **ADD L3VPNINST**
    > 4. **可选：**配置Gy接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   **SET CONCENPOINT**
  L143:
    > 3. 创建L3VPN实例。
    >   ```
    >   ADD L3VPNINST: VRFNAME="vpn_gy";
    >   ADD VPNINSTAF:VRFNAME="vpn_gy", AFTYPE=ipv4uni;
    >   MOD VPNINSTAF:VRFNAME="vpn_gy", AFTYPE=ipv4uni, VRFRD="2050:1";

## ④ 自动比对
- 命令真相参数（2）：['VRFDESCRIPTION', 'VRFNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 7}（多值→atom 应考虑 decision_driven）
