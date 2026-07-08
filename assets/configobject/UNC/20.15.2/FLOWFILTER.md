---
id: UNC@20.15.2@ConfigObject@FLOWFILTER
type: ConfigObject
name: FLOWFILTER（流过滤器）
nf: UNC
version: 20.15.2
object_name: FLOWFILTER
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# FLOWFILTER（流过滤器）

## 说明

**适用NF：PGW-C、SMF**

该命令用于添加流过滤器。主要有两个用途：

UL CL分流场景下，在会话相关流程中，SMF会将流过滤器下发给UPF，UPF基于流过滤器执行相应的数据转发动作。ADC场景下，用于匹配PCF下发的ADC规则中的AppId，若匹配成功则将该ADC规则下发给UPF，指示UPF进行应用检测（详情参见WSFD-109102 ADC基本功能）。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-FLOWFILTER]] · ADD FLOWFILTER
- [[command/UNC/20.15.2/LST-FLOWFILTER]] · LST FLOWFILTER
- [[command/UNC/20.15.2/RMV-FLOWFILTER]] · RMV FLOWFILTER

## 证据

- 原始手册：`evidence/UNC/20.15.2/FLOWFILTER.md`
- 原始手册：`evidence/UNC/20.15.2/FLOWFILTER.md`
- 原始手册：`evidence/UNC/20.15.2/FLOWFILTER.md`
