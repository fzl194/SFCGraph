---
id: UNC@20.15.2@MMLCommand@MOD N26GWSELPLCY
type: MMLCommand
name: MOD N26GWSELPLCY（修改N26融合网关选择策略）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD N26GWSELPLCY（修改N26融合网关选择策略）

## 功能

**适用网元：MME**

该命令用于LTE和5G互通组网部署时，修改5G用户的融合PGW-C/SMF选择策略。

## 注意事项

- 该命令执行后不会对正在进行信令流程的用户立即生效，该命令中的限制会在用户的下一次信令流程中生效。
- 此配置涉及“LTE和5G SA网络间重选”特性（特性编号：WSFD-104510，license部件编码：LKV2NRBL5）和“LTE和5G SA网络间切换”特性（特性编号：WSFD-104511，license部件编码：LKV2PHBL5），请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置融合PGW-C/SMF选择策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “HOME_USER（本网用户）”<br>- “FOREIGN_USER（外网用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用以指定待配置融合PGW-C/SMF选择策略用户的IMSI前缀。<br>前提条件：只有<br>“SUBRANGE（用户范围）”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>说明：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI。<br>数据来源：全网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>- 符号“*”表示通配符，即不限制APNNI。如果“APNNI”为“*”，表示该记录适用于所有的APNNI，否则该记录适用于指定的APNNI记录。 |
| CUSLABEL | 定制标识 | 可选必选说明：可选参数<br>参数含义：该参数用于为具有访问5G能力的用户配置定制的APN域名标识，以便为终端选择特定融合的PGW-C/SMF。<br>数据来源：本端规划<br>取值范围：1～32位字符串。<br>默认值：无<br>配置原则：LABEL的构成字符只能是字母A～Z或a～z、数字0～9、符号“-”和“.”，并且“-”和“.”不能是LABEL的开头和结尾，字母不区分大小写。<br>说明：在使用APN进行DNS解析寻址PGW-C+SMF前，将为5G终端定制标识并加入到APN-NI和APN-OI之间，然后将扩展的APN发送到DNS Server或Hostfile进行DNS解析。例如APN-NI为“HUAWEI.COM”，APN-OI为“MNC123.MCC456.GPRS”，<br>“定制标识”<br>为<br>“N1”<br>，则发送到DNS Server或Hostfile进行DNS解析的扩展APN为“HUAWEI.COM.N1.MNC123.MCC456.GPRS”。如果启用定制标识后，APN长度超过100字节，可能会被DNS服务器拒绝。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于对配置记录的描述。<br>数据来源：本端规划<br>取值范围：1～32位字符串。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N26GWSELPLCY]] · N26融合网关选择策略（N26GWSELPLCY）

## 使用实例

修改N26融合网关选择策略，配置 “用户范围” 为 “ALL_USER（所有用户）” ， “APNNI” 为 “HUAWEI1.com” ， “定制标识” 为 “Huawei” ：

```
MOD N26GWSELPLCY:SUBRANGE=ALL_USER, APNNI="HUAWEI1.com", CUSLABEL="Huawei";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改N26融合网关选择策略(MOD-N26GWSELPLCY)_26146138.md`
