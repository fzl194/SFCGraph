---
id: UNC@20.15.2@MMLCommand@RMV SMSFFUNCTION
type: MMLCommand
name: RMV SMSFFUNCTION（删除SMSF功能实体配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMSFFUNCTION
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMSF性能对象管理
status: active
---

# RMV SMSFFUNCTION（删除SMSF功能实体配置）

## 功能

**适用NF：SMSF**

该命令用于删除SMSF功能实体配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | NF实例号 | 可选必选说明：必选参数<br>参数含义：NF实例号。用于SMSF与北向网管对接使用，通过NFInstance ID可以实现与北向网管上与网元的话统、告警信息的关联。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：<br>该参数需要根据北向网管的要求来填写，例如，填写为在MANO上创建VNF时的InstanceID。 |
| SERVICENAME | SMSF服务列表 | 可选必选说明：必选参数<br>参数含义：特定SMSF功能实例服务名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSFFUNCTION]] · SMSF功能实例信息（SMSFFUNCTION）

## 使用实例

删除InstanceID为“b7b621d82dfb4a009d492491bd9d72a4”的SMSF功能实体。

```
RMV SMSFFUNCTION: INSTANCEID="b7b621d82dfb4a009d492491bd9d72a4", SERVICENAME="nsmsf-sms";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SMSF功能实体配置（RMV-SMSFFUNCTION）_35083983.md`
