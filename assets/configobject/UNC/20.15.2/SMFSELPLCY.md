---
id: UNC@20.15.2@ConfigObject@SMFSELPLCY
type: ConfigObject
name: SMFSELPLCY（SMF选择策略）
nf: UNC
version: 20.15.2
object_name: SMFSELPLCY
object_kind: entity
applicable_nf:
- AMF
status: active
---

# SMFSELPLCY（SMF选择策略）

## 说明

![](增加SMF选择策略（ADD SMFSELPLCY）_09653765.assets/notice_3.0-zh-cn_2.png)

执行该命令配置用户范围会影响部分用户SMF选择策略，可能导致业务受损。特别注意：ISMFSW参数为“NO”，且TAISW参数为“NO”时，不会将UE当前所驻留的TAI作为目标SMF的选择条件。

**适用NF：AMF**

该命令用于对指定的用户（群）增加SMF的选择策略。通过本配置，AMF可以对不同用户（群）使用差异化的条件选择到不同的SMF，以满足运营商灵活部署网络的要求。

## 操作本对象的命令

- [ADD SMFSELPLCY](command/UNC/20.15.2/ADD-SMFSELPLCY.md)
- [LST SMFSELPLCY](command/UNC/20.15.2/LST-SMFSELPLCY.md)
- [MOD SMFSELPLCY](command/UNC/20.15.2/MOD-SMFSELPLCY.md)
- [RMV SMFSELPLCY](command/UNC/20.15.2/RMV-SMFSELPLCY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SMF选择策略（MOD-SMFSELPLCY）_09651762.md`
- 原始手册：`evidence/UNC/20.15.2/删除SMF选择策略（RMV-SMFSELPLCY）_09652104.md`
- 原始手册：`evidence/UNC/20.15.2/增加SMF选择策略（ADD-SMFSELPLCY）_09653765.md`
- 原始手册：`evidence/UNC/20.15.2/查询SMF选择策略（LST-SMFSELPLCY）_09653111.md`
