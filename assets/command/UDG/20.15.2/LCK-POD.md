---
id: UDG@20.15.2@MMLCommand@LCK POD
type: MMLCommand
name: LCK POD（锁定/解锁POD）
nf: UDG
version: 20.15.2
verb: LCK
object_keyword: POD
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
- POD锁定开关
status: active
---

# LCK POD（锁定/解锁POD）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](锁定_解锁POD（LCK POD）_64015273.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，POD锁定后无法激活新用户，请及时解锁。

锁定POD，POD锁定后无法激活新用户。

## 注意事项

- 该命令执行后立即生效。
- 此命令不导出。
- 当参数MULPDN为DISABLE，并且一直有多PDN用户激活时，基于POD去活可能有部分多PDN用户未被去活。如需去活全部去活，建议将MULPDN设置为ENABLE再执行去活命令。
- 只支持锁定spu-pod或isu-pod。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：必选参数<br>参数含义：POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCKSWITCH | 锁定POD开关 | 可选必选说明：必选参数<br>参数含义：该参数使能时，POD为锁定状态，该参数为不使能时，POD为解锁状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| MULPDN | 多PDN接入开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“LOCKSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数不使能时，允许多PDN接入，使能时，不允许多PDN接入。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：无 |
| FULLMESHNGVN | FullMesh 5G LAN组会话接入开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“LOCKSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数不使能时，允许FullMesh 5G LAN组会话接入，使能时，不允许FullMesh 5G LAN组会话接入。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/POD]] · POD停止（POD）

## 使用实例

锁定POD, 名称为ssgpod-0：

```
LCK POD: PODNAME="ssgpod-0", LOCKSWITCH=ENABLE, MULPDN=DISABLE,FULLMESHNGVN=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LCK-POD.md`
