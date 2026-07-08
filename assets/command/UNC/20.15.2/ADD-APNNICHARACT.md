---
id: UNC@20.15.2@MMLCommand@ADD APNNICHARACT
type: MMLCommand
name: ADD APNNICHARACT（增加APNNI属性配置信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNNICHARACT
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- APNNI属性
status: active
---

# ADD APNNICHARACT（增加APNNI属性配置信息）

## 功能

**适用网元：SGSN、MME**

该命令用于配置在非活动用户（指已附着，但不进行业务活动的用户）分离流程中需要进行特殊处理的APN。它主要实现了在非活动用户分离流程中，“基于APN的保护”与“基于APN配置定时器”的功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 每条记录中的APN NI字段不能重复。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：APN网络标识。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。<br>说明：- APN网络标识不区分大小写。<br>- APNNI在APN中所处的位置，例如：example1.com.mnc123.mcc123.gprs，其中NI= example1.com，OI= mnc123.mcc123.gprs。 |
| RSVIDLEUSER | 是否永久保留非活动用户 | 可选必选说明：可选参数<br>参数含义：该参数决定了当SGSN启动分离非活动用户功能时，签约了该APN NI的用户在处于非活动状态时是否进行分离。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>说明：- 对于配置的APN NI，当属性“是否永久保留非活动用户”设置为“是”时，标识SGSN在启动非活动用户分离功能后，签约了该APN NI的用户必须保留，即该用户不能被当作非活动用户而进行分离。<br>- 对于配置的APN NI，当属性“是否永久保留非活动用户”设置为“否”时，则需要同时设置该APN NI对应的“分离非活动用户定时器”时长，这就标识着SGSN在启动非活动用户分离功能后，签约了该APN NI的用户在指定的“分离非活动用户定时器”超时后才进行分离。 |
| RSVIDLEUSERTMR | 分离非活动用户定时器（min） | 可选必选说明：可选参数<br>参数含义：该参数决定了当SGSN启动非活动用户分离功能后，签约了该APNNI的用户在指定多长时间后才进行分离。当用户进入非活动状态时启动该定时器，当用户做业务时停止该定时器。定时器超时之后分离非活动用户。<br>前提条件：该参数在<br>“是否永久保留非活动用户”<br>参数设置为<br>“否”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0min～4320min<br>默认值：360min<br>配置原则：<br>- 该定时器的时长决定了分离该APNNI下用户的时长，其大小不受其他参数影响。<br>- 取值为0时，2G用户请参考**SET GBDETACH**命令的“非活动用户分离定时器”的时长。3G用户请参考**SET IUDETACH**命令的“非活动用户分离定时器”的时长。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNNICHARACT]] · APNNI属性配置信息（APNNICHARACT）

## 使用实例

增加记录，配置APN NI为 “example1.com” 的用户不启用分离非活动用户功能：

ADD APNNICHARACT: APNNI="example1.com", RSVIDLEUSER=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加APNNI属性配置信息(ADD-APNNICHARACT)_72345265.md`
