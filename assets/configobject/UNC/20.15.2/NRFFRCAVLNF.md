---
id: UNC@20.15.2@ConfigObject@NRFFRCAVLNF
type: ConfigObject
name: NRFFRCAVLNF（强制可用NF实例）
nf: UNC
version: 20.15.2
object_name: NRFFRCAVLNF
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFFRCAVLNF（强制可用NF实例）

## 说明

![](增加强制可用NF实例（ADD NRFFRCAVLNF）_71436523.assets/notice_3.0-zh-cn_2.png)

执行此命令增加强制可用NF实例时，可能会导致服务发现返回实际不可用的网元，影响业务引流。

**适用NF：NRF**

此命令用于配置NF为强制可用，被设置为强制可用的NF在暂停态也可以被发现，且在暂停态的NF在被设置为强制可用后其在发现，通知结果中NF状态字段会被强制设置为注册状态。对于配置为强制可用的NF，若开启忽略NF去注册开关，NRF将不处理该NF的去注册请求。

当NF因自身原因状态异常或者NRF系统心跳模块异常，但实际NF可正常接入业务时，NRF可通过本命令强制可用，使其他网元可正常发现该NF信息并确保状态正常。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFFRCAVLNF]] · ADD NRFFRCAVLNF
- [[command/UNC/20.15.2/LST-NRFFRCAVLNF]] · LST NRFFRCAVLNF
- [[command/UNC/20.15.2/RMV-NRFFRCAVLNF]] · RMV NRFFRCAVLNF

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除强制可用NF实例（RMV-NRFFRCAVLNF）_71436553.md`
- 原始手册：`evidence/UNC/20.15.2/增加强制可用NF实例（ADD-NRFFRCAVLNF）_71436523.md`
- 原始手册：`evidence/UNC/20.15.2/查询强制可用NF实例（LST-NRFFRCAVLNF）_24796820.md`
