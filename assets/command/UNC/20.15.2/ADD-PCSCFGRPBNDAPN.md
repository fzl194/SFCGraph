---
id: UNC@20.15.2@MMLCommand@ADD PCSCFGRPBNDAPN
type: MMLCommand
name: ADD PCSCFGRPBNDAPN（增加APN和P-CSCF组关联关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PCSCFGRPBNDAPN
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- IMS管理
- P-CSCF管理
- P-CSCF组与APN关联关系
status: active
---

# ADD PCSCFGRPBNDAPN（增加APN和P-CSCF组关联关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于将指定的P-CSCF组绑定到APN上，或在APN视图下的指定号段。

## 注意事项

- 该命令执行后立即生效。

- 每个APN下最多绑定10个号段，缺省配置最多有一个，也可以没有。
- 在业务处理过程中，如果SET APNIMSATTR的IMSSWITCH参数配置为ENABLE，则优先按照APN下的P-CSCF组和号段的绑定关系进行P-CSCF组选择，只有当所有号段都匹配不成功时，才会选用APN下的缺省P-CSCF组。未通过本命令明确指定缺省P-CSCF时，本命令配置的P-CSCF组和号段的绑定关系不生效。
- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| DEFAULTFLAG | 缺省标记 | 可选必选说明：必选参数<br>参数含义：该参数用于指定缺省标记。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（缺省）<br>- IMSI_MSISDN_SEG（IMSI/MSISDN号段）<br>默认值：无<br>配置原则：无 |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：该参数在"DEFAULTFLAG"配置为"IMSI_MSISDN_SEG"时为条件必选参数。<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数使用ADD PCSCFIMSISDNSEG命令配置生成。 |
| PRIORITY | 优先级 | 可选必选说明：该参数在"DEFAULTFLAG"配置为"IMSI_MSISDN_SEG"时为条件必选参数。<br>参数含义：该参数用于指定一个不重复的优先级。当一个IMSI/MSISDN匹配到两个或两个以上的P-CSCF组时，UNC优先选择优先级最高的P-CSCF组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。优先级不能重复。<br>默认值：无<br>配置原则：<br>取值越小，优先级越高。 |
| MPCSCFGRPIPV4 | 主IPv4 P-CSCF组 | 可选必选说明：可选参数<br>参数含义：该参数用于配置该APN的主IPv4 P-CSCF组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数由ADD PCSCFGROUP命令配置。<br>MPCSCFGRPIPV4和MPCSCFGRPIPV6至少填写1个。<br>MPCSCFGRPIPV4与SPCSCFGRPIPV4不能相同。 |
| SPCSCFGRPIPV4 | 备IPv4 P-CSCF组 | 可选必选说明：可选参数<br>参数含义：该参数用于配置该APN的备IPv4 P-CSCF组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数使用ADD PCSCFGROUP命令配置生成。<br>MPCSCFGRPIPV4与SPCSCFGRPIPV4不能相同。 |
| MPCSCFGRPIPV6 | 主IPv6 P-CSCF组 | 可选必选说明：可选参数<br>参数含义：该参数用于配置该APN的主IPv6 P-CSCF组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数使用ADD PCSCFGROUP命令配置生成。<br>MPCSCFGRPIPV4和MPCSCFGRPIPV6至少填写1个。<br>MPCSCFGRPIPV6与SPCSCFGRPIPV6不能相同。 |
| SPCSCFGRPIPV6 | 备IPv6 P-CSCF组 | 可选必选说明：可选参数<br>参数含义：该参数用于配置该APN的备IPv6 P-CSCF组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数使用ADD PCSCFGROUP命令配置生成。<br>MPCSCFGRPIPV6与SPCSCFGRPIPV6不能相同。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCSCFGRPBNDAPN]] · APN和P-CSCF组关联关系（PCSCFGRPBNDAPN）

## 使用实例

- 在P-CSCF组绑定到APN下将某固定号段：
  ```
  ADD PCSCFGRPBNDAPN: APN="huawei.com", DEFAULTFLAG=IMSI_MSISDN_SEG, IMSIMSISDNSEG="imsiseg1", PRIORITY=1, MPCSCFGRPIPV4="group1", SPCSCFGRPIPV4="group2", MPCSCFGRPIPV6="group10", SPCSCFGRPIPV6="group20";
  ```
- 将P-CSCF组绑定到APN：
  ```
  ADD PCSCFGRPBNDAPN: APN="huawei.com", DEFAULTFLAG=DEFAULT, MPCSCFGRPIPV4="group1", SPCSCFGRPIPV4="group2", MPCSCFGRPIPV6="group10", SPCSCFGRPIPV6="group11";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加APN和P-CSCF组关联关系（ADD-PCSCFGRPBNDAPN）_09653091.md`
