---
id: UDG@20.15.2@ConfigObject@NPDIRECTCONNECTPORT
type: ConfigObject
name: NPDIRECTCONNECTPORT（多框级联配置）
nf: UDG
version: 20.15.2
object_name: NPDIRECTCONNECTPORT
object_kind: entity
status: active
---

# NPDIRECTCONNECTPORT（多框级联配置）

## 说明

![](增加多框级联配置（ADD NPDIRECTCONNECTPORT）_38407891.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，仅适用于NP多框场景或者NP单框改造成NP多框场景，错误配置可能会造成业务流量损失，请谨慎使用并联系华为技术支持协助操作。

该命令用于新增一条多框级联配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令仅适用于NP卡加速模式场景，并且该命令在非省交换场景下不能执行。
> - 该命令在NP卡名称（通过DSP NPNODE查询）为NP121时不生效。
> - 该命令不适用于单框场景。执行该命令后，对应的外联口会变成级联口，请谨慎使用。
> - 通过MOD INTERFACE命令操作级联口，可能导致ALM-139591683 接口状态down误告警，需要手动清除。
>
> - 最多可输入100条记录。

## 操作本对象的命令

- [ADD NPDIRECTCONNECTPORT](command/UDG/20.15.2/ADD-NPDIRECTCONNECTPORT.md)
- [LST NPDIRECTCONNECTPORT](command/UDG/20.15.2/LST-NPDIRECTCONNECTPORT.md)
- [RMV NPDIRECTCONNECTPORT](command/UDG/20.15.2/RMV-NPDIRECTCONNECTPORT.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除多框级联配置（RMV-NPDIRECTCONNECTPORT）_38525051.md`
- 原始手册：`evidence/UDG/20.15.2/增加多框级联配置（ADD-NPDIRECTCONNECTPORT）_38407891.md`
- 原始手册：`evidence/UDG/20.15.2/查询多框级联配置（LST-NPDIRECTCONNECTPORT）_91460428.md`
