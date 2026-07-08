---
id: UNC@20.15.2@ConfigObject@IMSIBINDDEDSMF
type: ConfigObject
name: IMSIBINDDEDSMF（拨测用户和专网SMF的绑定关系）
nf: UNC
version: 20.15.2
object_name: IMSIBINDDEDSMF
object_kind: binding
applicable_nf:
- SMF
- PGW-C
status: active
---

# IMSIBINDDEDSMF（拨测用户和专网SMF的绑定关系）

## 说明

**适用NF：SMF、PGW-C**

该命令用于配置用户和专网SMF的绑定关系。

在多DNN分流场景下新规划单独的专网SMF时，可以通过本命令将拨测用户的IMSI、专用DNN信息和专网SMF绑定，让指定的拨测用户激活到专网SMF，实现对新规划的专网SMF进行测试。

## 操作本对象的命令

- [ADD IMSIBINDDEDSMF](command/UNC/20.15.2/ADD-IMSIBINDDEDSMF.md)
- [LST IMSIBINDDEDSMF](command/UNC/20.15.2/LST-IMSIBINDDEDSMF.md)
- [MOD IMSIBINDDEDSMF](command/UNC/20.15.2/MOD-IMSIBINDDEDSMF.md)
- [RMV IMSIBINDDEDSMF](command/UNC/20.15.2/RMV-IMSIBINDDEDSMF.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改拨测用户和专网SMF的绑定关系（MOD-IMSIBINDDEDSMF）_25477038.md`
- 原始手册：`evidence/UNC/20.15.2/删除拨测用户和专网SMF的绑定关系（RMV-IMSIBINDDEDSMF）_25796922.md`
- 原始手册：`evidence/UNC/20.15.2/增加拨测用户和专网SMF的绑定关系（ADD-IMSIBINDDEDSMF）_25317226.md`
- 原始手册：`evidence/UNC/20.15.2/查询拨测用户和专网SMF的绑定关系（LST-IMSIBINDDEDSMF）_74276777.md`
