---
id: UNC@20.15.2@MMLCommand@RMV UNCINTFALL
type: MMLCommand
name: RMV UNCINTFALL（删除UNC所有接口名称）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UNCINTFALL
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SGW-C
- AMF
- PGW-C
- SMF
- NRF
- NSSF
- GGSN
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- 北向配置管理
status: active
---

# RMV UNCINTFALL（删除UNC所有接口名称）

## 功能

![](删除UNC所有接口名称（RMV UNCINTFALL）_50572312.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作此命令会导致已上报至北向的网元的接口信息全部被删除，影响北向上报。

**适用NF：SGSN、MME、SGW-C、AMF、PGW-C、SMF、NRF、NSSF、GGSN、SMSF、NCG**

该命令用于删除已经上报至网管北向UNC网元的所有业务或者管理接口的名称。

## 注意事项

- 该命令执行后立即生效。

- 如果需要执行此命令，删除所有上报给网管北向的接口信息，不配置输入参数即可。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRMVNFTYPE | 北向网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC网元的北向网元类型。<br>数据来源：本端规划<br>取值范围：<br>- AMF（AMF）<br>- MME（MME）<br>- SGSN（SGSN）<br>- SMF（SMF）<br>- PGWC（PGWC）<br>- SGWC（SGWC）<br>- GGSNC（GGSNC）<br>- ProxySGWC（ProxySGWC）<br>- NRF（NRF）<br>- NSSF（NSSF）<br>- SMSF（SMSF）<br>- CHF（CHF）<br>- ProxySMF（ProxySMF）<br>默认值：无<br>配置原则：无 |
| INTFTYPE | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UNC网元的接口名称。其中，Mgt为网元和网管的对接接口；DnsQry为SGSN、MME、AMF网元的DNS本端实体与DNS服务器进行通信的接口；Bx为NCG网元与计费账务域交互的文件接口；其他为协议定义的接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UNCINTFALL]] · UNC所有接口名称（UNCINTFALL）

## 使用实例

删除已经上报至网管北向UNC网元的所有业务或者管理接口的名称，执行以下命令：

```
RMV UNCINTFALL:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UNC所有接口名称（RMV-UNCINTFALL）_50572312.md`
