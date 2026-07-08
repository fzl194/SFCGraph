# 查询VoPS配置（LST NGIMSVOPS）

- [命令功能](#ZH-CN_MMLREF_0209653054__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653054__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653054__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653054__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653054__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653054)

**适用NF：AMF**

该命令用于查询AMF侧对PS域IMS语音能力的支持情况。

## [注意事项](#ZH-CN_MMLREF_0209653054)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209653054)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653054)

无

## [使用实例](#ZH-CN_MMLREF_0209653054)

执行如下命令查询AMF侧对PS域IMS语音能力的支持情况，执行如下命令：

```
%%LST NGIMSVOPS:;%%
RETCODE = 0  操作成功

结果如下
--------
          AMF是否支持IMS语音  =  支持
Data Centric类型终端支持VoPS  =  支持
           AMF是否支持IMS语音 =  先查询UE无线能力
   连接态下去激活用户面原因值 =  正常释放
       是否检查用户S1Mode能力 =  关闭
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209653054)

| 输出项名称 | 输出项解释 |
| --- | --- |
| AMF是否支持IMS语音 | 该参数用于指定AMF侧的所有跟踪区是否都支持PS域IMS语音能力。 |
| Data Centric类型终端支持VoPS | 该参数用于指定Data Centric类型终端是否都支持IMS语音能力。 |
| 用户无线能力检查时序 | 该参数用于配置AMF发送INITIAL CONTEXT SETUP REQUEST或者HANDOVER REQUEST驱动基站建立安全上下文和发送UE RADIO CAPABILITY CHECK REQUEST查询UE无线能力两种消息的先后顺序。 |
| 连接态下去激活用户面原因值 | 该参数用于控制在连接态下，AMF收到initial UE类型的服务请求和移动性注册消息时，发送给SMF的去激活用户面消息中携带的原因值。 |
| 是否检查用户S1Mode能力 | 该参数用于指定是否检查用户的S1Mode能力，开启后只有支持S1Mode的UE才允许使用IMS VoPS业务。该能力来源于UE在Registration request消息中携带的5GMM capability信元。 |
