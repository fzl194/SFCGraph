# 查询N7发送信元处理控制（LST N7SNDATTRCTRL）

- [命令功能](#ZH-CN_MMLREF_0296242211__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296242211__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296242211__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296242211__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0296242211__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0296242211)

**适用NF：GGSN**

该命令用于查询N7接口发送消息中部分信元的处理方式。

## [注意事项](#ZH-CN_MMLREF_0296242211)

无

#### [操作用户权限](#ZH-CN_MMLREF_0296242211)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0296242211)

无

## [使用实例](#ZH-CN_MMLREF_0296242211)

查询N7接口发送消息中部分信元的处理方式。

```
%%LST N7SNDATTRCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
携带GERAN类信元  =  是
携带UTRAN类信元  =  是
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0296242211)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 携带GERAN类信元 | 该参数用于指定2G接入时N7接口是否携带GERAN类信元。设置为使能时，2G接入时N7接口支持携带sgsnAddr、geraLocation、rattype信元。 |
| 携带UTRAN类信元 | 该参数用于指定3G接入时N7接口是否携带UTRAN类信元。设置为使能时，3G接入时N7接口支持携带sgsnAddr、utraLocation、rattype信元。 |
