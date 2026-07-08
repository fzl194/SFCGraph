---
id: UDG@20.15.2@MMLCommand@RMV UEINJECTPKT
type: MMLCommand
name: RMV UEINJECTPKT（删除UE灌包参数）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UEINJECTPKT
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- UE侧连通性检测
- UE灌包参数
status: active
---

# RMV UEINJECTPKT（删除UE灌包参数）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除UE下行灌包功能的UE灌包参数。

## 注意事项

- 该命令执行后立即生效。
- 删除已配置UE下行灌包功能的UE灌包参数时可以不指定imsi，msisdn或者imei，此时所有已配置的UE灌包参数将会全部被删除。
- 此命令不支持配置恢复，若整机重启则需要重新配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERID | 用户标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：用于指定用户标识为IMSI。<br>- MSISDN：用于指定用户标识为MSISDN。<br>- IMEI：用于指定用户标识为IMEI。<br>默认值：无<br>配置原则：无 |
| USERIDINFO | 用户ID信息 | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERID”配置为“IMSI”、“MSISDN” 或 “IMEI”时为必选参数。<br>参数含义：该参数用于指定用户ID信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～16。1、当用户ID类型为IMSI时，长度范围是1～15，每个字符必须为0~9的数字。 2、当用户ID类型为MSISDN时，长度范围是1～15，每个字符必须为0~9的数字。 3、当用户ID类型为IMEI时，长度范围是1～16，每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UEINJECTPKT]] · UE灌包参数（UEINJECTPKT）

## 使用实例

删除指定imsi为12345678901234的UE下行灌包功能的UE灌包参数：

```
RMV UEINJECTPKT: USERID=IMSI, USERIDINFO="12345678901234";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-UEINJECTPKT.md`
