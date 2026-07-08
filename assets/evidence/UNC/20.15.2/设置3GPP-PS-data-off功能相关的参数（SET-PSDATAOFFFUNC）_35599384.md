# 设置3GPP PS data off功能相关的参数（SET PSDATAOFFFUNC）

- [命令功能](#ZH-CN_MMLREF_0000001135599384__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001135599384__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001135599384__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001135599384__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001135599384)

**适用NF：PGW-C、SMF、GGSN**

该命令用于设置3GPP PS data off功能相关的参数。

## [注意事项](#ZH-CN_MMLREF_0000001135599384)

- 当PS data off功能开关从“DISABLE（不使能）”改为“ENABLE（使能）”时，在UE的下次激活流程中生效。当PS data off功能开关从“ENABLE（使能）”改为“DISABLE（不使能）”时，立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PSDATAOFFSWITCH |
| --- |
| DISABLE |

#### [操作用户权限](#ZH-CN_MMLREF_0000001135599384)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001135599384)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PSDATAOFFSWITCH | PS data off功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否使能3GPP PS data off功能。当使能3GPP PS data off功能，且UE上报的3GPP PS data off UE status为activated（关闭移动数据开关），网络侧会修改策略使UPF下行数据不转发给UE，下行数据不被计费。豁免业务不受3GPP PS data off能力控制。IMS业务不需要配置、直接为豁免业务，如果需要配置其他业务为豁免业务，请使用ADD EXEMPTSERVICE命令。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PSDATAOFFFUNC查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001135599384)

当运营商需要使用3GPP PS data off功能时，通过该命令打开功能开关：

```
SET PSDATAOFFFUNC: PSDATAOFFSWITCH=ENABLE;
```
