# 命令证据包：ADD SRROUTE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md`
> 用该命令的特性数：7

## ② 命令真相（mml_commands.jsonl）
**功能**：该命令用于添加IPv4静态路由。

静态路由是一种需要管理员手工配置的特殊路由。

当网络结构比较简单时，只需配置静态路由就可以使网络正常工作。当设备不能使用动态路由协议或者不能建立到达目的网络时，也可以使用静态路由。合理的静态路由可以改进网络性能，并为重要业务保证带宽。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为100000。
- 添加该静态路由时，要保证该路由未添加过。
- 不能在VPN实例__mpp_vpn_inner__和__mpp_vpn_inner_server__下添加默认静态路由。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| AFTYPE | 地址族 | local_planned | required | 无 | 枚举类型。 |
| PREFIX | 路由前缀 | local_planned | required | 无 | IPv4地址类型。 |
| MASKLENGTH | 路由掩码长度 | local_planned | required | 无 | 整数类型，取值范围为0～32。 |
| VRFNAME | VPN实例名称 | local_planned | optional | _public_ | 字符串类型，输入长度范围为1～31。 |
| DESTVRFNAME | 下一跳VPN名字 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。 |
| IFNAME | 路由出接口名字 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| NEXTHOP | 路由下一跳 | local_planned | optional | 无 | IPv4地址类型。 |
| PREFERENCE | 路由优先级 | local_planned | optional | 60 | 整数类型，取值范围为1～255。 |
| BFDENABLE | 动态BFD使能标识 | local_planned | optional | FALSE | 布尔类型，输入格式为“TRUE”或者“FALSE”。 |
| SESSIONNAME | 静态BFD会话名 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～64。 |
| TAG | 路由Tag值 | local_planned | optional | 0 | 整数类型，取值范围为0～4294967295。 |
| DESCRIPTION | 路由描述 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～35。 |
| DHCPENABLE | DHCP使能标识 | local_planned | optional | FALSE | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### IPFD-015002

**md：`IPFD-015002/激活支持GRE_06422610.md`**
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.202",MASKLENGTH=24,IFNAME="Tunnel1";`
  `ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.201",MASKLENGTH=24,IFNAME="Tunnel1";`
- 操作步骤上下文（±2 行原文）：
  L61:
    > 3. 配置隧道间静态路由
    >   在 “MML命令行-UNC” 窗口上执行：
    >   **[**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)** : AFTYPE=地址族, PREFIX="路由前缀", MASKLENGTH=路由掩码长度, IFNAME="路由接口名字";
    > 4. （可选）当配置GRE隧道时，使能隧道端到端校验功能。
    >   在 “MML命令行-UNC” 窗口上执行：
  L166:
    > 
    > ```
    > ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.202",MASKLENGTH=24,IFNAME="Tunnel1";
    > ```
    > 
  L212:
    > 
    > ```
    > ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.201",MASKLENGTH=24,IFNAME="Tunnel1";
    > ```
    > 

### IPFD-016000

**md：`IPFD-016000/激活IPsec功能（GRE over IPsec）_78985535.md`**
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.101.21",MASKLENGTH=32,IFNAME="Invalid0",NEXTHOP="192.168.2.2",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.105.224",MASKLENGTH=32,IFNAME="Tunnel2",NEXTHOP="10.102.101.21",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,IFNAME="Tunnel1",NEXTHOP="192.168.4.1",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.101.25",MASKLENGTH=32,IFNAME="Invalid0",NEXTHOP="192.168.1.2",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.105.238",MASKLENGTH=32,IFNAME="Tunnel2",NEXTHOP="10.102.101.25",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,IFNAME="Tunnel1",NEXTHOP="192.168.3.1",PREFERENCE=60,BFDENABLE=FALSE;`
- 操作步骤上下文（±2 行原文）：
  L208:
    >   [**SET IKEGLOBALCONFIG**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md)
    > 10. 配置静态路由用于IPsec引流。
    >   [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0278985535)
  L393:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.101.21",MASKLENGTH=32,IFNAME="Invalid0",NEXTHOP="192.168.2.2",PREFERENCE=60,BFDENABLE=FALSE;
    > ```
    > 
  L397:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.105.224",MASKLENGTH=32,IFNAME="Tunnel2",NEXTHOP="10.102.101.21",PREFERENCE=60,BFDENABLE=FALSE;
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（IPv4 IPsec主备隧道）_88744738.md`**
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.2",IFNAME="Tunnel17";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.2",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.169.2";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.3",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.164.4";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.1",IFNAME="Tunnel17";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.1",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.163.2",IFNAME="Invalid0";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.1",IFNAME="Tunnel17";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.1",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.163.2",IFNAME="Invalid0";`
- 操作步骤上下文（±2 行原文）：
  L159:
    >       [**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)
    >     d. 配置到达目的网络的静态路由，并与VPN实例绑定。
    >       [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
    > 2. 创建IPsec微服务的VPN和IPsec隧道接口。
    >     a. 创建VPN实例。
  L264:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.2",IFNAME="Tunnel17";
    > ```
    > 
  L268:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.2",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.169.2";
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（OSPF over IPsec）_90949389.md`**
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.105.224",MASKLENGTH=32,NEXTHOP="192.168.2.1",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.105.238",MASKLENGTH=32,NEXTHOP="192.168.1.1",PREFERENCE=60,BFDENABLE=FALSE;`
- 操作步骤上下文（±2 行原文）：
  L214:
    >   [**SET IKEGLOBALCONFIG**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md)
    > 10. 配置静态路由用于IPsec引流。
    >   [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
    > 11. 在VNRS上配置OSPF。
    >   **[ADD OSPF](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/OSPF管理/OSPF进程配置/创建OSPF进程配置（ADD OSPF）_00866089.md)**
  L407:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.105.224",MASKLENGTH=32,NEXTHOP="192.168.2.1",PREFERENCE=60,BFDENABLE=FALSE;
    > ```
    > 
  L609:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.105.238",MASKLENGTH=32,NEXTHOP="192.168.1.1",PREFERENCE=60,BFDENABLE=FALSE;
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（多Sequence的IPsec策略）_78985536.md`**
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.2",IFNAME="Tunnel10";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.2",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.163.2",IFNAME="Invalid0";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.3.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.3",IFNAME="Tunnel10";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.3",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.163.2",IFNAME="Invalid0";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.1",IFNAME="Tunnel10";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.1",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.163.2",IFNAME="Invalid0";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.1",IFNAME="Tunnel10";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.1",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.170.2",IFNAME="Invalid0";`
- 操作步骤上下文（±2 行原文）：
  L164:
    >       [**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)
    >     d. 配置到达目的网络的静态路由，并与VPN实例绑定。
    >       [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
    > 2. 创建IPsec微服务的VPN和IPsec隧道接口。
    >     a. 创建VPN实例。
  L269:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.2",IFNAME="Tunnel10";
    > ```
    > 
  L273:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.2",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.163.2",IFNAME="Invalid0";
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（指定本端接口建立IPsec隧道）_78985537.md`**
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,VRFNAME="vrf1",IFNAME="Tunnel2",NEXTHOP="10.3.4.3",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.3.4.3",MASKLENGTH=32,VRFNAME="vrf1",IFNAME="Ethernet66/0/3",NEXTHOP="192.168.2.2",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,VRFNAME="vpn1",IFNAME="Tunnel2",NEXTHOP="10.3.3.3",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.3.3.3",MASKLENGTH=32,VRFNAME="vpn1",IFNAME="Ethernet66/0/3",NEXTHOP="192.168.1.2",PREFERENCE=60,BFDENABLE=FALSE;`
- 操作步骤上下文（±2 行原文）：
  L180:
    >       [**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)
    >     d. 配置静态有用于IPsec引流。
    >       [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
    > 2. 创建IPsec微服务的VPN和IPsec隧道接口、Loopback接口。
    >     a. 创建VPN实例。
  L295:
    > 
    > ```
    > ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,VRFNAME="vrf1",IFNAME="Tunnel2",NEXTHOP="10.3.4.3",PREFERENCE=60,BFDENABLE=FALSE;
    > ```
    > 
  L299:
    > 
    > ```
    > ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.3.4.3",MASKLENGTH=32,VRFNAME="vrf1",IFNAME="Ethernet66/0/3",NEXTHOP="192.168.2.2",PREFERENCE=60,BFDENABLE=FALSE;
    > ```
    > 

**md：`IPFD-016000/激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md`**
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.2",IFNAME="Tunnel10";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.2",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.169.2",IFNAME="Invalid0";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.1",IFNAME="Tunnel10";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.1",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.163.2",IFNAME="Invalid0";`
- 操作步骤上下文（±2 行原文）：
  L154:
    >       [**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)
    >     d. 配置到达目的网络的静态路由，并与VPN实例绑定。
    >       [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
    > 2. 创建IPsec微服务的VPN和IPsec隧道接口。
    >     a. 创建VPN实例。
  L259:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.2",IFNAME="Tunnel10";
    > ```
    > 
  L263:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.2",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.169.2",IFNAME="Invalid0";
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（GRE over IPsec）_53928160.md`**
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.101.21",MASKLENGTH=32,IFNAME="Invalid0",NEXTHOP="192.168.2.2",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.105.224",MASKLENGTH=32,IFNAME="Tunnel2",NEXTHOP="10.102.101.21",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,IFNAME="Tunnel1",NEXTHOP="192.168.4.1",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.101.25",MASKLENGTH=32,IFNAME="Invalid0",NEXTHOP="192.168.1.2",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.105.238",MASKLENGTH=32,IFNAME="Tunnel2",NEXTHOP="10.102.101.25",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,IFNAME="Tunnel1",NEXTHOP="192.168.3.1",PREFERENCE=60,BFDENABLE=FALSE;`
- 操作步骤上下文（±2 行原文）：
  L208:
    >   [**SET IKEGLOBALCONFIG**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IPSEC功能管理/IP服务/IP安全管理/互联网密钥交换/IKE全局配置/设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.md)
    > 11. 配置静态路由用于IPsec引流。
    >   [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0000001453928160)
  L399:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.101.21",MASKLENGTH=32,IFNAME="Invalid0",NEXTHOP="192.168.2.2",PREFERENCE=60,BFDENABLE=FALSE;
    > ```
    > 
  L403:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.105.224",MASKLENGTH=32,IFNAME="Tunnel2",NEXTHOP="10.102.101.21",PREFERENCE=60,BFDENABLE=FALSE;
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（多Sequence的IPsec策略）_03408185.md`**
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.2",IFNAME="Tunnel10";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.2",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.163.2",IFNAME="Invalid0";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.3.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.3",IFNAME="Tunnel10";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.3",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.163.2",IFNAME="Invalid0";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.1",IFNAME="Tunnel10";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.1",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.163.2",IFNAME="Invalid0";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.1",IFNAME="Tunnel10";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.1",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.170.2",IFNAME="Invalid0";`
- 操作步骤上下文（±2 行原文）：
  L166:
    >       [**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)
    >     d. 配置到达目的网络的静态路由，并与VPN实例绑定。
    >       [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
    > 2. 创建IPsec微服务的VPN和IPsec隧道接口。
    >     a. 创建VPN实例。
  L269:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.2",IFNAME="Tunnel10";
    > ```
    > 
  L273:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.2",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.163.2",IFNAME="Invalid0";
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（指定本端接口建立IPsec隧道）_03567841.md`**
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,VRFNAME="vrf1",IFNAME="Tunnel2",NEXTHOP="10.3.4.3",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.3.4.3",MASKLENGTH=32,VRFNAME="vrf1",IFNAME="Ethernet66/0/3",NEXTHOP="192.168.2.2",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,VRFNAME="vpn1",IFNAME="Tunnel2",NEXTHOP="10.3.3.3",PREFERENCE=60,BFDENABLE=FALSE;`
  `ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.3.3.3",MASKLENGTH=32,VRFNAME="vpn1",IFNAME="Ethernet66/0/3",NEXTHOP="192.168.1.2",PREFERENCE=60,BFDENABLE=FALSE;`
- 操作步骤上下文（±2 行原文）：
  L182:
    >       [**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)
    >     d. 配置静态有用于IPsec引流。
    >       [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
    > 2. 创建IPsec微服务的VPN和IPsec隧道接口、Loopback接口。
    >     a. 创建VPN实例。
  L295:
    > 
    > ```
    > ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,VRFNAME="vrf1",IFNAME="Tunnel2",NEXTHOP="10.3.4.3",PREFERENCE=60,BFDENABLE=FALSE;
    > ```
    > 
  L299:
    > 
    > ```
    > ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.3.4.3",MASKLENGTH=32,VRFNAME="vrf1",IFNAME="Ethernet66/0/3",NEXTHOP="192.168.2.2",PREFERENCE=60,BFDENABLE=FALSE;
    > ```
    > 

**md：`IPFD-016000/激活国密IPsec支持IKEv1功能（普通IPv4 IPsec隧道）_03728909.md`**
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.2",IFNAME="Tunnel10";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.2",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.169.2",IFNAME="Invalid0";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.1.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.1",IFNAME="Tunnel10";`
  `ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.1",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.163.2",IFNAME="Invalid0";`
- 操作步骤上下文（±2 行原文）：
  L154:
    >       [**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)
    >     d. 配置到达目的网络的静态路由，并与VPN实例绑定。
    >       [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
    > 2. 创建IPsec微服务的VPN和IPsec隧道接口。
    >     a. 创建VPN实例。
  L257:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.2",IFNAME="Tunnel10";
    > ```
    > 
  L261:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.2",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.169.2",IFNAME="Invalid0";
    > ```
    > 

### WSFD-010102

**md：`WSFD-010102/配置到3GPP AAA Server的数据_80511835.md`**
- 任务示例脚本（该命令行）：
  `ADD SRROUTE: VRFNAME="vpn_3gpp_aaa",AFTYPE=ipv4unicast,PREFIX="0.0.0.0",MASKLENGTH=32,DESTVRFNAME="vpn_3gpp_aaa",IFNAME="Invalid0",NEXTHOP="10.3.37.81";`
- 操作步骤上下文（±2 行原文）：
  L81:
    >   [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > 6. 配置到3GPP AAA Server的VPN缺省路由。
    >   [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
    > 7. 如果通过SCTP方式与3GPP AAA Server建立链接，需要配置SCTP端点信息。
    >   **[ADD SCTPENDPOINT](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**
  L144:
    > 6. 配置到3GPP AAA Server的VPN缺省路由。
    >   ```
    >   ADD SRROUTE: VRFNAME="vpn_3gpp_aaa",AFTYPE=ipv4unicast,PREFIX="0.0.0.0",MASKLENGTH=32,DESTVRFNAME="vpn_3gpp_aaa",IFNAME="Invalid0",NEXTHOP="10.3.37.81";
    >   ```
    > 7. 配置SCTP端点信息。

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > - **[**ADD IFIPV4ADDRESS**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)**
    > - **[**ADD GRETUNNEL**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/GRE管理/GRE隧道/增加GRE隧道（ADD GRETUNNEL）_00841729.md)**
    > - **[**ADD SRROUTE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)**
    > - **[**SET IFIPV6ENABLE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6使能/修改接口IPv6使能（SET IFIPV6ENABLE）_00601329.md)**
    > - **[**ADD IFIPV6ADDRESS**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6地址/增加接口IPv6地址（ADD IFIPV6ADDRESS）_49961222.md)**

**md：`WSFD-011306/配置到AAA Server的数据（带内组网GRE VPN）_32723577.md`**
- 数据规划表（该命令的参数行）：
  | **[**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)** | 地址族 (AFTYPE) | ipv4unicast | 固定取值 | - |
  | **[**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)** | 路由前缀 (PREFIX) | 10.10.1.202 | 全网规划 | - |
  | **[**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)** | 路由掩码长度 (MASKLENGTH) | 30 | 全网规划 | - |
  | **[**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)** | VPN实例名称 (VRFNAME) | vpn_enterprise | 已配置数据中获取 | 已通过<br>[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)<br>命令进行配置，可以使用<br>**[**LST L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/查询L3VPN实例（LST L3VPNINST）_49961238.md)**<br>进行查询。 |
  | **[**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)** | 路由出接口名字 (IFNAME) | Tunnel1 | 已配置数据中获取 | 已通过<br>**[**ADD GRETUNNEL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/GRE管理/GRE隧道/增加GRE隧道（ADD GRETUNNEL）_00841729.md)**<br>命令进行配置，可以使用<br>**[**LST GRETUNNEL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/GRE管理/GRE隧道/查询GRE隧道（LST GRETUNNEL）_49802638.md)**<br>进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.202",MASKLENGTH=30,VRFNAME="vpn_enterprise",IFNAME="Tunnel1";`
- 操作步骤上下文（±2 行原文）：
  L120:
    >       **[**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)**
    >     e. 配置静态路由。
    >       **[**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)**
    >   > **说明**
    >   > 如果需要一同配置IPv6的GRE隧道，则步骤b、d均需要先使用 **[**SET IFIPV6ENABLE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6使能/修改接口IPv6使能（SET IFIPV6ENABLE）_00601329.md)** 命令开启IPv6使能，再使用 **[**ADD IFIPV6ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6地址/增加接口IPv6地址（ADD IFIPV6ADDRESS）_49961222.md)** 命令配置IPv6地址，步骤e需要使用 **[**ADD SRROUTE6**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv6静态路由/增加IPv6静态路由（ADD SRROUTE6）_50280922.md)** 命令配置IPv6静态路由。
  L218:
    > 
    > ```
    > ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.202",MASKLENGTH=30,VRFNAME="vpn_enterprise",IFNAME="Tunnel1";
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（带外组网GRE VPN）_32050904.md`**
- 数据规划表（该命令的参数行）：
  | **[**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)** | 地址族 (AFTYPE) | ipv4unicast | 固定取值 | - |
  | **[**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)** | 路由前缀 (PREFIX) | 10.10.1.202 | 全网规划 | - |
  | **[**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)** | 路由掩码长度 (MASKLENGTH) | 30 | 全网规划 | - |
  | **[**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)** | VPN实例名称 (VRFNAME) | vpn_enterprise | 已配置数据中获取 | 已通过<br>[**ADD L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/增加L3VPN实例（ADD L3VPNINST）_49802446.md)<br>命令进行配置，可以使用<br>**[**LST L3VPNINST**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例/查询L3VPN实例（LST L3VPNINST）_49961238.md)**<br>进行查询。 |
  | **[**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)** | 路由出接口名字 (IFNAME) | Tunnel1 | 已配置数据中获取 | 已通过<br>**[**ADD GRETUNNEL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/GRE管理/GRE隧道/增加GRE隧道（ADD GRETUNNEL）_00841729.md)**<br>命令进行配置，可以使用<br>**[**LST GRETUNNEL**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/GRE管理/GRE隧道/查询GRE隧道（LST GRETUNNEL）_49802638.md)**<br>进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.202",MASKLENGTH=30,VRFNAME="vpn_enterprise",IFNAME="Tunnel1";`
- 操作步骤上下文（±2 行原文）：
  L120:
    >       **[**ADD IFIPV4ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv4地址/增加接口IPv4地址（ADD IFIPV4ADDRESS）_00865509.md)**
    >     e. 配置静态路由。
    >       **[**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)**
    >   > **说明**
    >   > 如果需要一同配置IPv6的GRE隧道，则步骤b、d均需要先使用 **[**SET IFIPV6ENABLE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6使能/修改接口IPv6使能（SET IFIPV6ENABLE）_00601329.md)** 命令开启IPv6使能，再使用 **[**ADD IFIPV6ADDRESS**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/接口管理/IPv6地址/增加接口IPv6地址（ADD IFIPV6ADDRESS）_49961222.md)** 命令配置IPv6地址，步骤e需要使用 **[**ADD SRROUTE6**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv6静态路由/增加IPv6静态路由（ADD SRROUTE6）_50280922.md)** 命令配置IPv6静态路由。
  L219:
    > 
    > ```
    > ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.202",MASKLENGTH=30,VRFNAME="vpn_enterprise",IFNAME="Tunnel1";
    > ```
    > 

### WSFD-104506

**md：`WSFD-104506/激活支持Direct Tunnel功能_26375780.md`**
- 任务示例脚本（该命令行）：
  `ADD SRROUTE:VRFNAME="_public_",AFTYPE=ipv4unicast,PREFIX="10.3.1.1",MASKLENGTH=32,DESTVRFNAME="_public_",NEXTHOP="10.4.1.1",IFNAME="NULL0";`
  `ADD SRROUTE:VRFNAME="_public_",AFTYPE=ipv4unicast,PREFIX="10.1.1.1",MASKLENGTH=32,DESTVRFNAME="_public_",NEXTHOP="10.4.1.1",IFNAME="NULL0";`
- 操作步骤上下文（±2 行原文）：
  L171:
    >             重复执行可以指定多个APN用户关闭Direct Tunnel功能。
    >             [**ADD APNNIDT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/Direct Tunnel管理/增加APNNI Direct Tunnel配置(ADD APNNIDT)_72345645.md)
    >     e. 两次执行 [**ADD SRROUTE**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md) ，分别配置到GGSN和到RNC的控制面路由。
    > 
    > ## [任务示例](#ZH-CN_OPI_0226375780)
  L203:
    > 
    > ```
    > ADD SRROUTE:VRFNAME="_public_",AFTYPE=ipv4unicast,PREFIX="10.3.1.1",MASKLENGTH=32,DESTVRFNAME="_public_",NEXTHOP="10.4.1.1",IFNAME="NULL0";
    > ADD SRROUTE:VRFNAME="_public_",AFTYPE=ipv4unicast,PREFIX="10.1.1.1",MASKLENGTH=32,DESTVRFNAME="_public_",NEXTHOP="10.4.1.1",IFNAME="NULL0";
    > ```
  L204:
    > ```
    > ADD SRROUTE:VRFNAME="_public_",AFTYPE=ipv4unicast,PREFIX="10.3.1.1",MASKLENGTH=32,DESTVRFNAME="_public_",NEXTHOP="10.4.1.1",IFNAME="NULL0";
    > ADD SRROUTE:VRFNAME="_public_",AFTYPE=ipv4unicast,PREFIX="10.1.1.1",MASKLENGTH=32,DESTVRFNAME="_public_",NEXTHOP="10.4.1.1",IFNAME="NULL0";
    > ```

### WSFD-011201

**md：`WSFD-011201/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md`**
- 数据规划表（该命令的参数行）：
  | **ADD SRROUTE** | VPN实例名称（VRFNAME） | vpn_ga | 已配置数据中获取 | 已在该配置任务中通过命令<br>**ADD L3VPNINST**<br>配置，可以使用命令<br>**LST L3VPNINST**<br>进行查询。 |
  | **ADD SRROUTE** | 地址族（AFTYPE） | ipv4unicast | 固定取值 | 目的IP地址和掩码都为0.0.0.0的静态路由为缺省路由。 |
  | **ADD SRROUTE** | 路由前缀（PREFIX） | 0.0.0.0 | 固定取值 | 目的IP地址和掩码都为0.0.0.0的静态路由为缺省路由。 |
  | **ADD SRROUTE** | 路由掩码长度（MASKLENGTH） | 0 | 固定取值 | 目的IP地址和掩码都为0.0.0.0的静态路由为缺省路由。 |
  | **ADD SRROUTE** | 路由下一跳（NEXTHOP） | 10.3.37.81 | 全网规划 | 到CG路由的下一跳IP地址。 |

### WSFD-109001

**md：`WSFD-109001/配置到OCS的数据(静态路由+BFD组网)_95923542.md`**
- 数据规划表（该命令的参数行）：
  | **ADD SRROUTE** | VPN实例名称（VRFNAME） | vpn_gy | 已配置数据中获取 | 已在该配置任务中通过命令<br>**ADD L3VPNINST**<br>配置，可以使用<br>**LST L3VPNINST**<br>命令进行查询。 |
  | **ADD SRROUTE** | 地址族（AFTYPE） | ipv4unicast | 固定取值 | 目的IP地址和掩码都为0.0.0.0的路由为缺省路由。 |
  | **ADD SRROUTE** | 路由前缀（PREFIX） | 0.0.0.0 | 固定取值 | 目的IP地址和掩码都为0.0.0.0的路由为缺省路由。 |
  | **ADD SRROUTE** | 路由掩码长度（MASKLENGTH） | 0 | 固定取值 | 目的IP地址和掩码都为0.0.0.0的路由为缺省路由。 |
  | **ADD SRROUTE** | 路由下一跳（NEXTHOP） | 10.3.37.81 | 全网规划 | 到OCS路由的下一跳IP地址。 |

## ④ 自动比对
- 命令真相参数（13）：['AFTYPE', 'BFDENABLE', 'DESCRIPTION', 'DESTVRFNAME', 'DHCPENABLE', 'IFNAME', 'MASKLENGTH', 'NEXTHOP', 'PREFERENCE', 'PREFIX', 'SESSIONNAME', 'TAG', 'VRFNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'固定取值': 8, '全网规划': 6, '已配置数据中获取': 6}（多值→atom 应考虑 decision_driven）
