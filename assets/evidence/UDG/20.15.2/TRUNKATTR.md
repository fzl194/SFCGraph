# 设置宽带集群属性配置（SET TRUNKATTR）

- [命令功能](#ZH-CN_CONCEPT_0000202969122701__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202969122701__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202969122701__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202969122701__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202969122701__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202969122701)

**适用NF：SGW-U、PGW-U**

该命令用于控制是否对长时间处于空闲状态的集群用户进行去活处理，以及配置GTP-U消息头中是否携带Sequence Number字段。

#### [注意事项](#ZH-CN_CONCEPT_0000202969122701)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | IDLEDEASW | GTPUSEQUENCESW |
| --- | --- | --- |
| 初始值 | DISABLE | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0000202969122701)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202969122701)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDLEDEASW | 空闲去活开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否使能空闲去活功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| GTPUSEQUENCESW | Sequence Number开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置GTP-U消息头中是否携带Sequence Number字段。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000202969122701)

将长时间处于空闲状态的集群用户进行去活处理的开关设置为开启：

```
SET TRUNKATTR: IDLEDEASW=ENABLE, GTPUSEQUENCESW=DISABLE;
```
