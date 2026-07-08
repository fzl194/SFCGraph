# 显示SDRC中的策略Key信息（DSP SDRPOLICYKEYS）

- [命令功能](#ZH-CN_MMLREF_0000001322132897__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001322132897__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001322132897__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001322132897__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001322132897__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001322132897)

该命令用于显示SDRC中的策略Key信息。

## [注意事项](#ZH-CN_MMLREF_0000001322132897)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001322132897)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001322132897)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYTYPE | 策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定策略类型。<br>数据来源：本端规划<br>取值范围：<br>- AppRoute（AppRoute）<br>- Token（Token）<br>- Service（Service）<br>- NextHop（NextHop）<br>- KeyMatch（KeyMatch）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001322132897)

查询AppRoute存储的key信息：

```
%%DSP SDRPOLICYKEYS: POLICYTYPE=AppRoute;%%
RETCODE = 0  操作成功

结果如下
--------
Sdrc存储策略的Key
125
114
(结果个数 = 2)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001322132897)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Sdrc存储策略的Key | 该参数用于显示Sdrc存储策略的Key。 |
