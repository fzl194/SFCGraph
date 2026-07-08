---
id: UNC@20.15.2@MMLCommand@ADD GMLCAU
type: MMLCommand
name: ADD GMLCAU（增加GMLC权限配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GMLCAU
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 160
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- GMLC权限配置
status: active
---

# ADD GMLCAU（增加GMLC权限配置）

## 功能

**适用网元：MME**

此命令用于增加GMLC权限配置。配置指定的GMLC的定位权限信息，MME根据该权限信息来实现对GMLC发起的定位请求的接入控制。

对GMLC的接入权限进行控制，允许/禁止定位请求，只允许接入指定的客户端类型、LCS业务类型的定位请求。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为160，即最多支持160个GMLC标识不同的记录，但每次执行记录数可以超过160条。
- 一个GMLC标识最多可对应512条权限控制记录，即一个GMLC标识最大支持4个客户端类型，一个指定的(GMLC标识，客户端类型)最大支持128个LCS业务类型。
- 如果只输入GMLCID，则允许接入指定GMLC标识的所有客户端类型及所有LCS业务类型。
- 如果只输入GMLCID与CLTTYPE，则允许指定GMLC标识的指定客户端类型的所有LCS业务类型。
- 如果输入GMLCID、CLTTYPE、SERTYPE，则允许指定的GMLC标识的指定客户端类型的指定LCS业务类型。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCID | GMLC 标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GMLC标识。<br>数据来源：整网规划<br>取值范围：0～639<br>默认值 ：无<br>配置原则： GMLC ID必须和<br>[**ADD GMLC**](../GMLC配置/增加GMLC配置(ADD GMLC)_26145796.md)<br>配置表中的GMLC ID一致。 |
| CLTTYPE | 支持的客户端类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识客户端（LCS Client）类型。<br>数据来源：整网规划<br>取值范围：<br>- “EMERGENCY_SERVICES（紧急业务）”<br>- “VALUE_ADDED_SERVICES（增值业务）”<br>- “PLMN_OPERATOR_SERVICES（运营商业务）”<br>- “LAWFUL_INTERCEPT_SERVICES（合法定位）”<br>默认值 ：无 |
| SERTYPE | 支持的LCS业务类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于标识LCS Client的指定定位业务。<br>前提条件：该参数在<br>“支持的客户端类型”<br>输入时有效。<br>数据来源：整网规划<br>取值范围： 0～127<br>默认值 ：无<br>配置原则：请参考<br>[表1](#ZH-CN_MMLREF_0000001126145794__tab1)<br>。 |

## 操作的配置对象

- [GMLC权限配置（GMLCAU）](configobject/UNC/20.15.2/GMLCAU.md)

## 使用实例

增加一条 “GMLC标识” 为 “1” ， “支持的客户端类型” 为 “VALUE_ADDED_SERVICES（增值业务）” ， “支持的LCS业务类型” 为 “2” 的GMLC权限配置记录：

ADD GMLCAU: GMLCID=1, CLTTYPE=VALUE_ADDED_SERVICES, SERTYPE=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加GMLC权限配置(ADD-GMLCAU)_26145794.md`
