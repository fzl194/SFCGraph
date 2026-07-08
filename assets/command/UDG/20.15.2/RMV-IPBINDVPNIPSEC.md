---
id: UDG@20.15.2@MMLCommand@RMV IPBINDVPNIPSEC
type: MMLCommand
name: RMV IPBINDVPNIPSEC（删除接口绑定VPN）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IPBINDVPNIPSEC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- 绑定VPN
status: active
---

# RMV IPBINDVPNIPSEC（删除接口绑定VPN）

## 功能

![](删除接口绑定VPN（RMV IPBINDVPNIPSEC）_25830701.assets/notice_3.0-zh-cn.png)

删除接口和VPN的绑定关系，影响该隧道下的地址信息，有业务影响。

该命令用于配置接口去绑定VPN。

> **说明**
> - 该命令执行后立即生效。
>
> - 执行该命令将清除该接口下所有的IP配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：用于设置绑定VPN的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口绑定的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPBINDVPNIPSEC]] · 接口绑定VPN（IPBINDVPNIPSEC）

## 使用实例

配置接口去绑定VPN：

```
RMV IPBINDVPNIPSEC:IFNAME="Loopback1",VRFNAME="vrf1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-IPBINDVPNIPSEC.md`
