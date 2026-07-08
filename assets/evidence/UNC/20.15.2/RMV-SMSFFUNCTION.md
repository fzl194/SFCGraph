# 删除SMSF功能实体配置（RMV SMSFFUNCTION）

- [命令功能](#ZH-CN_MMLREF_0235083983__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0235083983__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0235083983__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0235083983__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0235083983)

**适用NF：SMSF**

该命令用于删除SMSF功能实体配置。

## [注意事项](#ZH-CN_MMLREF_0235083983)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0235083983)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0235083983)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | NF实例号 | 可选必选说明：必选参数<br>参数含义：NF实例号。用于SMSF与北向网管对接使用，通过NFInstance ID可以实现与北向网管上与网元的话统、告警信息的关联。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：<br>该参数需要根据北向网管的要求来填写，例如，填写为在MANO上创建VNF时的InstanceID。 |
| SERVICENAME | SMSF服务列表 | 可选必选说明：必选参数<br>参数含义：特定SMSF功能实例服务名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0235083983)

删除InstanceID为“b7b621d82dfb4a009d492491bd9d72a4”的SMSF功能实体。

```
RMV SMSFFUNCTION: INSTANCEID="b7b621d82dfb4a009d492491bd9d72a4", SERVICENAME="nsmsf-sms";
```
