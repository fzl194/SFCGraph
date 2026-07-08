---
id: UNC@20.15.2@MMLCommand@ADD CHGIMSICFG
type: MMLCommand
name: ADD CHGIMSICFG（增加IMSI计费配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CHGIMSICFG
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- IMSI计费配置
status: active
---

# ADD CHGIMSICFG（增加IMSI计费配置）

## 功能

**适用网元：SGSN**

该命令用于配置基于 “IMSI前缀” 、 “APNNI” 、 “用户拜访类型” 和 “计费属性” 的计费配置信息，可以用该命令根据 “IMSI前缀” 、 “APNNI” 、 “用户拜访属性” 和 “计费属性” 配置生成话单的触发条件。

## 注意事项

- 该命令执行后立即生效，但该配置只对之后激活的用户有效。
- 此表最大记录数为2048。
- 当[**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)命令的“PLMN ID控制策略（PLMNCTRL）”取值为“LOCINFO（位置信息）中的PLMN ID”时，相应选择[**ADD CHGPLMNCFG**](../PLMN计费配置/增加PLMN计费配置(ADD CHGPLMNCFG)_72225071.md)话单生成策略；当[**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)命令的“PLMN ID控制策略（PLMNCTRL）”取值为“IMSI（IMSI中的PLMN ID）”时，相应选择[**ADD CHGIMSICFG**](增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md)话单生成策略。
- 当前系统中[**ADD HPLMN**](../../控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)和[**ADD MVNONET**](../../控制面管理/网络管理/归属网络运营商管理/MVNO管理/MVNO网络标识配置表/增加MVNO网络配置信息(ADD MVNONET)_72345663.md)配置属于本网用户，[**ADD CONNECTPLMN**](../../控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md)配置属于漫游用户。
- 如果某条配置前提为“IMSI前缀”指定用户范围，此时“拜访类型”单独配置为“Roaming”或“Visiting”时，需要确定“IMSI前缀”指定用户为外网签约用户（通过[**ADD CONNECTPLMN**](../../控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md)配置），否则此条配置无效。
- 此配置产生S-CDR策略组合的默认优先级由高到低的顺序为：基于“IMSI前缀”和“APNNI”共同配置结合“计费属性”生成S-CDR话单策略、仅基于“IMSI前缀”结合“计费属性”生成S-CDR话单策略、基于“APNNI”生成S-CDR话单策略、基于“计费属性”S-CDR话单生成策略。
- 设置最大计费条件变更次数前，要与客户计费中心确认是否能够正常处理多流量节点话单，避免出现多流量节点话单被丢弃的情况。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于系统根据指定用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：当<br>“用户范围”<br>取值为<br>“指定IMSI前缀”<br>时生效。<br>数据来源：整网规划<br>取值范围：5～15位十进制字符串<br>默认值：无 |
| VISITTYPE | 拜访类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的拜访类型。<br>数据来源：整网规划<br>取值范围：<br>- “ROAMING（使用归属地GGSN的漫游用户）”：表示使用归属地GGSN的漫游用户。<br>- “VISITING（使用拜访地GGSN的漫游用户）”：表示使用拜访地GGSN的漫游用户。<br>默认值：<br>“ROAMING（使用归属地GGSN的漫游用户）&VISITING（使用拜访地GGSN的漫游用户）”<br>说明：- 此参数仅对漫游用户生效；当ROAMING（使用归属地GGSN的漫游用户）&VISITING（使用拜访地GGSN的漫游用户）已设置时，相同的APN NI和IMSI Prefix时不能添加其它的拜访类型；<br>- 此参数不允许设置为空。 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>说明：- 用户范围取“ALL_USER（所有用户）”值时，此参数不允许配置为“*”。<br>- 除了用户范围取“ALL_USER（所有用户）”的其他情况下，此参数只允许输入一个“*”或符合上述配置原则的字符串。 |
| CC | 计费属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定计费属性。<br>数据来源：整网规划<br>取值范围：<br>- HOT_BILLING(实时计费)<br>- FLAT_RATE(包月制)<br>- PREPAID_SERVICE（预付费）<br>- NORMAL_BILLING（普通计费）<br>默认值：HOT_BILLING(实时计费)&FLAT_RATE(包月制)&PREPAID_SERVICE（预付费）&NORMAL_BILLING（普通计费）<br>说明：- 针对同一APN NI和IMSI PRE不允许计费属性选择交叉，例如：同一APN NI（HUAWEI.COM）和IMSI PRE（12301）不允许配置同时配置CC为0011–Hot Billing and Flat Rate和0101–Hot Billing and Prepaid Service两条记录。<br>- 此参数不允许设置为空。 |
| SP | 生成S-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否生成S-CDR的标志。S-CDR的标志仅在本参数设置为<br>“YES”<br>时才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不生成)”<br>- “YES(生成)”<br>- “DFT(缺省策略)”<br>默认值：<br>“DFT(缺省策略)”<br>说明：取值为<br>“DFT(缺省策略)”<br>表示该字段值无效，不指定是否生成S-CDR。 |
| SPP | 周期生成S-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否周期生成部分S-CDR的标志。<br>数据来源：整网规划<br>取值范围：<br>- “FORBID(不生成)”：表示不周期生成S-CDR。<br>- “PERMIT(周期生成)”：表示周期生成S-CDR。<br>- “VOLUMN(有流量时周期生成)”：表示有流量时周期生成S-CDR。<br>- “DFT(缺省策略)”<br>默认值：<br>“DFT(缺省策略)”<br>说明：取值为<br>“DFT(缺省策略)”<br>表示该字段值无效，不指定是否生成S-CDR。 |
| SPL | S-CDR生成周期（min） | 可选必选说明：可选参数<br>参数含义：该参数用于表示生成部分S-CDR的周期。<br>数据来源：整网规划<br>取值范围： 0min～1440min<br>默认值：0min<br>说明：- 0表示无效值。<br>- 建议生成周期不小于15分钟。 |
| SVP | 流量生成S-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定有流量时是否生成部分S-CDR的标志。流量生成S-CDR标志仅在本参数设置为<br>“YES”<br>时才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不生成)”<br>- “YES(生成)”<br>- “DFT(缺省策略)”<br>默认值：<br>“DFT(缺省策略)”<br>说明：取值为<br>“DFT(缺省策略)”<br>表示该字段值无效，不指定是否生成S-CDR。 |
| SVL | 生成S-CDR流量阈值（KB） | 可选必选说明：可选参数<br>参数含义：该参数用于指定流量生成部分S-CDR的流量阈值。系统如果允许该用户流量生成部分S-CDR，则流量达到此阈值时生成部分S-CDR。<br>数据来源：整网规划<br>取值范围：0KB～1000000KB<br>默认值：0KB<br>说明：0表示无效值。 |
| SCCP | 计费条件变更生成S-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定在计费条件发生变更时（QoS变更或者费率时段变更）是否生成部分S-CDR的标志。计费条件变更生成S-CDR标志仅在本参数设置为<br>“YES”<br>时才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不生成)”<br>- “YES(生成)”<br>- “DFT(缺省策略)”<br>默认值：<br>“DFT(缺省策略)”<br>说明：取值为<br>“DFT(缺省策略)”<br>表示该字段值无效，不指定是否生成S-CDR。 |
| SCCL | 最大计费条件变更次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在计费条件变更时生成部分S-CDR的最大条件变更次数。系统如果允许该用户条件变更生成部分S-CDR，则计费条件变更次数达到此最大值时生成部分S-CDR。<br>数据来源：整网规划<br>取值范围：0～10<br>默认值：0<br>说明：0表示无效值。 |
| SLCP | 位置更新生成S-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定有位置更新时是否生成部分S-CDR的标志。位置更新生成S-CDR标志仅在本参数设置为<br>“YES”<br>时才有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不生成)”：不会导致inter RAU SGSN新侧不创建话单，只是位置更新时不会生成话单，流量或时间达到阈值仍会生成话单。<br>- “YES(生成)”：位置更新时生成话单。<br>- “DFT(缺省策略)”：位置更新是否生成S-CDR由[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)命令中的参数“位置更新生成S-CDR”取值决定。<br>默认值：<br>“DFT(缺省策略)”<br>说明：取值为<br>“DFT(缺省策略)”<br>表示该字段值无效，不指定是否生成S-CDR。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGIMSICFG]] · IMSI计费配置（CHGIMSICFG）

## 关联任务

- [[UNC@20.15.2@Task@0-00020]]

## 使用实例

配置 “IMSI前缀” 为 “1230362” 的外网用户， “拜访类型” 为 “使用归属地GGSN的漫游用户” ， “APNNI” 取值为 “1” ， “计费属性” 为 “实时计费” 且不生成S-CDR：

ADD CHGIMSICFG: SUBRANGE=IMSI_PREFIX, IMSIPRE="1230362", VISITTYPE=ROAMING-1&VISITING-0, APNNI="1", CC=HOT_BILLING-1&FLAT_RATE-0&PREPAID_SERVICE-0&NORMAL_BILLING-0, SP=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-CHGIMSICFG.md`
