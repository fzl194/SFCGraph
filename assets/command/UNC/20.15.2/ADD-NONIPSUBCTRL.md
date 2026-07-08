---
id: UNC@20.15.2@MMLCommand@ADD NONIPSUBCTRL
type: MMLCommand
name: ADD NONIPSUBCTRL（增加Non-IP APNNI配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NONIPSUBCTRL
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
- M2M管理
- Non-IP APNNI配置
status: active
---

# ADD NONIPSUBCTRL（增加Non-IP APNNI配置）

## 功能

**适用网元：MME**

此命令用于配置支持激活Non-IP类型PDN的APNNI。当HSS中未给用户签约Non-IP签约数据且需要使用Non-IP业务时，需要执行此命令。

## 注意事项

- 该命令执行后只对新激活PDN生效。
- 此配置涉及Non-IP数据传输特性（特性编号：WSFD-215103，license部件编码：LKV2NOIP01），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。
- 该命令对签约数据中包含Non-IP签约数据的用户不生效。
- “HSS免升级”特性（特性编号：WSFD-215301，license部件编码：LKV2HUNN01）的相关license授权并开启后，该命令生效。
- 支持Non-IP接入的APNNI为该命令配置的APNNI与用户签约的APNNI的交集。
- 此命令最大记录数为1024。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置生效的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX”<br>时，该参数才有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| SUPAPNNI | 支持Non-IP的APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定支持Non-IP接入的APNNI。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_APNNI（所有APNNI）”<br>- “SPECIAL_APNNI（指定APNNI）”<br>默认值：无<br>配置原则：<br>- 如果用户签约的所有APNNI均支持Non-IP接入且使用签约default APNNI作为Non-IP接入的default APNNI，配置为“ALL_APNNI”。<br>- 如果需要为用户指定支持Non-IP接入的APNNI，配置为“SPECIAL_APNNI”。 |
| APNNIGROUPID | APNNI组号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定APNNI组号。<br>前提条件：该参数在<br>“支持Non-IP的APNNI”<br>参数配置为<br>“指定APNNI”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～15<br>默认值：无<br>说明：- 该ID必须是[**ADD APNNIGROUP**](../../会话管理/APNNI信息管理/APNNI组管理/增加APNNI组(ADD APNNIGROUP)_26305508.md)命令中已配置的ID记录。 |
| DFTAPNNI | 缺省APNNI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定支持Non-IP接入的缺省APNNI。<br>前提条件：该参数在<br>“支持Non-IP的APNNI”<br>参数配置为<br>“指定APNNI”<br>后生效。<br>数据来源：全网规划<br>取值范围：输入长度范围为1～62<br>默认值：无<br>配置原则：<br>- 该参数所配置的APNNI必须是“APNNI组号”包含的APNNI。<br>说明：- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NONIPSUBCTRL]] · Non-IP APNNI配置（NONIPSUBCTRL）

## 使用实例

增加一条SUBRANGE为IMSI_PERFIX，IMSI前缀为“123038101”，支持Non-IP的APNNI为ALL_APNNI的Non-IP APNNI配置：

ADD NONIPSUBCTRL: SUBRANGE=IMSI_PREFIX, IMSIPRE="123038101", SUPAPNNI=ALL_APNNI;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NONIPSUBCTRL.md`
