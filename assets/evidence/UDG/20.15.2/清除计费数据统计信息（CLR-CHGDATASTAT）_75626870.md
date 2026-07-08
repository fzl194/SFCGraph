# 清除计费数据统计信息（CLR CHGDATASTAT）

- [命令功能](#ZH-CN_CONCEPT_0000203075626870__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203075626870__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203075626870__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203075626870__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203075626870__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203075626870)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于清除计费数据统计信息，比如预定义URR流量上报信息、UserProfile安装次数、整体转发和计费流量差异比例信息、缺省费率流量增量信息、子协议Top30的流量增量信息、预定义规则Top20的匹配次数增量信息、URR Top20的流量增量信息。

#### [注意事项](#ZH-CN_CONCEPT_0000203075626870)

- 该命令执行后立即生效。
- 执行该命令后会清空已保存的统计数据，导致历史数据无法查询。

#### [操作用户权限](#ZH-CN_CONCEPT_0000203075626870)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203075626870)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATTYPE | 统计类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要显示计费数据的统计类型。<br>数据来源：本端规划<br>取值范围：ENUM。<br>- UPINSTALL：查询UserProfile安装次数。<br>- URRVOLUME：查询URR流量统计信息。<br>- WHOLE_VOLUME_CONDITION：整体转发和计费流量差异比例信息。<br>- TOPN_URR_VOLUME：URR流量增量Top20信息。<br>- RULE_MATCH_NUM：预定义规则Top20的匹配次数增量信息。<br>- PROTOCOL_VOLUME：协议Top30的流量增量信息。<br>- DEFAULT_URR_VOLUME：缺省费率流量增量信息。<br>默认值：无<br>配置原则：无 |
| URRID | URRID(Predef) | 可选必选说明：条件可选参数<br>前提条件：该参数在“STATTYPE”配置为“URRVOLUME”时为可选参数。<br>参数含义：用于指示URR标识（预定义）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～2147483646。<br>默认值：无<br>配置原则：无 |
| USERPROFILENAME | UserProfileName | 可选必选说明：条件可选参数<br>前提条件：该参数在“STATTYPE”配置为“UPINSTALL”时为可选参数。<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000203075626870)

清除URR流量统计数据：

```
%%CLR CHGDATASTAT: STATTYPE=URRVOLUME;%%
RETCODE = 0  Operation succeeded

---    END
```
