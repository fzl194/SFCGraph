# 查询VLR向MME发送SGsAP-RESET-INDICATION消息定时器配置（LST VLRRESETTIMER）

- [命令功能](#ZH-CN_MMLREF_0000001411591169__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001411591169__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001411591169__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001411591169__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001411591169__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001411591169)

**适用NF：SMSF**

该命令用于查询VLR向MME发送SGsAP-RESET-INDICATION消息后，等待接收MME返回的SGsAP-RESET-ACK响应的定时器配置。

## [注意事项](#ZH-CN_MMLREF_0000001411591169)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001411591169)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001411591169)

无

## [使用实例](#ZH-CN_MMLREF_0000001411591169)

运营商希望查询VLR向MME发送SGsAP-RESET-INDICATION消息后，等待接收MME返回的SGsAP-RESET-ACK响应的定时器配置，执行如下命令：

```
LST VLRRESETTIMER:;
%%LST VLRRESETTIMER:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
重发开关 =  打开
重发次数 =  2
VLR等待接收MME SGsAP-RESET-ACK响应(秒) = 5

(结果个数 = 1)
```

## [输出结果说明](#ZH-CN_MMLREF_0000001411591169)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 重发开关 | 该参数用于设置VLR向MME发送SGsAP-RESET-INDICATION消息定时器超时后，重发SGsAP-RESET-INDICATION消息的开关。 |
| 重发次数 | 该参数用于设置VLR向MME发送SGsAP-RESET-INDICATION消息定时器超时后，可重发的最大次数。 |
| VLR等待接收MME SGsAP-RESET-ACK响应(秒) | 该参数用于设置VLR向MME发送SGsAP-RESET-INDICATION消息后，等待接收MME返回的SGsAP-RESET-ACK响应的定时器超时时长。 |
