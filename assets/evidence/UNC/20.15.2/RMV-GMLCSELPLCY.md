# 删除GMLC选择策略(RMV GMLCSELPLCY)

- [命令功能](#ZH-CN_MMLREF_0000001126305622__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305622__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305622__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305622__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305622__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305622__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305622)

**适用网元：MME**

该命令用于删除指定条件下的GMLC选择策略。

#### [注意事项](#ZH-CN_MMLREF_0000001126305622)

- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305622)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305622)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305622)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCGRPID | GMLC选择策略组索引 | 可选必选说明：必选参数<br>参数含义：该参数在系统内唯一标识一个GMLC组。<br>数据来源：本端规划<br>取值范围：0~191<br>默认值：无<br>配置原则：该参数需要在<br>[**ADD GMLCSELGRP**](../GMLC选择策略组/增加GMLC选择策略组(ADD GMLCSELGRP)_26145810.md)<br>中事先配置，可执行<br>[**LST GMLCSELGRP**](../GMLC选择策略组/查询GMLC选择策略组(LST GMLCSELGRP)_72345411.md)<br>进行查看。 |
| LCSCLIENTTYPE | LCS客户端类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识LCS客户端类型。<br>数据来源：整网规划<br>取值范围：<br>- “EMERGENCY_SERVICES(紧急业务)”<br>- “VALUE_ADDED_SERVICES(增值业务)”<br>- “PLMN_OPERATOR_SERVICES(运营商业务)”<br>- “LAWFUL_INTERCEPT_SERVICES(合法定位)”<br>默认值：无 |
| LOCATIONTYPE | 位置区标识类型 | 可选必选说明：必选参数<br>参数含义：该参数标识位置标识类型。<br>数据来源：整网规划<br>取值范围：<br>- “ECI(小区标识)”<br>- “TAC(跟踪区编码)”<br>默认值：无 |
| TACBEGIN | 跟踪区起始编码 | 可选必选说明：条件必选参数<br>参数含义：该参数表示跟踪区起始编码。<br>前提条件：该参数在"位置区标识类型"参数配置为"跟踪区编码"后生效。<br>数据来源：整网规划<br>取值范围：0x0000~0xFFFF<br>默认值：无 |
| ECIBEGIN | 小区起始标识 | 可选必选说明：条件必选参数<br>参数含义：该参数表示E-UTRAN小区起始标识。<br>前提条件：该参数在"位置区标识类型"参数配置为"小区标识"后生效。<br>数据来源：整网规划<br>取值范围：0~268435455<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305622)

删除索引为0的GMLC选择策略组内一条选择策略。该记录的LCS客户端类型为EMERGENCY_SERVICES（紧急业务）、小区起始标识为1。

RMV GMLCSELPLCY: GMLCGRPID=0, LCSCLIENTTYPE=EMERGENCY_SERVICES, LOCATIONTYPE=ECI, ECIBEGIN=1;
