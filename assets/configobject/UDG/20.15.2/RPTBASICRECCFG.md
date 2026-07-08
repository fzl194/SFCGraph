---
id: UDG@20.15.2@ConfigObject@RPTBASICRECCFG
type: ConfigObject
name: RPTBASICRECCFG（基础单据上报功能开关）
nf: UDG
version: 20.15.2
object_name: RPTBASICRECCFG
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# RPTBASICRECCFG（基础单据上报功能开关）

## 说明

**适用NF：PGW-U、UPF**

![](设置基础单据上报配置开关（SET RPTBASICRECCFG）_46919341.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令会导致用户匹配数发生变化，可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

该命令用于配置基础单据上报功能开关，包括用户信息开关、用户统计开关、APP统计开关和资源开关。当运营商部署业务报表业务时使用该命令。

## 操作本对象的命令

- [LST RPTBASICRECCFG](command/UDG/20.15.2/LST-RPTBASICRECCFG.md)
- [SET RPTBASICRECCFG](command/UDG/20.15.2/SET-RPTBASICRECCFG.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示基础单据上报功能开关（LST-RPTBASICRECCFG）_61159772.md`
- 原始手册：`evidence/UDG/20.15.2/设置基础单据上报配置开关（SET-RPTBASICRECCFG）_46919341.md`
