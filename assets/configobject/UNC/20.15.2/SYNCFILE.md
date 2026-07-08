---
id: UNC@20.15.2@ConfigObject@SYNCFILE
type: ConfigObject
name: SYNCFILE（生成对账文件）
nf: UNC
version: 20.15.2
object_name: SYNCFILE
object_kind: action
status: active
---

# SYNCFILE（生成对账文件）

## 说明

![](生成对账文件(SAV SYNCFILE)_43159620.assets/notice_3.0-zh-cn_2.png)

该命令执行可能导致系统CPU和内存升高，如在话务高峰期需谨慎执行。

ACS服务将配置数据通过文件的方式同步给其他微服务，此文件称为对账文件或配置对账文件。

该命令默认功能，用于手动生成对账文件，确保生成最新的对账文件，提高对账效率；该命令导出控制选择YES，用于导出之前生成的对账文件支撑问题定位。

- 导出的对账文件可以下载到本地。在CSP界面选择“监控分析>运行日志>服务日志收集”，选择ACS服务进行收集。
- 导出的对账文件命名规则为：“pre_sync_config _<PID>_AP<PeerID>.zip”，其中PID和PeerID可以通过DSP NCCPEERLIST: DATATYPE=PEER, SERVICEINSTANCE="ACS";命令查询。
- 每次只允许导出一个对账文件，导出的对账文件老化时间是半小时。
- ACS重启后会主动清除导出的对账文件，避免文件残留。

## 操作本对象的命令

- [[command/UNC/20.15.2/SAV-SYNCFILE]] · SAV SYNCFILE

## 证据

- 原始手册：`evidence/UNC/20.15.2/生成对账文件(SAV-SYNCFILE)_43159620.md`
