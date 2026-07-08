# 设置用户ARP优先级配置（SET USERPRIORARP）

- [命令功能](#ZH-CN_MMLREF_0000001427933281__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001427933281__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001427933281__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001427933281__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001427933281)

**适用NF：PGW-C、GGSN**

该命令用来设置全局的QoS信息，包括漫游以及拜访用户的级别限制功能。

## [注意事项](#ZH-CN_MMLREF_0000001427933281)

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ROAMHIGHESTARP | VISITHIGHESTARP | ROAMARPSWITCH | VISITARPSWITCH |
| --- | --- | --- | --- |
| NORMAL | NORMAL | DISABLE | DISABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0000001427933281)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001427933281)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROAMHIGHESTARP | 漫游用户ARP级别限制 | 可选必选说明：该参数在"ROAMARPSWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于表示漫游用户的ARP级别限制（将漫游用户的ARP级别限制为某一固定值，并非最高级别）。<br>数据来源：本端规划<br>取值范围：<br>- LOW（低优先级）<br>- NORMAL（正常优先级）<br>- HIGH（高优先级）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST USERPRIORARP查询当前参数配置值。<br>配置原则：无 |
| VISITHIGHESTARP | 拜访用户ARP级别限制 | 可选必选说明：该参数在"VISITARPSWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于表示拜访用户的ARP级别限制（将拜访用户的ARP级别限制为某一固定值，并非最高级别）。<br>数据来源：本端规划<br>取值范围：<br>- LOW（低优先级）<br>- NORMAL（正常优先级）<br>- HIGH（高优先级）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST USERPRIORARP查询当前参数配置值。<br>配置原则：无 |
| ROAMARPSWITCH | 漫游用户级别限制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表明系统是否支持漫游用户级别限制。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST USERPRIORARP查询当前参数配置值。<br>配置原则：无 |
| VISITARPSWITCH | 拜访用户级别限制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表明系统是否支持拜访用户级别限制。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST USERPRIORARP查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001427933281)

假设运营商需要配置漫游以及拜访用户的级别限制功能：

```
SET USERPRIORARP:ROAMARPSWITCH=ENABLE,ROAMHIGHESTARP=HIGH,VISITARPSWITCH=ENABLE,VISITHIGHESTARP=HIGH;
```
