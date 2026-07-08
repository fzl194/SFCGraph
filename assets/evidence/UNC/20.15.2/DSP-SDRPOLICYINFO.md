# 显示SDRC中的策略版本信息（DSP SDRPOLICYINFO）

- [命令功能](#ZH-CN_MMLREF_0000001321972917__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001321972917__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001321972917__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001321972917__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001321972917__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001321972917)

该命令用于查询SDRC中的策略版本信息，包括版本号、Checksum、更新时间信息。

## [注意事项](#ZH-CN_MMLREF_0000001321972917)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001321972917)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001321972917)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLCYTYPE | 策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定策略类型。<br>数据来源：本端规划<br>取值范围：<br>- AppRoute（AppRoute）<br>- Topic（Topic）<br>- VpnIp（VpnIp）<br>- Token（Token）<br>- KeyMatch（KeyMatch）<br>- Service（Service）<br>- NextHop（NextHop）<br>- LbPolicy（LbPolicy）<br>- Vpn（Vpn）<br>- LbTopo（LbTopo）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001321972917)

查询SDRC中的策略版本信息：

```
%%DSP SDRPOLICYINFO: PLCYTYPE=Token;%%
RETCODE = 0  操作成功

结果如下
--------
策略         版本号  Checksum  更新时间
Token:1034   1       1         2022-05-16 15:04:05
Token:129    2       2         2022-05-16 14:04:05
(结果个数 = 2)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001321972917)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 策略 | 该参数用于显示策略。 |
| 版本号 | 该参数用于显示策略的版本号。 |
| Checksum | 该参数用于显示策略的Checksum信息。 |
| 更新时间 | 该参数用于显示策略的更新时间。 |
