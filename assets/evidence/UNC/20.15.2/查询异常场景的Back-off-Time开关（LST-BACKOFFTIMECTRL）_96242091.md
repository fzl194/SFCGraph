# 查询异常场景的Back-off Time开关（LST BACKOFFTIMECTRL）

- [命令功能](#ZH-CN_MMLREF_0296242091__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296242091__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296242091__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296242091__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0296242091__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0296242091)

**适用NF：GGSN、PGW-C、SGW-C**

该命令用来查询异常场景下激活响应中携带Back-off Time开关。

## [注意事项](#ZH-CN_MMLREF_0296242091)

无

#### [操作用户权限](#ZH-CN_MMLREF_0296242091)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0296242091)

无

## [使用实例](#ZH-CN_MMLREF_0296242091)

查询异常场景的携带Back-off Time的开关：

```
%%LST BACKOFFTIMECTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
 控制APN锁定导致激活失败应答消息中携带Back-off Time字段的开关  =  不使能
           控制激活应答消息中携带GGSN Back-off Time字段的开关  =  不使能
控制承载受限导致激活失败应答消息中携带Back-off Time字段的开关  =  不使能
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0296242091)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 控制APN锁定导致激活失败应答消息中携带Back-off Time字段的开关 | 该参数用于控制APN锁定导致激活失败应答消息中是否携带Back-off Time。 |
| 控制激活应答消息中携带GGSN Back-off Time字段的开关 | 该参数用于控制激活应答消息中是否携带GGSN Back-off Time。 |
| 控制承载受限导致激活失败应答消息中携带Back-off Time字段的开关 | 该参数用于控制因为承载受限导致激活失败应答消息中是否携带Back-off Time字段。 |
