---
id: UNC@20.15.2@MMLCommand@STR OFFLOADBYSGSN
type: MMLCommand
name: STR OFFLOADBYSGSN（启动SGSN迁移任务）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: OFFLOADBYSGSN
command_category: 动作类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 迁移控制
status: active
---

# STR OFFLOADBYSGSN（启动SGSN迁移任务）

## 功能

**适用网元：SGSN**

此命令用于启动SGSN迁移任务：

1. 启动以SGSN为单位的迁移任务，如指定目的SGSN则将本SGSN上的用户按设定的迁入百分比迁移到各个目的SGSN中。
2. 未指定目的SGSN则由RAN侧选择目的SGSN。

## 注意事项

- 此命令执行后立即生效。
- 启动迁移前必须确保已通过[**SET OFFLOADINF**](设置迁移配置表（SET OFFLOADINF）_72345695.md)命令设置过迁移参数信息，且保证迁移参数中的“NULL NRI值”已配置，否则将无法启动迁移任务。
- 迁移启动前需确保在本SGSN所在Pool内所有RNC/BSC上将本SGSN的状态设置为“Offload”，以避免RNC/BSC将被迁移用户和漫游至Pool内的新用户接入到本SGSN。
- 此命令将导致本SGSN下的用户被迁移到其它SGSN必须慎重使用。
- 类型为“IMSI(IMSI)”的迁移主要用于拨测，若多次启动该类型迁移任务，则只有最近一次启动的迁移任务生效。
- 如果系统当前已启动DCN迁移或POOL迁移任务且未结束，则不能再启动新的迁移任务。请执行[**DSP DCNOFFLOAD**](../DCN迁移控制/查询DCN迁移状态(DSP DCNOFFLOAD)_26305932.md)和[**DSP OFFLOAD**](显示迁移进度(DSP OFFLOAD)_72345691.md)命令查询系统迁移任务状态。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFFLOADTYPE | 迁移类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定迁移任务的迁移类型。<br>取值范围：<br>- “ALL（全部flex用户）”：表示将本SGSN上所有支持Flex功能的用户迁移到其它SGSN。<br>- “PART（部分用户）”：表示将本SGSN上指定数目的支持Flex功能的用户迁移到其它SGSN。<br>- “RATE（百分比）”：表示将本SGSN上指定百分比的支持Flex功能的用户迁移到其它SGSN。<br>- “IMSI（IMSI）”：表示将特定IMSI用户迁移到其它SGSN，指定的用户必须支持Flex功能。<br>- “MSISDN（MSISDN）”：表示将MSISDN范围内的用户迁移到其它SGSN，用户必须支持Flex功能。<br>默认值：无<br>说明：当迁移类型为IMSI时，最多指定一个目的SGSN。 |
| OFFLOADNUM | 迁移总数 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定迁移任务的迁移总数。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“PART（部分用户）”<br>值后生效。<br>取值范围：1~4294967295<br>默认值：无 |
| OFFLOADRATE | 迁移比率 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定迁移任务的迁移比率。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“RATE（百分比）”<br>值后生效。<br>取值范围：1~100<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定迁移任务的国际移动用户标识。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“IMSI（IMSI）”<br>值后生效。<br>取值范围：长度不超过15的字符串<br>默认值：无 |
| BEGMSISDN | 起始MSISDN | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定迁移任务的起始MSISDN标识。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| ENDMSISDN | 终止MSISDN | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定迁移任务的终止MSISDN标识。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| NRI_1 | NRI_1 | 可选必选说明：可选参数<br>参数含义：该参数用于指定目的SGSN_1对应的NRI值。<br>取值范围：0~1023<br>默认值：无 |
| OFFPERCENT_1 | 迁入百分比_1 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_1对应的迁入用户百分比。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：1~100<br>默认值：无<br>说明：- 各目的SGSN迁入用户百分比之和必须为100。<br>- 当输入迁入百分比时，则将本SGSN上迁出的用户按指定的百分比迁移到各个目的SGSN中； 如果未输入迁入百分比，则将本SGSN上迁出的用户平均分配到各个目的SGSN中。 |
| NRI_2 | NRI_2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_2对应的NRI值。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：0~1023<br>默认值：无 |
| OFFPERCENT_2 | 迁入百分比_2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_2对应的迁入用户百分比。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：1~100<br>默认值：无<br>说明：- 各目的SGSN迁入用户百分比之和必须为100。<br>- 当输入迁入百分比时，则将本SGSN上迁出的用户按指定的百分比迁移到各个目的SGSN中； 如果未输入迁入百分比，则将本SGSN上迁出的用户平均分配到各个目的SGSN中。 |
| NRI_3 | NRI_3 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_3对应的NRI值。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：0~1023<br>默认值：无 |
| OFFPERCENT_3 | 迁入百分比_3 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_3对应的迁入用户百分比。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：1~100<br>默认值：无<br>说明：- 各目的SGSN迁入用户百分比之和必须为100。<br>- 当输入迁入百分比时，则将本SGSN上迁出的用户按指定的百分比迁移到各个目的SGSN中； 如果未输入迁入百分比，则将本SGSN上迁出的用户平均分配到各个目的SGSN中。 |
| NRI_4 | NRI_4 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_4对应的NRI值。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：0~1023<br>默认值：无 |
| OFFPERCENT_4 | 迁入百分比_4 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_4对应的迁入用户百分比。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：1~100<br>默认值：无<br>说明：- 各目的SGSN迁入用户百分比之和必须为100。<br>- 当输入迁入百分比时，则将本SGSN上迁出的用户按指定的百分比迁移到各个目的SGSN中； 如果未输入迁入百分比，则将本SGSN上迁出的用户平均分配到各个目的SGSN中。 |
| NRI_5 | NRI_5 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_5对应的NRI值。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：0~1023<br>默认值：无 |
| OFFPERCENT_5 | 迁入百分比_5 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_5对应的迁入用户百分比。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：1~100<br>默认值：无<br>说明：- 各目的SGSN迁入用户百分比之和必须为100。<br>- 当输入迁入百分比时，则将本SGSN上迁出的用户按指定的百分比迁移到各个目的SGSN中； 如果未输入迁入百分比，则将本SGSN上迁出的用户平均分配到各个目的SGSN中。 |
| NRI_6 | NRI_6 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_6对应的NRI值。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：0~1023<br>默认值：无 |
| OFFPERCENT_6 | 迁入百分比_6 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_6对应的迁入用户百分比。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：1~100<br>默认值：无<br>说明：- 各目的SGSN迁入用户百分比之和必须为100。<br>- 当输入迁入百分比时，则将本SGSN上迁出的用户按指定的百分比迁移到各个目的SGSN中； 如果未输入迁入百分比，则将本SGSN上迁出的用户平均分配到各个目的SGSN中。 |
| NRI_7 | NRI_7 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_7对应的NRI值。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：0~1023<br>默认值：无 |
| OFFPERCENT_7 | 迁入百分比_7 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_7对应的迁入用户百分比。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：1~100<br>默认值：无<br>说明：- 各目的SGSN迁入用户百分比之和必须为100。<br>- 当输入迁入百分比时，则将本SGSN上迁出的用户按指定的百分比迁移到各个目的SGSN中； 如果未输入迁入百分比，则将本SGSN上迁出的用户平均分配到各个目的SGSN中。 |
| NRI_8 | NRI_8 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_8对应的NRI值。前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：0~1023<br>默认值：无 |
| OFFPERCENT_8 | 迁入百分比_8 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_8对应的迁入用户百分比。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：1~100<br>默认值：无<br>说明：- 各目的SGSN迁入用户百分比之和必须为100。<br>- 当输入迁入百分比时，则将本SGSN上迁出的用户按指定的百分比迁移到各个目的SGSN中； 如果未输入迁入百分比，则将本SGSN上迁出的用户平均分配到各个目的SGSN中。 |
| NRI_9 | NRI_9 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_9对应的NRI值。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：0~1023<br>默认值：无 |
| OFFPERCENT_9 | 迁入百分比_9 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_9对应的迁入用户百分比。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：1~100<br>默认值：无<br>说明：- 各目的SGSN迁入用户百分比之和必须为100。<br>- 当输入迁入百分比时，则将本SGSN上迁出的用户按指定的百分比迁移到各个目的SGSN中； 如果未输入迁入百分比，则将本SGSN上迁出的用户平均分配到各个目的SGSN中。 |
| NRI_10 | NRI_10 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_10对应的NRI值。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：0~1023<br>默认值：无 |
| OFFPERCENT_10 | 迁入百分比_10 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定目的SGSN_10对应的迁入用户百分比。<br>前提条件：该参数在<br>“OFFLOADTYPE（迁移类型）”<br>参数配置为<br>“ALL（全部flex用户）”<br>、<br>“PART（部分用户）”<br>、<br>“RATE（百分比）”<br>、<br>“MSISDN（MSISDN）”<br>值后生效。<br>取值范围：1~100<br>默认值：无<br>说明：- 各目的SGSN迁入用户百分比之和必须为100。<br>- 当输入迁入百分比时，则将本SGSN上迁出的用户按指定的百分比迁移到各个目的SGSN中； 如果未输入迁入百分比，则将本SGSN上迁出的用户平均分配到各个目的SGSN中。 |

## 操作的配置对象

- [SGSN迁移任务（OFFLOADBYSGSN）](configobject/UNC/20.15.2/OFFLOADBYSGSN.md)

## 使用实例

1. 将本SGSN中全部支持Flex功能的用户迁移到其它SGSN，不指定目的SGSN：
  STR OFFLOADBYSGSN: OFFLOADTYPE=ALL;
2. 将本SGSN中10000个支持Flex功能的用户迁移到NRI为9和10的两个SGSN上，两个SGSN的迁入用户百分比分别为80%和20%：
  STR OFFLOADBYSGSN: OFFLOADTYPE=PART, OFFLOADNUM=10000, NRI_1=9, OFFPERCENT_1=80, NRI_2=10, OFFPERCENT_2=20;
3. 将本SGSN中30％支持Flex功能的用户，迁移到NRI为9和10的两个SGSN上，不指定迁入百分比：
  STR OFFLOADBYSGSN: OFFLOADTYPE=RATE, OFFLOADRATE=30, NRI_1=9, NRI_2=10;
4. 将本SGSN中IMSI为123006666666663的用户，迁移到其它SGSN，不指定目的SGSN：
  STR OFFLOADBYSGSN: OFFLOADTYPE=IMSI, IMSI="123006666666663";
5. 将本SGSN中MSISDN区段从861390000到861399999的用户，迁移到其它SGSN，不指定目的SGSN：
  STR OFFLOADBYSGSN: OFFLOADTYPE=MSISDN, BEGMSISDN="861390000", ENDMSISDN="861399999";

> **说明**
> 指定MSISDN迁移的MSISDN形式应与DSP MMCTX命令执行结果中的MSISDN的形式保持一致，如DSP MMCTX执行结果中的MSISDN的形式为“86******”则指定MSISDN迁移的MSISDN形式也应为这种形式。

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动SGSN迁移任务（STR-OFFLOADBYSGSN）_26305904.md`
