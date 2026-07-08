---
id: UNC@20.15.2@MMLCommand@RMV M2MPLCY
type: MMLCommand
name: RMV M2MPLCY（删除M2M策略参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: M2MPLCY
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
- 业务安全管理
- M2M管理
- M2M策略参数配置
status: active
---

# RMV M2MPLCY（删除M2M策略参数）

## 功能

**适用网元：SGSN、MME**

该命令用于删除M2M的策略参数。

## 注意事项

该命令执行后对已经附着的用户不立即生效。用户下次RAU/TAU流程再生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除M2M策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “HOME_USER(本网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无<br>说明：当存在多条记录时，首先匹配<br>“IMSI_PREFIX（指定IMSI前缀）”<br>的记录，其次匹配<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>的记录，最后匹配<br>“ALL_USER（所有用户）”<br>的记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“FOREIGN_USER(外网用户)”<br>或<br>“HOME_USER(本网用户)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无<br>说明：当该参数配置生效时，按照IMSI最长匹配进行查询，如果有<br>“APNNI（APNNI）”<br>匹配的记录，使用该记录的配置；如果没有<br>“APNNI（APNNI）”<br>匹配的记录，则查找IMSI次长匹配的记录。 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI。<br>数据来源：全网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>- 符号“*”表示通配符，即不限制APNNI。 如果APNNI为“*”，表示该记录适用于所有的APNNI，否则该记录适用于指定的APNNI记录。<br>- 相同IMSI前缀的不同记录中“APNNI（APNNI）”配置不能相同。<br>- 当系统识别到UE支持“长周期RAU定时器”时，使用用户签约的“APNNI”进行匹配，若签约的“APNNI”匹配到多条记录，随机选择其中一条记录；若没有匹配到记录，使用“APNNI”为“*”的记录。<br>- 当系统识别到UE支持“长周期TAU定时器”、“PSM”、“eDRX”或者“NBIOT(CP优化)”时，使用用户实际使用的“APNNI”进行匹配，若用户为多PDN场景且使用的“APNNI”匹配到多条记录，随机选择其中一条记录；若没有匹配到记录，使用“APNNI”为“*”的记录。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M2MPLCY]] · M2M策略参数（M2MPLCY）

## 使用实例

删除 “用户范围” 为 “所有用户” ， “APNNI” 为 “HUAWEI1.com” 的配置：

RMV M2MPLCY: SUBRANGE=ALL_USER, APNNI="HUAWEI1.com";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除M2M策略参数(RMV-M2MPLCY)_26305574.md`
