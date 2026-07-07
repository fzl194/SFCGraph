# 命令证据包：ADD TNFINSIP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例IP地址管理/增加目标NF实例IP地址（ADD TNFINSIP）_09654443.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：![](增加目标NF实例IP地址（ADD TNFINSIP）_09654443.assets/notice_3.0-zh-cn_2.png)

配置相同TNFINSINDEX时PORT必须一致。如果配置相同TNFINSINDEX但是不同PORT的TNFINSIP，会覆盖对端NF实例配置中的PORT，导致对端NF实例配置中的IP使用不匹配的PORT。

**适用NF：AMF、SMF、NSSF、NRF
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 最多可输入4096条记录。
- 该命令配置时，如果存在关联的目标NF实例配置，用其目标NF名称匹配对端NF实例概述信息的NF实例标识（大小写不敏感匹配），如果存在匹配成功，则目标NF实例配置的IP必须属于该对端NF实例概述信息中的IP，否则配置失败。
- 该命令配置时，如果配置的IP包含在一个NF类型为NfCHF的对端NF实例概述信息中，确认目标NF实例索引关联的

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| TNFINSINDEX | 目标NF实例索引 | global_planned | required | 无 | 整数类型，取值范围是0~2047。 |
| IPTYPE | IP地址类型 | global_planned | required | 无 | <br>- “IPV4（IPv4）”：IPv4 |
| IPV4ADDR | IPV4类型地址 | global_planned | conditional | 无 | IPv4地址类型。 |
| IPV6ADDR | IPV6类型地址 | global_planned | conditional | 无 | IPv6地址类型。 |
| PORT | 端口号 | global_planned | conditional | 无 | 整数类型，取值范围是1~65535。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/WSFD-011206 支持融合计费参考信息_74013176.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - [**SET GLBCHARGECHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置对本地用户、漫游用户、拜访用户所采用的计费属性（SET GLBCHARGECHAR）_09896800.md)
    > - [**ADD TNFINS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例管理/增加目标NF实例（ADD TNFINS）_09652354.md)
    > - [**ADD TNFINSIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例IP地址管理/增加目标NF实例IP地址（ADD TNFINSIP）_09654443.md)
    > - [**ADD TNFGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF组管理/增加目标NF组（ADD TNFGRP）_09651791.md)
    > - [**ADD TNFBINDGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例绑定组管理/增加目标NF实例绑定组（ADD TNFBINDGRP）_09651533.md)

**md：`WSFD-011206/配置CHF选择方式_92091086.md`**
- 数据规划表（该命令的参数行）：
  | **ADD TNFINSIP** | 目标NF实例索引（TNFINSINDEX） | - 1<br>- 2 | 本端规划 | 增加主备CHF实例的IP地址。 |
  | **ADD TNFINSIP** | IP地址类型（IPTYPE） | - IPV4<br>- IPV4 | 全网规划 | 增加主备CHF实例的IP地址。 |
  | **ADD TNFINSIP** | IPV4类型地址（IPV4ADDR） | - 192.168.94.2<br>- 192.168.104.2 | 全网规划 | 增加主备CHF实例的IP地址。 |
  | **ADD TNFINSIP** | 端口号（PORT） | - 3220<br>- 3230 | 全网规划 | 增加主备CHF实例的IP地址。 |
- 任务示例脚本（该命令行）：
  `ADD TNFINSIP: TNFINSINDEX=1, IPTYPE=IPV4, IPV4ADDR="192.168.94.2", PORT=3220;`
  `ADD TNFINSIP: TNFINSINDEX=2, IPTYPE=IPV4, IPV4ADDR="192.168.104.2", PORT=3230;`
  `ADD TNFINSIP: TNFINSINDEX=1, IPTYPE=IPV4, IPV4ADDR="192.168.94.2", PORT=3220;`
  `ADD TNFINSIP: TNFINSINDEX=2, IPTYPE=IPV4, IPV4ADDR="192.168.104.2", PORT=3230;`
  `ADD TNFINSIP: TNFINSINDEX=1, IPTYPE=IPV4, IPV4ADDR="192.168.94.2", PORT=3220;`
  `ADD TNFINSIP: TNFINSINDEX=2, IPTYPE=IPV4, IPV4ADDR="192.168.104.2", PORT=3230;`
  `ADD TNFINSIP: TNFINSINDEX=1, IPTYPE=IPV4, IPV4ADDR="192.168.94.2", PORT=3220;`
  `ADD TNFINSIP: TNFINSINDEX=2, IPTYPE=IPV4, IPV4ADDR="192.168.104.2", PORT=3230;`
  `ADD TNFINSIP: TNFINSINDEX=1, IPTYPE=IPV4, IPV4ADDR="192.168.94.2", PORT=3220;`
  `ADD TNFINSIP: TNFINSINDEX=2, IPTYPE=IPV4, IPV4ADDR="192.168.104.2", PORT=3230;`
- 操作步骤上下文（±2 行原文）：
  L72:
    >       **ADD TNFINS**
    >     3. 配置目标CHF实例的IP地址信息。
    >       **ADD TNFINSIP**
    > - 配置基于CC值选择CHF。
    >     1. 配置计费属性。计费属性信息都能从UDM获取时，请跳过该步骤。
  L80:
    >             **ADD TNFINS**
    >           b. 配置目标CHF实例的IP地址信息。
    >             **ADD TNFINSIP**
    >           c. 配置CHF组。
    >             **ADD TNFGRP**
  L97:
    >             **ADD TNFINS**
    >           b. 配置目标CHF实例的IP地址信息。
    >             **ADD TNFINSIP**
    >           c. 配置CHF组。
    >             **ADD TNFGRP**

**md：`WSFD-011206/调测融合计费的主备CHF的可靠性_89257222.md`**
- 操作步骤上下文（±2 行原文）：
  L44:
    > 5. 如果通过本地配置基于CC选择CHF，执行 [**LST SELECTCHFGBYCC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/查询基于CC选择CHF处理（LST SELECTCHFGBYCC）_09653040.md) 、 [**LST TNFBINDGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例绑定组管理/查询目标NF实例绑定组（LST TNFBINDGRP）_09651395.md) 、 [**LST TNFGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF组管理/查询目标NF组（LST TNFGRP）_09652113.md) 、 [**LST TNFINSIP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例IP地址管理/查询目标NF实例IP地址（LST TNFINSIP）_09651383.md) 、 [**LST TNFINS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例管理/查询目标NF实例（LST TNFINS）_09652356.md) 命令，查看SMF本地是否配置备CHF组，且备用CHF配置了IP地址等信息。
    >     - 如果已配置，请执行[步骤 6](#ZH-CN_OPI_0289257222__step1321124813497)。
    >     - 如果未配置，请执行[**ADD TNFINSIP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例IP地址管理/增加目标NF实例IP地址（ADD TNFINSIP）_09654443.md)、[**MOD TNFINS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例管理/修改目标NF实例（MOD TNFINS）_09651413.md)、[**ADD TNFGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF组管理/增加目标NF组（ADD TNFGRP）_09651791.md)、[**MOD TNFBINDGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例绑定组管理/修改目标NF实例绑定组（MOD TNFBINDGRP）_09652550.md)、[**MOD SELECTCHFGBYCC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/修改基于CC选择CHF处理（MOD SELECTCHFGBYCC）_09651411.md)命令，根据规划配置基于CC绑定主备CHF组，并再次执行[步骤 3](#ZH-CN_OPI_0289257222__step2585105420194)。
    > 6. 查看用户跟踪消息，打开CHF给SMF发送的 Charging Data Response [initial] /Charging Data Response [update]消息，查看是否携带sessionFailover信元，且该信元为FAILOVER_NOT_SUPPORTED，即主用CHF故障时不支持向备用CHF发送计费消息。
    >     - 如果CHF下发了sessionFailover信元，且取值为FAILOVER_NOT_SUPPORTED，那么主用CHF故障时，SMF未向备用CHF发送计费消息是正常的。如果需要修改，则联系CHF端技术支持修改相关配置。

## ④ 自动比对
- 命令真相参数（5）：['IPTYPE', 'IPV4ADDR', 'IPV6ADDR', 'PORT', 'TNFINSINDEX']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 1, '全网规划': 3}（多值→atom 应考虑 decision_driven）
