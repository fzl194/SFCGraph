---
id: UNC@20.15.2@ConfigObject@NGTALISTPAGINGCFG
type: ConfigObject
name: NGTALISTPAGINGCFG（N2模式TALIST寻呼不重发TAC区间）
nf: UNC
version: 20.15.2
object_name: NGTALISTPAGINGCFG
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGTALISTPAGINGCFG（N2模式TALIST寻呼不重发TAC区间）

## 说明

**适用NF：AMF**

该命令用于设置N2模式TALIST寻呼不重发的TAC区间。

通过观察1929450177 指定TAI组的N2模式寻呼请求次数，1929450178 指定TAI组的N2模式一次寻呼响应次数，1929450179 指定TAI组的N2模式二次寻呼响应次数等话统指标，识别部分TAC下的gNodeB寻呼可能过载，则使用本命令配置TAC区间。当用户所在TALIST包含的任一TAC在本命令配置范围内时，该用户基于TALIST的下行寻呼不进行重发处理。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NGTALISTPAGINGCFG]] · ADD NGTALISTPAGINGCFG
- [[command/UNC/20.15.2/LST-NGTALISTPAGINGCFG]] · LST NGTALISTPAGINGCFG
- [[command/UNC/20.15.2/MOD-NGTALISTPAGINGCFG]] · MOD NGTALISTPAGINGCFG
- [[command/UNC/20.15.2/RMV-NGTALISTPAGINGCFG]] · RMV NGTALISTPAGINGCFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/NGTALISTPAGINGCFG.md`
- 原始手册：`evidence/UNC/20.15.2/NGTALISTPAGINGCFG.md`
- 原始手册：`evidence/UNC/20.15.2/NGTALISTPAGINGCFG.md`
- 原始手册：`evidence/UNC/20.15.2/NGTALISTPAGINGCFG.md`
