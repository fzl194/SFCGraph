---
id: UNC@20.15.2@ConfigObject@IU
type: ConfigObject
name: IU（复位Iu接口）
nf: UNC
version: 20.15.2
object_name: IU
object_kind: action
applicable_nf:
- SGSN
status: active
---

# IU（复位Iu接口）

## 说明

![](复位Iu接口(RST IU)_26305848.assets/notice_3.0-zh-cn_2.png)

该命令会导致SGSN与相关RNC之间的业务中断，需慎重使用。

**适用网元：SGSN**

该命令用于对SGSN与指定RNC之间的Iu接口进行软件复位，复位将导致此Iu接口上所有已激活会话的丢失和Iu连接的释放。通常，SGSN在发生错误的情况下，会自动发送reset消息，如果怀疑SGP进程上的连接资源和SPP进程或RNC的连接资源相差太大的时候，才需要进行手工Iu接口复位。

## 操作本对象的命令

- [[command/UNC/20.15.2/RST-IU]] · RST IU

## 证据

- 原始手册：`evidence/UNC/20.15.2/复位Iu接口(RST-IU)_26305848.md`
