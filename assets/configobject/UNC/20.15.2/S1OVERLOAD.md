---
id: UNC@20.15.2@ConfigObject@S1OVERLOAD
type: ConfigObject
name: S1OVERLOAD（S1接口过载控制）
nf: UNC
version: 20.15.2
object_name: S1OVERLOAD
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# S1OVERLOAD（S1接口过载控制）

## 说明

**适用网元：MME**

此命令用于设置S1过载控制信息，参见 3GPP TS 36.413协议。

当MME过载时可以通过本命令配置各过载级别的控制策略，向eNodeB发送Overload Start消息，通知eNodeB拒绝UE新建连接，从而减少对网络的信令冲击。当MME从过载状态恢复到正常状态后向eNodeB发送Overload Stop消息，通知eNodeB允许UE接入，继续为UE提供服务。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-S1OVERLOAD]] · LST S1OVERLOAD
- [[command/UNC/20.15.2/SET-S1OVERLOAD]] · SET S1OVERLOAD
- [[command/UNC/20.15.2/STP-S1OVERLOAD]] · STP S1OVERLOAD
- [[command/UNC/20.15.2/STR-S1OVERLOAD]] · STR S1OVERLOAD

## 证据

- 原始手册：`evidence/UNC/20.15.2/停止S1接口过载控制(STP-S1OVERLOAD)_26306062.md`
- 原始手册：`evidence/UNC/20.15.2/启动S1接口过载控制(STR-S1OVERLOAD)_72225929.md`
- 原始手册：`evidence/UNC/20.15.2/查询S1过载控制信息(LST-S1OVERLOAD)_26146250.md`
- 原始手册：`evidence/UNC/20.15.2/设置S1过载控制信息(SET-S1OVERLOAD)_72345849.md`
