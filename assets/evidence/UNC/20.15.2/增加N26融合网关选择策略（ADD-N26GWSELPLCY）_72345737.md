# 增加N26融合网关选择策略（ADD N26GWSELPLCY）

- [命令功能](#ZH-CN_CONCEPT_0000001172345737__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001172345737__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001172345737__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001172345737__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001172345737__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001172345737__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001172345737)

**适用网元：MME**

该命令用于LTE和5G互通组网部署时，为不同的5G用户配置融合的PGW-C/SMF选择策略。

#### [注意事项](#ZH-CN_CONCEPT_0000001172345737)

- 此命令最大记录数为4096。
- 该命令执行后不会对正在进行信令流程的用户立即生效，该命令中的限制会在用户的下一次信令流程中生效。
- 此配置涉及“LTE和5G SA网络间重选”特性（特性编号：WSFD-104510，license部件编码：LKV2NRBL5）和“LTE和5G SA网络间切换”特性（特性编号：WSFD-104511，license部件编码：LKV2PHBL5），请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性License是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。
- 当开启PGW重定向功能[ADD PGWRNSI](../../../GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN_P-GW选择/增加PGW重定向配置(ADD PGWRNSI)_18730832.md)后，且触发了PGW重定向时，重定向目标PGW优先级高于该命令策略选出的PGW。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001172345737)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0000001172345737)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001172345737)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置融合PGW-C/SMF选择策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “HOME_USER（本网用户）”<br>- “FOREIGN_USER（外网用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无<br>配置原则：<br>- LTE与5G互操作控制策略优先级高到低为：“IMSI_PREFIX（指定IMSI前缀）”，“FOREIGN_USER（外网用户）”或“HOME_USER（本网用户）”，“ALL_USER（所有用户）”。<br>- 系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用以指定待配置融合PGW-C/SMF选择策略用户的IMSI前缀。<br>前提条件：只有<br>“SUBRANGE（用户范围）”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI。<br>数据来源：全网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>- 符号“*”表示通配符，即不限制APNNI。如果“APNNI”为“*”，表示该记录适用于所有的APNNI，否则该记录适用于指定的APNNI记录。 |
| CUSLABEL | 定制标识 | 可选必选说明：必选参数<br>参数含义：该参数用于为具有访问5G能力的用户配置定制的APN域名标识，以便为终端选择特定融合的PGW-C/SMF。<br>数据来源：本端规划<br>取值范围：1～32位字符串。<br>默认值：无<br>配置原则：LABEL的构成字符只能是字母A～Z或a～z、数字0～9、符号“-”和“.”，并且“-”和“.”不能是LABEL的开头和结尾，字母不区分大小写。<br>说明：在使用APN进行DNS解析寻址PGW-C+SMF前，将为5G终端定制标识并加入到APN-NI和APN-OI之间，然后将扩展的APN发送到DNS Server或Hostfile进行DNS解析。例如APN-NI为“HUAWEI.COM”，APN-OI为“MNC123.MCC456.GPRS”，<br>“定制标识为”<br>“N1”<br>，则发送到DNS Server或Hostfile进行DNS解析的扩展APN为“HUAWEI.COM.N1.MNC123.MCC456.GPRS”。如果启用定制标识后，APN长度超过100字节，可能会被DNS服务器拒绝。<br>注：设置参数“定制标识”请同步参考ADD N26IWKPLCY中的“融合PGW-C/SMF选择策略”。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于对配置记录的描述。<br>数据来源：本端规划<br>取值范围：1～32位字符串。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001172345737)

增加N26融合网关选择策略， “用户范围” 为 “ALL_USER（所有用户）” ， “APNNI” 为 “HUAWEI1.com” ， “CUSLABEL” 为 “huawei” ：

```
ADD N26GWSELPLCY: SUBRANGE=ALL_USER, APNNI="HUAWEI1.com", CUSLABEL="huawei";
```
