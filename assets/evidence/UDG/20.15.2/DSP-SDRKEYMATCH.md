# 显示SDRC中的KeyMatch信息（DSP SDRKEYMATCH）

- [命令功能](#ZH-CN_MMLREF_0000001301704014__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001301704014__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001301704014__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001301704014__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001301704014__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001301704014)

该命令用于查询SDRC中指定AppType的KeyMatch策略信息。

> **说明**
> 无

#### [操作用户权限](#ZH-CN_MMLREF_0000001301704014)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001301704014)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPTYPE | App类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示该KeyMatch所归属业务的类型，可通过<br>[**DSP SDRPOLICYKEYS**](显示SDRC中的策略Key信息（DSP SDRPOLICYKEYS）_22132897.md)<br>: POLICYTYPE=KeyMatch;命令获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001301704014)

使用如下命令查询SDRC中缓存的KeyMatch策略信息：

```
%%DSP SDRKEYMATCH: APPTYPE=1035;%%
RETCODE = 0  操作成功

结果如下
--------
App类型                        身份标识

1035                              65465
1035                              10554
(结果个数 = 2)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001301704014)

| 输出项名称 | 输出项解释 |
| --- | --- |
| App类型 | 该参数用于表示该KeyMatch所归属业务的类型，可通过<br>[**DSP SDRPOLICYKEYS**](显示SDRC中的策略Key信息（DSP SDRPOLICYKEYS）_22132897.md)<br>: POLICYTYPE=KeyMatch;命令获取。 |
| 身份标识 | 该参数用于表示KeyMatch策略的Identity值。 |
