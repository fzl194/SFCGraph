---
id: UNC@20.15.2@ConfigObject@NFDISC
type: ConfigObject
name: NFDISC（测试服务发现）
nf: UNC
version: 20.15.2
object_name: NFDISC
object_kind: action
applicable_nf:
- NRF
status: active
---

# NFDISC（测试服务发现）

## 说明

**适用NF：NRF**

该命令用于测试本NRF的服务发现流程，并呈现服务发现结果。

服务发现参数在此命令中输入格式要求及参考信息如下：

此命令服务发现参数输入格式与服务发现消息中的JSON格式有一定差异，需要将标准JSON格式报文中的" " 用\进行转义。

例如：根据targetNfType，requesterNfType进行服务发现，标准的JSON格式如下{"targetNfType":4,"requesterNfType":3}，转义后的结果（即此命令参数需要输入格式）为{\"targetNfType\":4,\"requesterNfType\":3}。

此命令参数中针对枚举字段的取值进行了整数的替换对应。服务发现参数中涉及的枚举值与其对应的整数如下：

NFType:

NRF = 1。

UDM = 2。

AMF = 3。

SMF = 4。

AUSF = 5。

NEF = 6。

PCF = 7。

SMSF = 8。

NSSF = 9。

UDR = 10。

LMF = 11。

GMLC = 12。

5G_EIR = 13。

SEPP = 14。

UPF = 15。

N3IWF = 16。

AF = 17。

UDSF = 18。

BSF = 19。

CHF = 20。

NWDAF = 21。

PCSCF = 22。

CUSTOM_OCS = 23。

ServiceName:

nnrfNfm = 1。

nnrfDisc = 2。

nudmSdm = 3。

nudmUecm = 4。

nudmUeau = 5。

nudmEe = 6。

nudmPp = 7。

namfComm = 8。

namfEvts = 9。

namfMt = 10。

namfLoc = 11。

nsmfPdusession = 12。

nsmfEventExposure = 13。

nausfAuth = 14。

nausfSorprotection = 15。

nausfUpuprotection = 16。

nnefPfdmanagement = 17。

npcfAmPolicyControl = 18。

npcfSmpolicycontrol = 19。

npcfPolicyauthorization = 20。

npcfBdtpolicycontrol = 21。

npcfEventexposure = 22。

npcfUePolicyControl = 23。

nsmsfSms = 24。

nnssfNsselection = 25。

nnssfNssaiavailability = 26。

nudrDr = 27。

nlmfLoc = 28。

n5gEirEic = 29。

nbsfManagement = 30。

nchfSpendinglimitcontrol = 31。

nchfConvergedcharging = 32。

nnwdafEventssubscription = 33。

nnwdafAnalyticsinfo = 34。

nocsSpendinglimitcontrol = 35。

nocsConvergedcharging = 36。

ngmlcLoc = 37。

DataSetId:

SUBSCRIPTION = 1。

POLICY = 2。

EXPOSURE = 3。

APPLICATION = 4。

PduSessionType:

IPV4 = 1。

IPV6 = 2。

IPV4V6 = 3。

UNSTRUCTURED = 4。

ETHERNET = 5。

AccessType:

3GPP_ACCESS = 1。

NON_3GPP_ACCESS = 2。

## 操作本对象的命令

- [TST NFDISC](command/UNC/20.15.2/TST-NFDISC.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/测试服务发现（TST-NFDISC）_09652471.md`
