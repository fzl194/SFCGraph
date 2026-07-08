---
id: UDG@20.15.2@MMLCommand@LCK DNAI
type: MMLCommand
name: LCK DNAI（设置DNAI锁定配置）
nf: UDG
version: 20.15.2
verb: LCK
object_keyword: DNAI
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: true
category_path:
- 用户面服务管理
- DN管理
- DNAI管理
- 数据网络接入标识
status: active
---

# LCK DNAI（设置DNAI锁定配置）

## 功能

**适用NF：PGW-U、UPF**

![](设置DNAI锁定配置（LCK DNAI）_54287986.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，正在改变DNAI的锁定状态，如果配置为锁定，会导致用户接入失败。

该命令用来配置对指定DNAI进行锁定操作。当DNAI锁定后，对于后续使用该DNAI激活的用户激活失败，对于已经在线的用户无影响。缺省情况下DNAI未锁定。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 修改DNAI的锁定状态时，对后续激活的用户生效。当执行命令Lock DNAI为ENABLE时，后续用户激活失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络接入标识 | 可选必选说明：必选参数<br>参数含义：数据网络接入标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。名称中不能包含空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCKED | 锁定 | 可选必选说明：必选参数<br>参数含义：该参数用于配置DNAI进行锁定操作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DNAI配置（DNAI）](configobject/UDG/20.15.2/DNAI.md)

## 使用实例

锁定DNAI，DNAI名称为mtest：

```
LCK DNAI: DNAI="mtest", LOCKED=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置DNAI锁定配置（LCK-DNAI）_54287986.md`
