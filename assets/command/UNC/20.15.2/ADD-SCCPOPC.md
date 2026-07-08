---
id: UNC@20.15.2@MMLCommand@ADD SCCPOPC
type: MMLCommand
name: ADD SCCPOPC（增加SCCP本局信令点）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SCCPOPC
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: ''
is_dangerous: false
max_records: 64
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP本局信令点
status: active
---

# ADD SCCPOPC（增加SCCP本局信令点）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用于增加SCCP本局信令点。

## 注意事项

- 此命令的最大记录数为64。
- 本局信令点编码在同一网络中唯一。
- 本局信令点表中的网络标识必须在信令点属性表中设置（[**SET SIGATTR**](../../信令网属性管理/设置信令网属性(SET SIGATTR)_72226021.md)）。
- SCCP本局信令点的相关记录必须在M3UA本地实体表中存在，M3UA本局信令点表内记录可以通过命令[**LST M3LE**](../../M3UA管理/M3UA本地实体/查询M3UA本地实体(LST M3LE)_72225993.md)查看。
- 相同网络标识下本局信令点编码不能与目的信令点编码重复。
- 当本信令点只用于IU接口，与RNC对接时使用IUONLY；当本信令点只用于核心网侧的接口，例如GR接口（与HLR对接）或GS接口（与MSC对接）等时使用COREONLY；当本信令点可以同时用于IU接口和核心网侧接口时，使用IUANDCORE。
- 配置了多个SCCP本局信令点时，需要针对配置的多个SCCP本局信令点配置所有相关设备的目的信令点（[**ADD SCCPDPC**](../SCCP目的信令点/增加SCCP目的信令点(ADD SCCPDPC)_26306130.md)），同时需要在相关的设备内配置所有的SGSN的本局信令点数据才能正常使用。
- 此配置涉及“多信令点功能”特性（特性编号：WSFD-104409，License部件编码：LKV2MUSP01），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPX | 本局信令点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCCP本局信令点索引。<br>数据来源：本端规划<br>取值范围：1～64<br>默认值：无 |
| NI | 网络指示语 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络指示语。<br>数据来源：整网规划<br>取值范围：<br>- “INT（国际网）”<br>- “INTB（国际备用网）”<br>- “NAT（国内网）”<br>- “NATB（国内备用网）”<br>默认值：无<br>说明：配置的网络指示语在信令属性表中应该配置为有效（<br>[**SET SIGATTR**](../../信令网属性管理/设置信令网属性(SET SIGATTR)_72226021.md)<br>）。 |
| OPC | 本局信令点编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本局信令点编码，可以采用24位信令点编码或14位信令编码。<br>数据来源：整网规划<br>取值范围：长度不超过8的字符串<br>默认值：无<br>配置原则：<br>- 配置的信令点编码结构需要和信令属性表中对应的信令网络的网络结构保持一致。<br>- 取值为0x1~0x3FFF（对应14位编码）或0x1~0xFFFFFF（对应24位编码），不输入0x也取输入为十六进制值，即输入123等价于0x123。 |
| SPN | 信令点用途 | 可选必选说明：可选参数<br>参数含义：该参数用于指定信令点用途。<br>数据来源：整网规划<br>取值范围：<br>- “IUONLY（IU ONLY）”<br>- “COREONLY（CORE ONLY）”<br>- “IUANDCORE（IU AND CORE）”<br>默认值：<br>“COREONLY（CORE ONLY）” |
| SGSNN | 本局SGSN号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本局SGSN号。<br>数据来源：整网规划<br>取值范围：长度不超过16的十进制数字<br>默认值：无 |
| OPN | 本局信令点名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本局信令点名。<br>数据来源：本端规划<br>取值范围：长度不超过32的字符串<br>默认值：noname |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPOPC]] · SCCP本局信令点（SCCPOPC）

## 使用实例

增加SCCP本局信令点，本局信令点索引为1，网络指示语为INT，本局信令点编码为“0x55”，信令点用途为IUONLY，本局信令点名为“Peking”：

ADD SCCPOPC: OPX=1, NI=INT, OPC="0x55", SPN=IUONLY, OPN="Peking";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SCCP本局信令点(ADD-SCCPOPC)_72226009.md`
