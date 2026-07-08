---
id: UNC@20.15.2@MMLCommand@SET SECARPGRAT
type: MMLCommand
name: SET SECARPGRAT（设置免费ARP过滤）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SECARPGRAT
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略免费ARP
status: active
---

# SET SECARPGRAT（设置免费ARP过滤）

## 功能

该命令用于设置免费ARP过滤。

当网络中有新的设备接入时，该设备会以广播的方式发送免费ARP报文，向网络中的其他设备通告自己的存在。由于任何设备都可以发送免费ARP报文，且设备接收免费ARP报文时无需身份验证，所以网络中很容易出现大量的免费ARP报文，这会导致设备忙于免费ARP报文的处理，造成CPU超载，影响其它业务的正常运行。当网络中存在非法用户恶意发送报文内容不合理的ARP报文，可能造成协议栈崩溃或CPU利用率很高，影响正常业务。为了防止网络中出现免费ARP报文攻击，可以执行SET SECARPGRAT命令配置免费ARP报文主动丢弃的功能。设备收到免费ARP报文后直接将其丢弃，减少CPU资源的消耗，从而保证了用户业务的优先级。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| SECENABLE |
| --- |
| False |

- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：与设备接口名称保持一致，下发本MML命令前可使用LST INTERFACE查看设备接口。 |
| SECENABLE | 使能标记 | 可选必选说明：必选参数<br>参数含义：使能标记。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SECARPGRAT]] · 免费ARP过滤（SECARPGRAT）

## 使用实例

设置免费ARP过滤配置：

```
SET SECARPGRAT:IFNAME="Ethernet66/0/3",SECENABLE=TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SECARPGRAT.md`
