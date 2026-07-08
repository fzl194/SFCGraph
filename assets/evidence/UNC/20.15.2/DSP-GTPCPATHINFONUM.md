# 显示GTPC路径数目（DSP GTPCPATHINFONUM）

- [命令功能](#ZH-CN_MMLREF_0209651616__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651616__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651616__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651616__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209651616__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209651616)

**适用NF：AMF、PGW-C、SGW-C、GGSN**

该命令用于查询GTP-C路径数目。

## [注意事项](#ZH-CN_MMLREF_0209651616)

当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效，请使用命令DSP GTPCPATHNUM查询。

#### [操作用户权限](#ZH-CN_MMLREF_0209651616)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651616)

无

## [使用实例](#ZH-CN_MMLREF_0209651616)

查询GTP-C路径数目：DSP GTPCPATHINFONUM:;

```
%%DSP GTPCPATHINFONUM:;%%
RETCODE = 0  操作成功

结果如下
--------
路径数目  =  0
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209651616)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 路径数目 | 该参数用于指示GTP-C路径数目。 |
