---
id: UNC@20.15.2@MMLCommand@ADD SUBSCRIBERIDSEGGRP
type: MMLCommand
name: ADD SUBSCRIBERIDSEGGRP（增加IMSI/MSISDN/IMEISV号段组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SUBSCRIBERIDSEGGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务公共
- IMSI MSISDN IMEISV号段组
status: active
---

# ADD SUBSCRIBERIDSEGGRP（增加IMSI/MSISDN/IMEISV号段组）

## 功能

**适用NF：PGW-C、SMF**

该命令用来配置IMSI/MSISDN/IMEISV号码段组，用于根据号段组选择USERPROFILE作为本地策略、根据号段选择OCS、用户根据号段选择OCS组以及在线计费模板、根据号段选择CG组、根据号段选择SGW离线计费方式等。

## 注意事项

- 该命令执行后立即生效。
- 如果绑定多个IMSI/MSISDN/IMEISV号码段，需多次执行此命令。
- 系统最大支持配置128条IMSI/MSISDN/IMEISV号码段组。每条IMSI/MSISDN/IMEISV号码段组最大绑定12000条IMSI/MSISDN/IMEISV号码段，号段组单个UNC绑定规格为25000个。
- 配置SUBSCRIBERIDSEGGRP前，需要首先通过ADD IMSIMSISDNSEG命令或ADD IMEISVSEG命令配置号段。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGGROUPNAME | IMSI/MSISDN/IMEISV号段组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN/IMEISV号码段组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEGMENTNAME | IMSI/MSISDN/IMEISV号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN/IMEISV号码段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD IMSIMSISDNSEG命令配置生成。 |
| SEGMENTTYPE | 号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户标识号段类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSIMSISDN：IMSIMSISDN类型号段。<br>- IMEISV：IMEISV类型号段。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SUBSCRIBERIDSEGGRP]] · IMSI/MSISDN/IMEISV号段组（SUBSCRIBERIDSEGGRP）

## 使用实例

配置IMSI/MSISDN/IMEISV号码段组内添加一个号段，其中IMSI/MSISDN/IMEISV号段组名称为group1，IMSI/MSISDN号段名称为huawei：

```
ADD SUBSCRIBERIDSEGGRP: SEGGROUPNAME="group1", SEGMENTNAME="huawei", SEGMENTTYPE=IMEISV;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IMSI_MSISDN_IMEISV号段组（ADD-SUBSCRIBERIDSEGGRP）_65997002.md`
