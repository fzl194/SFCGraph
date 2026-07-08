---
id: UNC@20.15.2@MMLCommand@ADD NFNS
type: MMLCommand
name: ADD NFNS（增加NF支持的网络切片）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NFNS
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF支持的切片管理
status: active
---

# ADD NFNS（增加NF支持的网络切片）

## 功能

**适用NF：AMF、SMF、NSSF**

该命令用以给指定的NF增加其所支持的网络切片。

## 注意事项

- 该命令执行后立即生效。

- 当切片的NF类型为SMF时，需要通过命令ADD NSDNN添加对应的DNN，否则可能导致NF在NRF上注册或更新失败（NRF会严格检查切片下是否有DNN存在）。
- 如果启用了AMF与NSSF之间的网络切片可用性流程（NSSELPARA参数SYNSW设置为ON），那么当AMF新增支持网络切片，或者删除当前已支持的网络切片后，需要手工执行OPR NSAVLINFO向NSSF同步本AMF的网络切片可用性信息。

- 最多可输入8192条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：无效的NF<br>- “NfNRF（NfNRF）”：NRF<br>- “NfUDM（NfUDM）”：UDM<br>- “NfAMF（NfAMF）”：AMF<br>- “NfSMF（NfSMF）”：SMF<br>- “NfAUSF（NfAUSF）”：AUSF<br>- “NfNEF（NfNEF）”：NEF<br>- “NfPCF（NfPCF）”：PCF<br>- “NfSMSF（NfSMSF）”：SMSF<br>- “NfNSSF（NfNSSF）”：NSSF<br>- “NfUDR（NfUDR）”：UDR<br>- “NfLMF（NfLMF）”：LMF<br>- “NfGMLC（NfGMLC）”：GMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：5G_EIR<br>- “NfSEPP（NfSEPP）”：SEPP<br>- “NfUPF（NfUPF）”：UPF<br>- “NfN3IWF（NfN3IWF）”：N3IWF<br>- “NfAF（NfAF）”：AF<br>- “NfUDSF（NfUDSF）”：UDSF<br>- “NfBSF（NfBSF）”：BSF<br>- “NfCHF（NfCHF）”：CHF<br>- “NfNWDAF（NfNWDAF）”：NWDAF<br>- “NfTypeMAX（NfTypeMAX）”：NfTypeMAX<br>- “NfMBSMF（NfMBSMF）”：MBSMF<br>- “NfCBCF（NfCBCF）”：NfCBCF<br>- “NfSCF（NfSCF）”：NfSCF<br>- “NfSPF（NfSPF）”：NfSPF<br>默认值：无<br>配置原则：无 |
| NSIDX | 网络切片索引 | 可选必选说明：必选参数<br>参数含义：该参数在系统中唯一标识某个网络切片。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。本参数通过ADD PLMNNS命令进行配置。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数表示对网络切片的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [NF支持的网络切片（NFNS）](configobject/UNC/20.15.2/NFNS.md)

## 使用实例

AMF增加支持URLLC切片（索引值为11），执行如下命令：

```
ADD NFNS: NFTYPE=NfAMF, NSIDX=11, DESC="add urllc ns for amf";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加NF支持的网络切片（ADD-NFNS）_09651407.md`
