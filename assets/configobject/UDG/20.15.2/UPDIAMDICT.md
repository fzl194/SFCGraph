---
id: UDG@20.15.2@ConfigObject@UPDIAMDICT
type: ConfigObject
name: UPDIAMDICT（Diameter字典）
nf: UDG
version: 20.15.2
object_name: UPDIAMDICT
object_kind: action
applicable_nf:
- UPF
status: active
---

# UPDIAMDICT（Diameter字典）

## 说明

**适用NF：UPF**

![](加载Diameter字典（LOD UPDIAMDICT）_97314553.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，加载Diameter字典可能会导致UPF各Diameter应用对外接口呈现的变化，此时一般需要对端网元做同步的升级适配，否则可能造成业务异常。

该命令用于加载Diameter字典文件。

## 操作本对象的命令

- [[command/UDG/20.15.2/LOD-UPDIAMDICT]] · LOD UPDIAMDICT

## 证据

- 原始手册：`evidence/UDG/20.15.2/UPDIAMDICT.md`
