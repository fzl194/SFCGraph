---
id: UDG@20.15.2@MMLCommand@DSP RELAYALMDETAIL
type: MMLCommand
name: DSP RELAYALMDETAIL（显示媒体中继告警详情）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RELAYALMDETAIL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继告警详情
status: active
---

# DSP RELAYALMDETAIL（显示媒体中继告警详情）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示媒体中继告警详情。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ALARMTYPE | 告警类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定告警类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RELAY_RESOURCE_ALARM：资源过载告警。<br>- RELAY_SERVICE_FAULT：业务故障告警。<br>- RELAY_DNS_SERVER_NO_RESPONSE：dns服务器无响应告警。<br>- RELAY_CPU_OVERLOAD：CPU过载告警。<br>默认值：无<br>配置原则：无 |
| RESOURCETYPE | 资源类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ALARMTYPE”配置为“RELAY_RESOURCE_ALARM”时为可选参数。<br>参数含义：该参数用于指定资源类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL：ALL。<br>- FLOW_TABLE：流表资源。<br>- HTTP_REQUEST：HTTP请求资源。<br>- PBUFFER：PBuffer 资源。<br>- TCP_SOCKET：TCP Socket资源。<br>- DNS_DOMAIN_NODE：DNS Domain节点资源。<br>- DNS_DOMAIN_HASHNODE：DNS Domain哈希节点资源。<br>- IPV4_ADDRESS_POOL：IPv4地址池资源。<br>- IPV6_ADDRESS_POOL：IPv6地址池资源。<br>- TLS_CONNECTION：TLS连接资源。<br>默认值：无<br>配置原则：无 |
| RELAYDOMAINNAME | 媒体中继域名配置名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ALARMTYPE”配置为“RELAY_SERVICE_FAULT”时为可选参数。<br>参数含义：该参数用于设置媒体中继域名配置名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SERVICETYPE | 业务类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ALARMTYPE”配置为“RELAY_SERVICE_FAULT”时为可选参数。<br>参数含义：该参数用于指定业务类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL：ALL。<br>- RELAY_URL_AUTH_ALARM：URL鉴权失败告警。<br>- RELAY_REFER_CHECK_ALARM：Referer校验失败告警。<br>- RELAY_PULL_ALARM：媒体中继回源失败告警。<br>- RELAY_UNKNOWN_MEDIA_TYPE：未知类型的媒体访问告警。<br>- USER_RELAY_REQUEST_FAILURE：用户媒体中继请求失败告警。<br>默认值：无<br>配置原则：无 |
| DNSSERVERNAME | DNS服务名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ALARMTYPE”配置为“RELAY_DNS_SERVER_NO_RESPONSE”时为可选参数。<br>参数含义：该参数用来指定DNS服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RELAYALMDETAIL]] · 媒体中继告警详情（RELAYALMDETAIL）

## 使用实例

假如需要显示一组媒体中继告警详情，则命令如下：

```
%%DSP RELAYALMDETAIL: ALARMTYPE=RELAY_CPU_OVERLOAD;
```

```
%%
RETCODE = 0  操作成功
 
结果如下
------------------------
Pod名称     进程ID  告警类型          子告警类型  媒体中继域名配置名称  媒体中继模板名称  DNS服务名称  告警详情  
 
relay-pod-0  2           CPU Overload Alarm  NULL            NULL                                        NULL                       NULL             NULL          
relay-pod-0  0           CPU Overload Alarm  NULL            NULL                                        NULL                       NULL             NULL          
relay-pod-0  6           CPU Overload Alarm  NULL            NULL                                        NULL                       NULL             NULL          
relay-pod-0  4           CPU Overload Alarm  NULL            NULL                                        NULL                       NULL             NULL          
relay-pod-0  3           CPU Overload Alarm  NULL            NULL                                        NULL                       NULL             NULL          
relay-pod-0  7           CPU Overload Alarm  NULL            NULL                                        NULL                       NULL             NULL          
(结果个数 = 6)
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-RELAYALMDETAIL.md`
