---
id: UNC@20.15.2@ConfigObject@NRFNSDNNRT
type: ConfigObject
name: NRFNSDNNRT（DNN和网络切片路由）
nf: UNC
version: 20.15.2
object_name: NRFNSDNNRT
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFNSDNNRT（DNN和网络切片路由）

## 说明

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于DNN和网络切片的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

如果针对同一组DNN和网络切片配置了多个不同的下一跳归属NRF组名称，那么当前NRF会选取下一跳所有归属NRF组中优先级最高的NRF。

此命令受到SET NRFFUNCSW命令中DNNNIMATCHSW开关控制。发现消息中DNN携带网络标识（NI）和操作标识符(OI)进行路由转发，当开关打开时，NRF优先精确匹配DNN的路由，如果未匹配到，再精确匹配DNN只包含NI的路由。当开关关闭时，NRF只能精确匹配DNN的路由。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFNSDNNRT]] · ADD NRFNSDNNRT
- [[command/UNC/20.15.2/LST-NRFNSDNNRT]] · LST NRFNSDNNRT
- [[command/UNC/20.15.2/RMV-NRFNSDNNRT]] · RMV NRFNSDNNRT

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DNN和网络切片路由（RMV-NRFNSDNNRT）_09653011.md`
- 原始手册：`evidence/UNC/20.15.2/增加DNN和网络切片路由（ADD-NRFNSDNNRT）_09651810.md`
- 原始手册：`evidence/UNC/20.15.2/查询DNN和网络切片路由（LST-NRFNSDNNRT）_09654157.md`
