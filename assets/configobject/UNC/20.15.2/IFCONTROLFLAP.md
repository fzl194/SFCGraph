---
id: UNC@20.15.2@ConfigObject@IFCONTROLFLAP
type: ConfigObject
name: IFCONTROLFLAP（接口震荡抑制）
nf: UNC
version: 20.15.2
object_name: IFCONTROLFLAP
object_kind: entity
status: active
---

# IFCONTROLFLAP（接口震荡抑制）

## 说明

该命令用于添加接口震荡抑制。

网络应用中，由于物理信号干扰、链路层配置错误等原因可能导致设备接口频繁地交替出现Up和Down状态，造成路由协议反复震荡，对设备和网络产生较严重影响，甚至可能造成部分设备瘫痪，网络不可使用。

控制接口震荡特性用于降低接口状态变化对网络稳定性的影响。

给每个接口设置一个值，称为惩罚值（penalty value）。惩罚值的初始值为0，值越大说明该接口越不稳定。当某个接口的状态发生Up/Down变化时，就给予其惩罚，即：接口Down信号每到达一次就将其惩罚值增加一个固定值400，作为惩罚，而接口Up信号每到达一次，惩罚值进行一次指数衰减计算。当惩罚值达到一个设定的抑制门限（suppress value，简称suppress）时，就将该接口状态抑制住，即不上报该接口状态。惩罚值可随着时间推移按指数（半衰期法则）递减，当惩罚值下降到一个设定的重用门限（reuse value，简称reuse）时，就解除对该接口的抑制，重新上报告该接口状态信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IFCONTROLFLAP]] · ADD IFCONTROLFLAP
- [[command/UNC/20.15.2/DSP-IFCONTROLFLAP]] · DSP IFCONTROLFLAP
- [[command/UNC/20.15.2/LST-IFCONTROLFLAP]] · LST IFCONTROLFLAP
- [[command/UNC/20.15.2/RMV-IFCONTROLFLAP]] · RMV IFCONTROLFLAP
- [[command/UNC/20.15.2/RTR-IFCONTROLFLAP]] · RTR IFCONTROLFLAP

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除接口震荡抑制（RMV-IFCONTROLFLAP）_50120586.md`
- 原始手册：`evidence/UNC/20.15.2/显示接口震荡抑制动态信息（DSP-IFCONTROLFLAP）_50281650.md`
- 原始手册：`evidence/UNC/20.15.2/查询接口震荡抑制（LST-IFCONTROLFLAP）_00441165.md`
- 原始手册：`evidence/UNC/20.15.2/添加接口震荡抑制（ADD-IFCONTROLFLAP）_50121362.md`
- 原始手册：`evidence/UNC/20.15.2/清除接口震荡抑制信息（RTR-IFCONTROLFLAP）_50281094.md`
