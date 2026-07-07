# 命令证据包：ADD VPNINSTAF
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md`
> 用该命令的特性数：7

## ② 命令真相（mml_commands.jsonl）
**功能**：该命令用于设置指定VPN实例下的地址族。

使能VPN实例下的地址族后，才可以进行VPN该地址族下的相关配置。一些路由协议在对VPN路由进行操作时，也要求VPN使能相应的地址族。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为16378。
- 需要确保指定的VPN实例在设备上已经通过ADD L3VPNINST创建。
- 不能给VPN实例__mpp_vpn_inner__、__mpp_vpn_inner_server__添加地址族。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| VRFNAME | VPN实例名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。 |
| AFTYPE | 地址族类型 | local_planned | required | 无 | 枚举类型。 |
| VRFRD | 路由标识 | global_planned | optional | 无 | 字符串类型，输入长度范围为3～21。 |
| IMPOLICYNAME | 引入路由策略名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～200。 |
| LOCALCROSSNHPMOD | 可更改本地交叉下一跳 | local_planned | optional | FALSE | 布尔类型，输入格式为“TRUE”或者“FALSE”。 |
| EXPOLICYNAME | 发布路由策略名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～200。 |
| EXPLYADDERTFIRST | 路由上送时首先添加ERT | local_planned | optional | FALSE | 布尔类型，输入格式为“TRUE”或者“FALSE”。 |
| VRFLABELMODE | 实例的标签分配模式 | local_planned | optional | perRoute | 枚举类型。 |
| VRFLABEL | 实例的标签值 | local_planned | conditional | 无 | 整数类型，取值范围为16～32767。 |
| TNLPOLICYNAME | 隧道策略名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～39。 |
| FRRENABLE | FRR使能 | local_planned | optional | FALSE | 布尔类型，输入格式为“TRUE”或者“FALSE”。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### IPFD-016000

**md：`IPFD-016000/激活IPsec功能（GRE over IPsec）_78985535.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L155:
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 创建GRE本端源接口。
    >       [**ADD INTERFACE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACE）_49960870.md)
  L227:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 
  L413:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（IPv4 IPsec主备隧道）_88744738.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L149:
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
    >       [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
  L214:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 
  L378:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（IPv6 IPsec隧道主备方式）_53998700.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;`
- 操作步骤上下文（±2 行原文）：
  L150:
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
    >       [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
  L216:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;
    > ```
    > 
  L408:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（OSPF over IPsec）_90949389.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L165:
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 创建OSPF的loopback口。
    >       [**ADD INTERFACE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACE）_49960870.md)
  L238:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 
  L440:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（多Sequence的IPsec策略）_78985536.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L154:
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
    >       [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
  L219:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 
  L413:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（指定本端接口建立IPsec隧道）_78985537.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L170:
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
    >       [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
  L233:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 
  L399:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L144:
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
    >       [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
  L209:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 
  L363:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（普通IPv6 IPsec隧道）_78985538.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;`
- 操作步骤上下文（±2 行原文）：
  L142:
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
    >       [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
  L208:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;
    > ```
    > 
  L376:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（GRE over IPsec）_53928160.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L157:
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 创建GRE本端源接口。
    >       [**ADD INTERFACE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/接口配置/增加接口（ADD INTERFACE）_49960870.md)
  L227:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 
  L419:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（多Sequence的IPsec策略）_03408185.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L156:
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
    >       [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
  L219:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 
  L419:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（指定本端接口建立IPsec隧道）_03567841.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L172:
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
    >       [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
  L233:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 
  L405:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（普通IPv4 IPsec隧道）_03728909.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L144:
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
    >       [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
  L207:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 
  L367:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（普通IPv6 IPsec隧道）_53768408.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;`
  `ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;`
- 操作步骤上下文（±2 行原文）：
  L143:
    >     a. 创建VPN实例。
    >       [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >       [**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)
    >     b. 将与VPN网络连接的接口与VPN实例绑定，并配置接口IP地址。
    >       [**ADD IPBINDVPN**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IP绑定VPN/增加接口绑定VPN（ADD IPBINDVPN）_50120734.md)
  L207:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;
    > ```
    > 
  L381:
    > 
    > ```
    > ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;
    > ```
    > 

### WSFD-010102

**md：`WSFD-010102/配置到3GPP AAA Server的数据_80511835.md`**
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF: VRFNAME="vpn_3gpp_aaa",AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L75:
    > 3. 配置L3VPN实例。
    >   **[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)**
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. **可选：**配置S6b接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。
    >   [**SET CONCENPOINT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)
  L132:
    >   ```
    >   ```
    >   ADD VPNINSTAF: VRFNAME="vpn_3gpp_aaa",AFTYPE=ipv4uni;
    >   ```
    > 4. 配置S6b接口Diameter应用集中点模式。

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - [**ADD UPLIST4RDS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)
    > - [**ADD L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    > - **[**ADD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)

**md：`WSFD-011306/配置到AAA Server的数据（单平面+静态路由+BFD组网）_32044985.md`**
- 数据规划表（该命令的参数行）：
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | VPN实例名称 (VRFNAME) | vpn_pdn<br>vpn_aaa | 已配置数据中获取 | 已通过<br>[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)<br>命令进行配置，可以使用<br>**[**LST L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/查询L3VPN实例（LST L3VPNINST）_49961238.md)**<br>进行查询 |
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 地址族类型 (AFTYPE) | ipv4uni | 本端规划 | - |
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 路由标识（VRFRD） | 100:1<br>200:1 | 本端规划 | - |
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 实例的标签分配模式 (VRFLABELMODE) | perRoute | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF: VRFNAME ="vpn_pdn",AFTYPE=ipv4uni,VRFRD="100:1", VRFLABELMODE=perRoute;`
  `ADD VPNINSTAF: VRFNAME="vpn_aaa", AFTYPE=ipv4uni, VRFRD="200:1", VRFLABELMODE=perRoute;`
- 操作步骤上下文（±2 行原文）：
  L90:
    > 3. 创建L3VPN实例。
    >   [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 创建VPN实例。
    >   [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
  L141:
    > 
    > ```
    > ADD VPNINSTAF: VRFNAME ="vpn_pdn",AFTYPE=ipv4uni,VRFRD="100:1", VRFLABELMODE=perRoute;
    > ```
    > 
  L151:
    > 
    > ```
    > ADD VPNINSTAF: VRFNAME="vpn_aaa", AFTYPE=ipv4uni, VRFRD="200:1", VRFLABELMODE=perRoute;
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（双平面+OSPF动态路由+BFD组网 ）_31879931.md`**
- 数据规划表（该命令的参数行）：
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | VPN实例名称 (VRFNAME) | vpn_pdn | 已配置数据中获取 | 已通过<br>[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)<br>命令进行配置，可以使用<br>**[**LST L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/查询L3VPN实例（LST L3VPNINST）_49961238.md)**<br>进行查询 |
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 地址族类型 (AFTYPE) | ipv4uni | 本端规划 | - |
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 实例的标签分配模式 (VRFLABELMODE) | perRoute | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF: VRFNAME="vpn_pdn", AFTYPE=ipv4uni, VRFLABELMODE=perRoute;`
- 操作步骤上下文（±2 行原文）：
  L92:
    > 3. 创建L3VPN实例。
    >   [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 创建VPN实例。
    >   [**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
  L141:
    > 
    > ```
    > ADD VPNINSTAF: VRFNAME="vpn_pdn", AFTYPE=ipv4uni, VRFLABELMODE=perRoute;
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（带内组网GRE VPN）_32723577.md`**
- 数据规划表（该命令的参数行）：
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | VPN实例名称 (VRFNAME) | vpn_enterprise<br>vpn_tunnel | 已配置数据中获取 | 已通过<br>[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)<br>命令进行配置，可以使用<br>**[**LST L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/查询L3VPN实例（LST L3VPNINST）_49961238.md)**<br>进行查询。 |
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 地址族类型 (AFTYPE) | ipv4uni | 本端规划 | - |
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 实例的标签分配模式 (VRFLABELMODE) | perRoute | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF: VRFNAME ="vpn_enterprise",AFTYPE=ipv4uni;`
  `ADD VPNINSTAF: VRFNAME ="vpn_tunnel",AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L107:
    > 3. 创建L3VPN实例。
    >   [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 创建GRE隧道。
    >     a. 创建Loopback接口。
  L173:
    > 
    > ```
    > ADD VPNINSTAF: VRFNAME ="vpn_enterprise",AFTYPE=ipv4uni;
    > ```
    > 
  L181:
    > 
    > ```
    > ADD VPNINSTAF: VRFNAME ="vpn_tunnel",AFTYPE=ipv4uni;
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（带外组网GRE VPN）_32050904.md`**
- 数据规划表（该命令的参数行）：
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | VPN实例名称 (VRFNAME) | vpn_enterprise<br>vpn_tunnel<br>vpn_aaa | 已配置数据中获取 | 已通过<br>[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)<br>命令进行配置，可以使用<br>**[LST L3VPNINST](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/查询L3VPN实例（LST L3VPNINST）_49961238.md)**<br>进行查询。 |
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 地址族类型 (AFTYPE) | ipv4uni | 本端规划 | - |
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 路由标识（VRFRD） | 200:1 | 本端规划 | - |
  | **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 实例的标签分配模式 (VRFLABELMODE) | perRoute | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF: VRFNAME ="vpn_enterprise",AFTYPE=ipv4uni;`
  `ADD VPNINSTAF: VRFNAME ="vpn_tunnel",AFTYPE=ipv4uni;`
  `ADD VPNINSTAF:VRFNAME="vpn_aaa",AFTYPE=ipv4uni,VRFRD="200:1";`
- 操作步骤上下文（±2 行原文）：
  L107:
    > 3. 创建L3VPN实例。
    >   [**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 创建GRE隧道。
    >     a. 创建Loopback接口。
  L174:
    > 
    > ```
    > ADD VPNINSTAF: VRFNAME ="vpn_enterprise",AFTYPE=ipv4uni;
    > ```
    > 
  L182:
    > 
    > ```
    > ADD VPNINSTAF: VRFNAME ="vpn_tunnel",AFTYPE=ipv4uni;
    > ```
    > 

### WSFD-104004

**md：`WSFD-104004/WSFD-104004 IPv6前缀代理参考信息_76459529.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - **[**MOD L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/修改L3VPN实例（MOD L3VPNINST）_00840733.md)**
    > - **[**LST L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/查询L3VPN实例（LST L3VPNINST）_49961238.md)**
    > - **[**ADD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > - **[**RMV VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/删除L3VPN实例地址族（RMV VPNINSTAF）_00440685.md)**
    > - **[**MOD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/修改L3VPN实例地址族（MOD VPNINSTAF）_49961066.md)**

**md：`WSFD-104004/激活IPv6前缀代理_76459527.md`**
- 数据规划表（该命令的参数行）：
  | **[**ADD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | VPN实例名称（VRFNAME） | vpn1 | 已配置数据中获取 | 已通过<br>**[**ADD L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)**<br>命令配置，可以使用<br>**[**LST L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/查询L3VPN实例（LST L3VPNINST）_49961238.md)**<br>命令进行查询。 |
  | **[**ADD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)** | 地址族类型（AFTYPE） | ipv6uni | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF: VRFNAME="vpn1", AFTYPE=ipv6uni;`
- 操作步骤上下文（±2 行原文）：
  L51:
    >     b. 使能IPv6地址族。
    >       **[**ADD L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)**
    >       **[**ADD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    >     c. 配置路由标识符。
    >       **[**MOD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/修改L3VPN实例地址族（MOD VPNINSTAF）_49961066.md)**
  L88:
    > : VPNINSTANCE="vpn1";
    > ADD L3VPNINST: VRFNAME="vpn1";
    > ADD VPNINSTAF: VRFNAME="vpn1", AFTYPE=ipv6uni;
    > MOD VPNINSTAF: VRFNAME="vpn1", AFTYPE=ipv6uni, VRFRD="65512:2";
    > ```

### WSFD-104508

**md：`WSFD-104508/配置Gx over SCTP功能_30442391.md`**
- 操作步骤上下文（±2 行原文）：
  L82:
    >   **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 创建VPN实例。
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 配置SCTP本端端点。
    >   **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**

**md：`WSFD-104508/配置Gy over SCTP功能_30602207.md`**
- 操作步骤上下文（±2 行原文）：
  L79:
    >   **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    > 3. 创建VPN实例。
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 配置SCTP本端端点。
    >   **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**

### WSFD-011201

**md：`WSFD-011201/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md`**
- 数据规划表（该命令的参数行）：
  | **ADD VPNINSTAF** | VPN实例名称（VRFNAME） | vpn_ga | 已配置数据中获取 | 设置指定VPN实例下的地址族。 |
  | **ADD VPNINSTAF** | 地址族类型（AFTYPE） | ipv4uni | 本端规划 | 设置指定VPN实例下的地址族。 |
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vpn_ga", AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L121:
    >   ```
    >   ADD L3VPNINST: VRFNAME="vpn_ga";
    >   ADD VPNINSTAF:VRFNAME="vpn_ga", AFTYPE=ipv4uni;
    >   MOD VPNINSTAF:VRFNAME="vpn_ga", AFTYPE=ipv4uni, VRFRD="1050:1";
    >   ```

### WSFD-109001

**md：`WSFD-109001/配置到OCS的数据(静态路由+BFD组网)_95923542.md`**
- 数据规划表（该命令的参数行）：
  | **ADD VPNINSTAF** | VPN实例名称（VRFNAME） | vpn_gy | 已配置数据中获取 | VPN实例。 |
  | **ADD VPNINSTAF** | 地址族类型（AFTYPE） | ipv4uni | 本端规划 | VPN实例。 |
- 任务示例脚本（该命令行）：
  `ADD VPNINSTAF:VRFNAME="vpn_gy", AFTYPE=ipv4uni;`
- 操作步骤上下文（±2 行原文）：
  L144:
    >   ```
    >   ADD L3VPNINST: VRFNAME="vpn_gy";
    >   ADD VPNINSTAF:VRFNAME="vpn_gy", AFTYPE=ipv4uni;
    >   MOD VPNINSTAF:VRFNAME="vpn_gy", AFTYPE=ipv4uni, VRFRD="2050:1";
    >   ```

## ④ 自动比对
- 命令真相参数（11）：['AFTYPE', 'EXPLYADDERTFIRST', 'EXPOLICYNAME', 'FRRENABLE', 'IMPOLICYNAME', 'LOCALCROSSNHPMOD', 'TNLPOLICYNAME', 'VRFLABEL', 'VRFLABELMODE', 'VRFNAME', 'VRFRD']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 7, '本端规划': 13}（多值→atom 应考虑 decision_driven）
