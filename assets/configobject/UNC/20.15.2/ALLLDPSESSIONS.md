---
id: UNC@20.15.2@ConfigObject@ALLLDPSESSIONS
type: ConfigObject
name: ALLLDPSESSIONS（重启所有LDP会话）
nf: UNC
version: 20.15.2
object_name: ALLLDPSESSIONS
object_kind: action
status: active
---

# ALLLDPSESSIONS（重启所有LDP会话）

## 说明

该命令用于重启所有的LDP会话。当进行了新的LDP配置时，可以执行此命令使新的配置生效。

![](重启所有LDP会话（RBL ALLLDPSESSIONS）_00601097.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，该操作会导致所有邻居断连。如果不是优雅重启，业务流量会中断。

## 操作本对象的命令

- [[command/UNC/20.15.2/RBL-ALLLDPSESSIONS]] · RBL ALLLDPSESSIONS

## 证据

- 原始手册：`evidence/UNC/20.15.2/重启所有LDP会话（RBL-ALLLDPSESSIONS）_00601097.md`
