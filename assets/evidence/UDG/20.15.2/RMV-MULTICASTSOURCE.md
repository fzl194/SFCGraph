# 删除IGMP Snooping组播源配置（RMV MULTICASTSOURCE）

- [命令功能](#ZH-CN_CONCEPT_0000206855604486__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206855604486__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206855604486__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206855604486__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206855604486__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206855604486)

**适用NF：UPF**

该命令用于删除IGMP Snooping组播源配置。

#### [注意事项](#ZH-CN_CONCEPT_0000206855604486)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206855604486)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206855604486)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD NGVNINSTANCE命令配置生成。 |
| MCSOURCETYPE | 组播源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置组播源类型。<br>数据来源：全网规划<br>取值范围：<br>- IMSI：IMSI。<br>- DFSRPAIR：双发选收结对。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件可选参数<br>前提条件：该参数在“MCSOURCETYPE”配置为“IMSI”时为可选参数。<br>参数含义：组播源IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15，每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| DFSRPAIRID | 双发选收结对ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“MCSOURCETYPE”配置为“DFSRPAIR”时为可选参数。<br>参数含义：该参数用于配置双发选收结对ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1-2048。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000206855604486)

删除5G LAN组的N3侧的组播源：

```
RMV MULTICASTSOURCE: VNINSTANCE="a0000001-460-003-02", MCSOURCETYPE=IMSI, IMSI="217456789012353";

%%RMV MULTICASTSOURCE: VNINSTANCE="a0000001-460-003-02", MCSOURCETYPE=IMSI, IMSI="217456789012353";%%
RETCODE = 0  操作成功

---    END
```
