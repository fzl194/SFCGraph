# 设置TCP流老化功能配置（SET TOFLOWAGINGCFG）

- [命令功能](#ZH-CN_CONCEPT_0000201531379101__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201531379101__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201531379101__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201531379101__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201531379101__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201531379101)

**适用NF：UPF**

该命令用于设置TCP流老化功能配置。

#### [注意事项](#ZH-CN_CONCEPT_0000201531379101)

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 此配置时间应该大于保活时间，执行LST TORELIABLECFG命令确认KEEPALIVE配置时间。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | FLOWAGINGSWITCH | FLOWAGINGTIME |
| --- | --- | --- |
| 初始值 | ENABLE | 600 |

#### [操作用户权限](#ZH-CN_CONCEPT_0000201531379101)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201531379101)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWAGINGSWITCH | TCP流老化功能开关 | 可选必选说明：必选参数<br>参数含义：设置TCP流的老化功能开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| FLOWAGINGTIME | TCP流老化时间（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“FLOWAGINGSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：TCP流老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围30～7200，单位是秒。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000201531379101)

开启TCP流老化功能开关，设置TCP流老化时间为500秒：

```
SET TOFLOWAGINGCFG: FLOWAGINGSWITCH=ENABLE, FLOWAGINGTIME=500;
```
