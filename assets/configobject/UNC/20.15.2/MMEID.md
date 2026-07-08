---
id: UNC@20.15.2@ConfigObject@MMEID
type: ConfigObject
name: MMEID（MMEID配置）
nf: UNC
version: 20.15.2
object_name: MMEID
object_kind: entity
applicable_nf:
- MME
status: active
---

# MMEID（MMEID配置）

## 说明

![](增加MMEID配置(ADD MMEID)_26146088.assets/notice_3.0-zh-cn_2.png)

可能会造成IntraTAU成功率指标大幅下降。

**适用网元：MME**

此命令用于在MMEID表中增加一条记录，该记录在PLMN中唯一标识一个MME。在MME给用户分配GUTI时，系统会根据本命令中输入的 “MME编码（起始值）” 来生成GUTI。用户附着时，系统会将GUTI中的MCC、MNC、MMEGI及MMEC信息与MMEID中的信息比对，若不同则认为是Inter附着。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-MMEID]] · ADD MMEID
- [[command/UNC/20.15.2/LST-MMEID]] · LST MMEID
- [[command/UNC/20.15.2/MOD-MMEID]] · MOD MMEID
- [[command/UNC/20.15.2/RMV-MMEID]] · RMV MMEID

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改MMEID配置(MOD-MMEID)_26305898.md`
- 原始手册：`evidence/UNC/20.15.2/删除MMEID配置(RMV-MMEID)_72225767.md`
- 原始手册：`evidence/UNC/20.15.2/增加MMEID配置(ADD-MMEID)_26146088.md`
- 原始手册：`evidence/UNC/20.15.2/查询MMEID配置(LST-MMEID)_72345689.md`
