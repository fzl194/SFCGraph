---
id: UNC@20.15.2@ConfigObject@NSAVLINFO
type: ConfigObject
name: NSAVLINFO（操作网络切片可用性信息）
nf: UNC
version: 20.15.2
object_name: NSAVLINFO
object_kind: action
applicable_nf:
- AMF
status: active
---

# NSAVLINFO（操作网络切片可用性信息）

## 说明

**适用NF：AMF**

该命令用于在AMF上操作与NSSF之间的网络切片可用性信息。

NSSF集中管理了运营商的网络切片可用性信息，包括了网络中的跟踪区（TA）列表以及每个跟踪区支持的和限制使用的网络切片。NSSF上的网络切片可用性信息可能来自配置，也可能部分来自AMF的上报。操作员可通过本命令向NSSF上报或者删除网络切片可用性信息。

如果NSSF上的网络切片可用性信息只来自配置，在执行本命令前要确保NSSF的本地配置更新到最新。

此外，为了能及时感知NSSF侧的网络切片信息变化，AMF需要向NSSF提供其所服务的跟踪区列表（通过ADD NFTAI配置）以订阅这些跟踪区的网络切片信息。操作员可通过本命令触发订阅或者去订阅。

## 操作本对象的命令

- [[command/UNC/20.15.2/OPR-NSAVLINFO]] · OPR NSAVLINFO

## 证据

- 原始手册：`evidence/UNC/20.15.2/NSAVLINFO.md`
