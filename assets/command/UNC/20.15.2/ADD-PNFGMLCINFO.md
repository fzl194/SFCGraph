---
id: UNC@20.15.2@MMLCommand@ADD PNFGMLCINFO
type: MMLCommand
name: ADD PNFGMLCINFO（增加对端GMLC的信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PNFGMLCINFO
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端GMLC信息管理
status: active
---

# ADD PNFGMLCINFO（增加对端GMLC的信息）

## 功能

**适用NF：AMF**

该命令用于增加本地配置的对端GMLC支持的外部客户端类型。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入100条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）建议为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度建议不超过18且不输入只包含0-9和“.”的字符串，例如：1.2.3.4、不建议输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：无 |
| CLIENTTYPES | 外部客户端类型 | 可选必选说明：可选参数<br>参数含义：此参数用于表示该GMLC用于服务的外部客户端类型。此参数为空并且通过ADD PNFWILDCARD命令打开了CLIENTTYPE通配开关意味着GMLC可以用于所有客户端类型。<br>数据来源：全网规划<br>取值范围：<br>- EMERGENCY_SERVICES（紧急服务的外部客户端）<br>- VALUE_ADDED_SERVICES（增值业务外部客户端）<br>- PLMN_OPERATOR_SERVICES（PLMN运营商业务外部客户端）<br>- LAWFUL_INTERCEPT_SERVICES（合法拦截服务的外部客户端）<br>- PLMN_OPERATOR_BROADCAST_SERVICES（PLMN运营商广播业务外部客户端）<br>- PLMN_OPERATOR_OM（PLMN运营商运维外部客户端）<br>- PLMN_OPERATOR_ANONYMOUS_STATISTI（PLMN操作员匿名统计外部客户端）<br>- PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT（PLMN运营商目标MS服务支持的外部客户端）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [对端GMLC信息（PNFGMLCINFO）](configobject/UNC/20.15.2/PNFGMLCINFO.md)

## 使用实例

增加对端GMLC的信息，NF标识为GMLC_Instance_0，外部客户端类型为EMERGENCY_SERVICES;

```
ADD PNFGMLCINFO: NFINSTANCEID="GMLC_Instance_0", CLIENTTYPES=EMERGENCY_SERVICES-0&PLMN_OPERATOR_SERVICES-0&LAWFUL_INTERCEPT_SERVICES-0&PLMN_OPERATOR_BROADCAST_SERVICES-0&PLMN_OPERATOR_OM-0&PLMN_OPERATOR_ANONYMOUS_STATISTI-0&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT-0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加对端GMLC的信息（ADD-PNFGMLCINFO）_02910210.md`
