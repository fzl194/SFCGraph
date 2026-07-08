# 查询3GPP PS data off功能相关的参数（LST PSDATAOFFFUNC）

- [命令功能](#ZH-CN_MMLREF_0000001135439598__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001135439598__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001135439598__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001135439598__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001135439598__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001135439598)

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询3GPP PS data off功能相关的参数。

## [注意事项](#ZH-CN_MMLREF_0000001135439598)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001135439598)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001135439598)

无

## [使用实例](#ZH-CN_MMLREF_0000001135439598)

当运营商需要查询是否开启3GPP PS data off功能时，通过该命令查询开关状态：

```
%%LST PSDATAOFFFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
PS data off功能开关  =  使能
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001135439598)

| 输出项名称 | 输出项解释 |
| --- | --- |
| PS data off功能开关 | 该参数用于控制是否使能3GPP PS data off功能。当使能3GPP PS data off功能，且UE上报的3GPP PS data off UE status为activated（关闭移动数据开关），网络侧会修改策略使UPF下行数据不转发给UE，下行数据不被计费。豁免业务不受3GPP PS data off能力控制。IMS业务不需要配置、直接为豁免业务，如果需要配置其他业务为豁免业务，请使用ADD EXEMPTSERVICE命令。 |
