# 设置AMF小范围CHR存储配置（SET NGCHRSTORCFG）

- [命令功能](#ZH-CN_MMLREF_0000001214120442__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001214120442__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001214120442__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001214120442__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001214120442)

**适用NF：AMF**

该命令用于设置AMF小范围CHR存储配置。

## [注意事项](#ZH-CN_MMLREF_0000001214120442)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CHRSPESUBSAVE | CHRSAVEPATH |
| --- | --- |
| DISABLE | SAVE_OMU |

#### [操作用户权限](#ZH-CN_MMLREF_0000001214120442)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001214120442)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHRSPESUBSAVE | 小范围CHR使能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否开启小范围CHR功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGCHRSTORCFG查询当前参数配置值。<br>配置原则：<br>当UCF未部署时选择存储到OMU，否则按需选择。 |
| CHRSAVEPATH | 小范围CHR存储路径 | 可选必选说明：该参数在"CHRSPESUBSAVE"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于控制小范围CHR存储路径。<br>数据来源：本端规划<br>取值范围：<br>- SAVE_OMU（保存到OMU）<br>- SAVE_UCF（保存到UCF）<br>- SAVE_OMU_AND_UCF（保存到OMU和UCF）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NGCHRSTORCFG查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001214120442)

若开启小范围CHR功能且保存路径为OMU，执行如下命令：

```
SET NGCHRSTORCFG: CHRSPESUBSAVE=ENABLE, CHRSAVEPATH=SAVE_OMU;
```
