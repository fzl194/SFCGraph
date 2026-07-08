---
id: UNC@20.15.2@ConfigObject@UPGTSK
type: ConfigObject
name: UPGTSK（升级/补丁任务）
nf: UNC
version: 20.15.2
object_name: UPGTSK
object_kind: action
status: active
---

# UPGTSK（升级/补丁任务）

## 说明

![](停止升级_补丁任务(STP UPGTSK)_29989793.assets/notice_3.0-zh-cn_2.png)

- “快速失败”参数为空时，执行该命令会中止当前正在正常执行的升级/补丁任务，并重启后台升级工具服务，请谨慎操作。
- “快速失败”参数非空时，执行该命令会打开/关闭原子快速失败能力。
- 该命令会中止当前正在执行的升级/补丁任务，升级工具服务会重启（快速失败参数取值为ON/OFF时不会重启），请谨慎操作。
- 升级/补丁过程中执行mml命令时，若mml命令执行依赖的微服务状态异常、节点复位等阶段可能会导致命令不生效或者失败，执行命令时请尽量避开这些阶段。

- “快速失败”参数为空时，该命令用于停止正在执行的升级/补丁任务，并且在升级界面弹窗提示，用户可在界面上根据提示选择“继续”或“回退”。
- “快速失败”参数非空时，该命令仅用于打开/关闭原子快速失败能力。

## 操作本对象的命令

- [[command/UNC/20.15.2/STP-UPGTSK]] · STP UPGTSK

## 证据

- 原始手册：`evidence/UNC/20.15.2/UPGTSK.md`
