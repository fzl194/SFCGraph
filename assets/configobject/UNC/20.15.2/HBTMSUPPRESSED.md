---
id: UNC@20.15.2@ConfigObject@HBTMSUPPRESSED
type: ConfigObject
name: HBTMSUPPRESSED（NRF心跳超时抑制时长）
nf: UNC
version: 20.15.2
object_name: HBTMSUPPRESSED
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# HBTMSUPPRESSED（NRF心跳超时抑制时长）

## 说明

**适用NF：NRF**

该命令用于表示控制NRF心跳超时抑制时长，当NRF在备升主、NRF故障复位初期，双活断链恢复等场景下，为了防止NF还没完全接入新（恢复）NRF时，新（恢复）NRF可能短时间内根据心跳超时误判NF的状态，需要新（恢复）NRF增加一段时间做缓冲，在心跳超时抑制时长期间不启动心跳检测。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-HBTMSUPPRESSED]] · LST HBTMSUPPRESSED
- [[command/UNC/20.15.2/SET-HBTMSUPPRESSED]] · SET HBTMSUPPRESSED

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF心跳超时抑制时长（LST-HBTMSUPPRESSED）_86184259.md`
- 原始手册：`evidence/UNC/20.15.2/设置NRF心跳超时抑制时长（SET-HBTMSUPPRESSED）_86184326.md`
