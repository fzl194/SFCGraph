---
id: UNC@20.15.2@ConfigObject@VPROBECONFIG
type: ConfigObject
name: VPROBECONFIG（vProbe文件管理规格配置）
nf: UNC
version: 20.15.2
object_name: VPROBECONFIG
object_kind: global_setting
status: active
---

# VPROBECONFIG（vProbe文件管理规格配置）

## 说明

![](设置vProbe文件管理规格配置（SET VPROBECONFIG）_39242825.assets/notice_3.0-zh-cn_2.png)

使用该命令配置缓存文件存储空间时，请结合实际磁盘空间大小进行设置，或通过DSP VPROBEDISKSIZE命令进行查询，选取不大于输出结果中“vProbe可用磁盘总空间(GB)”的最小值作为输入，超出默认大小值（20GB）存在风险，请谨慎修改。如果配置存储空间大小超过实际可用磁盘空间大小，可能会导致服务复位，无法正常运行。请谨慎使用并联系华为技术支持协助操作。

该命令用于设置使用TCP/SFTP协议时vProbe的文件管理规格配置。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-VPROBECONFIG]] · LST VPROBECONFIG
- [[command/UNC/20.15.2/SET-VPROBECONFIG]] · SET VPROBECONFIG

## 证据

- 原始手册：`evidence/UNC/20.15.2/VPROBECONFIG.md`
- 原始手册：`evidence/UNC/20.15.2/VPROBECONFIG.md`
