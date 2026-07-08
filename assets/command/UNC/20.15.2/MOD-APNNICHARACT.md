---
id: UNC@20.15.2@MMLCommand@MOD APNNICHARACT
type: MMLCommand
name: MOD APNNICHARACT（修改APNNI属性配置信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNNICHARACT
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
- 会话管理
- APNNI属性
status: active
---

# MOD APNNICHARACT（修改APNNI属性配置信息）

## 功能

**适用网元：SGSN、MME**

该命令用于修改在非活动用户分离流程中需要进行特殊处理的APN NI（Network Identifier）属性。APN NI（Network Identifier）是APN中的必选部分，用于标识需要接入的外部数据网络的类型。APN NI需要在HLR中进行了签约，激活时才允许使用该APNNI。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：APN网络标识。<br>前提条件：APNNI已添加，参见<br>[**ADD APNNICHARACT**](增加APNNI属性配置信息(ADD APNNICHARACT)_72345265.md)<br>。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。<br>说明：- APN网络标识不区分大小写。<br>- APNNI在APN中所处的位置，例如：huawei1.com.mnc000.mcc123.gprs，其中NI= huawei1.com， OI= mnc.mcc.gprs。 |
| RSVIDLEUSER | 是否永久保留非活动用户 | 可选必选说明：可选参数<br>参数含义：该参数决定了当SGSN启动分离非活动用户功能时，签约了该APNNI的用户在处于非活动状态时是否进行分离。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无 |
| RSVIDLEUSERTMR | 分离非活动用户定时器（min） | 可选必选说明：条件必选参数<br>参数含义：该参数决定了当SGSN启动非活动用户分离功能后，签约了该APNNI的用户在指定多长时间后才进行分离。<br>前提条件：该参数在<br>“是否永久保留非活动用户”<br>参数设置为<br>“否”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0min～4320min<br>默认值：无<br>说明：该定时器的时长决定了分离该APN NI下用户的时长，其大小不受其他参数影响。 |

## 操作的配置对象

- [APNNI属性配置信息（APNNICHARACT）](configobject/UNC/20.15.2/APNNICHARACT.md)

## 使用实例

1. 修改签约APNNI为 “huawei1.com” 的用户不启用分离非活动用户功能：
  MOD APNNICHARACT: APNNI="huawei1.com", RSVIDLEUSER=YES;
2. 修改签约APNNI为 “huawei2.com” 的用户启用分离非活动用户功能并且分离非活动用户定时器时长为400min：
  MOD APNNICHARACT: APNNI="huawei2.com", RSVIDLEUSER=NO, RSVIDLEUSERTMR=400;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APNNI属性配置信息(MOD-APNNICHARACT)_72225349.md`
