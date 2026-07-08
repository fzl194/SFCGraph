# 配置CP白名单开关（SET CPACCESSLISTFUNC）

- [命令功能](#ZH-CN_CONCEPT_0186530396__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186530396__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186530396__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186530396__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186530396__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0186530396)

**适用NF：SGW-U、PGW-U、UPF**

![](配置CP白名单开关（SET CPACCESSLISTFUNC）_86530396.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请使用ADD CPACCESSLIST配置完整的白名单后再使用该功能，白名单外的设备将无法建立偶联。

该命令用于配置是否支持CP白名单功能。配置白名单后，将对CP发来的PFCP Association Setup Request消息进行控制，只有白名单范围内的CP才能和UPF建立偶联连接，才允许激活用户。

#### [注意事项](#ZH-CN_CONCEPT_0186530396)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令执行后，只对后续的SMF发来的PFCP Association Setup Request消息进行控制。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH |
| --- | --- |
| 初始值 | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0186530396)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186530396)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 开关标识 | 可选必选说明：必选参数<br>参数含义：配置系统是否开启CP白名单功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：表示不支持CP白名单功能。<br>- ENABLE：表示支持CP白名单功能。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0186530396)

使能CP白名单功能：

```
SET CPACCESSLISTFUNC: SWITCH=ENABLE;
```
