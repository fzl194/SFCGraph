# 显示本端Recovery值及系统重启时间（DSP LOCALRECOVERY）

- [命令功能](#ZH-CN_MMLREF_0000001088248944__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001088248944__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001088248944__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001088248944__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001088248944__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001088248944)

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF、GGSN、SMSF、NCG**

该命令用于查询本端Recovery值及系统重启时间。

## [注意事项](#ZH-CN_MMLREF_0000001088248944)

- 当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效，请使用命令DSP RECOVERY / MOD RECOVERY配置。
- 本端Recovery值仅在公共软参DWORD4 BIT16设置为1时增加。
- 系统重启时间是否刷新由DWORD4 BIT15软参控制。

#### [操作用户权限](#ZH-CN_MMLREF_0000001088248944)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001088248944)

无

## [使用实例](#ZH-CN_MMLREF_0000001088248944)

查询本端Recovery值及系统重启时间：DSP LOCALRECOVERY:;

```
%%DSP LOCALRECOVERY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
  本端Recovery值  =  0
      系统重启时间  =  2021-03-04 00:00:00
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001088248944)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 本端Recovery值 | 该参数用于表示本端Recovery值，系统重启后本值加1。 |
| 系统重启时间 | 该参数用于表示系统重启时间。如果值为1970-01-01 00:00:00，则说明系统没有重启，可以忽略。 |
