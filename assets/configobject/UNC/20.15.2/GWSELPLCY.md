---
id: UNC@20.15.2@ConfigObject@GWSELPLCY
type: ConfigObject
name: GWSELPLCY（GGSN/P-GW选择策略）
nf: UNC
version: 20.15.2
object_name: GWSELPLCY
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# GWSELPLCY（GGSN/P-GW选择策略）

## 说明

![](增加GGSN_P-GW选择策略（ADD GWSELPLCY）_26145944.assets/notice_3.0-zh-cn_2.png)

- 参数“起始IMSI”和“终止IMSI”: 为防止误操作，请务必确保起始IMSI和终止IMSI范围合理有效。
- 参数“运营商标识”：请务必确保本网和外网用户策略控制合理。
- 参数“IMSI前缀”：为防止误操作，请务必确保IMSI前缀的取值合理有效。

**适用网元：SGSN、MME**

该命令用于增加GGSN/P-GW选择策略，即为不同范围的用户配置不同的GGSN/P-GW选择方法和机制，以满足运营商对不同用户选择不同GGSN/P-GW，灵活部署网络的需求。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GWSELPLCY]] · ADD GWSELPLCY
- [[command/UNC/20.15.2/LST-GWSELPLCY]] · LST GWSELPLCY
- [[command/UNC/20.15.2/MOD-GWSELPLCY]] · MOD GWSELPLCY
- [[command/UNC/20.15.2/RMV-GWSELPLCY]] · RMV GWSELPLCY

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GGSN_P-GW选择策略（MOD-GWSELPLCY）_26305754.md`
- 原始手册：`evidence/UNC/20.15.2/删除GGSN_P-GW选择策略（RMV-GWSELPLCY）_72225623.md`
- 原始手册：`evidence/UNC/20.15.2/增加GGSN_P-GW选择策略（ADD-GWSELPLCY）_26145944.md`
- 原始手册：`evidence/UNC/20.15.2/查询GGSN_P-GW选择策略（LST-GWSELPLCY）_72345545.md`
