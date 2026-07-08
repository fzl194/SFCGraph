---
id: UDG@20.15.2@MMLCommand@RMV IPSQMVIPLIST
type: MMLCommand
name: RMV IPSQMVIPLIST（删除IPSQM VIP用户列表）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IPSQMVIPLIST
command_category: 配置类
applicable_nf:
- SGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- IPSQM控制
- IPSQM VIP用户列表
status: active
---

# RMV IPSQMVIPLIST（删除IPSQM VIP用户列表）

## 功能

**适用NF：SGW-U、UPF**

该命令用于删除不做IPSQM流量整形的VIP用户信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERID | 用户标识 | 可选必选说明：可选参数<br>参数含义：用户标识类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：用于指定用户标识为IMSI。<br>- MSISDN：用于指定用户标识为MSISDN。<br>默认值：无<br>配置原则：无 |
| USERIDINFO | 用户ID信息 | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERID”配置为“IMSI” 或 “MSISDN”时为必选参数。<br>参数含义：用户标识信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。1、当用户ID类型为IMSI时，长度范围是1～15，每个字符必须为0~9的数字。 2、当用户ID类型为MSISDN时，长度范围是1～15，每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPSQMVIPLIST]] · IPSQM VIP用户列表（IPSQMVIPLIST）

## 使用实例

删除IMSI为461000000000001的用户不做IPSQM流量整形的配置：

```
RMV IPSQMVIPLIST: USERID=IMSI, USERIDINFO="461000000000001";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除IPSQM-VIP用户列表（RMV-IPSQMVIPLIST）_08991783.md`
