# 查询Link MTU值（LST LINKMTU）

- [命令功能](#ZH-CN_MMLREF_0000001135519271__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001135519271__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001135519271__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001135519271__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001135519271__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001135519271)

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询设置的Link MTU值。

## [注意事项](#ZH-CN_MMLREF_0000001135519271)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001135519271)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001135519271)

无

## [使用实例](#ZH-CN_MMLREF_0000001135519271)

查询Link MTU配置：

```
%%LST LINKMTU:;%%
RETCODE = 0  操作成功

结果如下
------------------------
携带Link MTU开关  =  Enable
   IPv4 Link MTU  =  1358
 Non-IP Link MTU  =  1358
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001135519271)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 携带Link MTU开关 | 该参数用于控制UNC是否在PCO信元中携带Link MTU值给终端。 |
| IPv4 Link MTU | 该参数用于设置UNC在PCO信元中响应给终端的IPv4 Link MTU值。 |
| Non-IP Link MTU | 该参数用于设置UNC在PCO信元中响应给终端的Non-IP Link MTU值。 |
