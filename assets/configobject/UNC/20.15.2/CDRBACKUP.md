---
id: UNC@20.15.2@ConfigObject@CDRBACKUP
type: ConfigObject
name: CDRBACKUP（上传SFTP密钥文件到第三方服务器）
nf: UNC
version: 20.15.2
object_name: CDRBACKUP
object_kind: entity
applicable_nf:
- NCG
status: active
---

# CDRBACKUP（上传SFTP密钥文件到第三方服务器）

## 说明

**适用NF：NCG**

该命令用于将CG上的原始话单、第一份最终话单或第二份最终话单备份到第三方服务器或本地磁盘上实现数据可靠性备份。从而提高数据的安全性。目前的备份方案有：

- 将话单实时备份到第三方服务器。
- 将历史话单一次性备份到第三方服务器（建议该任务的第三方服务器与已有的实时备份任务的第三方服务器保持一致）。
- 将话单实时备份到本地磁盘上。

仅某些局点有特殊要求，才配置话单备份任务。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CDRBACKUP]] · ADD CDRBACKUP
- [[command/UNC/20.15.2/DSP-CDRBACKUP]] · DSP CDRBACKUP
- [[command/UNC/20.15.2/LST-CDRBACKUP]] · LST CDRBACKUP
- [[command/UNC/20.15.2/MOD-CDRBACKUP]] · MOD CDRBACKUP
- [[command/UNC/20.15.2/RMV-CDRBACKUP]] · RMV CDRBACKUP
- [[command/UNC/20.15.2/UPL-CDRBACKUP]] · UPL CDRBACKUP

## 证据

- 原始手册：`evidence/UNC/20.15.2/上传SFTP密钥文件到第三方服务器（UPL-CDRBACKUP）_51174249.md`
- 原始手册：`evidence/UNC/20.15.2/修改话单备份（MOD-CDRBACKUP）_51174246.md`
- 原始手册：`evidence/UNC/20.15.2/删除话单备份（RMV-CDRBACKUP）_51174245.md`
- 原始手册：`evidence/UNC/20.15.2/增加话单备份（ADD-CDRBACKUP）_51174244.md`
- 原始手册：`evidence/UNC/20.15.2/显示备份任务状态（DSP-CDRBACKUP）_51174248.md`
- 原始手册：`evidence/UNC/20.15.2/查询话单备份（LST-CDRBACKUP）_51174247.md`
