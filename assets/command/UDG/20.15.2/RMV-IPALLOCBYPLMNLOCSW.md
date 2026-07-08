---
id: UDG@20.15.2@MMLCommand@RMV IPALLOCBYPLMNLOCSW
type: MMLCommand
name: RMV IPALLOCBYPLMNLOCSW（删除基于位置区+PLMN分配地址的开关）
nf: UDG
version: 20.15.2
verb: RMV
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

# RMV IPALLOCBYPLMNLOCSW（删除基于位置区+PLMN分配地址的开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除基于位置区+PLMN分配地址开关配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCATIONGRPTYPE | 位置区组类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区组类型。<br>数据来源：本端规划<br>取值范围：枚举类型。只能选取一个选项。<br>- LAC：LAC。<br>- TAC：TAC。<br>默认值：无<br>配置原则：无 |
| LOCATIONGRPNAME | 位置区组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，为3位数字，000～999。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网络号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网络号。<br>数据来源：全网规划<br>取值范围：字符串类型，可为2或3位数字，00~99或000~999。<br>默认值：无<br>配置原则：MNC有效配置长度为两位或三位。配置长度取决于PFCP Session Establishment Request消息ULI信元中携带的MNC有效值的长度，两位有效数字即配置两位，三位有效数字需配置三位。不受ADD MNCLEN影响。 |

## 操作的配置对象

- [基于位置区+PLMN分配地址的开关（IPALLOCBYPLMNLOCSW）](configobject/UDG/20.15.2/IPALLOCBYPLMNLOCSW.md)

## 使用实例

删除位置区组名为tacgrp1，plmn为460011的 ‘基于位置区+PLMN分配地址开关-ADD IPALLOCBYPLMNLOCSW’ 的配置：

```
RMV IPALLOCBYPLMNLOCSW: LOCATIONGRPTYPE=TAC, LOCATIONGRPNAME="tacgrp1", MCC="460", MNC="01";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除基于位置区+PLMN分配地址的开关（RMV-IPALLOCBYPLMNLOCSW）_41443958.md`
