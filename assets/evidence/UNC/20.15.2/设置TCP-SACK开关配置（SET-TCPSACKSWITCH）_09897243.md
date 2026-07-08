# 设置TCP SACK开关配置（SET TCPSACKSWITCH）

- [命令功能](#ZH-CN_CONCEPT_0209897243__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897243__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897243__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897243__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897243__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897243)

**适用NF：SGW-C、PGW-C、SMF**

SET TcpSackSwitch命令用来修改Gx，Gy接口TCP协议是否支持SACK选项。

#### [注意事项](#ZH-CN_CONCEPT_0209897243)

- 该命令需要重新建链后才能生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | GX | GY |
| --- | --- | --- |
| 初始值 | DISABLE | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0209897243)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897243)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GX | Gx接口TCP协议支持SACK选项开关 | 可选必选说明：可选参数<br>参数含义：Gx接口TCP是否支持SACK选项。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：<br>- ENABLE：Gx接口支持TCP SACK选项。<br>- DISABLE：Gx接口不支持TCP SACK选项。 |
| GY | Gy接口TCP协议支持SACK选项开关 | 可选必选说明：可选参数<br>参数含义：Gy接口TCP是否支持SACK选项。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：<br>- ENABLE：Gy接口支持TCP SACK选项。<br>- DISABLE：Gy接口不支持TCP SACK选项。 |

#### [使用实例](#ZH-CN_CONCEPT_0209897243)

GX接口使能TCP的SACK选项，GY接口使能TCP的SACK选项：

```
SET TCPSACKSWITCH:GX=ENABLE,GY=ENABLE;
```
