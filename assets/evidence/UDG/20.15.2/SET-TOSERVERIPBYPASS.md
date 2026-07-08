# 设置异常Server IP自动bypass功能（SET TOSERVERIPBYPASS）

- [命令功能](#ZH-CN_CONCEPT_0000206977522776__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206977522776__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206977522776__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206977522776__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206977522776__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206977522776)

**适用NF：UPF**

该命令用于设置异常Server IP自动bypass功能，当开启该功能后，若存在五次及以上建链尝试仍无法正常建链的Server IP地址，该Server IP地址后续的所有流将被Bypass。

#### [注意事项](#ZH-CN_CONCEPT_0000206977522776)

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 当Server地址和POD内部网络冲突时，需要开启异常Server IP自动bypass功能。
- 老化时间应该大于异常状态重置为初始状态时间。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SERVERIPBYPASSSWITCH | AGETIME | RESETTIME |
| --- | --- | --- | --- |
| 初始值 | DISABLE | 86400 | 21600 |

#### [操作用户权限](#ZH-CN_CONCEPT_0000206977522776)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206977522776)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVERIPBYPASSSWITCH | 异常Server IP自动bypass功能开关 | 可选必选说明：必选参数<br>参数含义：设置异常Server IP自动bypass功能开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| AGETIME | 老化时间（秒） | 可选必选说明：可选参数<br>参数含义：设置异常ServerIP表节点老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：无 |
| RESETTIME | 异常状态重置为初始状态时间（秒） | 可选必选说明：可选参数<br>参数含义：设置异常ServerIP表节点异常状态重置为初始状态时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000206977522776)

开启异常Server IP自动bypass功能：

```
SET TOSERVERIPBYPASS: SERVERIPBYPASSSWITCH=ENABLE;
```
