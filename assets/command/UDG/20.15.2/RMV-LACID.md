---
id: UDG@20.15.2@MMLCommand@RMV LACID
type: MMLCommand
name: RMV LACID（从LAC组内删除一个LAC）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: LACID
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
- LAC段
status: active
---

# RMV LACID（从LAC组内删除一个LAC）

## 功能

**适用NF：PGW-U、UPF**

该命令用来删除LAC组内绑定的LAC号段。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LACGROUPNAME | 指定LAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LACSECNUM | Lac 段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～23999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [从LAC组内删除一个LAC（LACID）](configobject/UDG/20.15.2/LACID.md)

## 使用实例

假设运营商需要删除指定LAC组绑定的某个LAC号段，LAC组为beijing，LAC号段为2时，执行该命令：

```
RMV LACID:LACGROUPNAME="beijing",LACSECNUM=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/从LAC组内删除一个LAC（RMV-LACID）_82837198.md`
