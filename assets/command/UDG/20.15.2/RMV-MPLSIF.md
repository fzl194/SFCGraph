---
id: UDG@20.15.2@MMLCommand@RMV MPLSIF
type: MMLCommand
name: RMV MPLSIF（删除MPLS接口）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: MPLSIF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- MPLS基础
- MPLS接口
status: active
---

# RMV MPLSIF（删除MPLS接口）

## 功能

该命令用于删除MPLS接口。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MPLSIF]] · MPLS接口（MPLSIF）

## 使用实例

删除MPLS接口：

```
RMV MPLSIF:IFNAME="Ethernet64/0/3";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除MPLS接口（RMV-MPLSIF）_50121554.md`
