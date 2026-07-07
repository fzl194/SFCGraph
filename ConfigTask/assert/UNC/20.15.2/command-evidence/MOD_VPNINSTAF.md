# 命令证据包：MOD VPNINSTAF
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/修改L3VPN实例地址族（MOD VPNINSTAF）_49961066.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：![](修改L3VPN实例地址族（MOD VPNINSTAF）_49961066.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会导致此VPN实例地址族下的配置和此VPN实例在BGP中的相关配置被删除，请谨慎使用并联系华为技术支持协助操作。

该命令用于修改设备上VPN实例下配置的地址族参数，例如修改VPN实例地址族下的路由标识符RD、应用策略等。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令删除RD会导致此VPN实例地址族下的配置和此VPN实例在BGP中的相关配置被删除
- 配置该命令前，需要对应的VPN实例地址族已创建。
- 不能修改VPN实例__mpp_vpn_inner__、__mpp_vpn_inner_server__的配置。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| VRFNAME | VPN实例名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。 |
| AFTYPE | 地址族类型 | local_planned | required | 无 | 枚举类型。 |
| VRFRD | 路由标识 | global_planned | optional | 无 | 字符串类型，输入长度范围为3～21。 |
| IMPOLICYNAME | 引入路由策略名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～200。 |
| LOCALCROSSNHPMOD | 可更改本地交叉下一跳 | local_planned | optional | 无 | 布尔类型，输入格式为“TRUE”或者“FALSE”。 |
| EXPOLICYNAME | 发布路由策略名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～200。 |
| EXPLYADDERTFIRST | 路由上送时首先添加ERT | local_planned | optional | 无 | 布尔类型，输入格式为“TRUE”或者“FALSE”。 |
| VRFLABELMODE | 实例的标签分配模式 | local_planned | optional | 无 | 枚举类型。 |
| VRFLABEL | 实例的标签值 | local_planned | conditional | 无 | 整数类型，取值范围为16～32767。 |
| TNLPOLICYNAME | 隧道策略名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～39。 |
| FRRENABLE | FRR使能 | local_planned | optional | 无 | 布尔类型，输入格式为“TRUE”或者“FALSE”。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-104004

**md：`WSFD-104004/WSFD-104004 IPv6前缀代理参考信息_76459529.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - **[**ADD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > - **[**RMV VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/删除L3VPN实例地址族（RMV VPNINSTAF）_00440685.md)**
    > - **[**MOD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/修改L3VPN实例地址族（MOD VPNINSTAF）_49961066.md)**
    > - **[**LST VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/查询L3VPN实例地址族（LST VPNINSTAF）_50121422.md)**
    > - [**ADD ADDRPOOL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池管理/增加地址池（ADD ADDRPOOL）_09653289.md)

**md：`WSFD-104004/激活IPv6前缀代理_76459527.md`**
- 数据规划表（该命令的参数行）：
  | **[**MOD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/修改L3VPN实例地址族（MOD VPNINSTAF）_49961066.md)** | VPN实例名称（VRFNAME） | vpn1 | 已配置数据中获取 | 已通过<br>**[**ADD L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)**<br>命令配置，可以使用<br>**[**LST L3VPNINST**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/查询L3VPN实例（LST L3VPNINST）_49961238.md)**<br>命令进行查询。 |
  | **[**MOD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/修改L3VPN实例地址族（MOD VPNINSTAF）_49961066.md)** | 地址族类型（AFTYPE） | ipv6uni | 已配置数据中获取 | - |
  | **[**MOD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/修改L3VPN实例地址族（MOD VPNINSTAF）_49961066.md)** | 路由标识（VRFRD） | 65512:2 | 本端规划 | - |
- 任务示例脚本（该命令行）：
  `MOD VPNINSTAF: VRFNAME="vpn1", AFTYPE=ipv6uni, VRFRD="65512:2";`
- 操作步骤上下文（±2 行原文）：
  L53:
    >       **[**ADD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    >     c. 配置路由标识符。
    >       **[**MOD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/修改L3VPN实例地址族（MOD VPNINSTAF）_49961066.md)**
    > 4. 配置分配IPv6代理前缀。
    >     a. 配置IPv6地址前缀名和IPv6前缀关联的VPN实例。
  L89:
    > ADD L3VPNINST: VRFNAME="vpn1";
    > ADD VPNINSTAF: VRFNAME="vpn1", AFTYPE=ipv6uni;
    > MOD VPNINSTAF: VRFNAME="vpn1", AFTYPE=ipv6uni, VRFRD="65512:2";
    > ```
    > 

### WSFD-011201

**md：`WSFD-011201/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md`**
- 数据规划表（该命令的参数行）：
  | **MOD VPNINSTAF** | VPN实例名称（VRFNAME） | vpn_ga | 已配置数据中获取 | RD（Route Distinguisher）用来唯一标识一个VPN。 |
  | **MOD VPNINSTAF** | 地址族类型（AFTYPE） | ipv4uni | 全网规划 | RD（Route Distinguisher）用来唯一标识一个VPN。 |
  | **MOD VPNINSTAF** | 路由标识（VRFRD） | 1050:1 | 全网规划 | RD（Route Distinguisher）用来唯一标识一个VPN。 |
- 任务示例脚本（该命令行）：
  `MOD VPNINSTAF:VRFNAME="vpn_ga", AFTYPE=ipv4uni, VRFRD="1050:1";`
- 操作步骤上下文（±2 行原文）：
  L122:
    >   ADD L3VPNINST: VRFNAME="vpn_ga";
    >   ADD VPNINSTAF:VRFNAME="vpn_ga", AFTYPE=ipv4uni;
    >   MOD VPNINSTAF:VRFNAME="vpn_ga", AFTYPE=ipv4uni, VRFRD="1050:1";
    >   ```
    > 3. 创建VPN实例。

### WSFD-109001

**md：`WSFD-109001/配置到OCS的数据(静态路由+BFD组网)_95923542.md`**
- 数据规划表（该命令的参数行）：
  | **MOD VPNINSTAF** | VPN实例名称（VRFNAME） | vpn_gy | 已配置数据中获取 | 修改设备上VPN实例下配置的地址族参数。<br>RD（Route Distinguisher）用来唯一标识一个VPN。 |
  | **MOD VPNINSTAF** | 地址族类型（AFTYPE） | ipv4uni | 已配置数据中获取 | 修改设备上VPN实例下配置的地址族参数。<br>RD（Route Distinguisher）用来唯一标识一个VPN。 |
  | **MOD VPNINSTAF** | 路由标识（VRFRD） | 2050:1 | 全网规划 | 修改设备上VPN实例下配置的地址族参数。<br>RD（Route Distinguisher）用来唯一标识一个VPN。 |
- 任务示例脚本（该命令行）：
  `MOD VPNINSTAF:VRFNAME="vpn_gy", AFTYPE=ipv4uni, VRFRD="2050:1";`
- 操作步骤上下文（±2 行原文）：
  L145:
    >   ADD L3VPNINST: VRFNAME="vpn_gy";
    >   ADD VPNINSTAF:VRFNAME="vpn_gy", AFTYPE=ipv4uni;
    >   MOD VPNINSTAF:VRFNAME="vpn_gy", AFTYPE=ipv4uni, VRFRD="2050:1";
    >   ```
    > 4. 配置Gy接口Diameter应用集中点模式。

## ④ 自动比对
- 命令真相参数（11）：['AFTYPE', 'EXPLYADDERTFIRST', 'EXPOLICYNAME', 'FRRENABLE', 'IMPOLICYNAME', 'LOCALCROSSNHPMOD', 'TNLPOLICYNAME', 'VRFLABEL', 'VRFLABELMODE', 'VRFNAME', 'VRFRD']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 5, '本端规划': 1, '全网规划': 3}（多值→atom 应考虑 decision_driven）
