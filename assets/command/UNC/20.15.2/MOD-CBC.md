---
id: UNC@20.15.2@MMLCommand@MOD CBC
type: MMLCommand
name: MOD CBC（修改CBC）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CBC
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- CBC配置
status: active
---

# MOD CBC（修改CBC）

## 功能

**适用网元：MME**

此命令用于修改CBC（Cell Broadcast Center）配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CBCIDX | CBC索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待修改的CBC的索引。<br>数据来源：本端规划<br>取值范围：0~127<br>默认值：无<br>说明：可以通过<br>[**LST CBC**](查询CBC(LST CBC)_26146372.md)<br>命令查看已有配置，确认所要修改的CBC的索引。 |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CBC IP的地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无<br>配置原则：系统目前仅支持IPV4地址。 |
| IPV4_1 | CBC IPv4地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定CBC第一个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_2 | CBC IPv4地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第二个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_3 | CBC IPv4地址3 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第三个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_4 | CBC IPv4地址4 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第四个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_5 | CBC IPv4地址5 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第五个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_6 | CBC IPv4地址6 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第六个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_7 | CBC IPv4地址7 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第七个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_8 | CBC IPv4地址8 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第八个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV6_1 | CBC IPv6地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定CBC第一个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_2 | CBC IPv6地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第二个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_3 | CBC IPv6地址3 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第三个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_4 | CBC IPv6地址4 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第四个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_5 | CBC IPv6地址5 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第五个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_6 | CBC IPv6地址6 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第六个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_7 | CBC IPv6地址7 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第七个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_8 | CBC IPv6地址8 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第八个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| CBCNAME | CBC名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CBC名称。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无<br>配置原则：建议取有实际意义的名称，以方便识别。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CBC]] · CBC（CBC）

## 使用实例

修改一个CBC配置：该CBC索引号为0，地址类型为IPv4，IP1改为10.10.10.17，IP2为10.10.10.18。

MOD CBC: CBCIDX=0, IPTYPE=IPV4, IPV4_1="10.10.10.17", IPV4_2="10.10.10.18";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-CBC.md`
