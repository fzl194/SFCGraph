---
id: UNC@20.15.2@MMLCommand@ADD DMLE
type: MMLCommand
name: ADD DMLE（增加Diameter本端实体）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DMLE
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 32
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter本地实体
status: active
---

# ADD DMLE（增加Diameter本端实体）

## 功能

**适用网元：SGSN、MME**

该命令用于增加Diameter链路本端实体信息。Diameter协议用于支持MME与HSS（Home Subscriber Server）传递签约及鉴权数据；或用于检查MME与EIR（Equipment Identity Register）用户设备标识是否合法，以授权用户接入EPS（Evolved Packet System）网络。

## 注意事项

- 该命令执行后立即生效。
- 该表最大记录数为32。
- 该命令默认仅支持1条记录，在多HPLMN场景下，才能使用多条记录，此时需要开启软参BYTE_EX145 BIT1支持。
- 一个运营商建议只加一个DMLE。如强行添加，会导致现网业务因选择错误的DMLE而导致业务受损。如果需要添加多个DMLE，请通过[**ADD IMSICHAR**](../../../网络管理/归属网络运营商管理/IMSI号段属性配置表/增加IMSI号段属性配置(ADD IMSICHAR)_72225729.md)或[**ADD HNOINFO**](../../../网络管理/归属网络运营商管理/归属网络信息管理/增加归属网络信息(ADD HNOINFO)_26305862.md)指定本端标识，详情请参考WSFD-104401支持多HPLMN功能。
- 该命令为S6a口、S13口、SLg口基本配置，在UNC与HSS、EIR、DRA或GMLC对接的时候必须配置，当配置用于S13口时，本地实体索引（LOINDEX）需要配置为0。如果需要使用其他本地实体索引，请参考DWORD_EX18 BIT1–6的配置说明。DWORD_EX18 BIT6 控制UNC在发送S13接口消息时是否根据“DWORD_EX18” BIT1-BIT5设置的“本地实体索引”携带对应的本地域名和本地主机名，DWORD_EX18 BIT1-BIT5 控制UNC根据指定的ADD DMLE记录携带本地域名和本地主机名。
- 使用此本端实体与对端进行消息交互时，需要配置引用了此本端实体与对端实体的[**ADD DMLKS**](../Diameter链路集/增加Diameter链路集配置(ADD DMLKS)_72225957.md)命令及其所属的[**ADD DMLNK**](../Diameter链路/增加Diameter链路配置(ADD DMLNK)_72225953.md)命令，才能保证消息选路成功。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOINDEX | 本地实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地实体的索引，在Diameter链路中唯一标识一个本地实体。<br>数据来源：本端规划<br>取值范围：0～31<br>默认值：<br>“0” |
| LOHSTNAME | 本地实体主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本地实体的主机名信息，在Diameter链路中唯一标识一个本地实体。例如mme.epc.mnc123.mcc123.3gppnetwork.org。<br>数据来源：全网规划<br>取值范围：1～127位字符串，只能是字母A～Z或a～z、数字0～9、符号“-”和“.”。<br>默认值：无<br>配置原则：与对端HSS、EIR、DRA配置的对端实体主机名一致。 |
| LORLMNAME | 本地实体域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本地实体的域名信息，例如：epc.mnc123.mcc123.3gppnetwork.org。<br>数据来源：全网规划<br>取值范围：1～127位字符串，只能是字母A～Z或a～z、数字0～9、符号“-”和“.”。<br>默认值：无<br>配置原则：与对端HSS、EIR、DRA配置的对端实体的域名一致。 |
| PDTNAME | 产品名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定产品的名称，标识本地的产品信息。<br>数据来源：本端规划<br>取值范围：0～32位字符串<br>默认值：vUSN<br>配置原则：该参数用来标识本端的产品信息，一般可直接填写产品的名称，如填写<br>UNC<br>。 |
| LOINFONAME | 本地实体名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地实体的名称，标示本地实体。<br>数据来源：本端规划<br>取值范围：0～32位字符串<br>默认值：无<br>配置原则：用来标识本地实体时，一般配置为DMLE。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMLE]] · Diameter本端实体（DMLE）

## 使用实例

增加本地索引为0，本地的主机名为mme.epc.mnc123.mcc123.3gppnetwork.org，域名为epc.mnc123.mcc123.3gppnetwork.org，产品名称为UNC，本地实体名为DMLE的本地实体记录：

ADD DMLE: LOINDEX=0, LOHSTNAME="mme.epc.mnc123.mcc123.3gppnetwork.org", LORLMNAME="epc.mnc123.mcc123.3gppnetwork.org", PDTNAME="UNC", LOINFONAME="DMLE";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Diameter本端实体(ADD-DMLE)_72345881.md`
