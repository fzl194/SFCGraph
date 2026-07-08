# 显示NSSF的局向内统概要数据（DSP NSSFIPSTAT）

- [命令功能](#ZH-CN_MMLREF_0000001222836789__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001222836789__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001222836789__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001222836789__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001222836789__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001222836789)

**适用NF：NSSF**

显示NSSF的局向内统概要数据。

## [注意事项](#ZH-CN_MMLREF_0000001222836789)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001222836789)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001222836789)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPADDRESSTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF的客户端IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPTypeV4（IPV4类型）<br>- IPTypeV6（IPV6类型）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPV4地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定对端NF的客户端IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPV6地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定对端NF的客户端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001222836789)

运营商想要查询NSSF的局向内统概要数据，执行此命令。

```
DSP NSSFIPSTAT:;
%%DSP NSSFIPSTAT:;%%
RETCODE = 0  操作成功

结果如下
--------
         Pod名称  =  uncpod-0
          局向IP  =  10.10.10.10
      NF实例标识  =  123e4567-e89b-12d3-a456-426655440000
发送消息统计信息  =  [NsSelectRspMsg: 1][NsAvailInfoUpdateRspMsg: 0][NsAvailInfoDeleteRspMsg: 0][NsAvailInfoPatchRspMsg: 0][NsAvailInfoSubscriptionRspMsg: 0][NsAvailInfoNotifyMsg: 0][NsAvailInfoUnsubscribeRspMsg: 0][NsAvailInfoOptionsRspMsg: 0][sendMsgTotal: 1]
接收消息统计信息  =  [nsSelectMsg: 1][nsAvailInfoUpdateMsg: 0][nsAvailInfoDeleteMsg: 0][nsAvailInfoPatchMsg: 0][nsAvailInfoSubscriptionMsg: 0][nsAvailInfoNotifyRspMsg: 0][nsAvailInfoUnsubscribeMsg: 0][nsAvailInfoOptionsMsg: 0][receiveMsgTotal: 1]
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001222836789)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Pod名称 | 该参数表示NSSF Pod名称。 |
| 局向IP | 该参数表示与NSSF交互的对端NF的IP。 |
| NF实例标识 | 该参数表示局向IP对应NF的实例标识。 |
| 发送消息统计信息 | 该参数用于表示NSSF向局向IP对应NF发送消息的统计信息。 |
| 接收消息统计信息 | 该参数用于表示NSSF从局向IP对应NF接收消息的统计信息。 |
