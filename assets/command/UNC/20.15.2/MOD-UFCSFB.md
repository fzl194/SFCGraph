---
id: UNC@20.15.2@MMLCommand@MOD UFCSFB
type: MMLCommand
name: MOD UFCSFB（修改预留功能策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: UFCSFB
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- 预留功能策略管理
status: active
---

# MOD UFCSFB（修改预留功能策略）

## 功能

**适用网元：MME**

该命令用于修改系统的预留功能策略，配置允许哪些用户和终端使用预留功能。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “HOME_USER(本网用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无<br>配置原则：<br>- “SUBRANGE（用户范围）”的优先级从高到低为：“IMSI_PREFIX（指定IMSI前缀）”，“FOREIGN_USER（外网用户）”或“HOME_USER（本网用户）”，“ALL_USER（所有用户）”。<br>- 系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 当用户为MNO用户时，该参数需要配置为0或128～254之间的值，该取值必须和[**ADD MNO**](../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置的“MNOID”参数取值相同。<br>- 当用户为MVNO用户时，该参数需要配置为1～64之间的值，该取值必须和[**ADD MVNO**](../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置的“MVNOID”参数取值相同。<br>说明：对于外网用户，该参数是与其归属运营商签订可漫游协议，为其提供服务的MNO/MVNO运营商标识。对于本网用户，该参数是该用户归属的MNO/MVNO运营商标识。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于系统对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：此参数在<br>“SUBRANGE（用户范围）”<br>设置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无<br>说明：IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。比如：同时存在IMSI前缀为30801和3080101的配置，则优先使用3080101的配置。 |
| UFCSFB | 预留功能 | 可选必选说明：可选参数<br>参数含义：该命令用于设置是否允许用户进行预留功能。<br>数据来源：全网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：<br>- “NO(否)”：表示系统不允许“SUBRANGE（用户范围）”参数指定的用户进行预留功能。<br>- “YES(是)”：表示系统允许“SUBRANGE（用户范围）”参数指定的用户进行预留功能 |
| IMEICTRL | 基于IMEI控制 | 可选必选说明：条件可选参数<br>参数含义：该参数用于配置基于IMEI的预留功能控制方式。<br>前提条件：此参数在<br>“UFCSFB（预留功能）”<br>设置为<br>“YES”<br>时有效。<br>数据来源：本端规划<br>取值范围：<br>- “NO(否)”<br>- “WHITELIST(白名单)”<br>配置原则：<br>- “NO(否)”：系统不基于终端IMEI控制是否允许用户进行预留功能。<br>- “WHITELIST(白名单)”：系统只允许IMEI白名单内的终端进行预留功能，不允许其它终端进行预留功能。<br>- 需要根据IMEI控制预留功能业务时，例如从终端兼容性考虑需要限定某几款手机才能进行预留功能时，建议将该参数设置为“WHITELIST(白名单)”。<br>默认值：无 |
| IMEIGPID | IMEI群组标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于配置IMEI群组的标识。<br>前提条件：<br>- 该参数在“IMEICTRL(基于IMEI控制)”参数设置为“WHITELIST(白名单)”时，有效。<br>- “IMEI群组标识”已经通过[**ADD IMEIGP**](../../业务安全管理/用户终端管理/IMEI群组管理/增加IMEI群组(ADD IMEIGP)_72225435.md)配置。<br>数据来源：本端规划<br>取值范围：1～50<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UFCSFB]] · 预留功能策略（UFCSFB）

## 使用实例

运营商允许本网用户使用预留功能业务，且优先使用基于白名单的控制方式，不允许外网用户使用预留功能业务：

- 修改本网用户的预留功能策略：
  ADD IMEIGP: IMEIGPID=1;
  MOD UFCSFB: SUBRANGE=HOME_USER, NOID=0, UFCSFB=YES, IMEICTRL=WHITELIST, IMEIGPID=1;
- 修改外网用户的预留功能策略：
  MOD UFCSFB: SUBRANGE=FOREIGN_USER, NOID=0, UFCSFB=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-UFCSFB.md`
