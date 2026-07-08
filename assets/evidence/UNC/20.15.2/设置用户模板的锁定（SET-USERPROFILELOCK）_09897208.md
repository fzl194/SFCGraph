# 设置用户模板的锁定（SET USERPROFILELOCK）

- [命令功能](#ZH-CN_CONCEPT_0209897208__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897208__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897208__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897208__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897208__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897208)

**适用NF：PGW-C、SMF**

该命令用于设置用户模板的锁定。当运营商需要按照用户模板去活用户时，需先锁定该用户模板。

#### [注意事项](#ZH-CN_CONCEPT_0209897208)

- 该命令执行后立即生效。
- 此命令用来设置UserProfile是否锁定，在锁定UserProfile后，禁止使用UserProfile。当需要按照UserProfile去活用户时，需先锁定该UserProfile。由ENABLE状态设置为DISABLE状态，需要判断是否已经将UserProfile下用户都去活成功，如果正在去活用户，则禁止修改。
- 对于每个UserProfile，初始的锁定标记为DISABLE。
- 该命令设定后的数据，需要通过LST USERPROFILE命令进行查看。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897208)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897208)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |
| LOCKFLAG | 锁定标记 | 可选必选说明：必选参数<br>参数含义：指定锁定标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：<br>- 如果运营商不希望按照用户模板去活用户时，则配置该参数为DISABLE。<br>- 如果运营商希望按照用户模板去活用户时，则配置该参数为ENABLE。 |

#### [使用实例](#ZH-CN_CONCEPT_0209897208)

假如运营商需要锁定名称为“testuserprofilename”的用户模板：

```
SET USERPROFILELOCK:USERPROFILENAME="testuserprofilename",LOCKFLAG=ENABLE;
```
