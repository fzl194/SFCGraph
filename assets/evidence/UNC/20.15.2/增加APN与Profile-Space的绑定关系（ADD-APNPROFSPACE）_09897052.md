# 增加APN与Profile Space的绑定关系（ADD APNPROFSPACE）

- [命令功能](#ZH-CN_CONCEPT_0209897052__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897052__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897052__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897052__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897052__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897052)

**适用NF：PGW-C、SMF**

本命令用于配置APN与ProfileSpace的绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0209897052)

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为3000。
- 每个APN最多可以绑定一个ProfileSpace。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897052)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897052)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：配置的APN必须是系统已经存在的APN对象名称。 |
| PROFSPACENAME | Profile Space名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ProfileSpace实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD PROFILESPACE命令配置生成。<br>- 配置的ProfSpaceName必须是ProfileSpace的对象名。 |

#### [使用实例](#ZH-CN_CONCEPT_0209897052)

将Profile Space名称为“profilespace1”的Profile Space绑定到指定APN “apn1”下：

```
ADD APNPROFSPACE:APN="apn1",PROFSPACENAME="profilespace1";
```
