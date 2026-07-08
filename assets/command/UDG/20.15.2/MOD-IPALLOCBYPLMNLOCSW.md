---
id: UDG@20.15.2@MMLCommand@MOD IPALLOCBYPLMNLOCSW
type: MMLCommand
name: MOD IPALLOCBYPLMNLOCSW（修改基于位置区+PLMN分配地址的开关）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: IPALLOCBYPLMNLOCSW
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 基于位置区分配地址开关
status: active
---

# MOD IPALLOCBYPLMNLOCSW（修改基于位置区+PLMN分配地址的开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改基于位置区+PLMN分配地址开关配置。

## 注意事项

- 该命令执行后立即生效。
- 在位置区组+PLMN映射地址池存在的情况下，若对应 ‘基于位置区组+PLMN分配地址开关-ADD IPALLOCBYPLMNLOCSW’ 配置为使能： 漫游用户需严格基于位置区组+PLMN匹配地址池组，即仅能匹配中位置区组+PLMN映射地址池。 本地用户优先匹配位置区组+PLMN映射址池组；若匹配不中，二次匹配单独基于位置区组映射地址池。
- 在位置区组+PLMN映射地址池存在的情况下，若对应 ‘基于位置区组+PLMN分配地址开关-ADD IPALLOCBYPLMNLOCSW’ 不存在或者配置为INHERIT状态时，地址分配流程受 ‘基于位置区组分配地址的开关-SET IPALLOCBYLOCSW’ 的控制。
- 在位置区组+PLMN映射地址池不存在的情况下，地址分配流程受 ‘基于位置区组分配地址的开关-SET IPALLOCBYLOCSW’ 的控制，不受 ‘基于位置区组+PLMN分配地址开关-ADD IPALLOCBYPLMNLOCSW’ 的控制。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCATIONGRPTYPE | 位置区组类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区组类型。<br>数据来源：本端规划<br>取值范围：枚举类型。只能选取一个选项。<br>- LAC：LAC。<br>- TAC：TAC。<br>默认值：无<br>配置原则：无 |
| LOCATIONGRPNAME | 位置区组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：该位置区组名称必须通过ADD LACGROUP或ADD TACGROUP命令配置过。 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，为3位数字，000～999。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网络号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网络号。<br>数据来源：全网规划<br>取值范围：字符串类型，可为2或3位数字，00~99或000~999。<br>默认值：无<br>配置原则：MNC有效配置长度为两位或三位。配置长度取决于PFCP Session Establishment Request消息ULI信元中携带的MNC有效值的长度，两位有效数字即配置两位，三位有效数字需配置三位。不受ADD MNCLEN影响。 |
| SWITCH | IPv4 开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于位置区分配地址的IPv4开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：无 |
| IPV6SWITCH | IPv6 开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于位置区分配地址的IPv6开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPALLOCBYPLMNLOCSW]] · 基于位置区+PLMN分配地址的开关（IPALLOCBYPLMNLOCSW）

## 使用实例

在位置区组tacgrp1+PLMN 460011映射地址池存在的情况下，允许激活携带信源tac属于tacgrp1，且PLMN为460011的用户基于位置区分配IPV4和IPV6地址：

```
MOD IPALLOCBYPLMNLOCSW: LOCATIONGRPTYPE=TAC, LOCATIONGRPNAME="tacgrp1", MCC="460", MNC="011", SWITCH=ENABLE, IPV6SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-IPALLOCBYPLMNLOCSW.md`
