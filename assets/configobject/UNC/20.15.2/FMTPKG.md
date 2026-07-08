---
id: UNC@20.15.2@ConfigObject@FMTPKG
type: ConfigObject
name: FMTPKG（同步格式引擎包）
nf: UNC
version: 20.15.2
object_name: FMTPKG
object_kind: action
applicable_nf:
- NCG
status: active
---

# FMTPKG（同步格式引擎包）

## 说明

![](同步格式引擎包（SYN FMTPKG）_51174304.assets/notice_3.0-zh-cn_2.png)

此命令会覆盖目的地的文件，使用此命令正向同步时（即选择参数“REVSYN”为“NO”时），需要执行“RST VNFC”重启服务才能使格式引擎包生效。

**适用NF：NCG**

该命令用于从工作区目录获取格式引擎包或者向工作区目录同步格式引擎包。

## 操作本对象的命令

- [[command/UNC/20.15.2/SYN-FMTPKG]] · SYN FMTPKG

## 证据

- 原始手册：`evidence/UNC/20.15.2/同步格式引擎包（SYN-FMTPKG）_51174304.md`
