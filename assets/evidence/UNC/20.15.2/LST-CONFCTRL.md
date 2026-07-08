# 查看冲突控制参数（LST CONFCTRL）

- [命令功能](#ZH-CN_MMLREF_0209654431__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209654431__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209654431__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209654431__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209654431__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209654431)

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询低优先级流程消息的缓存重发次数和缓存重发时间间隔。

## [注意事项](#ZH-CN_MMLREF_0209654431)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209654431)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209654431)

无

## [使用实例](#ZH-CN_MMLREF_0209654431)

查询缓存重发次数和缓存重发时间间隔：

```
%%LST CONFCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
       EPS消息缓存重发的次数  =  3
EPS消息缓存重发的时间间隔(s)  =  2
        NR消息缓存重发的次数  =  3
 NR消息缓存重发的时间间隔(s)  =  2
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209654431)

| 输出项名称 | 输出项解释 |
| --- | --- |
| EPS消息缓存重发的次数 | 该参数用于设置冲突场景下，Create Bearer Request/Update Bearer Request/Delete Bearer Request消息的缓存次数，次数达到设置值时，消息将被丢弃。 |
| EPS消息缓存重发的时间间隔(s) | 该参数用于设置冲突场景下，从收到Create Bearer Response/Update Bearer Response/Delete Bearer Response开始，到重发Create Bearer Request/Update Bearer Request/Delete Bearer Request的时间间隔。 |
| NR消息缓存重发的次数 | 该参数用于设置冲突场景下，缓存网络侧触发的Session Modify流程的次数，次数达到设置值时，消息将被丢弃。 |
| NR消息缓存重发的时间间隔(s) | 该参数用于设置冲突场景下，缓存的网络侧触发的Session Modify流程重发的时间间隔。 |
