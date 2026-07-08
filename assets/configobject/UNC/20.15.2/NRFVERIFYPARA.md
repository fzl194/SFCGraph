---
id: UNC@20.15.2@ConfigObject@NRFVERIFYPARA
type: ConfigObject
name: NRFVERIFYPARA（NF属性冲突核验参数）
nf: UNC
version: 20.15.2
object_name: NRFVERIFYPARA
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFVERIFYPARA（NF属性冲突核验参数）

## 说明

**适用NF：NRF**

该命令用于设置NF属性冲突核验参数，可以通过OPR NRFNFATTRVRY命令启动某NF的属性冲突核验功能。当前支持以下两种核验行为：

- 本NRF管理的同类型NF间属性冲突交叉验证：针对选中的属性，NRF会核验当前NF的属性值，如果存在同类型的其他NF的属性值与当前NF属性值相同，而这些NF的实例标识中对应的大区及省份信息与当前NF不一致，则判断当前NF存在NF间属性冲突。
- NF属性与跨NRF寻址信息冲突交叉验证：针对选中的属性，NRF会核验当前NF的属性值，如果存在跨NRF寻址信息与当前NF属性值相同，则判断存在NF属性与跨NRF寻址信息冲突。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NRFVERIFYPARA]] · LST NRFVERIFYPARA
- [[command/UNC/20.15.2/SET-NRFVERIFYPARA]] · SET NRFVERIFYPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/NRFVERIFYPARA.md`
- 原始手册：`evidence/UNC/20.15.2/NRFVERIFYPARA.md`
