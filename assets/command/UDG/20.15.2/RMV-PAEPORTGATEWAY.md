---
id: UDG@20.15.2@MMLCommand@RMV PAEPORTGATEWAY
type: MMLCommand
name: RMV PAEPORTGATEWAY（删除网关转发地址）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PAEPORTGATEWAY
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# RMV PAEPORTGATEWAY（删除网关转发地址）

## 功能

![](删除网关转发地址（RMV PAEPORTGATEWAY）_98164009.assets/notice_3.0-zh-cn.png)

删除网关地址后，可能会导致内联口报文无法跨子网通信，业务会出现呼损。同时会产生告警“ALM-100338 Fabric平面状态为Down”。请联系华为技术支持协助操作。

该命令用于删除指定网段索引下内联口的网关地址。

> **说明**
> - 该命令执行后立即生效。
>
> - 当有内联口在使用该网段时，不允许删除。可以通过[**DSP PAEPORTGATEWAY**](../端口/显示PAE端口网关信息（DSP PAEPORTGATEWAY）_48803866.md)命令查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NETWORKINDEX | 网段索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网段索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [PAE端口网关信息（PAEPORTGATEWAY）](configobject/UDG/20.15.2/PAEPORTGATEWAY.md)

## 使用实例

删除网段索引为1的内联口的网关地址：

```
RMV PAEPORTGATEWAY: NETWORKINDEX=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除网关转发地址（RMV-PAEPORTGATEWAY）_98164009.md`
