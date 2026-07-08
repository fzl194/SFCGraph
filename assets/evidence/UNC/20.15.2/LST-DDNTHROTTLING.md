# 查询DDN Throttling功能（LST DDNTHROTTLING）

- [命令功能](#ZH-CN_MMLREF_0304284711__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0304284711__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0304284711__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0304284711__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0304284711__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0304284711)

**适用NF：SGW-C、SMF**

该命令用于查询DDN Throttling功能是否开启。

## [注意事项](#ZH-CN_MMLREF_0304284711)

无

#### [操作用户权限](#ZH-CN_MMLREF_0304284711)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0304284711)

无

## [使用实例](#ZH-CN_MMLREF_0304284711)

假设要查询DDN Throttling功能：

```
%%LST DDNTHROTTLING:;%%
RETCODE = 0  操作成功

DDN Throttling
--------------
DDN Throttling功能开关  =  使能
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0304284711)

| 输出项名称 | 输出项解释 |
| --- | --- |
| DDN Throttling功能开关 | 该参数用于控制DDN Throttling功能是否开启。 |
