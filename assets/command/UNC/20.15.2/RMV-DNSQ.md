---
id: UNC@20.15.2@MMLCommand@RMV DNSQ
type: MMLCommand
name: RMV DNSQ（删除DNS查询控制参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DNSQ
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- DNS
- DNS查询管理
status: active
---

# RMV DNSQ（删除DNS查询控制参数）

## 功能

**适用网元：SGSN、MME**

该命令用于删除DNS查询控制参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后，相应的DNS查询控制参数将失效。
- 该命令执行后，需要执行[**CLR DNSC**](../../../系统管理/DNS维护管理/清除DNS Cache/清除DNS缓存(CLR DNSC)_72345945.md)来清除L1，L2 缓存，以保证使用最新的配置进行查询。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于表示签约用户的范围。<br>数据来源：整网规划<br>取值范围：<br>- “All（所有用户）”<br>- “SPECIFY（指定用户）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示IMSI前缀。<br>前提条件：当<br>“用户范围”<br>为<br>“SPECIFY（指定用户）”<br>时，此参数为必选参数。<br>数据来源：整网规划<br>取值范围：5~15位数字<br>默认值：无<br>说明：IMSI前缀按照IMSI最长匹配进行查询，相同IMSI前缀的DNS域名后缀不能相同。 |
| DNSUF | 域名后缀 | 可选必选说明：必选参数<br>参数含义：该参数用于表示DNS服务器域名后缀。<br>数据来源：整网规划<br>取值范围：1~255<br>默认值：无<br>说明：- 按照域名后缀选择合适的DNS服务器。域名后缀在比较时从后向前进行最大匹配。<br>- 域名后缀支持配置为*。任何域名和*比较，都认为匹配。<br>- 域名后缀不能以“.”开始，也不能以“.”结束。<br>- 相同域名后缀下的IMSI前缀不能相同，相同IMSI前缀下的域名后缀不能相同。<br>- 该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）、通配符（*）和点（.）组成。<br>- 按照协议RFC1035规定，Hostname最大有效字符数为253，并且每个Label最大长度为63个字节。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DNSQ]] · DNS查询控制参数（DNSQ）

## 使用实例

删除 “用户范围” 为 “所有用户” ， “域名后缀” 为 “huawei.com” 的DNS查询管理参数：

RMV DNSQ: SUBRANGE=All, DNSUF="huawei.com";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DNSQ.md`
