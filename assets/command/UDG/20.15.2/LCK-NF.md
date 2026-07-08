---
id: UDG@20.15.2@MMLCommand@LCK NF
type: MMLCommand
name: LCK NF（设置NF锁定开关）
nf: UDG
version: 20.15.2
verb: LCK
object_keyword: NF
command_category: 动作类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- NF锁定开关
status: active
---

# LCK NF（设置NF锁定开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](设置NF锁定开关（LCK NF）_82837078.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，会改变NF的锁定状态，如果配置为锁定，会导致用户接入失败。

该命令用来设置NF的锁定状态，处于锁定状态中时，该NF无法正常接入业务。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCKSWITCH | NF锁定状态开关 | 可选必选说明：必选参数<br>参数含义：该参数使能时，NF为锁定状态，该参数为不使能时，NF为解锁状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NF]] · NF的锁定信息（NF）

## 使用实例

配置NF为锁定状态：

```
LCK NF: LOCKSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LCK-NF.md`
