---
id: UDG@20.15.2@MMLCommand@SET UEINJECTLIST
type: MMLCommand
name: SET UEINJECTLIST（设置UE灌包白名单）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UEINJECTLIST
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 10
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- UE侧连通性检测
- UE灌包白名单
status: active
---

# SET UEINJECTLIST（设置UE灌包白名单）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于配置UE下行灌包功能的白名单。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为10。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERID | 用户标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：用于指定用户标识为IMSI。<br>- MSISDN：用于指定用户标识为MSISDN。<br>- IMEI：用于指定用户标识为IMEI。<br>默认值：无<br>配置原则：无 |
| USERIDINFO | 用户ID信息 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户ID信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～16。1、当用户ID类型为IMSI时，长度范围是1～15，每个字符必须为0~9的数字。 2、当用户ID类型为MSISDN时，长度范围是1～15，每个字符必须为0~9的数字。 3、当用户ID类型为IMEI时，长度范围是1～16，每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UE灌包白名单（UEINJECTLIST）](configobject/UDG/20.15.2/UEINJECTLIST.md)

## 使用实例

配置指定imsi为12345678901234的白名单：

```
SET UEINJECTLIST: USERID=IMSI, USERIDINFO="12345678901234";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置UE灌包白名单（SET-UEINJECTLIST）_82837102.md`
