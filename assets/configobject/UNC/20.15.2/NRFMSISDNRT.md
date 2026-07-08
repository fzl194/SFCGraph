---
id: UNC@20.15.2@ConfigObject@NRFMSISDNRT
type: ConfigObject
name: NRFMSISDNRT（MSISDN号段路由）
nf: UNC
version: 20.15.2
object_name: NRFMSISDNRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFMSISDNRT（MSISDN号段路由）

## 说明

![](增加MSISDN号段路由（ADD NRFMSISDNRT）_09652377.assets/notice_3.0-zh-cn_2.png)

配置号段路由较多，将会增大CPU的负载。

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于MSISDN号段的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

## 操作本对象的命令

- [ADD NRFMSISDNRT](command/UNC/20.15.2/ADD-NRFMSISDNRT.md)
- [DSP NRFMSISDNRT](command/UNC/20.15.2/DSP-NRFMSISDNRT.md)
- [LST NRFMSISDNRT](command/UNC/20.15.2/LST-NRFMSISDNRT.md)
- [MOD NRFMSISDNRT](command/UNC/20.15.2/MOD-NRFMSISDNRT.md)
- [RMV NRFMSISDNRT](command/UNC/20.15.2/RMV-NRFMSISDNRT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改MSISDN号段路由（MOD-NRFMSISDNRT）_09654073.md`
- 原始手册：`evidence/UNC/20.15.2/删除MSISDN号段路由（RMV-NRFMSISDNRT）_09651755.md`
- 原始手册：`evidence/UNC/20.15.2/增加MSISDN号段路由（ADD-NRFMSISDNRT）_09652377.md`
- 原始手册：`evidence/UNC/20.15.2/显示MSISDN路由匹配信息（DSP-NRFMSISDNRT）_45444647.md`
- 原始手册：`evidence/UNC/20.15.2/查询MSISDN号段路由（LST-NRFMSISDNRT）_09653023.md`
