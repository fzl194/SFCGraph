---
id: UNC@20.15.2@MMLCommand@CLR NGDNSCACHE
type: MMLCommand
name: CLR NGDNSCACHE（清除DNS缓存）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: NGDNSCACHE
command_category: 动作类
applicable_nf:
- AMF
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- DNS客户端缓存管理
status: active
---

# CLR NGDNSCACHE（清除DNS缓存）

## 功能

![](清除DNS缓存（CLR NGDNSCACHE）_55845121.assets/notice_3.0-zh-cn_2.png)

清除DNS缓存会导致系统的CPU负荷增大，系统向DNS服务的查询次数可能会增加。

**适用NF：AMF、SGW-C**

该命令用于清除DNS缓存。

## 注意事项

- 当“清除速率”参数设置为0时，本命令执行后立即生效，否则，本命令执行后延时生效。

- 当“清除速率”参数设置为非0值时，本命令执行延时生效，参数值设置越大，本命令执行延时越小。请使用DSP NGDNSCACHE命令确认缓存清除状态。
- 若期望向DNS服务器发起查询，则需要使用本命令清除DNS客户端缓存，同时使用CLR DNSC命令清除缓存。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是3~100。<br>默认值：无<br>配置原则：<br>服务实例所在Pod名称，该参数仅在“Pod查询类型”取值为“Pod名称”时有效。 |
| PROCESSID | 进程ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示微服务进程ID，查询进程ID为PROCESSID的进程信息。命令按进程类型名查询会返回该类型的所有进程ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~100。<br>默认值：无<br>配置原则：无 |
| QUERYTYPE | DNS查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNS的查询类型。<br>数据来源：本端规划<br>取值范围：取值为“AAAA/A类型查询”时为预留功能，当前版本不支持。<br>- QUERY_TYPE_A（AAAA/A类型查询）<br>- QUERY_TYPE_NAPTR（NAPTR类型查询）<br>默认值：无<br>配置原则：无 |
| CLEARMANNER | 清除方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定缓存清除的方式。<br>数据来源：本端规划<br>取值范围：<br>- “All（所有缓存）”：所有缓存记录<br>- “BYDOMAINNAME（指定域名）”：指定域名的记录<br>- “SUBSTRMATCH（子串匹配）”：域名包含指定子串的所有记录<br>默认值：无<br>配置原则：<br>该参数设置为“所有缓存”或“子串匹配”时，系统CPU负荷可能会增大。 |
| DOMAINNAME | 域名 | 可选必选说明：该参数在"CLEARMANNER"配置为"BYDOMAINNAME"、"SUBSTRMATCH"时为条件必选参数。<br>参数含义：该参数用于指定待查询的域名或域名子串。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>当“清除方式”参数设置为“指定域名”时，该参数应设置为完整域名；当“清除方式”参数设置为“子串匹配”时，该参数可设置为完整域名或域名的子字符串。 |
| CLEARRATE | 清除速率(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定每秒清除的最大域名数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~10000。<br>默认值：无<br>配置原则：<br>该参数设置为0时表示不限制速率，立即清除；设置为非0时，表示每秒可以清除的最大域名数量，请使用DSP NGDNSCACHE命令确认缓存的清除状态。该参数设置越大，系统的CPU负荷越高，短时间内向DNS服务器发起的查询次数越多。 |

## 操作的配置对象

- [DNS缓存（NGDNSCACHE）](configobject/UNC/20.15.2/NGDNSCACHE.md)

## 使用实例

使用以下命令清除所有DNS客户端缓存：

```
CLR NGDNSCACHE: QUERYTYPE=QUERY_TYPE_NAPTR, CLEARMANNER=All;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除DNS缓存（CLR-NGDNSCACHE）_55845121.md`
