---
id: UNC@20.15.2@MMLCommand@ADD CBC
type: MMLCommand
name: ADD CBC（增加CBC）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CBC
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- CBC配置
status: active
---

# ADD CBC（增加CBC）

## 功能

**适用网元：MME**

此命令用于增加CBC（Cell Broadcast Center）配置。涉及小区广播服务特性。

当 UNC 启用小区广播服务时，需要配置此命令。

## 注意事项

- 该命令执行后立即生效。
- 该表最大记录数为128。
- 每个CBC最多可以配置8个IP。
- 每个HPLMN能配置多个CBC。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CBCIDX | CBC索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待添加的CBC的索引。<br>数据来源：本端规划<br>取值范围：0~127<br>默认值：无<br>配置原则：<br>- 此CBC索引在系统范围内唯一。<br>- 建议从“0”开始顺序取值。 |
| MCC | CBC归属的MCC | 可选必选说明：必选参数<br>参数含义：该参数用于指定本CBC归属HPLMN的MCC。<br>前提条件：在<br>UNC<br>MML窗口上执行命令<br>[**ADD HPLMN**](../../网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)<br>设置此参数。<br>数据来源：整网规划<br>取值范围：3位BCD码<br>默认值：无 |
| MNC | CBC归属的MNC | 可选必选说明：必选参数<br>参数含义：该参数用于指定本CBC归属HPLMN的MNC。<br>前提条件：在<br>UNC<br>MML窗口上执行命令<br>[**ADD HPLMN**](../../网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)<br>设置此参数。<br>数据来源：整网规划<br>取值范围：位数为2或3的BCD码<br>默认值：无 |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CBC IP的地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：“IPV4(IPv4)”<br>配置原则：系统目前仅支持IPV4地址。 |
| IPV4_1 | CBC IPv4地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定CBC第一个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_2 | CBC IPv4地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第二个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_3 | CBC IPv4地址3 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第三个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_4 | CBC IPv4地址4 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第四个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_5 | CBC IPv4地址5 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第五个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_6 | CBC IPv4地址6 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第六个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_7 | CBC IPv4地址7 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第七个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_8 | CBC IPv4地址8 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第八个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV6_1 | CBC IPv6地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定CBC第一个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_2 | CBC IPv6地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第二个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_3 | CBC IPv6地址3 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第三个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_4 | CBC IPv6地址4 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第四个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_5 | CBC IPv6地址5 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第五个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_6 | CBC IPv6地址6 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第六个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_7 | CBC IPv6地址7 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第七个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_8 | CBC IPv6地址8 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定CBC第八个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| CBCNAME | CBC名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CBC名称。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：noname<br>配置原则：建议取有实际意义的名称，以方便识别。 |

## 操作的配置对象

- [CBC（CBC）](configobject/UNC/20.15.2/CBC.md)

## 使用实例

增加一个CBC配置：该CBC索引号为0，归属的MCC为123，归属的MNC为03，地址类型为IPv4，IP1为10.10.10.10，IP2为10.10.10.11，CBC名称为CBC1。

ADD CBC: CBCIDX=0, MCC="123", MNC="03", IPTYPE=IPV4, IPV4_1="10.10.10.10", IPV4_2="10.10.10.11", CBCNAME="CBC1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加CBC(ADD-CBC)_72226049.md`
