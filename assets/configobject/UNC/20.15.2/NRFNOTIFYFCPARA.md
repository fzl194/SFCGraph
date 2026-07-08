---
id: UNC@20.15.2@ConfigObject@NRFNOTIFYFCPARA
type: ConfigObject
name: NRFNOTIFYFCPARA（通知流控参数）
nf: UNC
version: 20.15.2
object_name: NRFNOTIFYFCPARA
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFNOTIFYFCPARA（通知流控参数）

## 说明

![](设置通知流控参数（SET NRFNOTIFYFCPARA）_09653165.assets/notice_3.0-zh-cn_2.png)

NFNTYNUM参数范围过大，会导致通知消息增多，引起cpu升高，影响性能。

**适用NF：NRF**

该命令用于配置通知流程的固定速率流控信息 。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NRFNOTIFYFCPARA]] · LST NRFNOTIFYFCPARA
- [[command/UNC/20.15.2/SET-NRFNOTIFYFCPARA]] · SET NRFNOTIFYFCPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询通知流控参数（LST-NRFNOTIFYFCPARA）_09654449.md`
- 原始手册：`evidence/UNC/20.15.2/设置通知流控参数（SET-NRFNOTIFYFCPARA）_09653165.md`
