---
id: UNC@20.15.2@MMLCommand@RMV N26GWSELPLCY
type: MMLCommand
name: RMV N26GWSELPLCY（删除N26融合网关选择策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: N26GWSELPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- N26互操作管理
- N26融合网关选择策略
status: active
---

# RMV N26GWSELPLCY（删除N26融合网关选择策略）

## 功能

**适用网元：MME**

该命令用于LTE和5G互通组网部署时，删除5G用户的融合PGW-C/SMF选择策略。

## 注意事项

- 该命令执行后不会对正在进行信令流程的用户立即生效，该命令中的限制会在用户的下一次信令流程中生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置融合PGW-C/SMF选择策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “HOME_USER（本网用户）”<br>- “FOREIGN_USER（外网用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用以指定待配置融合PGW-C/SMF选择策略用户的IMSI前缀。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI。<br>数据来源：全网规划<br>取值范围：1～62位字符串<br>默认值：无<br>说明：- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>- 符号“*”表示通配符，即不限制APNNI。如果“APNNI”为“*”，表示该记录适用于所有的APNNI，否则该记录适用于指定的APNNI记录。 |

## 操作的配置对象

- [N26融合网关选择策略（N26GWSELPLCY）](configobject/UNC/20.15.2/N26GWSELPLCY.md)

## 使用实例

删除 “用户范围” 为 “ALL_USER（所有用户）” ， “APNNI” 为 “HUAWEI1.com” 的配置：

```
RMV N26GWSELPLCY: SUBRANGE=ALL_USER, APNNI="HUAWEI1.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除N26融合网关选择策略(RMV-N26GWSELPLCY)_72225817.md`
