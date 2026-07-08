---
id: UNC@20.15.2@MMLCommand@RMV PCRFGRPBNDAPN
type: MMLCommand
name: RMV PCRFGRPBNDAPN（删除APN和Pcrf组关联关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PCRFGRPBNDAPN
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- PCRF组绑定APN
status: active
---

# RMV PCRFGRPBNDAPN（删除APN和Pcrf组关联关系）

## 功能

**适用NF：PGW-C、GGSN**

此命令用来删除APN和Pcrf组关联关系。

给APN字段赋值，删除指定APN的记录；给APN和DEFAULTFLAG字段赋值，删除满足条件的记录。

如果DEFAULTFLAG字段的值为DEFAULT，删除APN的缺省PCRFGroup；如果DEFAULTFLAG字段的值为IMSI_MSISDN_SEG，用于解除PCRF组与APN的绑定关系。不指定号段，删除APN下缺省PCRF组名称绑定关系；指定号段，删除指定号段的PCRF组名称绑定。删除PCRF组与APN的绑定关系，不会影响已经建立的IP-CAN Session状态。如果删除APN绑定的PCRF组之后未重新予以绑定，之后新的IP-CAN Session将因为无法关联到PCRF而建立失败。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |
| DEFAULTFLAG | 缺省标记 | 可选必选说明：可选参数<br>参数含义：该参数用于指定缺省标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DEFAULT<br>- IMSI_MSISDN_SEG<br>默认值：无<br>配置原则：无 |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DEFAULTFLAG”配置为“IMSI_MSISDN_SEG”时为必选参数。<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN和Pcrf组关联关系（PCRFGRPBNDAPN）](configobject/UNC/20.15.2/PCRFGRPBNDAPN.md)

## 使用实例

删除APN和Pcrf组关联关系，APN为“aaa”：

```
RMV PCRFGRPBNDAPN:APN="aaa";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN和Pcrf组关联关系（RMV-PCRFGRPBNDAPN）_09897108.md`
