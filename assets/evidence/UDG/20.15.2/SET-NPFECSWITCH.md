# 设置NP FEC配置（SET NPFECSWITCH）

- [命令功能](#ZH-CN_TOPIC_0250068362__1.3.1.1)
- [注意事项](#ZH-CN_TOPIC_0250068362__1.3.2.1)
- [操作用户权限](#ZH-CN_TOPIC_0250068362__1.3.3.1)
- [参数说明](#ZH-CN_TOPIC_0250068362__1.3.4.1)
- [使用实例](#ZH-CN_TOPIC_0250068362__1.3.5.1)

#### [命令功能](#ZH-CN_TOPIC_0250068362)

该命令用来设置NP卡端口FEC功能状态。

#### [注意事项](#ZH-CN_TOPIC_0250068362)

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。
- 当前NP卡FEC状态支持NP_FEC_NONE和FEC_MOD_RS两种状态，当NP卡外联口和交换机外联口的FEC状态不一致或NP卡级联口和对框级联口FEC状态不一致时，端口会物理DOWN。
- 当NP外联口插入40GE/10GE光模块时，仅支持设置为NP_FEC_NONE状态。当插入100GE/25GE光模块时，支持设置为NP_FEC_NONE或FEC_MOD_RS状态。当插入400GE/200GE光模块时，支持设置为NP_FEC_NONE或FEC_MOD_RS544_2CWORD状态。

#### [操作用户权限](#ZH-CN_TOPIC_0250068362)

G_1，管理员级别命令组；G_2，操作员级别命令组；

#### [参数说明](#ZH-CN_TOPIC_0250068362)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NPINTERFACENAME | 接口名称 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定NP卡上的端口。<br>数据来源：本端规划。<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，区分大小写。<br>配置原则：通过<br>**[LST INTERFACE](../../../../IP服务/接口管理/接口配置/查询接口（LST INTERFACE）_49801850.md)**<br>命令查询。<br>默认值：无。 |
| NPSWITCH | FEC状态 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定FEC功能状态。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>- NP_FEC_NONE：FEC不使能。<br>- FEC_MOD_RS：RS-FEC(528,514)模式。<br>- FEC_MOD_RS544_2CWORD：RS-FEC(544,514)模式。<br>默认值：无。 |

#### [使用实例](#ZH-CN_TOPIC_0250068362)

- 设置100GE66/0/8接口的FEC功能状态为FEC_MOD_RS：
  ```
  SET NPFECSWITCH:NPINTERFACENAME="100GE66/0/8",NPSWITCH=FEC_MOD_RS;
  ```
