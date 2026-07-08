# 查询间接路由功能（LST SCPFUNCSW）

- [命令功能](#ZH-CN_MMLREF_0000001102630398__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001102630398__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001102630398__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001102630398__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001102630398__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001102630398)

**适用NF：AMF、SMF、SMSF、NCG**

该命令用于显示间接路由功能和服务发现代理开关配置信息。

## [注意事项](#ZH-CN_MMLREF_0000001102630398)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001102630398)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001102630398)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNFTYPE | 本端NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端NF的类型。<br>数据来源：全网规划<br>取值范围：<br>- “AMF（AMF）”：NF类型为AMF<br>- “SMF（SMF）”：NF类型为SMF<br>- “SMSF（SMSF）”：NF类型为SMSF<br>- “CHF（CHF）”：NF类型为CHF<br>- “NWDAF（NWDAF）”：NF类型为NWDAF<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001102630398)

运营商A需要查询间接路由功能配置。

```
%%LST SCPFUNCSW:;%%
RETCODE = 0  操作成功

结果如下
------------------------
本端NF类型  对端NF类型  间接路由功能开关  服务发现代理开关  区域位置开关  拨测开关

AMF         UDM         OFF               OFF               OFF           OFF
AMF         AUSF        OFF               OFF               OFF           OFF
AMF         PCF         OFF               OFF               OFF           OFF
AMF         AMF         OFF               OFF               OFF           OFF
AMF         SMF         OFF               OFF               OFF           OFF
AMF         SMSF        OFF               OFF               OFF           OFF
AMF         5G-EIR      OFF               OFF               OFF           OFF
SMF         UDM         OFF               OFF               OFF           OFF
SMF         PCF         OFF               OFF               OFF           OFF
SMF         CHF         OFF               OFF               OFF           OFF
SMF         AMF         OFF               OFF               OFF           OFF
SMF         SMF         OFF               OFF               OFF           OFF
SMSF        UDM         OFF               OFF               OFF           OFF
SMSF        AMF         OFF               OFF               OFF           OFF
CHF         CUSTOM_OCS  OFF               OFF               OFF           OFF
(结果个数 = 15)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001102630398)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 本端NF类型 | 该参数用于指定本端NF的类型。 |
| 对端NF类型 | 该参数用于指定对端NF的类型。 |
| 间接路由功能开关 | 该参数用于设置间接路由功能，如果设置为ON，则指定的本端和对端类型的NF之间通过SCP转发。 |
| 服务发现代理开关 | 该参数用于设置是否使用SCP代理NF的服务发现功能，如果设置为ON，则指定的本端和对端类型之间的NF服务发现功能通过SCP间接实现。注意，不是通过直接和SCP进行服务发现交互，而是在业务消息交互的过程中，SCP解码业务消息获得用户号码等信息进行消息路由或抽取业务消息里携带的服务发现头到NRF进行服务发现。 |
| 区域位置开关 | 该参数用于指定Model C间接路由模式下，是否对请求方NF和目标NF进行同区域判断以便进行对应的直接/间接路由策略。当开关设置为“ON”时，系统对请求方NF和目标NF进行区域判断，当两者属于同一区域时，NF间使用直连路由的方式；当两者属于不同区域时，NF间使用Model C间接路由方式。当开关设置为“OFF”时，系统不对请求方NF和目标NF进行区域判断，直接使用Model C间接路由。请求方NF和目标NF进行同区域判断时，NF所在的区域信息在SET NFREGIONINFO中配置。<br>该参数在"SCPROUTESW"设置为"ON"，"SCPDISCSW"设置为"OFF"的Model C场景下才有效。 |
| 拨测开关 | 该参数用于指定是否开启Model-D或Model-C模式的业务拨测阶段。<br>拨测只支持基于SUPI号段、GPSI号段、ROUTINGIND及PLMN控制。<br>Model-D拨测支持的对端NF类型只包括：UDM、PCF、AUSF。<br>Model-C拨测目前支持的本端NF类型只包括：AMF、SMF。<br>当该参数取值为ON时，只针对通过ADD PNFSUPI、ADD PNFGPSI、ADD PNFROUTEIND及ADD PNFPLMN命令配置的用户生效Model-D或Model-C模式，并且NFINSTANCEID配置为"sbidialtest"。<br>直连不支持拨测。 |
