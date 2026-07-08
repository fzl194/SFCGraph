# 删除CG组绑定关系（RMV CGGRPBINDING）

- [命令功能](#ZH-CN_CONCEPT_0209896886__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896886__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896886__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896886__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896886__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896886)

**适用NF：SGW-C、PGW-C、SMF**

该命令用来删除CG组绑定关系。支持批量删除，给OFCTEMPLATENAME字段赋值，删除指定OFCTEMPLATENAME的记录；给OFCTEMPLATENAME和CGGRPID字段赋值，删除满足条件的记录。

#### [注意事项](#ZH-CN_CONCEPT_0209896886)

- 该命令执行后只对新激活用户生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896886)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896886)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCTEMPLATENAME | 离线计费模板名 | 可选必选说明：必选参数<br>参数含义：指定离线计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |
| CGGRPID | CG组ID | 可选必选说明：可选参数<br>参数含义：指定CG组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896886)

删除CG组绑定关系（离线计费模板为ofctemplate1，CG组ID为1），命令为：

```
RMV CGGRPBINDING: OFCTEMPLATENAME="ofctemplate1", CGGRPID=1;
```
