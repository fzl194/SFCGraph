# 删除OCS组绑定关系（RMV OCSGRPBINDING）

- [命令功能](#ZH-CN_CONCEPT_0209896977__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896977__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896977__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896977__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896977__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896977)

**适用NF：PGW-C、SMF**

![](删除OCS组绑定关系（RMV OCSGRPBINDING）_09896977.assets/notice_3.0-zh-cn_2.png)

该命令属于高危命令，如果不输入主备用标记和OCS组名，表示删除此DCCTMPLTNAME下绑定的所有OCS组，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

该命令用来删除OCS组绑定关系。支持批量删除，给DCCTMPLTNAME字段赋值，删除指定DCCTMPLTNAME的记录；给DCCTMPLTNAME、PRIORSEC和OCSGRPNAME字段赋值，删除满足条件的记录。

#### [注意事项](#ZH-CN_CONCEPT_0209896977)

- 该命令执行后只对新激活用户生效。
- 删除OCS组绑定关系后，对应新激活在线计费用户立即生效，可能导致该用户激活失败。
- 删除OCS组绑定关系后，对应已经选择该OCS组中的OCS服务器的在线计费用户，如果链路正常的话，仍然会选择该OCS服务器发送消息。
- 该命令属于高危命令，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896977)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896977)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCCTMPLTNAME | DCC模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定操作的DCC在线计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| PRIORSEC | 主备用标记 | 可选必选说明：可选参数<br>参数含义：该参数用于指定OCS组的主备标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PRIMARY：表示该服务器是主用服务器。<br>- SECONDARY：表示该服务器是备用服务器。<br>默认值：无<br>配置原则：无 |
| OCSGRPNAME | OCS组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定OCS组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896977)

删除OCS组绑定关系（DCC模板为dcc1，OCS组为ocsgroup1，服务器为主用），命令为：

```
RMV OCSGRPBINDING: DCCTMPLTNAME="dcc1", PRIORSEC=PRIMARY, OCSGRPNAME="ocsgroup1";
```
