---
id: UNC@20.15.2@MMLCommand@ADD SBCMME
type: MMLCommand
name: ADD SBCMME（增加SBC MME实体）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SBCMME
command_category: 配置类
applicable_nf:
- CBCF
effect_mode: 立即生效
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- SBC MME配置
status: active
---

# ADD SBCMME（增加SBC MME实体）

## 功能

**适用网元：CBCF**

此命令用于增加SBC MME实体配置。

## 注意事项

- 该命令执行后立即生效。
- 该表最大记录数为128。
- 每个SBC MME最多可以配置8个IP。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEIDX | MME索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待添加的MME的索引。<br>数据来源：本端规划<br>取值范围：0~127<br>默认值：无<br>配置原则：<br>- 此MME索引在系统范围内唯一。<br>- 建议从“0”开始顺序取值。 |
| MMENAME | MME名称 | 可选必选说明：必选参数<br>参数含义：该参数于用于指定与本局对接的MME的号码，MME号码长度为12位，编码格式为：MCC＋MNC＋MMEGI＋MMEC，例如，一个典型的MME号码为：“460008000101”<br>数据来源：整网规划<br>取值范围：字符串类型，输入长度为12位。<br>默认值：无<br>配置原则：<br>- MCC（Mobile Country Code）：移动国家码，用于标识MME所属的国家。移动国家码由3位数字组成，它由ETSI在全球范围内统一分配，例如，中国的“移动国家码”为“460”、英国的“移动国家码”为“234”等。<br>- MNC（Mobile Network Code）：移动网络码，用于标识MME的归属PLMN。移动网络码由2位或3位数字组成，如果为2位的场景需要补0，它由本国电信主管部门在本国范围内统一分配，例如，目前在中国，补0后中国移动GSM网络的“移动网络码”为“000”、中国联通GSM网络的“移动网络码”为“001”等。<br>- MMEGI（MME Group ID）：MME分组内的组号，用来标识MME属于哪个POOL区。由4位字符（0～9、A～F或a～f）组成。<br>- MMEC（MME Code）：组内的MME编码，用来标识MME在POOL区内的编码。由2位字符（0～9、A～F或a～f）组成。 |
| POOLGRPID | MME POOL标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME归属的MME POOL群组，该参数只有在MME为POOL组网时有效。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：255<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME IP的地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：“IPV4(IPv4)”<br>配置原则：系统目前仅支持IPV4地址。 |
| IPV4_1 | MME IPv4地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定MME第一个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_2 | MME IPv4地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第二个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_3 | MME IPv4地址3 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第三个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_4 | MME IPv4地址4 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第四个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_5 | MME IPv4地址5 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第五个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_6 | MME IPv4地址6 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第六个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_7 | MME IPv4地址7 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第七个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV4_8 | MME IPv4地址8 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第八个IPv4类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV4(IPv4)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV6_1 | MME IPv6地址1 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定MME第一个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_2 | MME IPv6地址2 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第二个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_3 | MME IPv6地址3 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第三个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_4 | MME IPv6地址4 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第四个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_5 | MME IPv6地址5 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第五个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_6 | MME IPv6地址6 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第六个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_7 | MME IPv6地址7 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第七个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| IPV6_8 | MME IPv6地址8 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MME第八个IPv6类型的IP地址。<br>前提条件：“IP地址类型”设置为“IPV6(IPv6)”时，该字段有效。<br>数据来源：整网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>说明：目前不支持IPV6地址的配置。 |
| MMEDESC | MME描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME描述信息。<br>数据来源：整网规划<br>取值范围：0~255位字符串<br>默认值：noname<br>配置原则：建议填有实际意义的描述，以方便识别。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SBCMME]] · SBC MME实体（SBCMME）

## 使用实例

增加一个SBC MME配置：该MME索引号为0， 名称 为012345678901，地址类型为IPv4，IP1为10.10.10.10，IP2为10.10.10.11，描述为MME1。

```
ADD SBCMME: MMEIDX=0, MMENAME="012345678901", IPTYPE=IPV4, IPV4_1="10.10.10.10", IPV4_2="10.10.10.11", MMEDESC="MME1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SBCMME.md`
