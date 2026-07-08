---
id: UNC@20.15.2@ConfigObject@NFDISCPLCY
type: ConfigObject
name: NFDISCPLCY（NF的服务发现策略）
nf: UNC
version: 20.15.2
object_name: NFDISCPLCY
object_kind: global_setting
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- NCG
status: active
---

# NFDISCPLCY（NF的服务发现策略）

## 说明

![](设置NF的服务发现策略（SET NFDISCPLCY）_09651764.assets/notice_3.0-zh-cn_2.png)

如果CACHESWITCH设置为OFF，会导致CPU升高，可能影响用户业务；如果CACHELOCK设置为ON，会导致NF不再去NRF进行服务发现，导致服务发现结果可能不准确。

**适用NF：AMF、SMF、NSSF、NRF、NCG**

该命令用于配置服务发现流程的策略。

## 操作本对象的命令

- [LST NFDISCPLCY](command/UNC/20.15.2/LST-NFDISCPLCY.md)
- [SET NFDISCPLCY](command/UNC/20.15.2/SET-NFDISCPLCY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF的服务发现策略（LST-NFDISCPLCY）_09651379.md`
- 原始手册：`evidence/UNC/20.15.2/设置NF的服务发现策略（SET-NFDISCPLCY）_09651764.md`
