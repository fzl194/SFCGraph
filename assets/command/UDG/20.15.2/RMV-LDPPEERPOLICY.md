---
id: UDG@20.15.2@MMLCommand@RMV LDPPEERPOLICY
type: MMLCommand
name: RMV LDPPEERPOLICY（删除LDP邻居策略）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: LDPPEERPOLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP邻居策略
status: active
---

# RMV LDPPEERPOLICY（删除LDP邻居策略）

## 功能

该命令用于删除LDP邻居策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| PEERID | 对等体的LSR ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定对等体的LSR ID。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LDPPEERPOLICY]] · LDP邻居策略（LDPPEERPOLICY）

## 使用实例

删除LDP邻居策略：

```
RMV LDPPEERPOLICY:VRFNAME="_public_",PEERID="192.168.1.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除LDP邻居策略（RMV-LDPPEERPOLICY）_00866437.md`
