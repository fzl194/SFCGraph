---
id: UDG@20.15.2@MMLCommand@RMV S1TACID
type: MMLCommand
name: RMV S1TACID（从S1TAC组内删除一个S1TAC）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: S1TACID
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- S1TAC段
status: active
---

# RMV S1TACID（从S1TAC组内删除一个S1TAC）

## 功能

**适用NF：PGW-U、UPF**

该命令用来删除S1TAC组内绑定的S1TAC号段。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | 指定S1TAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定S1TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| TACSECNUM | S1Tac 段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S1TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～15999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [从S1TAC组内删除一个S1TAC（S1TACID）](configobject/UDG/20.15.2/S1TACID.md)

## 使用实例

假设运营商需要在一个本地已经配置的S1TAC组删除一个S1TAC号段：

```
RMV S1TACID:TACGROUPNAME="beijing",TACSECNUM=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/从S1TAC组内删除一个S1TAC（RMV-S1TACID）_97358678.md`
