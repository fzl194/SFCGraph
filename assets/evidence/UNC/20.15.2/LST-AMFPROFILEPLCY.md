# 查询AMF上报NFPROFILE策略（LST AMFPROFILEPLCY）

- [命令功能](#ZH-CN_MMLREF_0000001095774946__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001095774946__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001095774946__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001095774946__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001095774946__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001095774946)

**适用NF：AMF**

该命令用于查询AMF向NRF上报NFPROFILE信息的策略。

## [注意事项](#ZH-CN_MMLREF_0000001095774946)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001095774946)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001095774946)

无

## [使用实例](#ZH-CN_MMLREF_0000001095774946)

查询AMF向NRF上报NFPROFILE信息的策略。

```
%%LST AMFPROFILEPLCY:;%%
RETCODE = 0  操作成功

结果如下
--------
TAI上报策略  =  TAILIST格式
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001095774946)

| 输出项名称 | 输出项解释 |
| --- | --- |
| TAI上报策略 | 该参数用于指定AMF向NRF上报的TAI列表的格式。AMF向NRF最终上报的TAI列表的格式还受SET NFNRFMGMTPARA命令的影响。 |
