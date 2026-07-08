# 查询S1模式信令抑制规则(LST S1SMARTRULE)

- [命令功能](#ZH-CN_MMLREF_0000001172345347__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345347__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345347__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345347__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345347__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345347__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172345347__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345347)

**适用网元：MME**

该命令用于查询基于用户终端类型的S1模式信令抑制规则。

#### [注意事项](#ZH-CN_MMLREF_0000001172345347)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345347)

manage-ug; system-ug; monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345347)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345347)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UETYPE | 终端类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的终端类型。<br>数据来源：本端规划<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>- “UNKNOWN_TYPE(未知类型)”<br>默认值：无<br>说明：“UNKNOWN_TYPE(未知类型)”：未获取到IMEI的终端类型或者没有匹配的<br>[**ADD IMEILIB**](../../终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md)<br>配置的终端类型。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345347)

查询 “终端类型” 为“ANDROID”的S1模式异常信令抑制规则：

LST S1SMARTRULE: UETYPE=ANDROID;

```
%%LST S1SMARTRULE: UETYPE=ANDROID;%%
RETCODE = 0  操作成功。

输出结果如下
------------
                  终端类型  =  Android
              附着抑制措施  =  NULL
              附着拒绝原因  =  NO_SUITABLE_CELLS_IN_TA_15
          服务请求抑制措施  =  NULL
          服务请求拒绝原因  =  NO_SUITABLE_CELLS_IN_TA_15
    控制面服务请求抑制措施  =  NULL
    控制面服务请求拒绝原因  =  NO_SUITABLE_CELLS_IN_TA_15
           PDN连接抑制措施  =  NULL
           PDN连接拒绝原因  =  MULTI_PDN_FOR_APN_NOT_ALLOWED_55
     Backoff Timer分配开关  =  开启
Back off timer最小值（秒）  =  660
Back off timer最大值（秒）  =  3000
              抑制分离原因  =  NO_SUITABLE_CELLS_IN_TA_15
       Parking APN唤醒措施  =  网络侧去激活
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172345347)

参见 [**ADD S1SMARTRULE**](增加S1模式信令抑制规则(ADD S1SMARTRULE)_26145746.md) 的参数说明。
