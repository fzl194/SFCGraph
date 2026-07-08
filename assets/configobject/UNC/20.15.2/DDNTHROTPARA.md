---
id: UNC@20.15.2@ConfigObject@DDNTHROTPARA
type: ConfigObject
name: DDNTHROTPARA（DDN信令抑制状态）
nf: UNC
version: 20.15.2
object_name: DDNTHROTPARA
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# DDNTHROTPARA（DDN信令抑制状态）

## 说明

![](设置DDN信令抑制参数(SET DDNTHROTPARA)_26305980.assets/notice_3.0-zh-cn_2.png)

请仔细阅读本命令的注意事项，确保开启本功能对网络中的S-GW不造成预期外的影响。

**适用网元：MME**

该命令用于设置MME上DDN信令抑制（DDN Throttling）的功能开关，以及MME生成DDN信令抑制策略的控制参数。打开DDN信令抑制功能开关后，如果MME由于收到大量DDN（Downlink Data Notification）消息导致过载，那么MME将在返回给S-GW的DDN Ack消息中携带Throttling信元。S-GW根据Throttling信元的指示，丢弃一部分低优先级的DDN信令，从而缓和MME的过载状况。 Throttling信元包含了抑制策略，抑制策略是由MME根据自身的过载状况制定的，其中包括了抑制比例（Throttling Factor）和抑制时长（Throttling Delay）两个关键信息。抑制比例指示S-GW丢弃DDN数量占所有低优先级的DDN信令数量的比值；抑制时长指示S-GW丢弃低优先级DDN的持续时间。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-DDNTHROTPARA]] · DSP DDNTHROTPARA
- [[command/UNC/20.15.2/LST-DDNTHROTPARA]] · LST DDNTHROTPARA
- [[command/UNC/20.15.2/SET-DDNTHROTPARA]] · SET DDNTHROTPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示DDN信令抑制状态(DSP-DDNTHROTPARA)_26146172.md`
- 原始手册：`evidence/UNC/20.15.2/查询DDN信令抑制参数(LST-DDNTHROTPARA)_72345771.md`
- 原始手册：`evidence/UNC/20.15.2/设置DDN信令抑制参数(SET-DDNTHROTPARA)_26305980.md`
