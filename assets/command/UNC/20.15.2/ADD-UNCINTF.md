---
id: UNC@20.15.2@MMLCommand@ADD UNCINTF
type: MMLCommand
name: ADD UNCINTF（增加UNC接口名称）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UNCINTF
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
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- 北向配置管理
status: active
---

# ADD UNCINTF（增加UNC接口名称）

## 功能

**适用NF：SGSN、MME、SGW-C、AMF、PGW-C、SMF、NRF、NSSF、GGSN、SMSF、NCG**

该命令用于增加需要上报至网管北向的UNC网元所有业务或者管理接口的名称。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1000条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

> **说明**
> 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| NRMVNFTYPE | INTFTYPE |
| --- | --- |
| SMF | Mgt |
| SMF | N4 |
| SMF | Nnrf |
| SMF | N10 |
| SMF | N7 |
| SMF | N16a |
| SMF | N11 |
| SMF | Nbsf |
| SMF | N40 |
| SMF | Radius |
| SGWC | Mgt |
| SGWC | Sx |
| SGWC | Ga |
| SGWC | S5_S |
| SGWC | S8_S |
| SGWC | S11 |
| PGWC | Mgt |
| PGWC | Sx |
| PGWC | Ga |
| PGWC | Radius |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRMVNFTYPE | 北向网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UNC网元的北向网元类型。<br>数据来源：本端规划<br>取值范围：<br>- AMF（AMF）<br>- MME（MME）<br>- SGSN（SGSN）<br>- SMF（SMF）<br>- PGWC（PGWC）<br>- SGWC（SGWC）<br>- GGSNC（GGSNC）<br>- ProxySGWC（ProxySGWC）<br>- NRF（NRF）<br>- NSSF（NSSF）<br>- SMSF（SMSF）<br>- CHF（CHF）<br>- ProxySMF（ProxySMF）<br>默认值：无<br>配置原则：无 |
| INTFTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UNC网元的接口名称。其中，Mgt为网元和网管的对接接口；DnsQry为SGSN、MME、AMF网元的DNS本端实体与DNS服务器进行通信的接口；Bx为NCG网元与计费账务域交互的文件接口；其他为协议定义的接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UNCINTF]] · UNC接口名称（UNCINTF）

## 使用实例

增加需要上报至网管北向UNC网元的所有业务或者管理接口的名称，执行以下命令：

```
ADD UNCINTF:NRMVNFTYPE=ProxySMF,INTFTYPE="Mgt";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-UNCINTF.md`
