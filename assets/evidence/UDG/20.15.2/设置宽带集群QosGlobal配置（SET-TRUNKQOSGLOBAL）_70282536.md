# 设置宽带集群QosGlobal配置（SET TRUNKQOSGLOBAL）

- [命令功能](#ZH-CN_CONCEPT_0000202770282536__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202770282536__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202770282536__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202770282536__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202770282536__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202770282536)

**适用NF：SGW-U、PGW-U**

该命令用于设置整机的宽带集群Qos功能。如果开启QosCar功能，则系统将会对集群用户的报文进行Qos控制。如果开QosRemark功能，则系统将会对集群用户的报文进行remark处理。

#### [注意事项](#ZH-CN_CONCEPT_0000202770282536)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | QOSFUNCTION | QOSCAR | QOSREMARK |
| --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0000202770282536)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202770282536)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSFUNCTION | 宽带集群QoS功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置整机使能和去使能宽带集群QoS功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| QOSCAR | 宽带集群QoSCar功能 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QOSFUNCTION”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于使能和去使能宽带集群QoSCar功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| QOSREMARK | 宽带集群QoSRemark功能 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QOSFUNCTION”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于使能和去使能宽带集群QoSRemark功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000202770282536)

开启整机的宽带集群Qos功能，同时打开QosCar和QosRemark功能：

```
SET TRUNKQOSGLOBAL: QOSFUNCTION=ENABLE, QOSCAR=ENABLE, QOSREMARK=ENABLE;
```
