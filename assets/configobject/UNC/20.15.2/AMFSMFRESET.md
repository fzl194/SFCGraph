---
id: UNC@20.15.2@ConfigObject@AMFSMFRESET
type: ConfigObject
name: AMFSMFRESET（AMF的SMF故障处理策略）
nf: UNC
version: 20.15.2
object_name: AMFSMFRESET
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# AMFSMFRESET（AMF的SMF故障处理策略）

## 说明

![](设置AMF的SMF故障处理策略（SET AMFSMFRESET）_96805502.assets/notice_3.0-zh-cn_2.png)

执行该命令，如果RATE，INTERVAL，SCANNUM速率设置不合理可能对系统性能造成影响。

**适用NF：AMF**

该命令用于设置AMF的SMF故障处理策略，支持扫描任务或数据业务请求两种语音业务恢复方式，可同时开启或单独开启。

## 操作本对象的命令

- [LST AMFSMFRESET](command/UNC/20.15.2/LST-AMFSMFRESET.md)
- [SET AMFSMFRESET](command/UNC/20.15.2/SET-AMFSMFRESET.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF的SMF故障处理策略（LST-AMFSMFRESET）_96805381.md`
- 原始手册：`evidence/UNC/20.15.2/设置AMF的SMF故障处理策略（SET-AMFSMFRESET）_96805502.md`
