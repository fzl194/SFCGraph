# 查询UPF选择策略次序（LST UPSELECTPRI）

- [命令功能](#ZH-CN_MMLREF_0209652669__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652669__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652669__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652669__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209652669__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209652669)

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询SMF选择UPF场景下的UPF选择策略次序。

## [注意事项](#ZH-CN_MMLREF_0209652669)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209652669)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652669)

无

## [使用实例](#ZH-CN_MMLREF_0209652669)

查询SMF选择UPF场景下的优选条件： LST UPSELECTPRI:;

```
%%LST UPSELECTPRI:;%%
RETCODE = 0  操作成功。

结果如下
------------------------
第一优先级  =  LocS11Priority
第二优先级  =  Combined UPF
第三优先级  =  Load Balancing Policy
(结果个数 = 1)
```

## [输出结果说明](#ZH-CN_MMLREF_0209652669)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 第一优先级 | 该参数用于标识SMF选择UPF时的第一优先级。 |
| 第二优先级 | 该参数用于标识SMF选择UPF时的第二优先级。 |
| 第三优先级 | 该参数用于标识SMF选择UPF时的第三优先级。 |
