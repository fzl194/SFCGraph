---
id: UNC@20.15.2@MMLCommand@ADD NRFADDR
type: MMLCommand
name: ADD NRFADDR（增加NRF实例地址信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFADDR
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
- CBCF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NRF管理
- NRF地址管理
- NRF实例地址管理
status: active
---

# ADD NRFADDR（增加NRF实例地址信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBCF**

该命令用于添加NRF实例地址信息。在对接真实NRF的场景下，需要配置该命令。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入2048条记录。
- IPADDRESSTYPE为NoneIP的记录最多只能配置一条。
- 在已配置的ADD NRF中，相同NRFINSTANCENAME记录的FQDN为空时，不支持将ADD NRFADDR中的IPADDRESSTYPE配置为NoneIP。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFINSTANCENAME | NRF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NRF的实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~38。<br>默认值：无<br>配置原则：<br>- 该参数构成字符只能是字母A～Z或a～z、数字0～9和下划线“-”和中划线“_”。<br>- 本参数来源于ADD NRF命令中的“NRF实例名称”参数。 |
| IPADDRESSTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NRF的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPTypeV4（IPTypeV4）<br>- IPTypeV6（IPTypeV6）<br>- NoneIP（无IP）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPV4地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定IPV4类型地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>- 1.0.0.0~255.255.255.254。<br>- IPv4地址不能为组播地址（224.x.y.z）和环回地址(127.x.y.z)。<br>- IPv4地址必须是A、B或者C类地址。 |
| IPV6ADDRESS | IPV6地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定IPV6类型地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>- 取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）和IPv4映射地址（::FFFF:XXXX:XXXX），若为IPv4兼容地址时，需判断是否符合IPv4地址要求。 |
| PORT | 端口 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"NoneIP"时为条件必选参数。该参数在"IPADDRESSTYPE"配置为"IPTypeV4"、"IPTypeV6"时为条件可选参数。<br>参数含义：该参数用于指定NRF的端口号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：<br>取值为0或不填时，如果关联的ADD NRF配置中TLS字段为TRUE，则使用443端口，反之则使用80端口。 |

## 操作的配置对象

- [NRF实例地址信息（NRFADDR）](configobject/UNC/20.15.2/NRFADDR.md)

## 使用实例

增加NRF地址信息，NRF实例名称为NRF_Instance_0，IP地址类型为IPV4类型，IPV4地址为192.168.0.1，端口号为8081。

```
ADD NRFADDR: NRFINSTANCENAME="NRF_Instance_0", IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS="192.168.0.1", PORT=8081;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加NRF实例地址信息（ADD-NRFADDR）_09653061.md`
