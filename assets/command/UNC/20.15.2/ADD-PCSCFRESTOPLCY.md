---
id: UNC@20.15.2@MMLCommand@ADD PCSCFRESTOPLCY
type: MMLCommand
name: ADD PCSCFRESTOPLCY（增加P-CSCF故障恢复策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PCSCFRESTOPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- P-CSCF故障恢复策略
status: active
---

# ADD PCSCFRESTOPLCY（增加P-CSCF故障恢复策略）

## 功能

**适用网元：MME**

该命令用于增加P-CSCF故障恢复策略配置。

该命令的使用场景：当P-CSCF故障时，可以设置该命令通过承载更新流程刷新故障的P-CSCF，减少IMS会话重建。

## 注意事项

- 该命令执行后立即生效。
- 最大配置记录数是1024条。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置P-CSCF故障恢复策略的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- ALL_USER（所有用户）：表示用户范围为系统内所有用户。<br>- HOME_USER（本网用户）：表示用户范围为本网用户。<br>- FOREIGN_USER（外网用户）：表示用户范围为外网用户。<br>- IMSI_PREFIX（指定IMSI前缀）：表示用户范围通过IMSI前缀指定。<br>- SPECIFIC_IMSI（特定IMSI）：表示用户范围通过IMSI指定。<br>默认值：无<br>配置原则：<br>- 控制策略优先级高到低为：“SPECIFIC_IMSI（特定IMSI）”，“IMSI_PREFIX（指定IMSI前缀）”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。<br>- 系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“HOME_USER(本网用户)”<br>或<br>“FOREIGN_USER(外网用户)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>后生效。<br>数据来源：整网规划<br>取值范围：5~14位十进制数字字符串<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIFIC_IMSI（特定IMSI）”<br>后生效。<br>数据来源：整网规划<br>取值范围：14~15位十进制数字字符串<br>默认值：无 |
| PCOOPEX | PCO-based optional extension功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启基于HSS的P-CSCF故障恢复机制中的PCO-based optional extension功能。<br>数据来源：整网规划<br>取值范围：<br>- "OFF（关闭）"<br>- "ON（开启）"<br>默认值：<br>“OFF（关闭）”<br>配置原则：<br>- “ 基于HSS的P-CSCF故障恢复”特性的相关License授权并开启后，此参数配置才生效（特性编号：WSFD-201205，License部件编码：LKV2FRPH02）<br>- 功能同时受[**ADD SGWCHARACT**](../../../GTP-C接口管理/S11接口管理/S-GW属性/增加S-GW特性对接配置(ADD SGWCHARACT)_26305778.md)的“S-GW支持P-CSCF Restoration Indication”参数、[**ADD PGWCHARACT**](../../../GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/P-GW属性/增加P-GW特性对接配置（ADD PGWCHARACT）_26305748.md)的“P-GW支持P-CSCF Restoration Indication”参数控制，只有全部开启功能才生效。<br>说明：PCO-based optional extension为基于HSS的P-CSCF故障恢复机制的可选扩展，通过更新承载流程来刷新故障的P-CSCF，减少IMS会话的重建流程，参考协议3GPP TS 23.380<br>说明：该参数功能在UNC<br>20.15.2.25<br>补丁生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCSCFRESTOPLCY]] · P-CSCF故障恢复策略（PCSCFRESTOPLCY）

## 使用实例

增加一条 “用户范围” 为 “所有用户” ， “PCO-based optional extension功能” 为 “ON（开启）” 的记录；

```
ADD PCSCFRESTOPLCY: SUBRANGE=ALL_USER, PCOOPEX=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PCSCFRESTOPLCY.md`
