---
id: UNC@20.15.2@MMLCommand@MOD IMSICHAR
type: MMLCommand
name: MOD IMSICHAR（修改IMSI号段属性配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IMSICHAR
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- IMSI号段属性配置表
status: active
---

# MOD IMSICHAR（修改IMSI号段属性配置）

## 功能

**适用网元：SGSN、MME**

该命令用于修改IMSI号段属性配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定起始IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无<br>配置原则：<br>- 输入的起始IMSI必须小于或者等于终止IMSI。<br>- 输入的起始IMSI和终止IMSI定义的IMSI号段范围不允许与其它记录定义的IMSI号段范围相互交叉、包含或重合。<br>说明：判断起始IMSI和终止IMSI大小的原则是：对于输入IMSI的长度小于系统规定IMSI长度时，将该IMSI补足0到规定长度后进行大小比较，且起始IMSI必须小于终止IMSI。只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。对于系统规定IMSI长度为15的情况，如<br>[表1](#ZH-CN_MMLREF_0000001172345651__tab1)<br>所示。 |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定终止IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无<br>配置原则：终止IMSI要大于起始IMSI。 |
| SGSNNO | 本局SGSN号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定的服务GPRS支持节点（SGSN）号码，是SGSN的E.164地址。<br>前提条件：该参数已增加，参见<br>[**ADD SCCPOPC**](../../../信令传输管理/SCCP管理/SCCP本局信令点/增加SCCP本局信令点(ADD SCCPOPC)_72226009.md)<br>。<br>数据来源：整网规划<br>取值范围：1～16位十进制数字<br>默认值：无<br>说明：系统获取本端SGSN号的策略：<br>- 如果IMSICHAR表配置了，从IMSICHAR表中获取。<br>- 如果IMSICHAR中没有配置，则从HNOINFO表中获取。<br>- 如果IMSICHAR和HNOINFO都没有配置，则从SCCPOPC表中获取。 |
| LOINDEX | 本地实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定添加的本地实体的索引信息。<br>前提条件：<br>在“MML命令行-UNC”窗口上执行命令<br>[**ADD DMLE**](../../../信令传输管理/Diameter管理/Diameter本地实体/增加Diameter本端实体(ADD DMLE)_72345881.md)<br>设置此参数。<br>数据来源：本端规划<br>取值范围：0～31<br>默认值：无<br>说明：系统获取本地实体索引信息的策略：<br>- 如果IMSICHAR表配置了，从IMSICHAR表中获取。<br>- 如果IMSICHAR中没有配置，则从HNOINFO表中获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSICHAR]] · IMSI号段属性配置（IMSICHAR）

## 使用实例

修改一条IMSICHAR属性配置记录， “用户范围” 为 “指定IMSI前缀” ， “IMSI前缀” 为 “123003” ， “本局SGSN号” 为 “861390218601” ：

MOD IMSICHAR: SUBRANGE=IMSI_PREFIX, IMSIPRE="123003", SGSNNO="861390218601";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-IMSICHAR.md`
