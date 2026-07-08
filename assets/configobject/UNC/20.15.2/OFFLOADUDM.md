---
id: UNC@20.15.2@ConfigObject@OFFLOADUDM
type: ConfigObject
name: OFFLOADUDM（UDM注册上下文的迁移）
nf: UNC
version: 20.15.2
object_name: OFFLOADUDM
object_kind: action
applicable_nf:
- AMF
- SMF
status: active
---

# OFFLOADUDM（UDM注册上下文的迁移）

## 说明

![](启动UDM注册上下文的迁移（STR OFFLOADUDM）_96243244.assets/notice_3.0-zh-cn_2.png)

执行该命令，如果参数设置不合理可能影响UDM间的用户数不均衡。

**适用NF：AMF、SMF**

该命令用于触发AMF或SMF在UDM的注册上下文的迁移流程，比如在特定的UDM发生故障或升级等场景下，AMF或SMF通过本命令触发将原本注册在该UDM上的上下文迁移到其它UDM。

## 操作本对象的命令

- [STR OFFLOADUDM](command/UNC/20.15.2/STR-OFFLOADUDM.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动UDM注册上下文的迁移（STR-OFFLOADUDM）_96243244.md`
