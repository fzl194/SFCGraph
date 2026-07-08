# 设置校验和开关（SET CHKSUM）

- [命令功能](#ZH-CN_CONCEPT_0251174297__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0251174297__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0251174297__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0251174297__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0251174297__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0251174297__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0251174297)

**适用NF：NCG**

该命令用于设置UDP校验和校验开关，当需要开启或者关闭接收、发送UDP报文的校验和开关，可以使用这个命令。

#### [注意事项](#ZH-CN_CONCEPT_0251174297)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令的默认记录为打开UDP校验和校验开关。
- 该命令存在系统初始设置记录，参数的初始设置值如下表：

| NETPURPOSE | RCVUDPCHKSW | SENDUDPCHKSW |
| --- | --- | --- |
| Ga | ON | ON |

#### [本地用户权限](#ZH-CN_CONCEPT_0251174297)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0251174297)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0251174297)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NETPURPOSE | 网络用途 | 可选必选说明：必选参数<br>参数含义：网络资源用途。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Ga：Ga。<br>默认值：无<br>配置原则：无 |
| RCVUDPCHKSW | 接收UDP校验和校验开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“NETPURPOSE”配置为“Ga”时为条件可选参数。<br>参数含义：接收UDP校验和校验开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：开启。<br>默认值：无<br>配置原则：无 |
| SENDUDPCHKSW | 发送UDP校验和校验开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“NETPURPOSE”配置为“Ga”时为条件可选参数。<br>参数含义：发送UDP校验和校验开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：开启。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0251174297)

设置UDP校验和开关关闭：

```
SET CHKSUM: NETPURPOSE=Ga, RCVUDPCHKSW=OFF, SENDUDPCHKSW=OFF;
```
