---
id: UNC@20.15.2@MMLCommand@MOD SRVCCLMTPLCY
type: MMLCommand
name: MOD SRVCCLMTPLCY（修改SRVCC流程限制策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SRVCCLMTPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 流程限制管理
status: active
---

# MOD SRVCCLMTPLCY（修改SRVCC流程限制策略）

## 功能

**适用网元：MME**

该命令用于修改SRVCC流程限制策略。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- ALL_USER（所有用户）：表示用户范围为系统内所有用户。<br>- HOME_USER（本网用户）：表示用户范围为本网用户。<br>- FOREIGN_USER（外网用户）：表示用户范围为外网用户。<br>- IMSI_PREFIX（指定IMSI前缀）：表示用户范围通过IMSI前缀指定。<br>- SPECIFIC_IMSI（指定IMSI）：表示用户范围通过IMSI指定。<br>默认值：无<br>配置原则：SRVCC流程限制策略匹配优先级从高到低为：<br>“SPECIFIC_IMSI（指定IMSI）”<br>，<br>“IMSI_PREFIX（指定IMSI前缀）”<br>，<br>“FOREIGN_USER(外网用户)”<br>或<br>“HOME_USER(本网用户)”<br>，<br>“ALL_USER(所有用户)”<br>。 系统优先匹配高优先级的配置记录，如果匹配不到，再匹配低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“HOME_USER(本网用户)”<br>或<br>“FOREIGN_USER(外网用户)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>后生效。<br>数据来源：整网规划<br>取值范围：5～14位十进制字符串<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数。<br>参数含义：该参数用于指定用户的IMSI（完整IMSI）。<br>前提条件：该参数在<br>“用户范围”<br>配置为<br>“SPECIFIC_IMSI（指定IMSI）”<br>后生效。<br>数据来源：全网规划<br>取值范围：15位十进制字符串<br>默认值：无<br>配置原则：无 |
| SRVCCCAPCFG | 是否限制携带SRVCC能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否限制SRVCC流程，如果限制则不携带SRVCC Operation Possible信元给eNodeB。<br>数据来源：整网规划<br>取值范围：<br>- NO(否)<br>- YES(是)<br>默认值：无<br>配置原则：当SRVCC功能支持，但不期望用户发起SRVCC流程，限制在DOWNLINK NAS TRANSPORT、INITIAL CONTEXT SETUP REQUEST、HANDOVER REQUEST消息中携带SRVCC Operation Possible信元给eNodeB，将该参数设置为<br>“YES(是)”<br>。否则配置为<br>“NO(否)”<br>，保持原有实现。 |
| EMGCAPCFG | 紧急呼叫是否限制SRVCC能力 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定是否限制紧急呼叫SRVCC流程。如果限制则不携带SRVCC Operation Possible信元给eNodeB。<br>前提条件：该参数在<br>“是否限制携带SRVCC能力”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- NO(否)<br>- YES(是)<br>默认值：无<br>配置原则：当SRVCC功能支持时，但不期望用户发起紧急呼叫SRVCC流程，限制在DOWNLINK NAS TRANSPORT、INITIAL CONTEXT SETUP REQUEST、HANDOVER REQUEST消息中携带SRVCC Operation Possible信元给eNodeB，将该参数设置为<br>“YES(是)”<br>。否则配置为<br>“NO(否)”<br>，保持原有实现。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRVCCLMTPLCY]] · SRVCC流程限制策略（SRVCCLMTPLCY）

## 使用实例

修改一条SRVCC流程限制策略配置， “用户范围” 为 “ALL_USER” ， “是否限制携带SRVCC能力” 为 “YES(是)” ， “紧急呼叫是否限制SRVCC能力” 为 “NO(否)” ：

```
MOD SRVCCLMTPLCY: SUBRANGE=ALL_USER, SRVCCCAPCFG=YES, EMGCAPCFG=NO;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SRVCC流程限制策略(MOD-SRVCCLMTPLCY)_83402477.md`
