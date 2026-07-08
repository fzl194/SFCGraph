# 设置MBS QosGlobal配置（SET MBSQOSGLOBAL）

- [命令功能](#ZH-CN_CONCEPT_0000203347263205__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203347263205__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203347263205__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203347263205__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203347263205__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203347263205)

**适用NF：UPF**

该命令用于配置MBS会话是否支持QOS功能。

#### [注意事项](#ZH-CN_CONCEPT_0000203347263205)

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- MBS QOS SHAPE和MBS QOS CAR同时打开时，MBS QOS SHAPE优先生效。
- 开启后会导致性能下降。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | QOSFUNCTION | QOSCAR | QOSSHAPE |
| --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0000203347263205)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203347263205)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSFUNCTION | MBS QoS功能开关 | 可选必选说明：必选参数<br>参数含义：该参数配置整机使能和去使能MBS QoS功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| QOSCAR | MBS QosCar功能 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QOSFUNCTION”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于使能和去使能MBS QosCar功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| QOSSHAPE | MBS QosShape功能 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QOSFUNCTION”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于使能和去使能MBS QoShape功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000203347263205)

配置MBS会话的QOS功能开关和QOS SHAPE开关为ENABLE：

```
SET MBSQOSGLOBAL: QOSFUNCTION=ENABLE, QOSSHAPE=ENABLE;
```
