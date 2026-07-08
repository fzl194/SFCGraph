---
id: UNC@20.15.2@MMLCommand@RMV SUBSCRIBERIDSEGGRP
type: MMLCommand
name: RMV SUBSCRIBERIDSEGGRP（删除IMSI/MSISDN/IMEISV号段组）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV SUBSCRIBERIDSEGGRP（删除IMSI/MSISDN/IMEISV号段组）

## 功能

**适用NF：PGW-C、SMF**

该命令用来删除IMSI/MSISDN/IMEISV号码段组或号段组与号段的绑定关系。如果删除号段组，该号段组下所有的号段绑定关系同步删除。

## 注意事项

- 该命令执行后立即生效。
- 如果输入IMSI/MSISDN/IMEISV号码段组与IMSI/MSISDN/IMEISV号码段，表示解除该号码段组与号码段的绑定关系。如果只输入IMSI/MSISDN/IMEISV号码段组，表示解除该号码段组下所有号码段的绑定信息并删除该号码段组。如果此IMSI/MSISDN/IMEISV号码段组被其他命令使用，则不允许删除。可以通过LST OCSBINDING/LST OCSGRPBINDING/LST CGGRPBINDING/LST SGWSEGGCHGMETH/LST UPBINDUPG分别查询不同的引用记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGGROUPNAME | IMSI/MSISDN/IMEISV号段组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI/MSISDN/IMEISV号码段组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEGMENTNAME | IMSI/MSISDN/IMEISV号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI/MSISDN/IMEISV号码段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：若此参数未填充，则删除号段组下所有号段信息。 |
| SEGMENTTYPE | 号段类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户标识号段类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSIMSISDN：IMSIMSISDN类型号段。<br>- IMEISV：IMEISV类型号段。<br>默认值：无<br>配置原则：若指定了SegmentName，此参数需要指定。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SUBSCRIBERIDSEGGRP]] · IMSI/MSISDN/IMEISV号段组（SUBSCRIBERIDSEGGRP）

## 使用实例

删除IMSI/MSISDN/IMEISV号码段组，其中IMSI/MSISDN/IMEISV号段组名称为group1：

```
RMV SUBSCRIBERIDSEGGRP: SEGGROUPNAME="group1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SUBSCRIBERIDSEGGRP.md`
