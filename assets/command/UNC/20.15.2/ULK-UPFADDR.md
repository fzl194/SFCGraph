---
id: UNC@20.15.2@MMLCommand@ULK UPFADDR
type: MMLCommand
name: ULK UPFADDR（解锁UPF地址）
nf: UNC
version: 20.15.2
verb: ULK
object_keyword: UPFADDR
command_category: 动作类
applicable_nf:
- SGW-C
- GGSN
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP路径管理
- PFCP路径选择管理
status: active
---

# ULK UPFADDR（解锁UPF地址）

## 功能

**适用NF：SGW-C、GGSN、PGW-C、SMF**

该命令用于解锁UPF地址。解锁后新激活的用户可以选择该UPF地址建立PFCP会话。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPINSTANCEID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。不区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致。 |
| IPVERSION | UPF的IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | UPF的IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定UPF的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。IPv4只支持A，B，C类地址。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | UPF的IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定UPF的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。IPv6必须是全球单播地址；不能为“FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF”、环回地址(“::1”)、链路本地地址(“FE80::/10”)和组播地址(“FF00::/8”)。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [解锁UPF地址（UPFADDR）](configobject/UNC/20.15.2/UPFADDR.md)

## 使用实例

为实例名称为“UP1”的UPF解锁其“10.0.0.2”的IPV4地址。

```
ULK UPFADDR: UPINSTANCEID="UP1", IPVERSION=IPV4, IPV4ADDR="10.0.0.2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/解锁UPF地址（ULK-UPFADDR）_50361721.md`
