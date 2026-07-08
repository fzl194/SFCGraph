# 查询Credit Pooling功能（LST CREDITPOOLFUNC）

- [命令功能](#ZH-CN_MMLREF_0000002175240938__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000002175240938__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000002175240938__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000002175240938__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000002175240938__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000002175240938)

**适用NF：PGW-C、GGSN**

该命令用以查询配置的Credit Pooling功能参数。

## [注意事项](#ZH-CN_MMLREF_0000002175240938)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000002175240938)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000002175240938)

无

## [使用实例](#ZH-CN_MMLREF_0000002175240938)

查询配置的Credit Pooling特性功能参数，执行如下命令：

```
%%LST CREDITPOOLFUNC:;%%
RETCODE = 0  操作成功
结果如下
------------------------
          Credit Pooling功能开关 = DISABLE  
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000002175240938)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Credit Pooling功能开关 | 该参数用于配置Credit Pooling功能开关。 |
