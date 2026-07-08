---
id: UNC@20.15.2@MMLCommand@SET SECARPSAFEGUARD
type: MMLCommand
name: SET SECARPSAFEGUARD（设置ARP双向分离）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SECARPSAFEGUARD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- ARP双向分离
status: active
---

# SET SECARPSAFEGUARD（设置ARP双向分离）

## 功能

该命令用于设置ARP双向分离。

应答报文是本机向其他设备发出的ARP请求报文得到的正常应答，所以只要能够判定其是本机发出的，可以认定并不是攻击报文。所以要解决瞬时超过设备处理能力范围的大流量ARP攻击问题，可以将ARP请求和ARP应答分开处理。

针对ARP请求进行“无状态应答”，即直接在转发层面进行ARP应答，之后不产生ARP表项及相关的状态，不上送CPU进行处理。

针对ARP应答只上送CPU请求过的ARP报文，CPU没有发出的ARP请求产生的ARP应答报文将被丢弃，可以有效保证CPU请求过的正常主机的ARP请求报文正常处理。

## 注意事项

- 该命令执行后立即生效。
- 该命令的设定值可通过LST SECARPSAFEGUARD命令进行查询。
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
| SECENABLE | 使能标记 | 可选必选说明：必选参数<br>参数含义：使能标记。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：与设备接口名称保持一致，下发本MML命令前可使用LST INTERFACE查看设备接口。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SECARPSAFEGUARD]] · ARP双向分离（SECARPSAFEGUARD）

## 使用实例

设置ARP双向分离配置：

```
SET SECARPSAFEGUARD: SECENABLE=TRUE, IFNAME="Ethernet66/0/2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SECARPSAFEGUARD.md`
