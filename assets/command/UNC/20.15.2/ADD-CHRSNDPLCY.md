---
id: UNC@20.15.2@MMLCommand@ADD CHRSNDPLCY
type: MMLCommand
name: ADD CHRSNDPLCY（增加CHR传输策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CHRSNDPLCY
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- CHR管理
- CHR传输策略
status: active
---

# ADD CHRSNDPLCY（增加CHR传输策略）

## 功能

**适用网元：SGSN、MME**

该命令用于增加CHR传输策略，满足CHR传输策略的用户的CHR才会传输给CloudUDN。

## 注意事项

- 此命令最大记录数为1000。
- CHR传输开关打开（[**SET CHRSTORECFG**](../CHR存盘管理/设置CHR存盘配置（SET CHRSTORECFG）_26145616.md)命令中参数“CHR存储开关”设置为“OFF”或参数“CHR存储开关”设置为“ON”并且参数“存储类型”设置为“STORE_AND_SEND”），且CHR传输策略控制参数（[**SET CHRSNDPLCYCFG**](设置CHR传输策略控制参数(SET CHRSNDPLCYCFG)_26305424.md)）中的“CHRSNDPLCYSELECT”参数设置为“自定义策略传输”时，该命令执行后立即生效。
- 本命令参数“TYPE”选择为“签约APN”时：
    1. 如果传输CHR时尚未获取到用户的签约数据，该用户的CHR是否传输受[**SET CHRSNDPLCYCFG**](设置CHR传输策略控制参数(SET CHRSNDPLCYCFG)_26305424.md)中的“NOSUBSWITCH”参数控制。
    2. 如果用户的签约数据中存在该命令配置的APNNI，该用户的CHR将传输给CloudUDN。
    3. 如果用户的签约数据中不存在该命令配置的APNNI，该用户的CHR不传输给CloudUDN。
- 本命令参数“TYPE”选择为“APNNI（签约APNNI）”时，只针对用户签约数据中的APNNI（如果用户配置了[**ADD SMSUBDATA**](../../../业务安全管理/会话管理/签约数据纠正/增加签约数据纠正参数(ADD SMSUBDATA)_26305486.md)，以修改后的签约数据为准）进行判断，不针对用户具体流程中请求的APNNI或者请求纠错后的APNNI进行判断；如果CHR传输时当前用户的网络类型与签约数据的网络类型不同，以签约数据的网络类型为准。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | CHR传输策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CHR传输策略类型。<br>数据来源：本端规划<br>取值范围：<br>- “APNNI（签约APNNI）”：表示签约数据中包含该APNNI的用户的CHR才会传输给CloudUDN。<br>默认值：无<br>配置原则：当前仅支持配置“签约APNNI” |
| APNNI | APN网络标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定满足CHR传输策略的签约APNNI。<br>该参数在<br>“CHR传输策略类型”<br>参数配置为<br>“APNNI（签约APNNI）”<br>后生效。<br>数据来源：本端规划<br>取值范围：1~62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔，每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>- 本命令中APNNI不允许配置为“*”。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHRSNDPLCY]] · CHR传输策略（CHRSNDPLCY）

## 使用实例

增加CHR传输策略，CHR存盘配置（SET CHRSTORECFG）中参数CHR存储开关打开， “存储类型” 设置为 “存储和转发” ；CHR传输策略控制参数（SET CHRSNDPLCYCFG）中的参数CHRSNDPLCYSELECT设置为 “自定义策略传输” ；CHR传输策略类型为 “签约APNNI” ，APNNI设置为 “HUAWEI.COM” ：

SET CHRSTORECFG: STOREALLFLAG=ON, STOREALLTYPE=STORE_AND_SEND;

SET CHRSNDPLCYCFG: CHRSNDPLCYSELECT=CUSTOMIZE;

ADD CHRSNDPLCY: TYPE=APNNI, APNNI="HUAWEI.COM";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-CHRSNDPLCY.md`
