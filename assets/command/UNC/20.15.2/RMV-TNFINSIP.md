---
id: UNC@20.15.2@MMLCommand@RMV TNFINSIP
type: MMLCommand
name: RMV TNFINSIP（删除目标NF实例IP地址）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TNFINSIP
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- NCG
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 目标NF实例IP地址管理
status: active
---

# RMV TNFINSIP（删除目标NF实例IP地址）

## 功能

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF**

该命令用于删除目标NF实例IP地址配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNFINSINDEX | 目标NF实例索引 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF实例索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~2047。<br>默认值：无<br>配置原则：<br>该参数取值与ADD TNFINS命令的TNFINSINDEX参数取值一致时，关联关系才能生效。 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPv4）”：IPv4<br>- “IPV6（IPv6）”：IPv6<br>- “NONEIP（无IP）”：无IP<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPV4类型地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：本参数用于指定IPV4类型地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>- 取值范围：1.0.0.0~255.255.255.254。<br>- Pv4地址不能为组播地址（224.x.y.z）和环回地址(127.x.y.z)。<br>- IPv4地址必须是A、B或者C类地址。 |
| IPV6ADDR | IPV6类型地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：本参数用于指定IPV6类型地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>- 取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）和IPv4映射地址（::FFFF:XXXX:XXXX），若为IPv4兼容地址时，需判断是否符合IPv4地址要求。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TNFINSIP]] · 目标NF实例IP地址（TNFINSIP）

## 使用实例

运营商A需要为索引1的目标NF实例删除如下地址信息，类型为IPV4，值为10.168.0.1。

```
RMV TNFINSIP: TNFINSINDEX=1, IPTYPE=IPV4, IPV4ADDR="10.168.0.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-TNFINSIP.md`
