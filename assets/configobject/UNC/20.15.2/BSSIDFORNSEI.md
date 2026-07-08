---
id: UNC@20.15.2@ConfigObject@BSSIDFORNSEI
type: ConfigObject
name: BSSIDFORNSEI（NSEI和BSSID值的对应关系）
nf: UNC
version: 20.15.2
object_name: BSSIDFORNSEI
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# BSSIDFORNSEI（NSEI和BSSID值的对应关系）

## 说明

**适用网元：SGSN**

此命令用于增加一个或一组NSEI和BSSID值的对应关系来指定BSSID的值。只适用于Gb over IP自动配置的场景。

如果自动上报的NSE在本命令中NSE的范围内不能查找到，该NSE对应BSSID的值则参照 [**LST BSSGP**](../../BSSGP参数/查询BSSGP参数(LST BSSGP)_26145988.md) 命令中的 “BSSID与NSEI的对应关系” 来指定。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-BSSIDFORNSEI]] · ADD BSSIDFORNSEI
- [[command/UNC/20.15.2/LST-BSSIDFORNSEI]] · LST BSSIDFORNSEI
- [[command/UNC/20.15.2/MOD-BSSIDFORNSEI]] · MOD BSSIDFORNSEI
- [[command/UNC/20.15.2/RMV-BSSIDFORNSEI]] · RMV BSSIDFORNSEI

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NSEI和BSSID值的对应关系(MOD-BSSIDFORNSEI)_72225675.md`
- 原始手册：`evidence/UNC/20.15.2/删除NSEI和BSSID值的对应关系(RMV-BSSIDFORNSEI)_26145996.md`
- 原始手册：`evidence/UNC/20.15.2/增加NSEI和BSSID值的对应关系(ADD-BSSIDFORNSEI)_72345595.md`
- 原始手册：`evidence/UNC/20.15.2/查询NSEI和BSSID值的对应关系(LST-BSSIDFORNSEI)_26305806.md`
