---
id: UNC@20.15.2@MMLCommand@ADD CHGPLMNCFG
type: MMLCommand
name: ADD CHGPLMNCFG（增加PLMN计费配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CHGPLMNCFG
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 1500
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- PLMN计费配置
status: active
---

# ADD CHGPLMNCFG（增加PLMN计费配置）

## 功能

**适用网元：SGSN**

该命令用于根据PLMN配置话单生成策略。

## 注意事项

- 该命令执行后立即生效，但该配置只对配置生效之后激活的用户有效。
- 该表最大记录数为1500。
- 该命令和[**ADD CHGIMSICFG**](../IMSI计费配置/增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md)中各字段默认值都为无效值。若需要使用该命令或[**ADD CHGIMSICFG**](../IMSI计费配置/增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md)的配置策略，则需要设置各字段都为有效值，否则只有配置有效值的字段生效，例如当SCCL字段设置为有效值时则该字段生效，其它字段不生效。
- 当[**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)命令的“PLMN ID控制策略（PLMNCTRL）”取值为“LOCINFO（位置信息）中的PLMN ID”时，相应选择[**ADD CHGPLMNCFG**](增加PLMN计费配置(ADD CHGPLMNCFG)_72225071.md)话单生成策略；当[**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)命令的“PLMN ID控制策略（PLMNCTRL）”取值为“IMSI（IMSI中的PLMN ID）”时，相应选择[**ADD CHGIMSICFG**](../IMSI计费配置/增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md)话单生成策略。
- 此配置产生S-CDR策略组合的默认优先级由高到低的顺序为：基于PLMN和“APNNI”共同配置生成S-CDR话单策略、仅基于PLMN生成S-CDR话单策略、基于“APNNI”生成S-CDR话单策略。
- 设置最大计费条件变更次数前，要与客户计费中心确认是否能够正常处理多流量节点话单，避免出现多流量节点话单被丢弃的情况。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “CELL_PLMNID（指定CELL_PLMNID）”<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示PLMN的移动国家号码。<br>数据来源：整网规划<br>取值范围：位数为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示PLMN的移动网号码。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>说明：- 用户范围取“ALL_USER（所有用户）”值时，此参数不允许配置为“*”。<br>- 除了用户范围取“ALL_USER（所有用户）”的其他情况下，此参数只允许输入一个“*”，不允许输入多个“*”。 |
| SP | 生成S-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否生成S-CDR的标志。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不生成)”<br>- “YES(生成)”<br>- “DFT(缺省策略)”<br>默认值：<br>“DFT(缺省策略)”<br>说明：取值为<br>“DFT(缺省策略)”<br>，表示无效值。 |
| SPP | 周期生成S-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否周期生成部分S-CDR的标志。<br>数据来源：整网规划<br>取值范围：<br>- “FORBID(不生成)”：表示不周期生成S-CDR。<br>- “PERMIT(周期生成)”：表示周期生成S-CDR。<br>- “VOLUMN(有流量时周期生成)”：表示有流量时周期生成S-CDR。<br>- “DFT(缺省策略)”<br>默认值：<br>“DFT(缺省策略)”<br>说明：取值为<br>“DFT(缺省策略)”<br>，表示无效值。 |
| SPL | S-CDR生成周期（min） | 可选必选说明：可选参数<br>参数含义：该参数用于表示生成部分S-CDR的周期。<br>数据来源：整网规划<br>取值范围：0min～1440min<br>默认值：0min<br>配置原则：建议生成周期不小于15分钟。<br>说明：取值为0，表示无效值。 |
| SVP | 流量生成S-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定有流量时是否生成部分S-CDR的标志。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不生成)”<br>- “YES(生成)”<br>- “DFT(缺省策略)”<br>默认值：<br>“DFT(缺省策略)”<br>说明：取值为<br>“DFT(缺省策略)”<br>，表示无效值。 |
| SVL | 生成S-CDR流量阈值（KB） | 可选必选说明：可选参数<br>参数含义：该参数用于指定流量生成部分S-CDR的流量阈值。系统如果允许该用户流量生成部分S-CDR，则流量达到此阈值时生成部分S-CDR。<br>数据来源：整网规划<br>取值范围：0KB～1000000KB<br>默认值：0KB<br>配置原则：建议流量阈值不小于100KBYTE。<br>说明：取值为0，表示无效值。 |
| SCCP | 计费条件变更生成S-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定在计费条件发生变更时（QoS变更或者费率时段变更）是否生成部分S-CDR的标志。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不生成)”<br>- “YES(生成)”<br>- “DFT(缺省策略)”<br>默认值：<br>“DFT(缺省策略)”<br>说明：取值为<br>“DFT(缺省策略)”<br>，表示无效值。 |
| SCCL | 最大计费条件变更次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在计费条件变更时生成部分S-CDR的最大条件变更次数。系统如果允许该用户条件变更生成部分S-CDR，则计费条件变更次数达到此最大值时生成部分S-CDR。<br>数据来源：整网规划<br>取值范围：0～10<br>默认值：0<br>说明：取值为0，表示无效值。 |
| SLCP | 位置更新生成S-CDR | 可选必选说明：可选参数<br>参数含义：该参数用于指定有位置更新时是否生成部分S-CDR的标志。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不生成)”：不会导致inter RAU SGSN新侧不创建话单，只是位置更新时不会生成话单，流量或时间达到阈值仍会生成话单。<br>- “YES(生成)”：位置更新时生成话单。<br>- “DFT(缺省策略)”：位置更新是否生成S-CDR由[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)命令中的参数“位置更新生成S-CDR”取值决定。<br>默认值：<br>“DFT(缺省策略)”<br>说明：取值为<br>“DFT(缺省策略)”<br>，表示无效值。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGPLMNCFG]] · PLMN计费配置（CHGPLMNCFG）

## 关联任务

- [[UNC@20.15.2@Task@0-00021]]

## 使用实例

添加移动国家码为“123”，移动网络码为“001”，S-CDR生成周期(min)为30，计费条件变更生成S-CDR为YES，最大计费条件变更次数为5，位置更新生成S-CDR为YES的话单生成策略：

ADD CHGPLMNCFG: SUBRANGE=CELL_PLMNID, MCC="123", MNC="001", APNNI="huawei", SPL=30, SCCP=YES, SCCL=5, SLCP=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加PLMN计费配置(ADD-CHGPLMNCFG)_72225071.md`
