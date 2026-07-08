---
id: UNC@20.15.2@ConfigObject@IULOAD
type: ConfigObject
name: IULOAD（用户Iu连接负荷状态）
nf: UNC
version: 20.15.2
object_name: IULOAD
object_kind: global_setting
applicable_nf:
- SGSN
status: active
---

# IULOAD（用户Iu连接负荷状态）

## 说明

![](设置SGP负荷配置(SET IULOAD)_26305846.assets/notice_3.0-zh-cn_2.png)

如果未立即复位SGP，在后续的系统运行中如果发生部分SGP的复位，将会导致系统内的Iu接口负荷分担错误，导致负荷不均用户无法接入。

**适用网元：SGSN**

该命令用于设置Iu接口负荷在SGP进程间分担的控制参数。

## 操作本对象的命令

- [DSP IULOAD](command/UNC/20.15.2/DSP-IULOAD.md)
- [LST IULOAD](command/UNC/20.15.2/LST-IULOAD.md)
- [SET IULOAD](command/UNC/20.15.2/SET-IULOAD.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示用户Iu连接负荷状态(DSP-IULOAD)_26146038.md`
- 原始手册：`evidence/UNC/20.15.2/查询SGP负荷配置(LST-IULOAD)_72345637.md`
- 原始手册：`evidence/UNC/20.15.2/设置SGP负荷配置(SET-IULOAD)_26305846.md`
