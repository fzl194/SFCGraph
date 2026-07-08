---
id: UNC@20.15.2@MMLCommand@RMV QOSRDRVPN
type: MMLCommand
name: RMV QOSRDRVPN（删除QoS重定向VPN）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOSRDRVPN
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 重定向VPN
status: active
---

# RMV QOSRDRVPN（删除QoS重定向VPN）

## 功能

该命令用于删除非本地报文重定向到指定VPN的配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSRDRVPN]] · QoS重定向VPN（QOSRDRVPN）

## 使用实例

删除以太接口Ethernet66/0/3上的重定向配置：

```
RMV QOSRDRVPN:IFNAME="Ethernet66/0/3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除QoS重定向VPN（RMV-QOSRDRVPN）_00600549.md`
