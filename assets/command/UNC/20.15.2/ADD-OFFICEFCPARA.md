---
id: UNC@20.15.2@MMLCommand@ADD OFFICEFCPARA
type: MMLCommand
name: ADD OFFICEFCPARA（增加指定NF的流控参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: OFFICEFCPARA
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF局向流控参数
status: active
---

# ADD OFFICEFCPARA（增加指定NF的流控参数）

## 功能

![](增加指定NF的流控参数（ADD OFFICEFCPARA）_86184258.assets/notice_3.0-zh-cn_2.png)

执行该命令后，指定IP对应的所有NF（可能是多个）的请求都受该命令对应的流控限制，请谨慎操作。

**适用NF：NRF**

该命令用于添加NRF基于局向IP的单进程流控参数配置。

当NRF需要针对某个特定NF进行流控时，可执行此命令。

## 注意事项

- 该命令执行后立即生效。

- 该命令只针对进程粒度流控参数的配置，而非整系统粒度。
- 指定的IP可能对应多个NF时，多个NF都受该配置影响，需要谨慎操作。

- 最多可输入2048条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPADDRESSTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF的客户端IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPTypeV4（IPTypeV4）<br>- IPTypeV6（IPTypeV6）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPV4地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定对端NF的客户端IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。取值范围：1.0.0.0~255.255.255.254。IPv4地址不能为组播地址（224.x.y.z）和环回地址(127.x.y.z)。IPv4地址必须是A、B或者C类地址。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPV6地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定对端NF的客户端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）和IPv4映射地址（::FFFF:XXXX:XXXX），若为IPv4兼容地址时，需判断是否符合IPv4地址要求。<br>默认值：无<br>配置原则：无 |
| FCPERIOD | 流控周期(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于配置流控周期，在此流控周期内进行对应的速率流控。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~120，单位是秒。<br>默认值：1<br>配置原则：无 |
| DISCRATE | 服务发现请求(个) | 可选必选说明：可选参数<br>参数含义：该参数用于表示在流控周期内，允许接入的NF服务发现请求个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535，单位是个。<br>默认值：65535<br>配置原则：<br>该值取值65535表示不流控。 |
| RETRIEVALRATE | 检索请求(个) | 可选必选说明：可选参数<br>参数含义：该参数用于表示在流控周期内，允许接入的NF检索请求个数，检索包括NF列表检索和NF Profile检索。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535，单位是个。<br>默认值：65535<br>配置原则：<br>该值取值65535表示不流控。 |
| REGISTERRATE | 注册请求(个) | 可选必选说明：可选参数<br>参数含义：该参数用于表示在流控周期内，允许接入的NF注册请求个数，注册包括NF注册、全量更新和去注册。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535，单位是个。<br>默认值：65535<br>配置原则：<br>该值取值65535表示不流控。 |
| UPDATERATE | 更新请求(个) | 可选必选说明：可选参数<br>参数含义：该参数用于表示在流控周期内，允许接入的NF部分更新请求个数，不包含心跳。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535，单位是个。<br>默认值：65535<br>配置原则：<br>该值取值65535表示不流控。 |
| HEARTBEATRATE | 心跳请求(个) | 可选必选说明：可选参数<br>参数含义：该参数用于表示在流控周期内，允许接入的NF心跳请求个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535，单位是个。<br>默认值：65535<br>配置原则：<br>该值取值65535表示不流控。 |
| SUBSCRIPRATE | 订阅请求(个) | 可选必选说明：可选参数<br>参数含义：该参数用于表示在流控周期内，允许接入的NF订阅请求个数，订阅请求包括订阅、订阅更新和去订阅。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535，单位是个。<br>默认值：65535<br>配置原则：<br>该值取值65535表示不流控。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OFFICEFCPARA]] · 指定NF的流控参数（OFFICEFCPARA）

## 使用实例

手动添加一组局向流控参数，IP类型为IPTypeV4，IPv4地址为“10.2.3.4”，其他参数为默认值，执行如下命令：

```
ADD OFFICEFCPARA: IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS="10.2.3.4", CONFIRM=Y;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-OFFICEFCPARA.md`
