---
id: UNC@20.15.2@MMLCommand@RMV IMSIMSISDNSEG
type: MMLCommand
name: RMV IMSIMSISDNSEG（删除IMSI和MSISDN号段）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IMSIMSISDNSEG
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务公共
- IMSI MSISDN号段
status: active
---

# RMV IMSIMSISDNSEG（删除IMSI和MSISDN号段）

## 功能

**适用NF：PGW-C、SMF**

![](删除IMSI和MSISDN号段（RMV IMSIMSISDNSEG）_09897130.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，如果不输入IMSI/MSISDN号段名称，表示删除系统内的所有IMSI/MSISDN号码段。删除后引用IMSI/MSISDN号码段的用户可能会因为无法命中PCRFGRPBNDAPN/GLBPCRFGROUP/UPBINDUPG/SUBSCRIBERIDSEGGRP/GLBDIAMREALM/L2RULEGRPBIND导致业务受损，请谨慎使用并联系华为支持协助操作。

该命令用于删除IMSI/MSISDN号码段。

## 注意事项

- 该命令执行后立即生效。
- 如果输入的字段SEGMENTNAME被引用，则不能删除该记录。可以通过LST PCRFGRPBNDAPN/LST GLBPCRFGROUP/LST UPBINDUPG/LST SUBSCRIBERIDSEGGRP/LST GLBDIAMREALM/LST L2RULEGRPBIND分别查询不同的引用记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：若此参数未填充，则删除所有号段。 |

## 操作的配置对象

- [IMSI和MSISDN号段（IMSIMSISDNSEG）](configobject/UNC/20.15.2/IMSIMSISDNSEG.md)

## 使用实例

删除IMSI和MSISDN号段，SEGMENTNAME为huawei，命令为：

```
RMV IMSIMSISDNSEG:SEGMENTNAME="huawei";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IMSI和MSISDN号段（RMV-IMSIMSISDNSEG）_09897130.md`
