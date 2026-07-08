---
id: UNC@20.15.2@MMLCommand@MOD GWPRESELBYIMSI
type: MMLCommand
name: MOD GWPRESELBYIMSI（修改指定用户优选网关）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: GWPRESELBYIMSI
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- 网关优选
- 指定用户优选网关
status: active
---

# MOD GWPRESELBYIMSI（修改指定用户优选网关）

## 功能

**适用网元：MME**

该命令用于修改指定用户优选网关记录。

## 注意事项

无。

## 权限

manage-ug；system-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户IMSI。<br>数据来源：整网规划<br>取值范围：14~15位十进制数字<br>默认值：无 |
| RATTYPE | RAT TYPE | 可选必选说明：可选参数<br>参数含义：该参数用于控制需要进行优选网关的用户接入模式。<br>数据来源：整网规划<br>取值范围：<br>- “Gb_MODE（Gb模式）”<br>- “Iu_MODE（Iu模式）”<br>- “S1_MODE（S1模式）”说明：参数初始设置值非全部选中，不勾选时不会被修改或者清空。 |
| SGW_HSNAME | SGW 主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定优选的SGW主机名。<br>前提条件：该参数在<br>“RATTYPE”<br>设置了<br>“S1_MODE（S1模式）”<br>后生效。<br>数据来源：整网规划<br>取值范围：1～255 位字符串（大小写不敏感）<br>默认值：无<br>配置原则：按照协议RFC1035规定，Hostname最大有效字符数为253，并且每个Label最大长度为63个字节。 |
| GGSN_HSNAME | GGSN 主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定优选的GGSN主机名。<br>前提条件：该参数在<br>“RATTYPE”<br>设置了<br>“Gb_MODE（Gb模式）”<br>或者<br>“Iu_MODE（Iu模式）”<br>后生效。<br>数据来源：整网规划<br>取值范围：1～255 位字符串（大小写不敏感）<br>默认值：无<br>配置原则：按照协议RFC1035规定，Hostname最大有效字符数为253，并且每个Label最大长度为63个字节。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GWPRESELBYIMSI]] · 指定用户优选网关（GWPRESELBYIMSI）

## 使用实例

修改用户IMSI为 "123030000100001" 的指定用户优选网关记录，控制需要进行网关优选的制式为“ Gb_MODE-1&Iu_MODE-1&S1_MODE-1 ”，指定优选的SGW主机名为 "TOPON.SGW.SGW1.EPC.MNC03.MCC123.3GPPNETWORK.ORG" ，指定优选的GGSN主机名为“ INTERNET.MNC003.MCC123.GPRS ”：

MOD GWPRESELBYIMSI: IMSI="123030000100001", RATTYPE=Gb_MODE-1&Iu_MODE-1&S1_MODE-1, SGW_HSNAME="TOPON.SGW.SGW1.EPC.MNC03.MCC123.3GPPNETWORK.ORG", GGSN_HSNAME="INTERNET.MNC003.MCC123.GPRS";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-GWPRESELBYIMSI.md`
