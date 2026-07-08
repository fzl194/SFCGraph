# 设置DCC模板OCS初始化（SET OCSINIT）

- [命令功能](#ZH-CN_CONCEPT_0209896932__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896932__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896932__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896932__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896932__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896932)

**适用NF：PGW-C、SMF**

该命令用于设置DCC在线计费模板OCS初始化。

#### [注意事项](#ZH-CN_CONCEPT_0209896932)

- 该命令执行后立即生效。
- 该命令最大记录数为101。
- SESSIONMODE配置为MULTIPLE时，OCSINIT不能配置成ENABLE。
- 该命令设定后的数据，需要通过LST DCCTEMPLATE命令进行查看。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | DCCTMPLTNAME | OCSINIT | WAITOCSRESP |
| --- | --- | --- | --- |
| 初始值 | global | ENABLE | ENABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0209896932)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896932)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCCTMPLTNAME | DCC模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定操作的DCC在线计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD DCCTEMPLATE命令配置生成。<br>- 该命令基于此参数配置DCC在线计费模板的OCS初始化。 |
| OCSINIT | OCS交互使能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置在线计费模板中在线计费用户激活时候是否需要到OCS交互。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>- INHERIT：继承上级。<br>默认值：无<br>配置原则：SESSIONMODE配置为MULTIPLE时，该参数不能配置成ENABLE。 |
| WAITOCSRESP | OCS交互等待OCS响应开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“OCSINIT”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置在线计费模板中在线计费用户激活需要到OCS交互的情况下是否需要等待OCS响应。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896932)

设置名为“DccTemplate”的DCC在线计费模板的OCS交互使能开关使能：

```
SET OCSINIT:DCCTMPLTNAME="DccTemplate",OCSINIT=ENABLE;
```
