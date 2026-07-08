---
id: UNC@20.15.2@MMLCommand@ADD IUSUBRRLST
type: MMLCommand
name: ADD IUSUBRRLST（增加Iu模式用户漫游限制列表）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IUSUBRRLST
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 区域漫游限制管理
- Iu模式用户漫游限制管理
status: active
---

# ADD IUSUBRRLST（增加Iu模式用户漫游限制列表）

## 功能

**适用网元：SGSN**

该命令用于增加Iu模式用户漫游限制列表，此命令可基于“用户范围”配置禁止或允许某用户范围接入的“黑名单”、“白名单”区域，控制用户是否允许接入当前所在的区域。

## 注意事项

- 该命令执行后立即生效。
- 最多可以输入2048条记录。
- 如果[**ADD IUACCAREALST**](../Iu模式区域漫游限制参数/增加Iu模式区域漫游限制参数(ADD IUACCAREALST)_72345151.md)配置或当前配置中存在禁止用户接入的记录，那么用户会被禁止接入。
- 当该配置增加上百条记录时，对系统性能影响较大。
- 输入的起始IMSI必须小于或者等于终止IMSI。判断起始IMSI和终止IMSI大小的原则是：对于输入IMSI的长度小于系统规定IMSI长度时，将该IMSI补足0到规定长度后进行大小比较，且起始IMSI必须小于终止IMSI。只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。 对于系统规定IMSI长度为15的情况，如[表1](#ZH-CN_MMLREF_0000001126305360__tab1)所示：
  *表1 IMSI限定范围*

  | 起始IMSI | 终止IMSI | 实际限定IMSI范围 |
  | --- | --- | --- |
  | 123002666 | 123002 | 增加记录失败，起始IMSI大于终止IMSI |
  | 123002 | 123002666 | 123002000000000 ～ 123002666000000，即区间[123002000000000，123002666000000] |
  | 123002 | 123002 | 增加记录失败，起始IMSI不能等于终止IMSI |
  | 123002000000000 | 123002000000000 | 仅限定IMSI号码123002000000000 |
  | 123003000000000 | 123004000000000 | 123003000000000 ～ 123004000000000，即区间[123003000000000，123004000000000] |
- 输入的起始IMSI和终止IMSI定义的IMSI号段范围不允许与其它记录定义的IMSI号段范围相互交叉、包含或重合。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>- “IMSI_RANGE（指定IMSI范围）”<br>- “FOREIGN_USER（外网用户）”<br>- “HOME_USER（本网用户）”<br>- “ALL_USER（所有用户）”<br>默认值：无<br>配置原则：<br>- “IMSI_PREFIX（指定IMSI前缀）”和“IMSI_RANGE（指定IMSI范围）”取值对应的记录不能同时存在。<br>- “用户范围”的优先级从高到低为：“IMSI_PREFIX（指定IMSI前缀）”或“IMSI_RANGE（指定IMSI范围）”，“FOREIGN_USER（外网用户）”或“HOME_USER（本网用户）”，“ALL_USER（所有用户）” |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于系统对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>后生效。<br>数据来源：整网规划<br>取值范围：5～15位十进制字符串<br>默认值：无<br>说明：- 按照IMSI最长匹配进行查询，相同IMSI前缀只能配置一条记录。<br>- IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定起始IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_RANGE（指定IMSI范围）”<br>后生效。<br>数据来源：整网规划<br>取值范围：5～15位十进制字符串<br>默认值：无<br>配置原则：当<br>“起始IMSI”<br>与<br>“终止IMSI”<br>长度全为15位时，<br>“起始IMSI”<br>要小于等于<br>“终止IMSI”<br>，否则<br>“起始IMSI”<br>要小于<br>“终止IMSI” |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定终止IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_RANGE（指定IMSI范围）”<br>后生效。<br>数据来源：整网规划<br>取值范围：5～15位十进制字符串<br>默认值：无<br>配置原则：当<br>“终止IMSI”<br>与<br>“起始IMSI”<br>长度全为15位时，<br>“终止IMSI”<br>要大于等于<br>“起始IMSI”<br>，否则<br>“终止IMSI”<br>要大于<br>“起始IMSI”<br>。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>配置为<br>“FOREIGN_USER(外网用户)”<br>或<br>“HOME_USER（本网用户）”<br>后生效。对于外网用户，该参数是外网用户对应的签订互联PLMN漫游协议的运营商标识， 对于本网用户，该参数是本网用户对应的运营商标识。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>说明：- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| LARAGPID | 区域群标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的区域群标识。<br>数据来源：整网规划<br>取值范围：1～2048<br>默认值：无<br>配置原则：该参数需要在<br>[**ADD LARAGPMEM**](../../位置区管理/位置区群组成员管理/增加位置区群组成员(ADD LARAGPMEM)_72345081.md)<br>中事先配置，可执行<br>[**LST LARAGPMEM**](../../位置区管理/位置区群组成员管理/查询位置区群组成员(LST LARAGPMEM)_72225165.md)<br>进行查看。 |
| ARMODE | 区域限制模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的区域限制模式。<br>数据来源：整网规划<br>取值范围：<br>- “BLACKLST(黑名单)”：“区域群标识”指定的区域为禁止用户接入区域，“区域群标识”未指定的区域为允许用户接入区域；<br>- “WHITELST(白名单)”：“区域群标识”指定的区域为允许用户接入区域，“区域群标识”未指定的区域为禁止用户接入区域。<br>默认值：无<br>配置原则：无 |
| CAUSE | 拒绝原因值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在“黑名单”或“白名单”模式中拒绝用户接入时使用的原因值。<br>数据来源：整网规划<br>取值范围：<br>- “CUSTOMER_DEFINED(自定义)”：表示拒绝用户接入时使用的原因值为自定义。<br>- “GPRS_SERVICE_NOT_ALLOWED(GPRS服务被禁止)”：表示拒绝用户接入时使用的指定原因值为GPRS服务被禁止。<br>- “GPRS_NONGPRS_SRV_NOT_ALLOWED(GPRS和非GPRS服务都被禁止)”：表示拒绝用户接入时使用的原因值为GPRS和非GPRS服务都被禁止。<br>- “PLMN_NOT_ALLOWED(PLMN被禁止)”：表示拒绝用户接入时使用的原因值为PLMN被禁止。<br>- “LA_NOT_ALLOWED(本地区域被禁止)”：表示拒绝用户接入时使用的原因值为本地区域被禁止。<br>- “ROAMING_NOT_ALLOWED_IN_LA(本地漫游被禁止)”：表示拒绝用户接入时使用的原因值为本地漫游被禁止。<br>- “GPRS_SRV_NOT_ALLOWED_IN_PLMN (本PLMN内GPRS服务被禁止)”：表示拒绝用户接入时使用的原因值为PLMN内GPRS服务被禁止。<br>- “NO_SUITABLE_CELLS_IN_LA(本地无合适小区)”：表示拒绝用户接入时使用的原因值为本地无合适单元。<br>默认值：<br>“NO_SUITABLE_CELLS_IN_LA(本地无合适小区)”<br>配置原则：无<br>说明：附着或路由更新拒绝的原因值，请参考3GPP TS 24.008输入。 |
| SDCAUSE | 自定义原因值 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定自定义原因值。<br>前提条件：该参数在<br>“CAUSE(原因值)”<br>设置为<br>“CUSTOMER_DEFINED(自定义)”<br>时生效。<br>数据来源：整网规划<br>取值范围：1～254<br>默认值：无<br>说明：当原因值为自定义时显示，根据3GPP TS 24.008填写。原因值为NAS消息里携带的拒绝原因值。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IUSUBRRLST]] · Iu模式用户漫游限制列表（IUSUBRRLST）

## 使用实例

增加一条Iu模式用户漫游限制列表记录，用于控制IMSI前缀为123456的用户群，不允许在位置区为0x1000，路由区为0x20的区域接入，拒绝原因值为 “NO_SUITABLE_CELLS_IN_LA(本地无合适小区)” ：

ADD LARAGP: LARAGPID=55;

ADD LARAGPMEM: LARAGPID=55, IDTYPE=RA, MCC="123", MNC="05", LAC="0x1000", RAC="0x20";

ADD IUSUBRRLST: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456", LARAGPID=55, ARMODE=BLACKLST, CAUSE=NO_SUITABLE_CELLS_IN_LA;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Iu模式用户漫游限制列表(ADD-IUSUBRRLST)_26305360.md`
