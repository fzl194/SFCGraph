---
id: UNC@20.15.2@MMLCommand@RMV APNNILIB
type: MMLCommand
name: RMV APNNILIB（删除APNNI库记录）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNNILIB
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- Smartphone管理
- 终端类型识别
- APNNI库管理
status: active
---

# RMV APNNILIB（删除APNNI库记录）

## 功能

**适用网元：SGSN**

该命令用于删除APNNI的库记录。APNNI库是用户请求的APNNI或签约数据中的APNNI和终端类型的对应关系表，用于通过APNNI识别智能终端类型。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SELMODE | 选择方式 | 可选必选说明：必选参数<br>参数含义：该参数用于选择删除APNNI库记录的方式。<br>取值范围：<br>- “APNNI(APNNI)”<br>- “UE_TYPE(终端类型)”<br>- “ALL(所有)”<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待删除的用户请求的APNNI或签约数据中的APNNI。<br>取值范围：1~62位字符串<br>默认值：无<br>说明：- 当“SELMODE（选择方式）”选择为“APNNI(APNNI)”时，此参数才生效。<br>- “APNNI”（APN网络标识地址）由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |
| UETYPE | 终端类型 | 可选必选说明：条件必选参数<br>参数含义：该参数为用于删除APNNI库记录的终端类型。<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>默认值：无<br>说明：当<br>“选择方式”<br>选择<br>“UE_TYPE(终端类型)”<br>时，此参数才生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNNILIB]] · APNNI库记录（APNNILIB）

## 使用实例

删除所有终端类型为Android用户APNNI库记录：

RMV APNNILIB: SELMODE=UE_TYPE, UETYPE=ANDROID;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APNNILIB.md`
