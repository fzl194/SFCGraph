---
id: UDG@20.15.2@MMLCommand@RMV HOSTSTCIF
type: MMLCommand
name: RMV HOSTSTCIF（删除接口协议报文统计配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HOSTSTCIF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- 主机报文统计
- 统计功能配置
status: active
---

# RMV HOSTSTCIF（删除接口协议报文统计配置）

## 功能

该命令用于删除接口协议报文统计配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HOSTSTCIF]] · 接口协议报文统计配置（HOSTSTCIF）

## 使用实例

删除接口协议报文统计配置：

```
RMV HOSTSTCIF: IFNAME="GigabitEthernet0/0/1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除接口协议报文统计配置（RMV-HOSTSTCIF）_49802518.md`
