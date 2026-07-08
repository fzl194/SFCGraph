# 修改EPS与5GS互操作本地策略(MOD N26IWKPLCY)

- [命令功能](#ZH-CN_CONCEPT_0000001172345735__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001172345735__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001172345735__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001172345735__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001172345735__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001172345735__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001172345735)

**适用网元：MME**

该命令用于5GS部署时，修改用户的EPS与5GS互操作本地策略。

#### [注意事项](#ZH-CN_CONCEPT_0000001172345735)

- 该命令执行后不会对正在进行信令流程的用户立即生效，该命令中的限制会在用户的下一次信令流程中生效。
- 此配置涉及“LTE和5G SA网络间重选”特性（特性编号：WSFD-104510，license部件编码：LKV2NRBL5）和“LTE和5G SA网络间切换”特性（特性编号：WSFD-104511，license部件编码：LKV2PHBL5），请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性License是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“打开”，具体相关特性请参考参数的说明。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001172345735)

manage-ug；system-ug；

#### [网管用户权限](#ZH-CN_CONCEPT_0000001172345735)

G_1，管理员级别命令组；G_2，操作员级别命令组。

#### [参数说明](#ZH-CN_CONCEPT_0000001172345735)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置EPS与5GS互操作策略的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：表示用户范围为系统内所有用户。<br>- “HOME_USER（本网用户）”：表示用户范围为本网用户。<br>- “FOREIGN_USER（外网用户）”：表示用户范围为外网用户。<br>- “IMSI_PREFIX（指定IMSI前缀）”：表示用户范围通过IMSI前缀指定。<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用以指定待配置EPS与5GS互操作本地策略用户的IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>后生效。<br>数据来源：整网规划<br>取值范围：5～15十进制数字字符串<br>默认值：无 |
| IS5GCALLOW | 是否支持接入5GC | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否允许有N1能力的终端接入5GC。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无 |
| ISNRALLOW | 是否允许接入5GS的NR | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定是否允许有N1能力的终端往5GS下的NR切换。<br>前提条件：该参数在<br>“是否支持接入5GC”<br>参数配置为<br>“YES（是）”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无 |
| SMFSELPLCY | 融合PGW-C/SMF选择策略 | 可选必选说明：可选参数<br>参数含义：该参数用于控制5G终端在EPC接入时选择融合PGW-C/SMF的策略。<br>数据来源：整网规划<br>取值范围：<br>- “N1CAP_CNR（N1能力+签约CNR）”<br>- “N1CAP（N1能力）”<br>- “CNR（签约CNR）”<br>- “RESV_PLCY1（预留策略1）”<br>- “RESV_PLCY2（预留策略2）”<br>- “RESV_PLCY3（预留策略3）”<br>- “RESV_PLCY4（预留策略4）”<br>默认值：无 |
| FIVEGSIWK | 5GSIWK策略 | 可选必选说明：可选参数<br>参数含义：该参数用于控制5GSIWK标识的置位策略。<br>数据来源：整网规划<br>取值范围：<br>- “SMF（SMF融合网关）”<br>- “SMF_N1CAP_CNR（SMF融合网关+N1能力+签约CNR）”<br>- “N1CAP_CNR（N1能力+签约CNR）”<br>默认值：“SMF（SMF融合网关）”<br>配置原则：<br>- 如果运营商希望只根据终端是否选择融合的PGW-C/SMF来置位5GSIWK标识，则配置成“SMF（SMF融合网关）”。<br>- 如果运营商希望根据终端是否选择融合的PGW-C/SMF、5G终端N1能力、签约数据的Core Network Restrction和5GS互操作标识的组合来置位5GSIWK标识，则配置成“SMF_N1CAP_CNR（SMF融合网关+N1能力+签约CNR）”。<br>- 如果运营商希望只根据5G终端N1能力、签约数据的Core Network Restrction和5GS互操作标识的组合来置位5GSIWK标识，不管是否选择融合的PGW-C/SMF，则配置成“N1CAP_CNR（N1能力+签约CNR）”。 |
| FIVEGCNRS | 5GCNRS策略 | 可选必选说明：可选参数<br>参数含义：该参数用于控制5GCNRS标识的置位策略。<br>数据来源：整网规划<br>取值范围：<br>- “SMF_SUPPORT(仅融合SMF网关支持)”<br>- “SUPPORT(支持)”<br>- “NOT_SUPPORT(不支持)”<br>默认值：“NOT_SUPPORT(不支持)”<br>配置原则：<br>如果运营商希望仅在选择融合的PGW-C/SMF携带5GCNRS和5GCNRI标识，则配置为“SMF_SUPPORT(仅融合SMF网关支持)”。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于对配置记录的描述。<br>数据来源：整网规划<br>取值范围：0～32位字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001172345735)

修改 “用户范围” 为“所有用户”， “是否支持接入5GC” 为 “NO（否）” ， “是否允许接入5GS的NR” 为 “NO（否）” ， “融合PGW-C/SMF选择策略” 为 “CNR（签约CNR）” 的记录。

MOD N26IWKPLCY: SUBRANGE=ALL_USER, IS5GCALLOW=NO, ISNRALLOW=NO, SMFSELPLCY=CNR;
