# 设置CHR单据的匿名化配置（SET CHRRECORDANONY）

- [命令功能](#ZH-CN_CONCEPT_0000206197242206__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206197242206__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206197242206__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206197242206__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206197242206__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206197242206)

**适用NF：SGW-U、PGW-U、UPF**

![](设置CHR单据的匿名化配置（SET CHRRECORDANONY）_97242206.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，涉及个人数据安全风险，请得到客户授权后谨慎使用。

该命令用于设置CHR单据的匿名化配置，包含N4信令CHR个人数据匿名化开关属性。

#### [注意事项](#ZH-CN_CONCEPT_0000206197242206)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 如客户需要关闭CHR匿名化处理，需将N4NONANONYSW参数设置为ENABLE。
- 收集非匿名化CHR，支撑N4接口CHR单据集采，协助问题定位。
- 暴露的个人数据：关闭CHR匿名化后，会暴露包括IMSI、MSIDN、IMEI、用户IP的个人数据。
- 若关闭CHR匿名化，网优Discovery 5GC工具支持CHR单据敏感信息匿名化。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | N4NONANONYSW |
| --- | --- |
| 初始值 | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0000206197242206)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206197242206)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| N4NONANONYSW | 该参数用于设置N4信令CHR个人数据匿名化开关。 | 可选必选说明：可选参数<br>参数含义：该参数用于设置N4信令CHR个人数据匿名化开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：<br>- ENABLE：关闭N4信令CHR个人数据匿名化，即明文。<br>- DISABLE：开启N4信令CHR个人数据匿名化。 |

#### [使用实例](#ZH-CN_CONCEPT_0000206197242206)

设置N4信令CHR个人数据匿名化开关为ENABLE：

```
SET CHRRECORDANONY:N4NONANONYSW=ENABLE;
```
