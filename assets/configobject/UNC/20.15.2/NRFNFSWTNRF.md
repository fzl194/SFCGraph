---
id: UNC@20.15.2@ConfigObject@NRFNFSWTNRF
type: ConfigObject
name: NRFNFSWTNRF（操作指示NF切换NRF）
nf: UNC
version: 20.15.2
object_name: NRFNFSWTNRF
object_kind: action
applicable_nf:
- NRF
status: active
---

# NRFNFSWTNRF（操作指示NF切换NRF）

## 说明

![](操作指示NF切换NRF（OPR NRFNFSWTNRF）_89132374.assets/notice_3.0-zh-cn_2.png)

执行该命令后会导致该NF实例注册或心跳请求短时间接收504响应，请谨慎操作。

**适用NF：NRF**

该命令用于NRF双活场景下指示NF切换到另外容灾的NRF上注册。

执行完该命令后，NRF会对NF限定次数的心跳和全量更新请求进行正常处理后返回504，或从下一次收到NF心跳或全量更新请求后的1分钟内对心跳和全量更新请求进行正常处理后返回504。

此命令执行结果通过DSP NRFNFSWTNRF命令查询。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-NRFNFSWTNRF]] · DSP NRFNFSWTNRF
- [[command/UNC/20.15.2/OPR-NRFNFSWTNRF]] · OPR NRFNFSWTNRF

## 证据

- 原始手册：`evidence/UNC/20.15.2/操作指示NF切换NRF（OPR-NRFNFSWTNRF）_89132374.md`
- 原始手册：`evidence/UNC/20.15.2/显示网元切换NRF记录（DSP-NRFNFSWTNRF）_34571879.md`
