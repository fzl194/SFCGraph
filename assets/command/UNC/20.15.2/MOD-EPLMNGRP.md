---
id: UNC@20.15.2@MMLCommand@MOD EPLMNGRP
type: MMLCommand
name: MOD EPLMNGRP（修改等价PLMN组）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: EPLMNGRP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- 等价PLMN组管理
status: active
---

# MOD EPLMNGRP（修改等价PLMN组）

## 功能

**适用NF：AMF**

该命令用于修改等价PLMN（Equivalent PLMN）组。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPIDX | 等价PLMN组号 | 可选必选说明：必选参数<br>参数含义：该参数用于在UNC系统内唯一标识一个等价PLMN组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |
| PLMNIDX | PLMN索引 | 可选必选说明：可选参数<br>参数含义：该参数表示配置等价PLMN列表的Serving PLMN的索引信息，需要通过ADD NGSRVPLMN提前配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |
| USRGRPID | 用户群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于标识EPLMN适用的用户群信息，需要通过ADD NGUSRGRP提前配置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：无 |
| TACGRPID | 跟踪区域组ID | 可选必选说明：可选参数<br>参数含义：该参数用于标识等价PLMN适用的区域，需要通过ADD EPLMNAREAMEM提前配置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：<br>如果该参数没有配置，则表示不需要根据区域来限制用户使用指定的等价PLMN列表。<br>当TACGRPID未输入取值时，系统会为此参数赋无效值4294967295(0xFFFFFFFF)。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于对等价PLMN组的描述，在运维中起助记的作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [等价PLMN组（EPLMNGRP）](configobject/UNC/20.15.2/EPLMNGRP.md)

## 使用实例

将组号为0的等价PLMN应用的Serving PLMN从12345改成123678，其中Serving PLMN 123678的索引为1，执行如下命令：

```
MOD EPLMNGRP: GRPIDX=0, PLMNIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改等价PLMN组（MOD-EPLMNGRP）_09651849.md`
