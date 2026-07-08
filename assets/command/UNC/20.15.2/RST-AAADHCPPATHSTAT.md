---
id: UNC@20.15.2@MMLCommand@RST AAADHCPPATHSTAT
type: MMLCommand
name: RST AAADHCPPATHSTAT（复位RADIUS或DHCP链路状态）
nf: UNC
version: 20.15.2
verb: RST
object_keyword: AAADHCPPATHSTAT
command_category: 动作类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 重置RADIUS或DHCP链路状态
status: active
---

# RST AAADHCPPATHSTAT（复位RADIUS或DHCP链路状态）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于手动复位RADIUS或DHCP链路状态，当对端服务器为直连RADIUS服务器、中转RADIUS服务器或DHCP服务器且链路状态为异常时，执行本命令可将链路状态全部置为正常。

## 注意事项

- 该命令执行后立即生效。

- 当对端服务器设置为RADIUS服务器时，本命令只对RADIUS鉴权服务器生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESETSERVERTYPE | 复位链路对端服务器类型 | 可选必选说明：必选参数<br>参数含义：复位链路状态时，对端的服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- RADIUSDIRECT（RADIUS直连服务器）<br>- RADIUSTRANSFER（RADIUS中转服务器）<br>- DHCPSERVER（DHCP服务器）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [复位RADIUS或DHCP链路状态（AAADHCPPATHSTAT）](configobject/UNC/20.15.2/AAADHCPPATHSTAT.md)

## 使用实例

配置通过直连的方式连接到RADIUS服务器，当对端RADIUS服务器链路状态为异常时，通过本命令进行复位，可以恢复对端RADIUS服务器的链路状态为正常。

```
RST AAADHCPPATHSTAT: RESETSERVERTYPE=RADIUSDIRECT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/复位RADIUS或DHCP链路状态（RST-AAADHCPPATHSTAT）_15764440.md`
