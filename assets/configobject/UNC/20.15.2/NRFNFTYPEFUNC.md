---
id: UNC@20.15.2@ConfigObject@NRFNFTYPEFUNC
type: ConfigObject
name: NRFNFTYPEFUNC（基于NFType设置NRF的各类功能开关）
nf: UNC
version: 20.15.2
object_name: NRFNFTYPEFUNC
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFNFTYPEFUNC（基于NFType设置NRF的各类功能开关）

## 说明

![](增加基于NFType设置NRF的各类功能开关（ADD NRFNFTYPEFUNC）_83319170.assets/notice_3.0-zh-cn_2.png)

开关设置将会导致以下影响:

- DISCFILTERSW开关关闭可能导致服务发现返回实际不可用的网元。
- DISCFILTERFWDSW、DISCROAFILFWDSW开关打开可能导致服务发现结果信息缺失。

**适用NF：NRF**

该命令用于增加基于NFType设置NRF的各类功能开关。

## 操作本对象的命令

- [ADD NRFNFTYPEFUNC](command/UNC/20.15.2/ADD-NRFNFTYPEFUNC.md)
- [LST NRFNFTYPEFUNC](command/UNC/20.15.2/LST-NRFNFTYPEFUNC.md)
- [MOD NRFNFTYPEFUNC](command/UNC/20.15.2/MOD-NRFNFTYPEFUNC.md)
- [RMV NRFNFTYPEFUNC](command/UNC/20.15.2/RMV-NRFNFTYPEFUNC.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于NFType设置NRF的各类功能开关（MOD-NRFNFTYPEFUNC）_83319174.md`
- 原始手册：`evidence/UNC/20.15.2/删除基于NFType设置NRF的各类功能开关（RMV-NRFNFTYPEFUNC）_29158013.md`
- 原始手册：`evidence/UNC/20.15.2/增加基于NFType设置NRF的各类功能开关（ADD-NRFNFTYPEFUNC）_83319170.md`
- 原始手册：`evidence/UNC/20.15.2/查询基于NFType设置NRF的各类功能开关（LST-NRFNFTYPEFUNC）_29158009.md`
