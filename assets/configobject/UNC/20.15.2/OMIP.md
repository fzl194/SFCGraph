---
id: UNC@20.15.2@ConfigObject@OMIP
type: ConfigObject
name: OMIP（OM IP）
nf: UNC
version: 20.15.2
object_name: OMIP
object_kind: global_setting
status: active
---

# OMIP（OM IP）

## 说明

![](设置OM IP (SET OMIP)_76163350.assets/notice_3.0-zh-cn_2.png)

该类命令执行之后 **可能会导致OM Portal断链** 、网管断链以及VNFM断链，需使用修改后IP重新登录OM Portal，并重新对接网管以及修改VNFM侧对应网元的IP。该命令若执行不当， **会导致所有业务中断** 。

用于修改系统OM网络配置参数，包括外部浮动IP地址、外部物理IP、子网掩码（IPV4场景）/前缀长度（IPV6场景）、默认网关。

## 操作本对象的命令

- [LST OMIP](command/UNC/20.15.2/LST-OMIP.md)
- [SET OMIP](command/UNC/20.15.2/SET-OMIP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询OM-IP-(LST-OMIP)_76163349.md`
- 原始手册：`evidence/UNC/20.15.2/设置OM-IP-(SET-OMIP)_76163350.md`
