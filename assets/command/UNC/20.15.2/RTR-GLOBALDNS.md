---
id: UNC@20.15.2@MMLCommand@RTR GLOBALDNS
type: MMLCommand
name: RTR GLOBALDNS（恢复系统默认DNS）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: GLOBALDNS
command_category: 动作类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- DNS选择管理
- 缺省DNS
status: active
---

# RTR GLOBALDNS（恢复系统默认DNS）

## 功能

**适用NF：SMF**

该命令用于恢复系统DNS地址配置信息，即将默认值设置成无效值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNSSERVERTYPE | DNS服务器类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNS服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- DNS_IPV4（IPv4 DNS Server）<br>- DNS_IPV6（IPv6 DNS Server）<br>- DNS_64（DNS64 Server）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [系统默认DNS（GLOBALDNS）](configobject/UNC/20.15.2/GLOBALDNS.md)

## 使用实例

在运营商网络中需要清除已经配置的系统的缺省的DNS配置信息，执行该命令：

```
RTR GLOBALDNS: DNSSERVERTYPE=DNS_IPV4;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/恢复系统默认DNS（RTR-GLOBALDNS）_09652557.md`
