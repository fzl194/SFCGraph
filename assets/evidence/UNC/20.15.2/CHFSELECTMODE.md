# 设置用户激活和在线恢复场景CHF的选择模式（SET CHFSELECTMODE）

- [命令功能](#ZH-CN_MMLREF_0234667404__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0234667404__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0234667404__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0234667404__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0234667404)

**适用NF：PGW-C、SMF**

该命令用于设置用户激活和在线恢复场景CHF的选择模式。

## [注意事项](#ZH-CN_MMLREF_0234667404)

- 该命令执行后立即生效。

- 不允许同时配置FIRSTMODE和SECONDMODE为NRF模式。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| FIRSTMODE |
| --- |
| MODE3GPP |

#### [操作用户权限](#ZH-CN_MMLREF_0234667404)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0234667404)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FIRSTMODE | 首选模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CHF的首选选择模式。<br>数据来源：全网规划<br>取值范围：<br>- “MODE3GPP（3GPP）”：按3GPP定义的优先进行选择CHF<br>- “PCF（PCF）”：使用PCF指定的CHF<br>- “NRF（NRF）”：使用NRF发现的CHF<br>- “LOCAL（Local）”：使用本地配置的CHF<br>默认值：无。<br>配置原则：无 |
| SECONDMODE | 备选模式 | 可选必选说明：该参数在"FIRSTMODE"配置为"PCF"、"NRF"时为条件可选参数。<br>参数含义：该参数用于指定CHF的备选选择模式。<br>数据来源：全网规划<br>取值范围：<br>- “NRF（NRF）”：使用NRF发现的CHF<br>- “LOCAL（Local）”：使用本地配置的CHF<br>- “NOCONFIG（不配置）”：不进行配置<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CHFSELECTMODE查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0234667404)

设置CHF选择模式：首选模式NRF，备选模式LOCAL。

```
SET CHFSELECTMODE: FIRSTMODE=NRF, SECONDMODE=LOCAL;
```
