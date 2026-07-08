---
id: UDG@20.15.2@ConfigObject@OSCONFIG
type: ConfigObject
name: OSCONFIG（OS配置）
nf: UDG
version: 20.15.2
object_name: OSCONFIG
object_kind: global_setting
status: active
---

# OSCONFIG（OS配置）

## 说明

![](设置OS配置 (SET OSCONFIG)_23147326.assets/notice_3.0-zh-cn.png)

该命令为高危命令，此命令将修改节点配置，会造成部分业务暂时不可用，请务必在华为技术支持人员的指导下使用该命令。

如果执行该命令，当命令的 “操作类型” 选择 “MULTICAST（组播）” 时，节点会在OS启动30分钟内自动同步网卡组播开关配置。

如果执行该命令，当命令的 “操作类型” 选择 “MEMSWAP（内存压缩）” 时，节点会在OS启动5分钟内自动同步内存压缩开关配置，并需要等待一段时间才能完成内存压缩。多次打开内存压缩开关，由于内存压缩率不同，内存使用存在少量波动。

如果执行该命令，当命令的 “操作类型” 选择 “DHEALGORITHM（DHE算法）” 时，节点会在OS启动10分钟内自动同步DHE密钥长度配置。

该命令用于设置OS配置。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

> **说明**
> 环境处于升级、回退、补丁、观察期或备份状态，禁止执行该命令。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-OSCONFIG]] · DSP OSCONFIG
- [[command/UDG/20.15.2/SET-OSCONFIG]] · SET OSCONFIG

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OS配置-(DSP-OSCONFIG)_71313093.md`
- 原始手册：`evidence/UDG/20.15.2/设置OS配置-(SET-OSCONFIG)_23147326.md`
