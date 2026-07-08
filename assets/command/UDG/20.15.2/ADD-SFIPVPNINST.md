---
id: UDG@20.15.2@MMLCommand@ADD SFIPVPNINST
type: MMLCommand
name: ADD SFIPVPNINST（添加SFIP VPN实例）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SFIPVPNINST
command_category: 配置类
applicable_nf:
- EPSN
effect_mode: 立即生效
is_dangerous: false
max_records: 4096
category_path:
- SFIP管理
- 网络管理
- SFIP VPN实例
status: active
---

# ADD SFIPVPNINST（添加SFIP VPN实例）

## 功能

**适用NF：EPSN**

该命令用于创建指定的VPN实例。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4096。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | VPN实例名 | 可选必选说明：必选参数<br>参数含义：该参数用于设置VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFIPVPNINST]] ·  SFIP VPN实例（SFIPVPNINST）

## 使用实例

增加SFIP VPNInst业务配置，VPN实例名称为vpn1，描述信息为vpn：

```
ADD SFIPVPNINST: VPNINSTANCE="vpn1", DESC="vpn";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-SFIPVPNINST.md`
