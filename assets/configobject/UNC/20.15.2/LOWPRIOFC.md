---
id: UNC@20.15.2@ConfigObject@LOWPRIOFC
type: ConfigObject
name: LOWPRIOFC（低优先级流控参数）
nf: UNC
version: 20.15.2
object_name: LOWPRIOFC
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# LOWPRIOFC（低优先级流控参数）

## 说明

![](设置低优先级流控参数(SET LOWPRIOFC)_72345759.assets/notice_3.0-zh-cn_2.png)

该命令主要用于低优先级业务的接入控制，配置不当可能导致业务受损，建议保持系统初始设置值。如需修改，请联系华为技术支持。

**适用网元：MME**

该命令用于设置低优先级接入流控功能的相关参数。

低优先级用户（比如M2M）一般是和普通用户共用核心网设备，M2M业务很多都是行业应用，一个行业应用下的所有M2M终端在很短的时间内同时发起业务，导致移动网络拥塞（如一个电力公司下的所有电表在很短的时间内同时上报数据到电力公司），影响普通用户业务。为了防止这类低优先级业务影响在网普通用户正常进行业务， UNC 系统能够基于当前CPU负荷，自动调节低优先级业务的接入消息允许处理速率。这些消息包括：Attach Request、Service Request、Control Plane Service Request、Connection Resume和Tracking Area Update Request消息。

## 操作本对象的命令

- [LST LOWPRIOFC](command/UNC/20.15.2/LST-LOWPRIOFC.md)
- [SET LOWPRIOFC](command/UNC/20.15.2/SET-LOWPRIOFC.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询低优先级流控参数(LST-LOWPRIOFC)_26146160.md`
- 原始手册：`evidence/UNC/20.15.2/设置低优先级流控参数(SET-LOWPRIOFC)_72345759.md`
