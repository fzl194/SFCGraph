---
id: UNC@20.15.2@MMLCommand@ADD N2INFAMFINFO
type: MMLCommand
name: ADD N2INFAMFINFO（增加AMF的N2接口信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: N2INFAMFINFO
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- AMF
- AMF的N2接口信息管理
status: active
---

# ADD N2INFAMFINFO（增加AMF的N2接口信息）

## 功能

**适用NF：AMF**

该命令用于添加AMF的N2接口信息。当前NF类型为AMF时，需要配置N2接口信息。

## 注意事项

- 该命令执行后立即生效。

- 当前注册该信息无法提供实际功能，NRF和基站不支持DNS信息同步。

- 最多可输入1条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |
| IPADDRESSTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定IP地址接入类型。<br>数据来源：全网规划<br>取值范围：<br>- IPTypeV4（IPV4类型）<br>- IPTypeV6（IPV6类型）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS1 | IPV4类型地址1 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：本参数用于指定IPV4类型地址1。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。0.0.0.0~255.255.255.255。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS2 | IPV4类型地址2 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV4"时为条件可选参数。<br>参数含义：本参数用于指定IPV4类型地址2。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>同IPV4ADDRESS1。 |
| IPV4ADDRESS3 | IPV4类型地址3 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV4"时为条件可选参数。<br>参数含义：本参数用于指定IPV4类型地址3。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>同IPV4ADDRESS1。 |
| IPV4ADDRESS4 | IPV4类型地址4 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV4"时为条件可选参数。<br>参数含义：本参数用于指定IPV4类型地址4。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>同IPV4ADDRESS1。 |
| IPV6ADDRESS1 | IPV6类型地址1 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：本参数用于指定IPV6类型地址1。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS2 | IPV6类型地址2 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV6"时为条件可选参数。<br>参数含义：本参数用于指定IPV6类型地址2。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>同IPV6ADDRESS1。 |
| IPV6ADDRESS3 | IPV6类型地址3 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV6"时为条件可选参数。<br>参数含义：本参数用于指定IPV6类型地址3。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>同IPV6ADDRESS1。 |
| IPV6ADDRESS4 | IPV6类型地址4 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV6"时为条件可选参数。<br>参数含义：本参数用于指定IPV6类型地址4。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>同IPV6ADDRESS1。 |
| AMFNAME | AMF名称 | 可选必选说明：可选参数<br>参数含义：本参数用于指定AMF名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>- AMF名称由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- 不能用“-”或者“.”开头和结尾，中间不能出现连续的两个“.”。例如：amf1.cluster1.net2.amf.5gc.mnc012.mcc345.3gppnetwork.org |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N2INFAMFINFO]] · AMF的N2接口信息（N2INFAMFINFO）

## 使用实例

运营商A需要给当前AMF配置N2接口信息：NF实例名称为AMF_Instance_0，IP地址类型为IPTypeV4，IPV4类型地址1为192.168.0.1，IPV4类型地址2为192.168.0.2，AMF名称为amf1.cluster1.net2.3gppnetwork.org。

```
ADD N2INFAMFINFO: NFINSTANCENAME="AMF_Instance_0", IPADDRESSTYPE=IPTypeV4, IPV4ADDRESS1="192.168.0.1", IPV4ADDRESS2="192.168.0.2", AMFNAME="amf1.cluster1.net2.3gppnetwork.org";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-N2INFAMFINFO.md`
