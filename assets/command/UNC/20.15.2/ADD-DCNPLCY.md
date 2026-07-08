---
id: UNC@20.15.2@MMLCommand@ADD DCNPLCY
type: MMLCommand
name: ADD DCNPLCY（增加DCN配置策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DCNPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- DCN管理
- DCN配置策略
status: active
---

# ADD DCNPLCY（增加DCN配置策略）

## 功能

**适用网元：MME**

该命令用于增加DCN的策略参数，即为用户配置DCN业务相关参数，以满足运营商灵活部署网络的需求。

## 注意事项

- 此命令最大记录数为1024。
- 此配置涉及DECOR基础功能特性（特性编号：WSFD-208001，license部件编码：LKV2DECOR00）和DECOR特性（特性编号：WSFD-208002，license部件编码：LKV2DECOR01），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“打开”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DCN策略的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PRE(指定IMSI前缀)”<br>默认值：无<br>说明：- 用户接入时首先按照用户的IMSI在“IMSI_PRE（指定IMSI前缀）”进行查询，如果查询成功则使用该记录对应的配置；如果查询失败，则查询“ALL_USER(所有用户)”对应的配置记录。<br>- 当“用户范围”设置为“IMSI_PRE(指定IMSI前缀)”时，如果匹配到多条记录，使用“IMSI前缀”最长匹配的记录。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>配置为<br>“IMSI_PRE(指定IMSI前缀)”<br>后生效。<br>数据来源：本端规划<br>取值范围：5~15位十进制数字字符串<br>默认值：无 |
| DCNSW | DCN开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否开启DCN功能。<br>数据来源：本端规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(打开)”<br>默认值：无<br>说明：此参数与DECOR基础功能特性（特性编号：WSFD-<br>208001<br>，license部件编码：LKV2DECOR00），DECOR特性（特性编号：WSFD-<br>208002<br>，license部件编码：LKV2DECOR01）共同作用开启DCN功能。 |
| SRUEUSAGETYPE | 源侧UE USAGE TYPE策略 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定新侧MME是否使用从源侧MME携带的UE USAGE TYPE。<br>前提条件: 该参数在<br>“DCN开关”<br>配置为<br>“ON(打开)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：YES(是)<br>配置原则：<br>- 如果源侧MME携带的UE USAGE TYPE不可信时，可以将此参数设置为“NO(否)”。<br>说明：- 源侧MME可能会在Attach流程的Identification Response消息、TAU流程的Context Response消息或者Handover流程Forward Relocation Request消息中携带UE USAGE TYPE到新侧MME。<br>- 如果此参数配置为“YES(是)”，系统会在收到源侧MME的UE USAGE TYPE后，如果可以查找到可服务的DCN，则认为查询成功；否则系统直接使用“UE USAGE TYPE获取策略”中的方式尝试查找DCN ID。<br>- 如果此参数配置为“NO(否)”，系统直接使用“UE USAGE TYPE获取策略”中的方式尝试查找DCN ID。 |
| UEUSAGETYPEPLCY | UE USAGE TYPE获取策略 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定UE USAGE TYPE的获取策略。<br>前提条件: 该参数在<br>“DCN开关”<br>参数配置为<br>“ON(打开)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “HSS(HSS获取)”<br>- “LOCAL(本地获取)”<br>默认值：<br>“HSS(HSS获取)”<br>配置原则：<br>- 如果HSS未配置用户的签约数据UE USAGE TYPE，可以将此参数设置为“LOCAL(本地获取)”。<br>说明：- 配置为“HSS(HSS获取)”，系统会通过Authentication Info Request消息向HSS请求获取UE USAGE TYPE；需要在[**ADD S1USRSECPARA**](../../用户安全管理/S1模式用户安全参数/增加S1模式用户安全配置(ADD S1USRSECPARA)_26305460.md)命令中设置用户的安全策略为鉴权并保护，否则由于无法通过Authentication Info Request消息获取UE USAGE TYPE，而导致业务流程失败。<br>- 配置为“LOCAL(本地获取)”，系统会使用“UEUSAGETYPE”参数配置的UE USAGE TYPE值。 |
| UEUSAGETYPE | UE USAGE TYPE | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定UE USAGE TYPE。<br>前提条件: 该参数在<br>“UE USAGE TYPE获取策略”<br>配置为<br>“LOCAL(本地获取)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~255<br>默认值：无<br>配置原则：0-127为预留的标准值，128-255为运营商规划值。此参数建议在规划值范围内进行配置，以防将来和预留的标准值产生冲突。请参见3GPP TS 29.272。 |
| GWSELPLCY | 网关选择策略 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制MME在通过DNS查询网关时是否使用UE USAGE TYPE。<br>前提条件: 该参数在<br>“DCN开关”<br>参数配置为<br>“ON(打开)”<br>后生效。<br>数据来源：全网规划<br>取值范围：<br>- “NO(不使用)”：系统保持原有实现来查询网关。<br>- “YES(使用)”：专网中的用户接入到指定的网关。<br>默认值：<br>“NO(不使用)”<br>配置原则：<br>- 如果不期望将专网中的用户接入到指定的网关时，将此参数配置为“NO(不使用)”。<br>- 如果期望将专网中的用户接入到指定的网关时，将此参数配置为“YES(使用)”。<br>说明：当参数配置为<br>“YES(使用)”<br>时，必须根据用户的UE USAGE TYPE部署DNS NAPTR记录，否则会导致网关查询失败。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DCNPLCY]] · DCN配置策略（DCNPLCY）

## 使用实例

为 “IMSI前缀” 为 “123003” 的用户打开DCN功能，优先使用源侧MME携带的UE USAGE TYPE，在源侧未携带时使用本地配置为100的UE USAGE TYPE查找可服务的DCN：

ADD DCNPLCY: SUBRANGE=IMSI_PRE, IMSIPRE="123003", DCNSW=ON, SRUEUSAGETYPE=YES, UEUSAGETYPEPLCY=LOCAL, UEUSAGETYPE=100, GWSELPLCY=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加DCN配置策略(ADD-DCNPLCY)_26305642.md`
