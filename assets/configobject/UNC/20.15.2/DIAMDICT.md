---
id: UNC@20.15.2@ConfigObject@DIAMDICT
type: ConfigObject
name: DIAMDICT（Diameter字典）
nf: UNC
version: 20.15.2
object_name: DIAMDICT
object_kind: action
applicable_nf:
- PGW-C
- SMF
status: active
---

# DIAMDICT（Diameter字典）

## 说明

**适用NF：PGW-C、SMF**

![](加载Diameter字典（LOD DIAMDICT）_09897254.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，加载Diameter字典可能会导致UNC各Diameter应用对外接口呈现的变化，此时一般需要对端网元做同步的升级适配，否则可能造成业务异常。

该命令用于加载Diameter字典文件。

## 操作本对象的命令

- [[command/UNC/20.15.2/LOD-DIAMDICT]] · LOD DIAMDICT

## 证据

- 原始手册：`evidence/UNC/20.15.2/DIAMDICT.md`
