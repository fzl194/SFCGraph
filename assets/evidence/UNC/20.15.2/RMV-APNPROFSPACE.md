# 删除APN与Profile Space的绑定关系（RMV APNPROFSPACE）

- [命令功能](#ZH-CN_CONCEPT_0209897054__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897054__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897054__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897054__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897054__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897054)

**适用NF：PGW-C、SMF**

本命令用于删除APN与Profile Space的绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0209897054)

该命令执行后只对新激活用户生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897054)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897054)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897054)

删除APNProfSpace配置，APN为“apn1”：

```
RMV APNPROFSPACE:APN="apn1";
```
