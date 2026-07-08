---
id: UDG@20.15.2@ConfigObject@COLOCATEDLBO
type: ConfigObject
name: COLOCATEDLBO（本地分流共部署参数）
nf: UDG
version: 20.15.2
object_name: COLOCATEDLBO
object_kind: global_setting
applicable_nf:
- UPF
status: active
---

# COLOCATEDLBO（本地分流共部署参数）

## 说明

**适用NF：UPF**

![](设置本地分流共部署参数（SET COLOCATEDLBO）_25895976.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，关闭ULCL分流功能ULCL分流会话会创建失败，业务不通。开启ULCL分流功能会导致设备性能下降。

该命令用于设置ULCL UPF和PSA UPF共部署的本地分流参数。此处PSA UPF可以是主锚点或辅锚点。

## 操作本对象的命令

- [LST COLOCATEDLBO](command/UDG/20.15.2/LST-COLOCATEDLBO.md)
- [SET COLOCATEDLBO](command/UDG/20.15.2/SET-COLOCATEDLBO.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示本地分流共部署参数（LST-COLOCATEDLBO）_25895977.md`
- 原始手册：`evidence/UDG/20.15.2/设置本地分流共部署参数（SET-COLOCATEDLBO）_25895976.md`
