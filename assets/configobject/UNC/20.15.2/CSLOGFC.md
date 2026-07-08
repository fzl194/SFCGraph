---
id: UNC@20.15.2@ConfigObject@CSLOGFC
type: ConfigObject
name: CSLOGFC（日志流控开关）
nf: UNC
version: 20.15.2
object_name: CSLOGFC
object_kind: global_setting
status: active
---

# CSLOGFC（日志流控开关）

## 说明

![](设置日志流控开关（SET CSLOGFC）_09587953.assets/notice_3.0-zh-cn_2.png)

当日志级别为ERR以下时，关闭日志流控，会造成CPU升高，可能触发进程复位，导致业务呼损等严重后果，不建议操作。

此命令用于设置日志流控开关。

日志流控是指同一文件同一行的日志在1分钟之内打印数量不能超过10条，超过10条将进行流控，同一文件同一行的日志不进行打印。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-CSLOGFC]] · LST CSLOGFC
- [[command/UNC/20.15.2/SET-CSLOGFC]] · SET CSLOGFC

## 证据

- 原始手册：`evidence/UNC/20.15.2/CSLOGFC.md`
- 原始手册：`evidence/UNC/20.15.2/CSLOGFC.md`
