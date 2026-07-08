# 显示5G定位上下文信息（DSP NGLCSCTX）

- [命令功能](#ZH-CN_MMLREF_0000001933696293__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001933696293__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001933696293__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001933696293__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001933696293__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001933696293)

**适用NF：AMF**

该命令用于查询5G定位上下文的相关信息。

## [注意事项](#ZH-CN_MMLREF_0000001933696293)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001933696293)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001933696293)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G用户的IMSI信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001933696293)

查询IMSI为123451234567890用户的定位上下文信息，执行如下命令：

```
%%DSP NGLCSCTX:IMSI="123451234567890";%%
RETCODE = 0  操作成功

结果如下
--------
                     IMSI  =  123451234567890
              CallBackURI  =  http://192.168.118.1:5080/ngmlc-loc/v1/location-update
              LMF的实例号  =  NULL
	    CorrelationId  =  NULL
                   Lmf Id  =  NULL
Location Notification Uri  =  http://192.168.118.1:5080/ngmlc-loc/hgmlc/v1/provide-location
             Lcs Location  =  DeferredLocation
          Lcs Client Type  =  ValueAddedServices
            Ldr Reference  =  11
                  Lcs QoS  =  HAccuracy:1;VAccuracy:1;VerticalRequested:false;ResponseTime:Invalid
 Lcs Supported GAD Shapes  =  Invalid
      Periodic Event Info  =  ReportingAmount:1;ReportingInterval:1
                 Priority  =  Invalid
       Velocity Requested  =  Invalid
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001933696293)

| 输出项名称 | 输出项解释 |
| --- | --- |
| IMSI | 该参数用于指定5G用户的IMSI信息。 |
| CallBackURI | 该参数用于表示GMLC的CallBackURI。 |
| LMF的实例号 | 该参数用于表示LMF的实例号。 |
| CorrelationId | 该参数用于表示AMF分配给LMF的CorrelationId。 |
| Lmf Id | 该参数用于表示GMLC携带的lmfId。 |
| Location Notification Uri | 该参数用于表示GMLC的locationNotificationUri。 |
| Lcs Location | 该参数用于表示GMLC携带的lcsLocation。 |
| Lcs Client Type | 该参数用于表示GMLC携带的lcsClientType。 |
| Ldr Reference | 该参数用于表示GMLC携带的ldrReference。 |
| Lcs QoS | 该参数用于表示GMLC携带的lcsQoS。 |
| Lcs Supported GAD Shapes | 该参数用于表示GMLC携带的lcsSupportedGADShapes。 |
| Periodic Event Info | 该参数用于表示GMLC携带的periodicEventInfo。 |
| Priority | 该参数用于表示GMLC携带的priority。 |
| Velocity Requested | 该参数用于表示GMLC携带的velocityRequested。 |
