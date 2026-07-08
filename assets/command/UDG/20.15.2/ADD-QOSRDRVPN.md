---
id: UDG@20.15.2@MMLCommand@ADD QOSRDRVPN
type: MMLCommand
name: ADD QOSRDRVPN（增加QoS重定向VPN）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: QOSRDRVPN
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65536
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 重定向VPN
status: active
---

# ADD QOSRDRVPN（增加QoS重定向VPN）

## 功能

该命令用于配置非本地报文重定向到指定VPN。用户不需要配置复杂流分类，只需要将接口上收到的所有非本地的单播报文全部重定向到指定的VPN，在该VPN内再查路由表项进行转发。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65536。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：与设备接口名称保持一致，下发本MML命令前可使用LST INTERFACE查看设备接口。 |
| VRFNAME | VPN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定重定向VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 需要先使用ADD L3VPNINST命令添加VPN实例。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/QOSRDRVPN]] · QoS重定向VPN（QOSRDRVPN）

## 使用实例

配置以太网接口Ethernet66/0/3重定向到VPN实例vpn1：

```
ADD QOSRDRVPN:IFNAME="Ethernet66/0/3",VRFNAME="vpn1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加QoS重定向VPN（ADD-QOSRDRVPN）_00441441.md`
