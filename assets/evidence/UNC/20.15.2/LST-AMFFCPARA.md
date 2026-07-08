# 查询AMF自保流控参数（LST AMFFCPARA）

- [命令功能](#ZH-CN_MMLREF_0225120883__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0225120883__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0225120883__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0225120883__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0225120883__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0225120883)

**适用NF：AMF**

该命令用于查询AMF自保流控参数。

## [注意事项](#ZH-CN_MMLREF_0225120883)

“CPU过载控制门限”参数在UNC 20.5.1版本及之后不再使用。“阈值”后续通过LST FCPARAM命令查询。

#### [操作用户权限](#ZH-CN_MMLREF_0225120883)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0225120883)

无

## [使用实例](#ZH-CN_MMLREF_0225120883)

查询AMF自保流控参数：

```
%%LST AMFFCPARA:;%%
RETCODE = 0  操作成功

输出结果如下
------------------------
              CPU过载控制门限(%)  =  70
                        流控措施  =  丢弃
           Backoff timer信元开关  =  关闭
         Backoff timer最小值(秒)  =  900
         Backoff timer最大值(秒)  =  1800
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0225120883)

| 输出项名称 | 输出项解释 |
| --- | --- |
| CPU过载控制门限(%) | 该参数用于设置AMF自保流控功能过载CPU门限。 |
| 流控措施 | 该参数用于设置初始注册请求消息被流控时系统采取的措施。其他消息则直接丢弃。 |
| Backoff Timer信元开关 | 该参数用于自保流控情况下，注册拒绝消息中是否携带backoff timer信元。 |
| Backoff timer最小值(秒) | 本参数用于设置Backoff timer的最小值，用于计算发给终端的Backoff timer时长。 |
| Backoff timer最大值(秒) | 本参数用于设置Backoff timer的最大值，用于计算发给终端的Backoff timer时长。 |
