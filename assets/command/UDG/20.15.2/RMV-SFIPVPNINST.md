---
id: UDG@20.15.2@MMLCommand@RMV SFIPVPNINST
type: MMLCommand
name: RMV SFIPVPNINST（删除SFIP VPN实例）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SFIPVPNINST
command_category: 配置类
applicable_nf:
- EPSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- 网络管理
- SFIP VPN实例
status: active
---

# RMV SFIPVPNINST（删除SFIP VPN实例）

## 功能

**适用NF：EPSN**

该命令用于删除指定的VPN实例。

## 注意事项

- 该命令执行后立即生效。
- 已被其他对象绑定的VPN实例不允许被删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | VPN实例名 | 可选必选说明：必选参数<br>参数含义：该参数用于设置VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFIPVPNINST]] ·  SFIP VPN实例（SFIPVPNINST）

## 使用实例

删除SFIP VPNInst业务配置，VPN实例名称为vpn1：

```
RMV SFIPVPNINST:VPNINSTANCE="vpn1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除SFIP-VPN实例（RMV-SFIPVPNINST）_42536155.md`
