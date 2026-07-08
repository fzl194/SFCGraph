---
id: UNC@20.15.2@MMLCommand@RMV BLKGWLST
type: MMLCommand
name: RMV BLKGWLST（删除被禁用网关配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BLKGWLST
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- S-GW_P-GW_GGSN被禁用
status: active
---

# RMV BLKGWLST（删除被禁用网关配置）

## 功能

SGSN，MME
该命令用以从被禁用网关列表删除指定的网关。

## 注意事项

- 该命令执行后只对新接入用户生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GWTYPE | 网关类型 | 可选必选说明：必选参数<br>参数含义：该参数表示被禁用网关的逻辑形态。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- “GGSN（GGSN）”<br>- “S-GW（S-GW）”<br>- “P-GW（P-GW）”<br>默认值：无。<br>配置原则：无。 |
| GWIPTYPE | 网关IP类型 | 可选必选说明：必选参数<br>参数含义：该参数表示被禁用网关的业务地址类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- “IPv4（IPv4）”<br>- “IPv6（IPv6）”<br>默认值：无<br>配置原则：无。 |
| GWIPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数表示被禁用网关的IPv4地址。<br>前提条件：该参数在<br>“网关IP类型”<br>参数配置为<br>“IPv4（IPv4）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.1~255.255.255.254<br>默认值：无<br>配置原则：<br>- 有效的IPv4地址不能为环回地址(127.x.y.z)。<br>- 有效的IPv4地址必须是A、B或者C类地址。 |
| GWIPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数表示被禁用网关的IPv6地址。<br>前提条件：该参数在<br>“网关IP类型”<br>参数配置为<br>“IPv6（IPv6）”<br>后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）、IPv4映射地址及IPv4兼容地址。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BLKGWLST]] · 被禁用网关配置（BLKGWLST）

## 使用实例

从被禁用网关列表中删除网关类型为S-GW ，IP为192.168.1.1的记录。

```
RMV BLKGWLST: GWTYPE=S-GW, GWIPTYPE=IPv4, GWIPV4="192.168.1.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-BLKGWLST.md`
