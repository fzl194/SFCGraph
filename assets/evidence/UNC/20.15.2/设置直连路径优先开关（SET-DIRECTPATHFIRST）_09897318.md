# 设置直连路径优先开关（SET DIRECTPATHFIRST）

- [命令功能](#ZH-CN_CONCEPT_0209897318__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897318__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897318__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897318__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897318__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897318)

**适用NF：SGW-C、PGW-C、SMF**

该命令用来配置diameter会话的CCR-U/T消息是否始终通过CCR-I的发送路径发送。

#### [注意事项](#ZH-CN_CONCEPT_0209897318)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令设定后的数据，需要通过LST DIRECTPATHFIRST命令进行查看。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | GXSWITCH |
| --- | --- |
| 初始值 | ENABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0209897318)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897318)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GXSWITCH | Gx接口直连路径优先开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制diameter会话的CCR-U/T消息是否始终通过CCR-I的发送路径发送。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：<br>- 如果取值为enable，直连路径优先。<br>- 如果取值为disable，CCR-U/T消息始终通过CCR-I的发送路径发送。 |

#### [使用实例](#ZH-CN_CONCEPT_0209897318)

使能direct-path-first功能：

```
SET DIRECTPATHFIRST: GXSWITCH=ENABLE;
```
