---
id: UNC@20.15.2@ConfigObject@UCFCONFIG
type: ConfigObject
name: UCFCONFIG（UCF文件管理规格配置）
nf: UNC
version: 20.15.2
object_name: UCFCONFIG
object_kind: global_setting
status: active
---

# UCFCONFIG（UCF文件管理规格配置）

## 说明

![](修改UCF文件管理规格配置（SET UCFCONFIG）_63673352.assets/notice_3.0-zh-cn_2.png)

使用该命令配置缓存文件存储空间时，请结合实际磁盘空间大小进行设置，或通过DSP UCFDISKSIZE命令进行查询，选取不大于输出结果中“UCF可用磁盘总空间(GB)”的最小值作为输入，超出默认大小值（20GB）存在风险，请谨慎修改。如果配置存储空间大小超过实际可用磁盘空间大小，可能会导致服务复位，无法正常运行。请谨慎使用并联系华为技术支持协助操作。

该命令用于修改使用TCP/SFTP/FTP协议时，UCF文件管理的规格配置。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-UCFCONFIG]] · LST UCFCONFIG
- [[command/UNC/20.15.2/SET-UCFCONFIG]] · SET UCFCONFIG

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改UCF文件管理规格配置（SET-UCFCONFIG）_63673352.md`
- 原始手册：`evidence/UNC/20.15.2/查询UCF文件管理规格配置（LST-UCFCONFIG）_63673349.md`
