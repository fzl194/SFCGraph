# 查询SDRC中的APPROUTERINFO信息（DSP SDRROUTE）

- [命令功能](#ZH-CN_MMLREF_0294730433__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0294730433__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0294730433__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0294730433__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0294730433__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0294730433)

该命令用于查询SDRC中指定APP的ROUTE策略信息。

> **说明**
> 无

#### [操作用户权限](#ZH-CN_MMLREF_0294730433)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0294730433)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPINFO | APP信息 | 可选必选说明：必选参数<br>参数含义：该参数用于表示下发APPROUTE策略的APP信息，可通过<br>[**DSP SDRPOLICYKEYS**](显示SDRC中的策略Key信息（DSP SDRPOLICYKEYS）_22132897.md)<br>: POLICYTYPE=AppRoute;命令获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0294730433)

使用如下命令查询SDRC中缓存的ROUTE策略信息：

```
%%DSP SDRROUTE: APPINFO=129;%%
RETCODE = 0  操作成功

结果如下
--------
                                             APP信息  =  129
                               APP将要发送的TOPIC ID  =  [40964 16387 4129 4135]
                                      APP订阅的TOPIC  =  [sub_topic_id:40961 key_type:2 ]
                                            路由算法  =  [key_type:2 endpoint_algo:<find_master:<> > ]
                                       第三方App标识  =  否
                第三方App和华为App之间的通信策略信息  =  <nil>
                         第三方App之间的通信策略信息  =  <nil>
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0294730433)

| 输出项名称 | 输出项解释 |
| --- | --- |
| APP信息 | 该参数用于表示下发APPROUTE策略的APP信息，可通过<br>[**DSP SDRPOLICYKEYS**](显示SDRC中的策略Key信息（DSP SDRPOLICYKEYS）_22132897.md)<br>: POLICYTYPE=AppRoute;命令获取。 |
| APP将要发送的TOPIC ID | 该参数用于表示业务app将要发送的topic id。 |
| APP订阅的TOPIC | 该参数用于表示业务app通过哪种类型的key或者instance来路由topic消息。 |
| 路由算法 | 该参数用于表示APPROUTE策略的路由算法。 |
| 第三方App的标识 | 该参数用于表示是否是第三方App的路由策略。<br>取值说明：<br>- TRUE(TRUE)<br>- FALSE(FALSE) |
| 第三方App和华为App之间的通信策略信息 | 该参数用于表示第三方App和华为App之间的通信策略信息。 |
| 第三方App之间的通信策略信息 | 该参数用于表示第三方App之间的通信策略信息。 |
