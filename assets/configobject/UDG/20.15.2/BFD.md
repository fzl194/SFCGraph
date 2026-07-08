---
id: UDG@20.15.2@ConfigObject@BFD
type: ConfigObject
name: BFD（BFD全局配置信息）
nf: UDG
version: 20.15.2
object_name: BFD
object_kind: global_setting
status: active
---

# BFD（BFD全局配置信息）

## 说明

![](设置BFD全局属性（SET BFD）_00840937.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会去使能BFD，导致BFD功能不可用，并且所有历史BFD配置全部删除，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置BFD全局属性。为了减小设备故障对业务的影响，提高网络的可靠性，网络设备需要能够尽快检测到与相邻设备间的通信故障，以便及时采取措施，保证业务继续进行。

## 操作本对象的命令

- [LST BFD](command/UDG/20.15.2/LST-BFD.md)
- [SET BFD](command/UDG/20.15.2/SET-BFD.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询BFD全局配置信息（LST-BFD）_00601193.md`
- 原始手册：`evidence/UDG/20.15.2/设置BFD全局属性（SET-BFD）_00840937.md`
