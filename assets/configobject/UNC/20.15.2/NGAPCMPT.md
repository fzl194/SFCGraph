---
id: UNC@20.15.2@ConfigObject@NGAPCMPT
type: ConfigObject
name: NGAPCMPT（NGAP兼容性参数）
nf: UNC
version: 20.15.2
object_name: NGAPCMPT
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# NGAPCMPT（NGAP兼容性参数）

## 说明

![](设置NGAP兼容性参数（SET NGAPCMPT）_09652644.assets/notice_3.0-zh-cn_2.png)

执行该命令，如果对端的网元不支持兼容性参数MSKIMEISV，REDFORVOEPSFB，可能导致用户接入失败。

**适用NF：AMF**

该命令用于为NGAP（NG Application Protocol）设置兼容性控制参数。NGAP是AMF与NG-RAN之间的应用协议，通过本命令可以控制AMF是否在该协议层的下行消息中携带指定的可选信元。

## 操作本对象的命令

- [LST NGAPCMPT](command/UNC/20.15.2/LST-NGAPCMPT.md)
- [SET NGAPCMPT](command/UNC/20.15.2/SET-NGAPCMPT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NGAP兼容性参数（LST-NGAPCMPT）_09653275.md`
- 原始手册：`evidence/UNC/20.15.2/设置NGAP兼容性参数（SET-NGAPCMPT）_09652644.md`
