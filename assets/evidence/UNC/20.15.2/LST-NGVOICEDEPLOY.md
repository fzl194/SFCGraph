# 查询5G语音部署配置（LST NGVOICEDEPLOY）

- [命令功能](#ZH-CN_MMLREF_0000001186180366__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001186180366__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001186180366__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001186180366__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001186180366__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001186180366)

**适用NF：AMF**

该命令用于查询UE使用5G网络接入时的IMS VoPS语音部署策略。

## [注意事项](#ZH-CN_MMLREF_0000001186180366)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001186180366)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001186180366)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定应用语音策略用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001186180366)

查询本网用户语音部署配置，执行如下命令：

```
%%LST NGVOICEDEPLOY: SUBRANGE=HOME_USER;%%
RETCODE = 0  操作成功

结果如下
------------------------
                    用户范围  =  本网用户
                    IMSI前缀  =  NULL
          AMF是否支持IMS语音  =  不支持
Data Centric类型终端支持VoPS  =  不支持
      是否检查用户S1Mode能力  =  关闭
                 语音业务DNN  =  1.1
检查语音DNN是否支持EPS互操作  =  关闭
(Number of results = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001186180366)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 用户范围 | 该参数用于指定用户范围。 |
| IMSI前缀 | 该参数用于指定应用语音策略用户的IMSI前缀。 |
| AMF是否支持IMS语音 | 该参数用于指定AMF侧的所有跟踪区是否都支持PS域IMS语音能力。 |
| Data Centric类型终端支持VoPS | 该参数用于指定Data Centric类型终端是否都支持IMS语音能力。 |
| 是否检查用户S1Mode能力 | 该参数用于指定是否检查用户的S1Mode能力，开启后只有支持S1Mode的UE才允许使用IMS VoPS业务。该能力来源于UE在Registration request消息中携带的5GMM capability信元。 |
| 语音业务DNN | 该参数用于指定语音业务DNN。 |
| 检查语音DNN是否支持EPS互操作 | 该参数用于指定系统是否检查语音DNN支持EPS互操作能力，开启后只有语音DNN支持EPS互操作才允许UE使用IMS语音能力。 |
