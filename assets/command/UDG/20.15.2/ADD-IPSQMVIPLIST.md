---
id: UDG@20.15.2@MMLCommand@ADD IPSQMVIPLIST
type: MMLCommand
name: ADD IPSQMVIPLIST（增加IPSQM VIP用户列表）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: IPSQMVIPLIST
command_category: 配置类
applicable_nf:
- SGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 用户面服务管理
- 业务控制策略
- IPSQM控制
- IPSQM VIP用户列表
status: active
---

# ADD IPSQMVIPLIST（增加IPSQM VIP用户列表）

## 功能

**适用NF：SGW-U、UPF**

该命令用于配置不做IPSQM流量整形的VIP用户信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERID | 用户标识 | 可选必选说明：必选参数<br>参数含义：用户标识类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：用于指定用户标识为IMSI。<br>- MSISDN：用于指定用户标识为MSISDN。<br>默认值：无<br>配置原则：无 |
| USERIDINFO | 用户ID信息 | 可选必选说明：必选参数<br>参数含义：用户标识信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。1、当用户ID类型为IMSI时，长度范围是1～15，每个字符必须为0~9的数字。 2、当用户ID类型为MSISDN时，长度范围是1～15，每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPSQMVIPLIST]] · IPSQM VIP用户列表（IPSQMVIPLIST）

## 关联任务

- [[UDG@20.15.2@Task@0-00234]]

## 使用实例

配置IMSI为461000000000001的用户不做IPSQM流量整形：

```
ADD IPSQMVIPLIST: USERID=IMSI, USERIDINFO="461000000000001";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加IPSQM-VIP用户列表（ADD-IPSQMVIPLIST）_08873217.md`
