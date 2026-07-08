---
id: UNC@20.15.2@ConfigObject@NGPRDREGTIMEDNN
type: ConfigObject
name: NGPRDREGTIMEDNN（基于DNN的周期性注册时长配置）
nf: UNC
version: 20.15.2
object_name: NGPRDREGTIMEDNN
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGPRDREGTIMEDNN（基于DNN的周期性注册时长配置）

## 说明

![](增加基于DNN的周期性注册时长配置（ADD NGPRDREGTIMEDNN）_21861953.assets/notice_3.0-zh-cn_2.png)

该命令仅建议对低功耗用户签约的DNN进行配置，如果DNN配置错误可能会对其它用户造成影响。

**适用NF：AMF**

该命令用于增加基于DNN配置周期性注册时长。

在大网和园区共享RAN场景下，园区用户和大网用户周期性注册时长不同，可通过该命令单独给园区用户基于签约的园区DNN配置周期性注册时长。

如果用户签约的多个DNN均添加了本配置，则AMF随机使用一个配置。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NGPRDREGTIMEDNN]] · ADD NGPRDREGTIMEDNN
- [[command/UNC/20.15.2/LST-NGPRDREGTIMEDNN]] · LST NGPRDREGTIMEDNN
- [[command/UNC/20.15.2/MOD-NGPRDREGTIMEDNN]] · MOD NGPRDREGTIMEDNN
- [[command/UNC/20.15.2/RMV-NGPRDREGTIMEDNN]] · RMV NGPRDREGTIMEDNN

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于DNN的周期性注册时长配置（MOD-NGPRDREGTIMEDNN）_21742357.md`
- 原始手册：`evidence/UNC/20.15.2/删除基于DNN的周期性注册时长配置（RMV-NGPRDREGTIMEDNN）_21742369.md`
- 原始手册：`evidence/UNC/20.15.2/增加基于DNN的周期性注册时长配置（ADD-NGPRDREGTIMEDNN）_21861953.md`
- 原始手册：`evidence/UNC/20.15.2/查询基于DNN的周期性注册时长配置（LST-NGPRDREGTIMEDNN）_75822976.md`
