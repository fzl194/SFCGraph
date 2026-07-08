# 设置分片方式（SET IFMTUFRAGMODE）

- [命令功能](#ZH-CN_CONCEPT_0000001600866285__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600866285__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600866285__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600866285__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600866285__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600866285)

该命令用来配置Label+IP分片方式。

#### [注意事项](#ZH-CN_CONCEPT_0000001600866285)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600866285)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600866285)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FRAGMODE | 分片方式 | 可选必选说明：必选参数<br>参数含义：该参数用于表示分片方式信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FRACHECKMODE_IP：IP分片方式。<br>- FRACHECKMODE_LABELANDIP：标签加IP分片方式。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600866285)

配置接口Label+IP分片方式：

```
SET IFMTUFRAGMODE:FRAGMODE=FRACHECKMODE_LABELANDIP;
```
