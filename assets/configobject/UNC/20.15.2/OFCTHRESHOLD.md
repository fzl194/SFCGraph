---
id: UNC@20.15.2@ConfigObject@OFCTHRESHOLD
type: ConfigObject
name: OFCTHRESHOLD（离线计费阈值）
nf: UNC
version: 20.15.2
object_name: OFCTHRESHOLD
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# OFCTHRESHOLD（离线计费阈值）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

该命令用来配置控制话单生成条件中的计费阈值，包括时间阈值、流量阈值、计费条件改变次数、话单最多携带的容器数、MME/SGSN/SGW/ePDG地址改变次数等。

## 操作本对象的命令

- [SET OFCTHRESHOLD](command/UNC/20.15.2/SET-OFCTHRESHOLD.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置离线计费阈值（SET-OFCTHRESHOLD）_09896910.md`
