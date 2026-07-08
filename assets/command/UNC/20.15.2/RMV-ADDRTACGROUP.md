---
id: UNC@20.15.2@MMLCommand@RMV ADDRTACGROUP
type: MMLCommand
name: RMV ADDRTACGROUP（删除TAC组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ADDRTACGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址分配位置区管理
- 地址分配TAC组
status: active
---

# RMV ADDRTACGROUP（删除TAC组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除指定TAC组。

## 注意事项

- 该命令执行后立即生效。

- 如果TAC组已经绑定了TAC号段，需要先执行RMV ADDRN2TACID、RMV ADDRS1TACID删除该TAC组内的所有TAC号段。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | TAC组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [TAC组（ADDRTACGROUP）](configobject/UNC/20.15.2/ADDRTACGROUP.md)

## 使用实例

删除TAC组，名称是“wz-sq”，类型是“S1TAC”：

```
RMV ADDRTACGROUP: TACGROUPNAME="wz-sq";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除TAC组（RMV-ADDRTACGROUP）_49644929.md`
