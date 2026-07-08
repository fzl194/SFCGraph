---
id: UNC@20.15.2@ConfigObject@FEATUREDISABLE
type: ConfigObject
name: FEATUREDISABLE（特性下线）
nf: UNC
version: 20.15.2
object_name: FEATUREDISABLE
object_kind: action
status: active
---

# FEATUREDISABLE（特性下线）

## 说明

![](特性下线（OPR FEATUREDISABLE）_14567233.assets/notice_3.0-zh-cn_2.png)

若选择普通下线，内部流程异常时下线任务会失败；修复问题后可以重新下发下线任务。

若选择强制下线，内部流程异常时也会强制将Pod删除。强制下线是高危命令，仅允许在部分特定场景使用（如资源不够情况下的上线失败）。建议操作该动作时，寻求研发工程师支持（如分析是否造成其他数据残留等情况）。

该命令用于网元动态下线一系列特性。

## 操作本对象的命令

- [[command/UNC/20.15.2/OPR-FEATUREDISABLE]] · OPR FEATUREDISABLE

## 证据

- 原始手册：`evidence/UNC/20.15.2/特性下线（OPR-FEATUREDISABLE）_14567233.md`
