---
id: UNC@20.15.2@MMLCommand@RMV CHGPLMNCFG
type: MMLCommand
name: RMV CHGPLMNCFG（删除PLMN计费配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CHGPLMNCFG
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- PLMN计费配置
status: active
---

# RMV CHGPLMNCFG（删除PLMN计费配置）

## 功能

**适用网元：SGSN**

该命令用来删除话单生成策略配置信息。

## 注意事项

该命令执行后立即生效。执行后会影响新激活用户的话单生成策略。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “CELL_PLMNID（指定CELL_PLMNID）”<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示PLMN的移动国家号码。<br>取值范围：位数为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示PLMN的移动网号码。<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。<br>取值范围：1～62位字符串<br>默认值：无<br>说明：- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

## 操作的配置对象

- [PLMN计费配置（CHGPLMNCFG）](configobject/UNC/20.15.2/CHGPLMNCFG.md)

## 使用实例

删除SUBRANGE= CELL_PLMNID，MCC="123", MNC="001"，APNNI="huawei"的话单生成策略：

RMV CHGPLMNCFG: SUBRANGE=CELL_PLMNID, MCC="123", MNC="001", APNNI="huawei";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除PLMN计费配置(RMV-CHGPLMNCFG)_26305206.md`
