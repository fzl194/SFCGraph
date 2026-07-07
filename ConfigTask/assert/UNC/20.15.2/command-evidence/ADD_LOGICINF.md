# 命令证据包：ADD LOGICINF
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md`
> 用该命令的特性数：9

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用于创建指定的逻辑接口。逻辑接口是指能够实现数据交换功能但物理上不存在，需要通过配置建立的接口。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为4096。
- 如果需要输入该命令的可选参数VPN实例名称（即逻辑接口与VPN绑定），则需要提前配置ADD VPNINST命令。如果用户没有对VPN实例进行配置，系统将会下发缺省VPN。
- 逻辑接口配置不支持在主备SMF之间自动同步，需要在主备SMF上分别配置。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| NAME | 逻辑接口名称 | global_planned | required | 无 | 字符串类型，输入长度范围为1～63。 |
| IPVERSION | 逻辑接口的IP版本 | global_planned | required | 无 | 枚举类型。 |
| IPV4ADDRESS1 | 逻辑接口的IPv4地址1 | global_planned | conditional | 无 | IPv4地址类型。采用点分十进制"X.X.X.X"格式。 |
| IPV4MASK1 | 逻辑接口的IPv4掩码1 | global_planned | conditional | 无 | IPv4地址类型。采用点分十进制"X.X.X.X"格式。 |
| IPV4ADDRESS2 | 逻辑接口的IPv4地址2 | global_planned | conditional | 无 | IPv4地址类型。采用点分十进制"X.X.X.X"格式。 |
| IPV4MASK2 | 逻辑接口的IPv4掩码2 | global_planned | conditional | 无 | IPv4地址类型。采用点分十进制"X.X.X.X"格式。 |
| IPV6ADDRESS1 | 逻辑接口的IPv6地址1 | global_planned | conditional | 无 | IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。 |
| VPNINSTANCE | VPN实例名称 | global_planned | conditional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，区分大小写。 |
| IPV6PREFIXLEN1 | IPv6前缀长度1 | global_planned | conditional | 无 | 整数类型，取值范围为128。 |
| IPV6ADDRESS2 | 逻辑接口的IPv6地址2 | global_planned | conditional | 无 | IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。 |
| IPV6PREFIXLEN2 | IPv6前缀长度2 | global_planned | conditional | 无 | 整数类型，取值范围为128。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-010102

**md：`WSFD-010102/配置到3GPP AAA Server的数据_80511835.md`**
- 任务示例脚本（该命令行）：
  `ADD LOGICINF:NAME="s6bif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="192.168.7.7",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_3gpp_aaa";`
- 操作步骤上下文（±2 行原文）：
  L79:
    >   [**SET CONCENPOINT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)
    > 5. 创建S6bif接口。
    >   [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > 6. 配置到3GPP AAA Server的VPN缺省路由。
    >   [**ADD SRROUTE**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/路由管理/静态路由管理/IPv4静态路由/增加IPv4静态路由（ADD SRROUTE）_49961498.md)
  L140:
    > 5. 创建S6bif接口。
    >   ```
    >   ADD LOGICINF:NAME="s6bif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="192.168.7.7",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_3gpp_aaa";
    >   ```
    > 6. 配置到3GPP AAA Server的VPN缺省路由。

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**SET CONCENPOINT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)
    > - [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > - [**ADD DIAMLOCINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > - [**ADD DIAMPEERADDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/服务器地址/增加Diameter对端地址（ADD DIAMPEERADDR）_09897257.md)

**md：`WSFD-109101/配置与PCRF对接数据_30805096.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口名称（NAME） | gxif1/0/0<br>gxif1/0/1 | 本端规划 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.10.1<br>10.8.10.2 | 全网规划 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | VPN实例名（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | 已通过命令<br>[**ADD VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口名称（NAME） | gxif1/0/0<br>gxif1/0/1 | 本端规划 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.10.1<br>10.8.10.2 | 全网规划 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 组级Gx逻辑接口。 |
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)<br>[**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) | VPN实例名（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | 已通过命令<br>[**ADD VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_gxif";`
  `ADD LOGICINF:NAME="gxif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_gxif";`
  `ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_gxif";`
  `ADD LOGICINF:NAME="gxif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_gxif";`
- 操作步骤上下文（±2 行原文）：
  L127:
    >       [**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    >     b. 配置Gx逻辑接口。
    >       [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    >   > **说明**
    >   > [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) 中的“IP地址+VPN实例名称”和 [**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) 命令中的“IP地址+VPN实例名称”必须一致。
  L129:
    >       [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    >   > **说明**
    >   > [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) 中的“IP地址+VPN实例名称”和 [**ADD LOGICIP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md) 命令中的“IP地址+VPN实例名称”必须一致。
    > 6. 配置GGSN/PGW-C的设备标识。
    >   [**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
  L213:
    >   ```
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1", VPNINSTNAME="vpn_gxif";
    >   ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_gxif";
    >   ```
    >   ```

**md：`WSFD-109101/调测到PCRF的数据_31422954.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | 逻辑接口名称（NAME） | gxif1/0/0<br>gxif1/0/1<br>gxif1/0/2 | 已配置数据中获取 | 取自<br>[配置与PCRF对接数据](../激活PCC基本功能/配置与PCRF对接数据_30805096.md)<br>中配置的数据。 |
- 操作步骤上下文（±2 行原文）：
  L154:
    >     b. 执行[**ADD DIAMLOCINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)和[**ADD DIAMCONNECTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/增加Diameter链路（ADD DIAMCONNECTION）_09897266.md)命令，按照规划数据重新配置GGSN/PGW-C的Gx口设备标识。
    >     c. **可选：**如果Gx接口IP与规划值不一致，请执行[**RMV LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/删除逻辑接口（RMV LOGICINF）_09896725.md)命令，删除原有配置。
    >     d. **可选：**执行[**ADD LOGICINF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)命令，按照规划数据重新配置GGSN/PGW-C的Gx接口IP数据。
    >     e. 再次执行[步骤 2](#ZH-CN_OPI_0231422954__stp1)，查看PCRF状态。
    >     - 如果检测PCRF状态正常，则GGSN/PGW-C和PCRF之间的链路互通调测结束。

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L21:
    > - **[**ADD VPNINSTAF**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > - [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
    > - **[ADD APNRDSCLIENTIP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/APN的Radius客户端地址属性/增加APN Radius Client IP接口（ADD APNRDSCLIENTIP）_09897362.md)**

**md：`WSFD-011306/配置到AAA Server的数据（单平面+静态路由+BFD组网）_32044985.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | giif1/0/0<br>giif1/0/1 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.20.1<br>10.8.20.2 | 全网规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_pdn<br>vpn_aaa | 已配置数据中获取 | 鉴权/计费AAA服务器所属的VPN实例名。已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";`
  `ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";`
- 操作步骤上下文（±2 行原文）：
  L95:
    > 5. 配置Gi逻辑接口。
    >   [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    >   **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 6. **可选：** 配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。
    >   **[ADD UPLIST4RDS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)**
  L167:
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_aaa";
    > ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";
    > ```
    > 
  L174:
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_aaa";
    > ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（双平面+OSPF动态路由+BFD组网 ）_31879931.md`**
- 数据规划表（该命令的参数行）：
  | **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | giif1/0/0<br>giif1/0/1 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.20.1<br>10.8.20.2 | 全网规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_pdn | 已配置数据中获取 | 鉴权/计费AAA服务器所属的VPN实例名。已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_pdn";`
  `ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_pdn";`
- 操作步骤上下文（±2 行原文）：
  L97:
    > 5. 配置Gi逻辑接口。
    >   [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    >   **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 6. **可选：** 配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。
    >   **[ADD UPLIST4RDS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)**
  L156:
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_pdn";
    > ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_pdn";
    > ```
    > 
  L163:
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_pdn";
    > ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_pdn";
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（带内组网GRE VPN）_32723577.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | giif1/0/0<br>giif1/0/1 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.20.1<br>10.8.20.2 | 全网规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_enterprise | 已配置数据中获取 | 鉴权AAA服务器所属的VPN实例名。<br>已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_enterprise";`
  `ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_enterprise";`
- 操作步骤上下文（±2 行原文）：
  L127:
    > 6. 配置Gi逻辑接口。
    >   [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    >   **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 7. **可选：** 配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。
    >   **[ADD UPLIST4RDS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)**
  L233:
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_pdn";
    > ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_enterprise";
    > ```
    > 
  L240:
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_pdn";
    > ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_enterprise";
    > ```
    > 

**md：`WSFD-011306/配置到AAA Server的数据（带外组网GRE VPN）_32050904.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | giif1/0/0<br>giif1/0/1 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.20.1<br>10.8.20.2 | 全网规划 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 配置使用的逻辑接口，其中“giif1/0/0”和“10.8.20.1”用于鉴权AAA服务器，“giif1/0/1”和“10.8.20.2”用于计费AAA服务器。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_aaa | 已配置数据中获取 | 鉴权AAA服务器所属的VPN实例名。已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";`
  `ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";`
- 操作步骤上下文（±2 行原文）：
  L127:
    > 6. 配置Gi逻辑接口。
    >   [**ADD LOGICIP**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    >   **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 7. **可选：** 配置鉴权或计费AAA服务器使用的PGW-U/UPF列表。
    >   **[ADD UPLIST4RDS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)**
  L250:
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_pdn";
    > ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";
    > ```
    > 
  L257:
    > ```
    > ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_pdn";
    > ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";
    > ```
    > 

### WSFD-104508

**md：`WSFD-104508/WSFD-104508 SCTP参考信息_29341126.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > - [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
    > - **[ADD SCTPTEMPLATE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP模板/增加SCTP模板（ADD SCTPTEMPLATE）_09897332.md)**

**md：`WSFD-104508/配置Gx over SCTP功能_30442391.md`**
- 数据规划表（该命令的参数行）：
  | **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | gxif1/0/0 | 本端规划 | 其中10.8.20.1为主IP地址，10.8.20.2为从IP地址。<br>逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1(IPV4ADDRESS1) | 10.8.20.1 | 全网规划 | 其中10.8.20.1为主IP地址，10.8.20.2为从IP地址。<br>逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 其中10.8.20.1为主IP地址，10.8.20.2为从IP地址。<br>逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1(IPV4MASK1) | 255.255.255.255 | 固定取值 | 其中10.8.20.1为主IP地址，10.8.20.2为从IP地址。<br>逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址2（IPV4ADDRESS2） | 10.8.20.2 | 全网规划 | 其中10.8.20.1为主IP地址，10.8.20.2为从IP地址。<br>逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码2(IPV4MASK2) | 255.255.255.255 | 固定取值 | 其中10.8.20.1为主IP地址，10.8.20.2为从IP地址。<br>逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | 接口绑定的VPN实例已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.20.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gxif";`
- 操作步骤上下文（±2 行原文）：
  L84:
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 配置SCTP本端端点。
    >   **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    >   > **说明**
    >   > 在对端的端口号为奇数时，可以通过 **[MOD DIAMCONNECTION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/修改Diameter链路（MOD DIAMCONNECTION）_09897267.md)** 命令设置 “REVERSEIP” 为 “ENABLE” 来颠倒本端的主从IP地址，与对端建立偶联，即本端配置的从IP作为偶联的主IP，本端配置的主IP作为偶联的从IP。
  L152:
    > ```
    > ADD VPNINST: VPNINSTANCE="vpn_gxif";
    > ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.20.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gxif";
    > ```
    > 

**md：`WSFD-104508/配置Gy over SCTP功能_30602207.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | gyif1/0/0 | 本端规划 | 其中10.8.10.1为主IP地址，10.8.10.2为从IP地址。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 其中10.8.10.1为主IP地址，10.8.10.2为从IP地址。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.10.1 | 全网规划 | 其中10.8.10.1为主IP地址，10.8.10.2为从IP地址。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址2（IPV4ADDRESS2） | 10.8.10.2 | 全网规划 | 其中10.8.10.1为主IP地址，10.8.10.2为从IP地址。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码2（IPV4MASK2） | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_gyif | 已配置数据中获取 | 接口绑定的VPN实例已通过<br>[**ADD VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICINF:NAME="gyif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";`
- 操作步骤上下文（±2 行原文）：
  L81:
    >   **[**ADD VPNINSTAF**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/L3VPN管理/L3VPN实例地址族/增加L3VPN实例地址族（ADD VPNINSTAF）_49802178.md)**
    > 4. 配置SCTP本端端点。
    >   **[ADD LOGICINF](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    >   > **说明**
    >   > 在对端的端口号为奇数时，可以通过 [**MOD DIAMCONNECTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter链路/修改Diameter链路（MOD DIAMCONNECTION）_09897267.md) 命令设置 “REVERSEIP” 为 “ENABLE” 来颠倒本端的主从IP地址，与对端建立偶联，即本端配置的从IP作为偶联的主IP，本端配置的主IP作为偶联的从IP。
  L145:
    > ```
    > ADD VPNINST: VPNINSTANCE="vpn_gyif";
    > ADD LOGICINF:NAME="gyif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";
    > ```
    > 

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L46:
    > - [**ADD CGBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG绑定/增加CG绑定关系（ADD CGBINDING）_09896874.md)
    > - [**SET SGWCHARGECFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW计费基础参数/SGW计费配置（SET SGWCHARGECFG）_09896989.md)
    > - [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > - [**ADD CPCGGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/抄送CG组/增加抄送CG组（ADD CPCGGRP）_09896864.md)
    > - [**ADD CPCGBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/抄送CG绑定/增加抄送CG绑定（ADD CPCGBINDING）_09896869.md)

**md：`WSFD-011201/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md`**
- 数据规划表（该命令的参数行）：
  | **ADD LOGICINF** | 逻辑接口名称（NAME） | gaif1/0/0 | 本端规划 | 组级Ga逻辑接口 |
  | **ADD LOGICINF** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 组级Ga逻辑接口 |
  | **ADD LOGICINF** | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 192.168.10.63 | 全网规划 | 组级Ga逻辑接口 |
  | **ADD LOGICINF** | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 组级Ga逻辑接口 |
  | **ADD LOGICINF** | VPN实例名（VPNINSTANCE） | vpn_ga | 已配置数据中获取 | 已在该配置任务中通过命令<br>**ADD VPNINST**<br>配置，可以使用<br>**LST VPNINST**<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICINF: NAME="gaif1/0/0", IPVERSION=IPV4, IPV4ADDRESS1="192.168.10.63", IPV4MASK1="255.255.255.255", VPNINSTANCE="vpn_ga";`
- 操作步骤上下文（±2 行原文）：
  L72:
    >       **ADD LOGICIP**
    >     b. 配置Ga逻辑接口。
    >       **ADD LOGICINF**
    >   > **说明**
    >   > **ADD LOGICINF** 中的“IP地址+VPN实例名称”和 **ADD LOGICIP** 命令中的“IP地址+VPN实例名称”必须一致。
  L74:
    >       **ADD LOGICINF**
    >   > **说明**
    >   > **ADD LOGICINF** 中的“IP地址+VPN实例名称”和 **ADD LOGICIP** 命令中的“IP地址+VPN实例名称”必须一致。
    > 6. 配置CG信息。
    >     a. 配置CG信息。
  L135:
    >   ```
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="192.168.10.63", VPNINSTNAME="vpn_ga";
    >   ADD LOGICINF: NAME="gaif1/0/0", IPVERSION=IPV4, IPV4ADDRESS1="192.168.10.63", IPV4MASK1="255.255.255.255", VPNINSTANCE="vpn_ga";
    >   ```
    > 6. 配置CG组信息以及GTP'消息控制。

### WSFD-109001

**md：`WSFD-109001/配置到OCS的数据(静态路由+BFD组网)_95923542.md`**
- 数据规划表（该命令的参数行）：
  | **ADD LOGICINF** | 逻辑接口名称（NAME） | Gyif1/0/0 | 本端规划 | 组级Gy逻辑接口1。 |
  | **ADD LOGICINF** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 已配置数据中获取 | 组级Gy逻辑接口1。 |
  | **ADD LOGICINF** | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.20.1 | 已配置数据中获取 | 组级Gy逻辑接口1。 |
  | **ADD LOGICINF** | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 组级Gy逻辑接口1。 |
  | **ADD LOGICINF** | VPN实例名（VPNINSTANCE） | vpn_gy | 已配置数据中获取 | 已在该配置任务中通过命令<br>**ADD VPNINST**<br>配置，可以使用<br>**LST VPNINST**<br>命令进行查询。 |
  | **ADD LOGICINF** | 逻辑接口名称（NAME） | Gyif1/0/1 | 本端规划 | 组级Gy逻辑接口2。 |
  | **ADD LOGICINF** | 逻辑接口的IP版本（IPVERSION） | IPV4 | 本端规划 | 组级Gy逻辑接口2。 |
  | **ADD LOGICINF** | 逻辑接口的IPv4地址1（IPV4ADDRESS1） | 10.8.20.2 | 全网规划 | 组级Gy逻辑接口2。 |
  | **ADD LOGICINF** | 逻辑接口的IPv4掩码1（IPV4MASK1） | 255.255.255.255 | 固定取值 | 组级Gy逻辑接口2。 |
  | **ADD LOGICINF** | VPN实例名（VPNINSTANCE） | vpn_gy | 已配置数据中获取 | 已在该配置任务中通过命令<br>**ADD VPNINST**<br>配置，可以使用<br>**LST VPNINST**<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICINF: NAME="Gyif1/0/0", IPVERSION=IPV4, IPV4ADDRESS1="10.8.20.1", IPV4MASK1="255.255.255.255", VPNINSTANCE="vpn_gy";`
  `ADD LOGICINF: NAME="Gyif1/0/1", IPVERSION=IPV4, IPV4ADDRESS1="10.8.20.2", IPV4MASK1="255.255.255.255", VPNINSTANCE="vpn_gy";`
- 操作步骤上下文（±2 行原文）：
  L90:
    >       **ADD LOGICIP**
    >     b. 配置Gy逻辑接口。
    >       **ADD LOGICINF**
    >   > **说明**
    >   > **ADD LOGICINF** 中的“IP地址+VPN实例名称”和 **ADD LOGICIP** 命令中的“IP地址+VPN实例名称”必须一致。
  L92:
    >       **ADD LOGICINF**
    >   > **说明**
    >   > **ADD LOGICINF** 中的“IP地址+VPN实例名称”和 **ADD LOGICIP** 命令中的“IP地址+VPN实例名称”必须一致。
    > 6. 配置在线计费中GGSN/PGW-C的设备标识。
    >   **ADD DIAMLOCINFO**
  L154:
    >   ```
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_gy";
    >   ADD LOGICINF: NAME="Gyif1/0/0", IPVERSION=IPV4, IPV4ADDRESS1="10.8.20.1", IPV4MASK1="255.255.255.255", VPNINSTANCE="vpn_gy";
    >   ```
    >   ```

### WSFD-011132

**md：`WSFD-011132/WSFD-011132 Gx over DRA参考信息_29315046.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
    > - **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > - **[ADD SCTPENDPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/SCTP管理/SCTP端点/增加SCTP端点（ADD SCTPENDPOINT）_09897321.md)**
    > - **[SET DIAMETERPARA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/路由控制/Diameter路由控制/设置Diameter参数（SET DIAMETERPARA）_09897315.md)**

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | gxif1/0/0 | 全网规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPv4 | 本端规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1(IPV4ADDRESS1) | 10.8.10.1 | 全网规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1(IPV4MASK1) | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址2(IPV4ADDRESS2) | 10.8.10.2 | 全网规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码2(IPV4MASK2) | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_gxif | 已配置数据中获取 | 接口绑定的VPN实例已通过<br>[**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gxif";`
  `ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gxif";`
- 操作步骤上下文（±2 行原文）：
  L132:
    > 5. 配置Gx逻辑接口。
    >   **[ADD LOGICIP](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)**
    >   **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 6. 配置GGSN/PGW-C的设备标识。
    >   **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)**
  L226:
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1";
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.2";
    >   ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gxif";
    >   ```
    > 3. 配置DRA数据。
  L316:
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1";
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.2";
    >   ADD LOGICINF:NAME="gxif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gxif";
    >   ```
    > 3. 配置DRA数据。

### WSFD-011133

**md：`WSFD-011133/WSFD-011133 Gy over DRA参考信息_29725462.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    > - **[SET CONCENPOINT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/基础参数/集中点模式/设置集中点部署模式（SET CONCENPOINT）_09896704.md)**
    > - **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > - **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)**
    > - **[ADD OCS](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/OCS Diameter连接/OCS Server/增加OCS（ADD OCS）_09896954.md)**

**md：`WSFD-011133/激活Gy over DRA（静态路由+BFD组网）_29725460.md`**
- 数据规划表（该命令的参数行）：
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | VPN实例名称（VPNINSTANCE） | vpn_gyif | 已配置数据中获取 | 接口绑定的VPN实例已通过<br>[**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口名称（NAME） | gxif1/0/0<br>gyif1/0/1 | 本端规划 | - |
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IP版本（IPVERSION） | IPv4 | 本端规划 | - |
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址1(IPV4ADDRESS1) | 10.8.10.1<br>10.8.10.2 | 本端规划 | 其中10.8.10.1、10.8.10.2是逻辑接口的主IP地址，10.8.10.4、10.8.10.5是逻辑接口的从IP地址。 |
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4地址2（IPV4ADDRESS2） | 10.8.10.4<br>10.8.10.5 | 本端规划 | 其中10.8.10.1、10.8.10.2是逻辑接口的主IP地址，10.8.10.4、10.8.10.5是逻辑接口的从IP地址。 |
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码1(IPV4MASK1) | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)** | 逻辑接口的IPv4掩码2（IPV4MASK2） | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICINF:NAME="gyif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.11.4",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";`
  `ADD LOGICINF:NAME="gyif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.2",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.5",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";`
  `ADD LOGICINF:NAME="gyif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.4",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";`
  `ADD LOGICINF:NAME="gyif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.2",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.5",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";`
- 操作步骤上下文（±2 行原文）：
  L124:
    > 5. 配置Gy逻辑接口。
    >   [**ADD LOGICIP**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/IP管理/IP配置/增加逻辑IP地址（ADD LOGICIP）_09587376.md)
    >   **[ADD LOGICINF](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)**
    > 6. 配置GGSN/PGW-C的设备标识信息。
    >   **[ADD DIAMLOCINFO](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)**
  L203:
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.1";
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.4";
    >   ADD LOGICINF:NAME="gyif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.11.4",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";
    >   ```
    > 
  L209:
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.2";
    >   ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.10.5";
    >   ADD LOGICINF:NAME="gyif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.2",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.5",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_gyif";
    >   ```
    > 3. 配置直连OCS相关信息。

### WSFD-011134

**md：`WSFD-011134/激活S6b over DRA（静态路由+BFD组网）_75821602.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | VPN实例名称（VPNINSTANCE） | vpn_s6bif | 已配置数据中获取 | 接口绑定的VPN实例已通过<br>[**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)<br>命令配置，可以使用<br>[**LST VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/查询VPN实例（LST VPNINST）_09651519.md)<br>命令进行查询。 |
  | [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | 逻辑接口名称（NAME） | s6bif1/0/0<br>s6bif1/0/1 | 全网规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | 逻辑接口的IP版本（IPVERSION） | IPv4 | 本端规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | 逻辑接口的IPv4地址1(IPV4ADDRESS1) | 10.8.10.1<br>10.8.10.4 | 全网规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | 逻辑接口的IPv4掩码1(IPV4MASK1) | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | 逻辑接口的IPv4地址2(IPV4ADDRESS2) | 10.8.10.2<br>10.8.10.5 | 全网规划 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
  | [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md) | 逻辑接口的IPv4掩码2(IPV4MASK2) | 255.255.255.255 | 固定取值 | 逻辑接口的IP掩码只能为255.255.255.255，或掩码长度32。 |
- 任务示例脚本（该命令行）：
  `ADD LOGICINF:NAME="s6bif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_s6bif";`
  `ADD LOGICINF:NAME="s6bif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.4",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.5",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_s6bif";`
  `ADD LOGICINF:NAME="s6bif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_s6bif";`
  `ADD LOGICINF:NAME="s6bif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.4",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.5",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_s6bif";`
- 操作步骤上下文（±2 行原文）：
  L103:
    >   > - LOCALPORT模式下，ADD DIAMCONNECTION命令添加的链路，仅LocalPort参数配置为非0的链路生效。LocalPort参数未配置或配置为0的链路，允许配置下发，但是不会建链。
    > 5. 配置S6b逻辑接口。
    >   [**ADD LOGICINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > 6. 配置GGSN/PGW-C的设备标识。
    >   [**ADD DIAMLOCINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter连接/Diameter本端信息/增加Diameter本端信息（ADD DIAMLOCINFO）_09897271.md)
  L184:
    > 
    >   ```
    >   ADD LOGICINF:NAME="s6bif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.1",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.2",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_s6bif";
    >   ```
    > 
  L188:
    > 
    >   ```
    >   ADD LOGICINF:NAME="s6bif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.10.4",IPV4MASK1="255.255.255.255",IPV4ADDRESS2="10.8.10.5",IPV4MASK2="255.255.255.255",VPNINSTANCE="vpn_s6bif";
    >   ```
    > 3. 配置DRA数据。

## ④ 自动比对
- 命令真相参数（11）：['IPV4ADDRESS1', 'IPV4ADDRESS2', 'IPV4MASK1', 'IPV4MASK2', 'IPV6ADDRESS1', 'IPV6ADDRESS2', 'IPV6PREFIXLEN1', 'IPV6PREFIXLEN2', 'IPVERSION', 'NAME', 'VPNINSTANCE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 27, '全网规划': 18, '固定取值': 19, '已配置数据中获取': 17}（多值→atom 应考虑 decision_driven）
