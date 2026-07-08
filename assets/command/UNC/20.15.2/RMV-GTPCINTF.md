---
id: UNC@20.15.2@MMLCommand@RMV GTPCINTF
type: MMLCommand
name: RMV GTPCINTF（删除GTP-C接口信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GTPCINTF
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C接口信息管理
status: active
---

# RMV GTPCINTF（删除GTP-C接口信息）

## 功能

![](删除GTP-C接口信息（RMV GTPCINTF）_09654360.assets/notice_3.0-zh-cn_2.png)

该命令用于删除GTP-C接口，该命令执行后删除指定GTP-C的接口配置，导致该接口与外部通讯异常，可能影响对应业务，请谨慎操作！。

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于删除GTP-C接口信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTFTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C接口类型。<br>数据来源：全网规划<br>取值范围：<br>- E_GTPCINTF_ITFS11（S11接口）<br>- E_GTPCINTF_ITFN26（N26接口）<br>- E_GTPCINTF_ITFS5_S（S5-S接口）<br>- E_GTPCINTF_ITFS8_S（S8-S接口）<br>- S5_P_OR_GN（S5-P/GN接口）<br>- S8_P_OR_GP（S8-P/GP接口）<br>- PROXY_SGSN_GP（Proxy SGSN GP接口）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [GTP-C接口信息（GTPCINTF）](configobject/UNC/20.15.2/GTPCINTF.md)

## 使用实例

删除S11 GTP-C接口:

```
RMV GTPCINTF:INTFTYPE=E_GTPCINTF_ITFS11;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GTP-C接口信息（RMV-GTPCINTF）_09654360.md`
