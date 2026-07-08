---
id: UNC@20.15.2@ConfigObject@S1UBLACKLST
type: ConfigObject
name: S1UBLACKLST（S1-U IP地址黑名单记录）
nf: UNC
version: 20.15.2
object_name: S1UBLACKLST
object_kind: entity
applicable_nf:
- MME
status: active
---

# S1UBLACKLST（S1-U IP地址黑名单记录）

## 说明

**适用网元：MME**

暂不支持本命令。该命令用于增加S1-U IP地址黑名单记录。当 **[SET S1UBLACKLSTPARA](../S1-U黑名单规则/设置S1-U黑名单参数(SET S1UBLACKLSTPARA)_89145434.md)** 中 **SNDBLKLSTPLCY** 配置为NO时，如果系统在流程中接收到S-GW发送的消息中携带的S1-U IP地址为该命令中配置的IP地址时，确保系统不向eNodeB发送携带该IP地址消息。

## 操作本对象的命令

- [ADD S1UBLACKLST](command/UNC/20.15.2/ADD-S1UBLACKLST.md)
- [LST S1UBLACKLST](command/UNC/20.15.2/LST-S1UBLACKLST.md)
- [RMV S1UBLACKLST](command/UNC/20.15.2/RMV-S1UBLACKLST.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除S1-U-IP地址黑名单记录(RMV-S1UBLACKLST)_24389181.md`
- 原始手册：`evidence/UNC/20.15.2/增加S1-U-IP地址黑名单记录(ADD-S1UBLACKLST)_24385877.md`
- 原始手册：`evidence/UNC/20.15.2/查询S1-U-IP地址黑名单记录(LST-S1UBLACKLST)_89144234.md`
