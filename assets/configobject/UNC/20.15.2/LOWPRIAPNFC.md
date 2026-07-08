---
id: UNC@20.15.2@ConfigObject@LOWPRIAPNFC
type: ConfigObject
name: LOWPRIAPNFC（低优先级APN流控参数）
nf: UNC
version: 20.15.2
object_name: LOWPRIAPNFC
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# LOWPRIAPNFC（低优先级APN流控参数）

## 说明

![](设置低优先级APN流控参数(SET LOWPRIAPNFC)_72345757.assets/notice_3.0-zh-cn_2.png)

如果低优先级APN流控功能被关闭或者相关流控参数设置不正确，可能影响低优先级APN流控的效果。

**适用网元：MME**

该命令用于设置低优先级APN流控功能的相关参数。本功能在SPP上的MM模块部署。

低优先级用户（比如M2M）一般是和普通用户共用核心网设备，M2M业务很多都是行业应用，可能发生一个行业应用下的所有M2M终端在很短的时间内同时发起业务，导致移动网络拥塞（如一个电力公司下的所有电表在很短的时间内同时上报数据到电力公司），影响普通用户业务。为了防止这类低优先级业务影响其他用户的正常业务， UNC 系统能够基于当前CPU负荷，自动调节低优先级业务的接入消息允许处理速率。这些消息包括：Attach Request、Service Request消息。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-LOWPRIAPNFC]] · LST LOWPRIAPNFC
- [[command/UNC/20.15.2/SET-LOWPRIAPNFC]] · SET LOWPRIAPNFC

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询低优先级APN流控参数（LST-LOWPRIAPNFC）_26146158.md`
- 原始手册：`evidence/UNC/20.15.2/设置低优先级APN流控参数(SET-LOWPRIAPNFC)_72345757.md`
