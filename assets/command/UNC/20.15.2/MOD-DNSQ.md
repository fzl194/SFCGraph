---
id: UNC@20.15.2@MMLCommand@MOD DNSQ
type: MMLCommand
name: MOD DNSQ（修改DNS查询控制参数）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD DNSQ（修改DNS查询控制参数）

## 功能

**适用网元：SGSN、MME**

该命令用于修改DNS查询控制参数，包括查询方式，以及DNS服务器组ID等。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后，需要执行[**CLR DNSC**](../../../系统管理/DNS维护管理/清除DNS Cache/清除DNS缓存(CLR DNSC)_72345945.md)来清除L1，L2 缓存，以保证本地缓存和DNS服务器中数据的一致性。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于表示签约用户的范围。<br>数据来源：整网规划<br>取值范围：<br>- “All（所有用户）”<br>- “SPECIFY（指定用户）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示IMSI前缀。<br>前提条件：当<br>“用户范围”<br>为<br>“SPECIFY（指定用户）”<br>时，此参数为必选参数。<br>数据来源：整网规划<br>取值范围：5~15位数字<br>默认值：无 |
| DNSUF | 域名后缀 | 可选必选说明：必选参数<br>参数含义：该参数用于表示域名后缀。<br>数据来源：整网规划<br>取值范围：1~255个字符<br>默认值：无<br>说明：- 按照域名后缀选择合适的DNS服务器。域名后缀在比较时从后向前进行最大匹配。<br>- 域名后缀支持配置为*。任何域名和*比较，都认为匹配。<br>- 域名后缀不能以“.”开始，也不能以“.”结束。<br>- 相同域名后缀下的IMSI前缀不能相同，相同IMSI前缀下的域名后缀不能相同。<br>- 该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）、通配符（*）和点（.）组成。<br>- 按照协议RFC1035规定，Hostname最大有效字符数为253，并且每个Label最大长度为63个字节。 |
| ANALYSETYPE | DNS解析方式 | 可选必选说明：可选参数<br>参数含义：该参数用于表示DNS解析方式，即控制DNS查询时优先使用server数据或者优先使用本地配置数据。<br>数据来源：整网规划<br>取值范围：<br>- “E_HOSTFILE_SERVER（本地数据优先）”：本地配置数据优先。<br>- “E_SERVER_HOSTFILE（服务器数据优先）”：服务器数据优先。<br>默认值：无 |
| DNSQUERYMODE | DNS查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于表示DNS查询方式，控制DNS查询时使用A记录还是NAPTR记录查询方法。<br>数据来源：整网规划<br>取值范围：<br>- “AAAA/A(AAAA/A)”：域名到IP的映射。<br>- “NAPTR(NAPTR)”：FQDN（标准规范域名）到域名的映射。<br>默认值：无<br>配置原则：建议值为<br>“NAPTR”<br>。 |
| GROUPID | DNS服务器组ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示DNS服务器组ID。<br>前提条件：该参数必须已经通过<br>[**ADD DNSS**](../DNS服务器管理/增加DNS服务器(ADD DNSS)_72345497.md)<br>配置，但是当输入的服务器组ID为0时，不受此约束，即使ID为0的服务器组未通过<br>[**ADD DNSS**](../DNS服务器管理/增加DNS服务器(ADD DNSS)_72345497.md)<br>配置，此处也可以引用0作为输入参数。但是如果ID为0的服务器组未配置，会导致向该服务器组发起的DNS查询失败。<br>数据来源：整网规划<br>取值范围：0~37<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述该命令的文字说明，目的是在配置的时候可以将对象属性、配置原因、背景等进行描述，以便在查询时能够在大量配置数据中清晰的掌握配置的原因。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DNSQ]] · DNS查询控制参数（DNSQ）

## 使用实例

修改 “用户范围” 为 “所有用户” 且 “域名后缀” 为 “gprs” 的DNS控制参数， “查询模式” 设为 “NAPTR” ， “描述” 设为 “For huawei rule01” ：

MOD DNSQ: SUBRANGE=All, DNSUF="gprs", DNSQUERYMODE=NAPTR, DESC="For huawei rule01";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-DNSQ.md`
