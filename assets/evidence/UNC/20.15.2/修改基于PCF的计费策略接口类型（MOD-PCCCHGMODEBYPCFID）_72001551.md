# 修改基于PCF的计费策略接口类型（MOD PCCCHGMODEBYPCFID）

- [命令功能](#ZH-CN_MMLREF_0272001551__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0272001551__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0272001551__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0272001551__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0272001551)

![](修改基于PCF的计费策略接口类型（MOD PCCCHGMODEBYPCFID）_72001551.assets/notice_3.0-zh-cn_2.png)

配置基于PCF的计费策略接口类型不当可能导致PCC用户选择错误接口的PCRF/PCF服务器，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：SMF**

修改基于PCF的计费策略接口类型。

## [注意事项](#ZH-CN_MMLREF_0272001551)

该命令执行后只对新激活用户生效。

#### [操作用户权限](#ZH-CN_MMLREF_0272001551)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0272001551)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCFINSID | PCF实例标识 | 可选必选说明：必选参数<br>参数含义：字符串唯一标识PCF实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>PCF实例标识在TOPO本地配置，或者由NRF返回。需要整网协商配置。 |
| POLICYINTF | 策略接口类型 | 可选必选说明：可选参数<br>参数含义：指定的策略接口类型。<br>数据来源：全网规划<br>取值范围：<br>- “INHERIT（继承）”：继承ADD APNPOLICYMODE或SET POLICYMODE命令配置。<br>- “N7（N7接口）”：使用N7接口。<br>- “Gx（Gx接口）”：使用Gx接口。<br>默认值：无<br>配置原则：无 |
| CHGINTF | 计费接口类型 | 可选必选说明：可选参数<br>参数含义：指定的计费接口类型。<br>数据来源：全网规划<br>取值范围：<br>- “INHERIT（继承）”：继承ADD APNCHGMODE或SET CHGMODE命令配置。<br>- “N40（N40接口）”：使用N40接口。<br>- “GaGy（GaGy接口）”：使用GaGy接口。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0272001551)

修改PCF实例标识为pcf1的策略接口类型为Gx

```
MOD PCCCHGMODEBYPCFID: PCFINSID="pcf1",POLICYINTF=Gx;
```
