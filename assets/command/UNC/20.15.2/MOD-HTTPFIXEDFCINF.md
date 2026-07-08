---
id: UNC@20.15.2@MMLCommand@MOD HTTPFIXEDFCINF
type: MMLCommand
name: MOD HTTPFIXEDFCINF（修改HTTP接口类型固定速率流控信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: HTTPFIXEDFCINF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP接口类型固定速率流控管理
status: active
---

# MOD HTTPFIXEDFCINF（修改HTTP接口类型固定速率流控信息）

## 功能

该命令用于修改HTTP接口类型固定速率流控门限值信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCIDX | 局向索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定局向索引。该参数来源于<br>[**ADD HTTPOFC**](../../HTTP管理/HTTP局向管理/增加HTTP局向（ADD HTTPOFC）_35230482.md)<br>命令的“局向索引”参数，可通过<br>[**LST HTTPOFC**](../../HTTP管理/HTTP局向管理/查询HTTP局向（LST HTTPOFC）_86150085.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：<br>此处只能绑定"NFITEM"包含"FIXSPDFCINTF（基于接口类型固定速率流控）"的局向。 |
| LETYPE | 本端实体类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP本端实体的类型。<br>数据来源：全网规划<br>取值范围：<br>- “SERVER（服务端）”：服务端<br>- “CLIENT（客户端）”：客户端<br>默认值：无<br>配置原则：<br>HTTP本端实体可以作为服务端也可以作为客户端，两者需要分别配置。 |
| SENDTHD | 发送消息流控门限(条/秒) | 可选必选说明：该参数在"LETYPE"配置为"CLIENT"时为条件必选参数。<br>参数含义：该参数用于指定发送消息流控门限。该门限按整机粒度设置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~4294967295。<br>默认值：无<br>配置原则：<br>门限值由对端网元的消息处理能力决定。设置过低会导致消息被丢弃，设置过高起不到保护对端网元不过载的作用。 |
| RECVTHD | 接收消息流控门限(条/秒) | 可选必选说明：该参数在"LETYPE"配置为"SERVER"时为条件必选参数。<br>参数含义：该参数用于指定接收消息流控门限。该门限按整机粒度设置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~4294967295。<br>默认值：无<br>配置原则：<br>门限值由本端网元的消息处理能力决定。设置过低会导致消息被丢弃，设置过高起不到保护本端网元不过载的作用。 |
| STATUSCODE | 状态码 | 可选必选说明：该参数在"LETYPE"配置为"SERVER"时为条件可选参数。<br>参数含义：该参数用于指定接收消息速率超过流控门限时，给对端网元响应的HTTP消息中的Status Code。该参数可以和“是否携带Retry-After消息头”参数配合使用，告知对端本端的过载情况的同时携带Retry-After来指示对端多久后再发送请求。<br>数据来源：全网规划<br>取值范围：<br>- “TooManyRequests（Too Many Requests）”：当NF服务生产者检测到给定NF服务消费者发送过多的流量时，可以发送该状态代码告知NF服务消费者生产者端即将过载。<br>- “ServiceUnavailable（Service Unavailable）”：当NF服务生产者检测到给定NF服务消费者发送过多的流量时，可以发送该状态代码告知NF服务消费者生产者端已经过载。<br>默认值：无<br>配置原则：无 |
| RETRYAFTERFLAG | 是否携带Retry-After消息头 | 可选必选说明：该参数在"LETYPE"配置为"SERVER"时为条件可选参数。<br>参数含义：该参数用于指定接收消息速率超过流控门限时，给对端网元响应的HTTP消息中是否携带Retry-After消息头。该参数可以和“状态码”参数配合使用，告知对端本端的过载情况的同时携带Retry-After来指示对端多久后再发送请求。<br>数据来源：全网规划<br>取值范围：<br>- “YES（YES）”：携带Retry-After消息头<br>- “NO（NO）”：不携带Retry-After消息头<br>默认值：无<br>配置原则：<br>携带Retry-After消息头可能会使对端网元不发请求消息给本端网元，导致业务受损。需谨慎使用该参数。如需设置Retry-After消息头，请联系华为技术支持。 |
| TIMER | Retry-After时长(秒) | 可选必选说明：该参数在"RETRYAFTERFLAG"配置为"YES"时为条件可选参数。<br>参数含义：该参数用于指定Retry-After的时长。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~3600。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPFIXEDFCINF]] · HTTP接口类型固定速率流控信息（HTTPFIXEDFCINF）

## 使用实例

- 修改局向索引为1，本端实体类型为客户端的HTTP接口类型固定速率流控门限值，将发送消息流控门限从1000改为100：
  ```
  MOD HTTPFIXEDFCINF: OFCIDX=1, LETYPE=CLIENT, SENDTHD=100;
  ```
- 修改局向索引为2，本端实体类型为服务端的HTTP接口类型固定速率流控门限值，将接收消息流控门限从1000改为100，状态码修改为ServiceUnavailable，是否携带Retry-After消息头修改为YES，Retry-After时长修改为100：
  ```
  MOD HTTPFIXEDFCINF: OFCIDX=2, LETYPE=SERVER, RECVTHD=100, STATUSCODE=ServiceUnavailable, RETRYAFTERFLAG=YES, TIMER=100;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-HTTPFIXEDFCINF.md`
