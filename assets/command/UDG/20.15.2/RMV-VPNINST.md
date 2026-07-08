---
id: UDG@20.15.2@MMLCommand@RMV VPNINST
type: MMLCommand
name: RMV VPNINST（删除VPN实例）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: VPNINST
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- VPN管理
- VPN
status: active
---

# RMV VPNINST（删除VPN实例）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除指定的VPN实例。

## 注意事项

- 该命令执行后立即生效。
- 已被其他对象绑定的VPN实例不允许被删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | VPN实例名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例，该参数一般由运营商规划给出。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：无<br>配置原则：“_public_”是公网缺省VPN的实例名，不允许用户删除。 |

## 操作的配置对象

- [VPN实例（VPNINST）](configobject/UDG/20.15.2/VPNINST.md)

## 使用实例

删除VPNInst业务配置，VPN实例名称为vpn1：

```
RMV VPNINST:VPNINSTANCE="vpn1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除VPN实例（RMV-VPNINST）_82837046.md`
