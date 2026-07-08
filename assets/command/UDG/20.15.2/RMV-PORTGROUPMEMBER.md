---
id: UDG@20.15.2@MMLCommand@RMV PORTGROUPMEMBER
type: MMLCommand
name: RMV PORTGROUPMEMBER（删除端口组成员）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PORTGROUPMEMBER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 端口组
status: active
---

# RMV PORTGROUPMEMBER（删除端口组成员）

## 功能

该命令用于删除端口组成员。

## 注意事项

- 该命令执行后立即生效。
- 删除端口组成员时，必须先配置所在的端口组。
- 批量删除时，成员接口类型要一致。
- 批量删除时，结束接口的名称排序需要在起始接口后。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PORTGROUPNAME | 端口组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示端口组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32；字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |
| MEMBERIFNAME | 端口组成员名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示端口组成员的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| ENDIFNAME | 批量添加时，结束的端口组成员名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示批量添加时结束的端口组成员的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PORTGROUPMEMBER]] · 端口组成员（PORTGROUPMEMBER）

## 使用实例

批量删除端口组ifm的成员：

```
RMV PORTGROUPMEMBER:PORTGROUPNAME="ifm",MEMBERIFNAME="Loopback1",ENDIFNAME="Loopback4";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-PORTGROUPMEMBER.md`
