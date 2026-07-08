---
id: UNC@20.15.2@MMLCommand@RMV FILTERGPMEMBER
type: MMLCommand
name: RMV FILTERGPMEMBER（删除过滤器组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: FILTERGPMEMBER
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- 过滤器组成员管理
status: active
---

# RMV FILTERGPMEMBER（删除过滤器组成员）

## 功能

**适用NF：SMF**

当UP不需要使用指定过滤规则时，使用该命令删除一个过滤器。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILTERGPID | 过滤组ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定过滤器从属过滤组的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1023。该参数应该与LST FILETERGP命令查询结果中FILTERGPID的值保持一致。<br>默认值：无<br>配置原则：无 |
| DIRECTION | 方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定此过滤器的过滤方向。<br>数据来源：全网规划<br>取值范围：<br>- “DownLink（下行）”：从网络侧到用户侧的数据流方向<br>- “UpLink（上行）”：从用户侧到网络侧的数据流方向<br>- “Bidirectional（双向）”：用户侧与网络侧之间互相传输的数据流方向<br>默认值：无<br>配置原则：无 |
| FILTERTYPE | 过滤器类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定过滤器类型。<br>数据来源：全网规划<br>取值范围：<br>- Ipv4（IPv4）<br>- Ipv6（IPv6）<br>默认值：无<br>配置原则：无 |
| REMOTEIPV4 | 远端IPv4 | 可选必选说明：该参数在"FILTERTYPE"配置为"Ipv4"时为条件必选参数。<br>参数含义：该参数用于指定远端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>默认为全0地址，表示在匹配过滤器时，该字段视为任意地址均匹配。 |
| REMOTEIPV6 | 远端IPv6 | 可选必选说明：该参数在"FILTERTYPE"配置为"Ipv6"时为条件必选参数。<br>参数含义：该参数用于指定远端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>默认为全0地址，表示在匹配过滤器时，该字段视为任意地址均匹配。 |
| UEIPV4 | UE IPv4 | 可选必选说明：该参数在"FILTERTYPE"配置为"Ipv4"时为条件必选参数。<br>参数含义：该参数用于指定UE的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>默认为全0地址，表示在匹配过滤器时，该字段视为任意地址均匹配。 |
| UEIPV6 | UE IPv6 | 可选必选说明：该参数在"FILTERTYPE"配置为"Ipv6"时为条件必选参数。<br>参数含义：该参数用于指定UE的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>默认为全0地址，表示在匹配过滤器时，该字段视为任意地址均匹配。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FILTERGPMEMBER]] · 过滤器组成员（FILTERGPMEMBER）

## 使用实例

删除某个过滤器，过滤器参数如下：过滤组的ID是1，方向是下行，远端的IPv4地址是10.151.73.175，UE的IPv4地址是10.152.73.175；

```
RMV FILTERGPMEMBER: FILTERGPID=1, DIRECTION=DownLink, FILTERTYPE=Ipv4, REMOTEIPV4="10.151.73.175", UEIPV4="10.152.73.175";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-FILTERGPMEMBER.md`
