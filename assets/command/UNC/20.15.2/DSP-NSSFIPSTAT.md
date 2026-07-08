---
id: UNC@20.15.2@MMLCommand@DSP NSSFIPSTAT
type: MMLCommand
name: DSP NSSFIPSTAT（显示NSSF的局向内统概要数据）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NSSFIPSTAT
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF维测管理
status: active
---

# DSP NSSFIPSTAT（显示NSSF的局向内统概要数据）

## 功能

**适用NF：NSSF**

显示NSSF的局向内统概要数据。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPADDRESSTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF的客户端IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPTypeV4（IPV4类型）<br>- IPTypeV6（IPV6类型）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPV4地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定对端NF的客户端IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPV6地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定对端NF的客户端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NSSF的局向内统概要数据（NSSFIPSTAT）](configobject/UNC/20.15.2/NSSFIPSTAT.md)

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NSSF的局向内统概要数据（DSP-NSSFIPSTAT）_22836789.md`
