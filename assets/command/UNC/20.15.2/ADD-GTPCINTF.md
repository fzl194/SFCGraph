---
id: UNC@20.15.2@MMLCommand@ADD GTPCINTF
type: MMLCommand
name: ADD GTPCINTF（增加GTP-C接口信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GTPCINTF
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C接口信息管理
status: active
---

# ADD GTPCINTF（增加GTP-C接口信息）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于增加GTP-C接口信息。

## 注意事项

- 命令执行后只对新接入用户生效。

- 4/5G互操作时如果是with N26场景则需要配置N26接口，如果是without N26场景则不需要配置N26接口。
- SGW-C/PGW-C合一场景下，S5-S和S5-P/Gn接口的配置都需要配置。
- S5-S和S8-S接口的组号允许相同。S5-P/Gn和S8-P/Gp接口的组号允许相同。其余接口的组号皆不允许相同。
- 同一接口类型只能配置一个组号。

- 最多可输入7条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTFTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C接口类型。<br>数据来源：全网规划<br>取值范围：<br>- E_GTPCINTF_ITFS11（S11接口）<br>- E_GTPCINTF_ITFN26（N26接口）<br>- E_GTPCINTF_ITFS5_S（S5-S接口）<br>- E_GTPCINTF_ITFS8_S（S8-S接口）<br>- S5_P_OR_GN（S5-P/GN接口）<br>- S8_P_OR_GP（S8-P/GP接口）<br>- PROXY_SGSN_GP（Proxy SGSN GP接口）<br>默认值：无<br>配置原则：无 |
| GROUPID | 组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C本地实体的组号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~31。该参数需要从ADD GTPCLEGRP以及ADD GTPCLEGRPMEM命令中已配置的组号参数中取值。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [GTP-C接口信息（GTPCINTF）](configobject/UNC/20.15.2/GTPCINTF.md)

## 使用实例

增加S11 GTP-C接口，组号为已通过ADD GTPCLEGRP以及ADD GTPCLEGRPMEM命令配置的组号0：

```
ADD GTPCINTF:INTFTYPE=E_GTPCINTF_ITFS11,GROUPID=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加GTP-C接口信息（ADD-GTPCINTF）_09651576.md`
