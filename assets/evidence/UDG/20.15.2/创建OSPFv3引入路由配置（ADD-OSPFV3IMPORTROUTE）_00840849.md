# 创建OSPFv3引入路由配置（ADD OSPFV3IMPORTROUTE）

- [命令功能](#ZH-CN_CONCEPT_0000001600840849__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600840849__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600840849__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600840849__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600840849__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600840849)

该命令用来将外部路由引入到OSPFv3域中，并在OSPFv3域中发布引入的路由信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001600840849)

- 该命令执行后立即生效。
- 该命令最大记录数为8000。
- 只有在执行ADD OSPFV3配置了OSPFv3进程后才能使用此命令。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600840849)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600840849)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPFv3进程必须已经存在。请使用LST OSPFV3命令查看可用的OSPFv3进程。 |
| TOPOID | 拓扑标识 | 可选必选说明：可选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：0<br>配置原则：目前只支持默认拓扑0。 |
| PROTOCOL | 协议号 | 可选必选说明：必选参数<br>参数含义：协议号。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- direct：直连路由。<br>- static：静态路由。<br>- bgp：BGP协议。<br>- ospfv3：OSPFv3协议。<br>- wlr：无线路由。<br>默认值：无 |
| PROTOCOLPROCID | 协议进程号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOL”配置为“ospfv3”时为可选参数。<br>参数含义：协议进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：1 |
| IMPTCOSTCFG | 引入路由开销值配置 | 可选必选说明：可选参数<br>参数含义：引入路由Cost使能标志。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：FALSE |
| IMPTTAGCFG | 引入路由标签配置 | 可选必选说明：可选参数<br>参数含义：引入路由Tag使能标志。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：FALSE |
| IMPTTYPECFG | 引入路由类型配置 | 可选必选说明：可选参数<br>参数含义：引入路由Type使能标志。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：FALSE |
| COST | 路径Cost值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMPTCOSTCFG”配置为“TRUE”时为必选参数。<br>参数含义：路径Cost值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～16777214。<br>默认值：无 |
| TAG | 标签 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMPTTAGCFG”配置为“TRUE”时为必选参数。<br>参数含义：标签。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| TYPE | 引入路由类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMPTTYPECFG”配置为“TRUE”时为必选参数。<br>参数含义：引入路由类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Type1：外部路由类型1。<br>- Type2：外部路由类型2。<br>默认值：无 |
| ROUPOLINAME | 路由策略名称 | 可选必选说明：可选参数<br>参数含义：路由策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：区分大小写。 |
| PERMITIBGPCFG | 允许BGP配置 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOL”配置为“bgp”时为可选参数。<br>参数含义：允许BGP配置。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| INHERITCOSTCFG | 指定引入路由时继承原路由的开销值 | 可选必选说明：可选参数<br>参数含义：指定引入路由时继承原路由的开销值。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE<br>配置原则：参数INHERITCOSTCFG不能与IMPTCOSTCFG同时配置为TRUE。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600840849)

在OSPFv3进程1下引入OSPFv3进程2的路由：

```
ADD OSPFV3IMPORTROUTE: PROCID=1, TOPOID=0, IMPTCOSTCFG=FALSE, IMPTTAGCFG=FALSE, IMPTTYPECFG=FALSE, PROTOCOL=ospfv3, PROTOCOLPROCID=2;
```
