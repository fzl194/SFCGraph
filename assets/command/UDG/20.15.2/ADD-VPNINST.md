---
id: UDG@20.15.2@MMLCommand@ADD VPNINST
type: MMLCommand
name: ADD VPNINST（增加VPN实例）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: VPNINST
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 4096
category_path:
- 用户面服务管理
- DN管理
- VPN管理
- VPN
status: active
---

# ADD VPNINST（增加VPN实例）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于创建指定的VPN实例。创建VPN实例后，还需要对VPN实例进行一系列的配置，必要的操作是将VPN实例与连向此VPN网络的接口绑定。通过配置接口与VPN实例绑定，该接口成为私网接口，从该接口进入的报文使用VPN实例中的转发信息进行转发。另外此VPN还需要与平台的ADD L3VPNINST添加的VPN命名一致，否则此VPN就会业务不通。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4096。
- 新增Vpn Instance后，需要确保在VNRS上ADD L3VPNINST添加了同名的VPN配置，否则此VPN会业务不通。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | VPN实例名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例，该参数一般由运营商规划给出。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：无<br>配置原则：“_public_”是公网缺省VPN的实例名，不允许用户配置。 |

## 操作的配置对象

- [VPN实例（VPNINST）](configobject/UDG/20.15.2/VPNINST.md)

## 关联任务

- [0-00041](task/UDG/20.15.2/0-00041.md)

## 使用实例

增加VPNInst业务配置，VPN实例名称为vpn1：

```
ADD VPNINST:VPNINSTANCE="vpn1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加VPN实例（ADD-VPNINST）_82837045.md`
