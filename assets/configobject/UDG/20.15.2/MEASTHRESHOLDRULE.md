---
id: UDG@20.15.2@ConfigObject@MEASTHRESHOLDRULE
type: ConfigObject
name: MEASTHRESHOLDRULE（话统阈值规则）
nf: UDG
version: 20.15.2
object_name: MEASTHRESHOLDRULE
object_kind: entity
status: active
---

# MEASTHRESHOLDRULE（话统阈值规则）

## 说明

该命令用于添加话统阈值规则，且支持配置导出。

> **说明**
> 1. 当“对象实例ID”和“测量指标ID”不存在相应周期的实时监控任务时，操作成功后会返回“ 操作成功，监控任务未开启 ”。
> 2. 整系统最多支持配置1000条话统阈值规则。
> 3. 至少需要填写一组告警阈值和告警偏移信息。
> 4. 当网元类型变更时，会清除当前未激活的“测量指标ID”对应的话统阈值规则。
> 5. 满足阈值规则条件会上报“ALM-136802 实时统计紧急阈值超限”、“ALM-136803 实时统计重要阈值超限”、“ALM-136804 实时统计次要阈值超限”或“ALM-136805 实时统计提示阈值超限”告警。
> 6. 英文环境设置阈值规则名称为中文时，在网管上显示的对应告警会出现乱码，在OM Portal界面显示正常。

## 操作本对象的命令

- [ADD MEASTHRESHOLDRULE](command/UDG/20.15.2/ADD-MEASTHRESHOLDRULE.md)
- [LST MEASTHRESHOLDRULE](command/UDG/20.15.2/LST-MEASTHRESHOLDRULE.md)
- [MOD MEASTHRESHOLDRULE](command/UDG/20.15.2/MOD-MEASTHRESHOLDRULE.md)
- [RMV MEASTHRESHOLDRULE](command/UDG/20.15.2/RMV-MEASTHRESHOLDRULE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改话统阈值规则(MOD-MEASTHRESHOLDRULE)_29263060.md`
- 原始手册：`evidence/UDG/20.15.2/删除话统阈值规则(RMV-MEASTHRESHOLDRULE)_29103316.md`
- 原始手册：`evidence/UDG/20.15.2/查询话统阈值规则(LST-MEASTHRESHOLDRULE)_75782757.md`
- 原始手册：`evidence/UDG/20.15.2/添加话统阈值规则(ADD-MEASTHRESHOLDRULE)_75942549.md`
