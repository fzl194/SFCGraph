---
id: UNC@20.15.2@MMLCommand@RMV PCSCFGRPBNDAPN
type: MMLCommand
name: RMV PCSCFGRPBNDAPN（删除APN和P-CSCF组关联关系）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV PCSCFGRPBNDAPN（删除APN和P-CSCF组关联关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

此命令用来删除APN和P-CSCF组关联关系，且命令支持多种删除方式。如果DEFAULTFLAG字段的值为DEFAULT，删除APN的缺省P-CSCF Group，如果DEFAULTFLAG字段的值为IMSI_MSISDN_SEG，用于解除P-CSCF组与APN的绑定关系。如果P-CSCF组参数的值均为空，解除所有P-CSCF组绑定关系，如果P-CSCF组参数的值不为空，则解除对应P-CSCF组绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 不指定号段，删除APN下缺省P-CSCF组名称绑定关系；指定号段，删除指定号段的P-CSCF组名称绑定。
- 不指定P-CSCF组，删除所有P-CSCF组名称绑定关系；指定P-CSCF组，删除对应P-CSCF组名称绑定关系。
- 删除后的P-CSCF组绑定关系需要满足配置约束。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| DEFAULTFLAG | 缺省标记 | 可选必选说明：必选参数<br>参数含义：该参数用于指定缺省标记。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（缺省）<br>- IMSI_MSISDN_SEG（IMSI/MSISDN号段）<br>默认值：无<br>配置原则：无 |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：该参数在"DEFAULTFLAG"配置为"IMSI_MSISDN_SEG"时为条件必选参数。<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数使用ADD PCSCFIMSISDNSEG命令配置生成。 |
| MPCSCFGRPIPV4 | 主IPv4 P-CSCF组 | 可选必选说明：可选参数<br>参数含义：该参数用于配置该APN的主IPv4 P-CSCF组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数由ADD PCSCFGROUP命令配置。<br>MPCSCFGRPIPV4和MPCSCFGRPIPV6至少填写1个。<br>MPCSCFGRPIPV4与SPCSCFGRPIPV4不能相同。 |
| SPCSCFGRPIPV4 | 备IPv4 P-CSCF组 | 可选必选说明：可选参数<br>参数含义：该参数用于配置该APN的备IPv4 P-CSCF组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数使用ADD PCSCFGROUP命令配置生成。<br>MPCSCFGRPIPV4与SPCSCFGRPIPV4不能相同。 |
| MPCSCFGRPIPV6 | 主IPv6 P-CSCF组 | 可选必选说明：可选参数<br>参数含义：该参数用于配置该APN的主IPv6 P-CSCF组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数使用ADD PCSCFGROUP命令配置生成。<br>MPCSCFGRPIPV4和MPCSCFGRPIPV6至少填写1个。<br>MPCSCFGRPIPV6与SPCSCFGRPIPV6不能相同。 |
| SPCSCFGRPIPV6 | 备IPv6 P-CSCF组 | 可选必选说明：可选参数<br>参数含义：该参数用于配置该APN的备IPv6 P-CSCF组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数使用ADD PCSCFGROUP命令配置生成。<br>MPCSCFGRPIPV6与SPCSCFGRPIPV6不能相同。 |

## 操作的配置对象

- [APN和P-CSCF组关联关系（PCSCFGRPBNDAPN）](configobject/UNC/20.15.2/PCSCFGRPBNDAPN.md)

## 使用实例

- 删除APN下缺省的P-CSCF组绑定关系：
  ```
  RMV PCSCFGRPBNDAPN: APN="huawei.com", DEFAULTFLAG=DEFAULT;
  ```
- 删除APN下指定号段和P-CSCF组绑定关系：
  ```
  RMV PCSCFGRPBNDAPN: APN="huawei.com", DEFAULTFLAG=IMSI_MSISDN_SEG, IMSIMSISDNSEG="imsiseg";
  ```
- 删除APN下缺省的指定P-CSCF组绑定关系：
  ```
  RMV PCSCFGRPBNDAPN: APN="huawei.com", DEFAULTFLAG=DEFAULT, MPCSCFGRPIPV4="group1";
  ```
- 删除APN下指定号段的指定P-CSCF组绑定关系：
  ```
  RMV PCSCFGRPBNDAPN: APN="huawei.com", DEFAULTFLAG=IMSI_MSISDN_SEG, IMSIMSISDNSEG="imsiseg", MPCSCFGRPIPV6="group2", SPCSCFGRPIPV6="group10";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN和P-CSCF组关联关系（RMV-PCSCFGRPBNDAPN）_09651444.md`
