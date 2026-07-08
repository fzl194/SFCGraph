# 设置全局RADIUS响应消息源IP/端口检查配置（SET RDSRSPADDRCHK）

- [命令功能](#ZH-CN_CONCEPT_0209896744__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896744__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896744__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896744__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896744__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896744)

**适用NF：PGW-C、SMF**

该命令用来设置全局RADIUS响应消息源IP/端口检查配置。使能该检查功能，如果RADIUS响应消息的源IP或者端口号与UNC配置的不一致，UNC将丢弃此消息。

#### [注意事项](#ZH-CN_CONCEPT_0209896744)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | AUTH | ACCT |
| --- | --- | --- |
| 初始值 | ENABLE | ENABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0209896744)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896744)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AUTH | RADIUS鉴权响应消息源IP/端口检查开关 | 可选必选说明：可选参数<br>参数含义：RADIUS鉴权响应消息源IP/端口检查开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| ACCT | RADIUS计费响应消息源IP/端口检查开关 | 可选必选说明：可选参数<br>参数含义：RADIUS计费响应消息源IP/端口检查开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896744)

使能RADIUS鉴权响应消息和计费响应消息源IP/端口检查：

```
SET RDSRSPADDRCHK: AUTH=ENABLE, ACCT=ENABLE;
```
