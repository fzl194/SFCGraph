---
id: UNC@20.15.2@MMLCommand@RMV LDPIF
type: MMLCommand
name: RMV LDPIF（删除LDP接口）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LDPIF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP接口管理
status: active
---

# RMV LDPIF（删除LDP接口）

## 功能

该命令用于删除LDP接口。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LDPIF]] · LDP接口（LDPIF）

## 使用实例

删除LDP接口：

```
RMV LDPIF:VRFNAME="_public_",IFNAME="Ethernet64/0/3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除LDP接口（RMV-LDPIF）_50281482.md`
