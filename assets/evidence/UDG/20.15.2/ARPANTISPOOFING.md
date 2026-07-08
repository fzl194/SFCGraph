# 设置ARP防欺骗信息（SET ARPANTISPOOFING）

- [命令功能](#ZH-CN_CONCEPT_0000001550121098__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550121098__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550121098__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550121098__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550121098__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550121098)

该命令用于配置ARP防欺骗功能。

#### [注意事项](#ZH-CN_CONCEPT_0000001550121098)

- 该命令执行后立即生效。
- 去使能ARP防欺骗功能时，ARP防欺骗告警清除，ARP动、静态黑名单删除。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| ENABLEANTISPOOFING | DETECTTIME | ENABLEALARM | THRESHOLDVALUE | EXPIRETIME |
| --- | --- | --- | --- | --- |
| DISABLE | 5 | DISABLE | 30 | 1200 |

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550121098)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550121098)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENABLEANTISPOOFING | ARP防欺骗使能 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP防欺骗是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：去使能。<br>- ENABLE：使能。<br>默认值：无 |
| DETECTTIME | ARP探测次数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENABLEANTISPOOFING”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定ARP冲突探测次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～15。<br>默认值：无 |
| ENABLEALARM | ARP防欺骗告警使能 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENABLEANTISPOOFING”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定ARP防欺骗告警是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：去使能。<br>- ENABLE：使能。<br>默认值：无 |
| THRESHOLDVALUE | ARP冲突阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENABLEALARM”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定一分钟内ARP冲突次数的阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1024。<br>默认值：无 |
| EXPIRETIME | 老化时间（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“ENABLEANTISPOOFING”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定ARP动态黑名单老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～86400，单位是秒。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001550121098)

配置ARP防欺骗功能使能：

```
SET ARPANTISPOOFING:ENABLEANTISPOOFING=ENABLE;
```
