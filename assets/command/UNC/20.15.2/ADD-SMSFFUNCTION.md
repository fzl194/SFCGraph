---
id: UNC@20.15.2@MMLCommand@ADD SMSFFUNCTION
type: MMLCommand
name: ADD SMSFFUNCTION（添加SMSF功能实体配置）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD SMSFFUNCTION（添加SMSF功能实体配置）

## 功能

**适用NF：SMSF**

该命令用于添加SMSF功能实体配置。

## 注意事项

- 该命令执行后立即生效。

- 该命令当前版本仅支持配置1条记录，否则会影响北向功能。

- 最多可输入100条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | NF实例号 | 可选必选说明：必选参数<br>参数含义：NF实例号。用于SMSF与北向网管对接使用，通过NFInstance ID可以实现与北向网管上与网元的话统、告警信息的关联。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：<br>该参数需要根据北向网管的要求来填写，例如，填写为在MANO上创建VNF时的InstanceID。 |
| SERVICENAME | SMSF服务列表 | 可选必选说明：必选参数<br>参数含义：特定SMSF功能实例服务名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |
| FQDN | FQDN | 可选必选说明：可选参数<br>参数含义：SMSF Function的FQDN。需要与ADD NFPROFILE中该NF使用的FQDN一致。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：<br>FQDN由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。 |
| MAXUSER | 最大注册用户数 | 可选必选说明：可选参数<br>参数含义：当前软硬件配置条件下（如licence限制），SMSF最大能够支持的注册用户数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>根据当前系统软硬之配置条件下，例如license中配置的数值进行设置。 |
| SMSCAPACITY | SMSF短信转发容量 | 可选必选说明：可选参数<br>参数含义：SMSF短信转发容量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>根据当前系统软硬之配置条件下，例如license中配置的数值进行设置。 |
| CAPACITY | 相对容量 | 可选必选说明：可选参数<br>参数含义：相对容量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSFFUNCTION]] · SMSF功能实例信息（SMSFFUNCTION）

## 使用实例

增加一个SMSF功能实体。

```
ADD SMSFFUNCTION: INSTANCEID="b7b621d82dfb4a009d492491bd9d72a4", SERVICENAME="nsmsf-sms", FQDN="smsf01.cmcc.PC.node.5gc.mnc002.mcc460.3gppnetwork.org", MAXUSER=50000, SMSCAPACITY=500, CAPACITY=25;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SMSFFUNCTION.md`
