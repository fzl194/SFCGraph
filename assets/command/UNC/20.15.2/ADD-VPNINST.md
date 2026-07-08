---
id: UNC@20.15.2@MMLCommand@ADD VPNINST
type: MMLCommand
name: ADD VPNINST（增加VPN实例）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: VPNINST
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- VPN
status: active
---

# ADD VPNINST（增加VPN实例）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于创建指定的VPN实例。创建VPN实例后，还需要对VPN实例进行一系列的配置，必要的操作如下：

- 将VPN实例与PE上连向VPN网络的接口绑定。
- 通过配置接口与VPN实例绑定，该接口成为私网接口，从该接口进入的报文使用VPN实例中的转发信息进行转发。

## 注意事项

- 该命令执行后立即生效。

- “_public_”是公网缺省VPN的实例名，不允许用户配置。

- 最多可输入10000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | VPN实例名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VPNINST]] · VPN实例（VPNINST）

## 使用实例

增加VPNInst业务配置，VPN实例名称为vpn1：

```
ADD VPNINST:VPNINSTANCE="vpn1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-VPNINST.md`
