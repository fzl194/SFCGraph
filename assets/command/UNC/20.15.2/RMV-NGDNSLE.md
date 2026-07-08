---
id: UNC@20.15.2@MMLCommand@RMV NGDNSLE
type: MMLCommand
name: RMV NGDNSLE（删除DNS本端实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGDNSLE
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- DNS客户端管理
status: active
---

# RMV NGDNSLE（删除DNS本端实体）

## 功能

**适用NF：AMF**

该命令用于删除DNS本端实体。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNS本端实体的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定DNS本端实体的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定DNS本端实体的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGDNSLE]] · DNS本端实体（NGDNSLE）

## 使用实例

删除DNS本端实体：IPTYPE为IPV4，IP地址192.168.101.100：

```
RMV NGDNSLE:IPTYPE=IPV4,IPV4="192.168.101.100";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGDNSLE.md`
