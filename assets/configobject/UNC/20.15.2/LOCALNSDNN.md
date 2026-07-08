---
id: UNC@20.15.2@ConfigObject@LOCALNSDNN
type: ConfigObject
name: LOCALNSDNN（网络切片或DNN纠正配置）
nf: UNC
version: 20.15.2
object_name: LOCALNSDNN
object_kind: entity
applicable_nf:
- AMF
status: active
---

# LOCALNSDNN（网络切片或DNN纠正配置）

## 说明

**适用NF：AMF**

该命令用于增加网络切片或者DNN纠正配置。

在PDU会话建立流程中，以下场景将使用本命令配置的纠正网络切片：

（1）用户没有携带请求的网络切片。

（2）DWORD70 BIT2设置为1时，用户请求切片不在Allowed NSSAI切片内，并且该用户没有签约的default S-NSSAI。

同样地，如果用户没有携带请求的DNN，或者请求的DNN不在选定的网络切片的签约列表中，那么通过本命令选择可用的DNN。特别地，如果选定的网络签约切片存在野卡DNN，那么UE请求携带的DNN都认为是与签约匹配的。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-LOCALNSDNN]] · ADD LOCALNSDNN
- [[command/UNC/20.15.2/LST-LOCALNSDNN]] · LST LOCALNSDNN
- [[command/UNC/20.15.2/MOD-LOCALNSDNN]] · MOD LOCALNSDNN
- [[command/UNC/20.15.2/RMV-LOCALNSDNN]] · RMV LOCALNSDNN

## 证据

- 原始手册：`evidence/UNC/20.15.2/LOCALNSDNN.md`
- 原始手册：`evidence/UNC/20.15.2/LOCALNSDNN.md`
- 原始手册：`evidence/UNC/20.15.2/LOCALNSDNN.md`
- 原始手册：`evidence/UNC/20.15.2/LOCALNSDNN.md`
