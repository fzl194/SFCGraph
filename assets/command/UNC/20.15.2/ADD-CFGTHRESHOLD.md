---
id: UNC@20.15.2@MMLCommand@ADD CFGTHRESHOLD
type: MMLCommand
name: ADD CFGTHRESHOLD（增加配置对象告警阈值）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CFGTHRESHOLD
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 配置服务管理
- 维护管理
status: active
---

# ADD CFGTHRESHOLD（增加配置对象告警阈值）

## 功能

该命令用于增加配置对象告警阈值。系统通过检测配置对象当前记录数与配置对象最大记录数的比值是否大于配置对象告警阈值决定是否上报“ALM-135602215 配置数量超阈值”。

## 注意事项

配置对象的告警阈值最大数量取决于系统实际配置对象数量，最大支持100000。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| OBJECTNAME | 配置对象名称 | 可选必选说明：必选参数。<br>参数含义：用于指定配置对象名称。<br>取值范围：长度不超过16的字符串。<br>默认值：无。<br>配置原则：如果无法确认该参数，请联系华为技术支持。 |
| OBJECTALARMTHRESHOLD | 配置对象告警阈值（%） | 可选必选说明：必选参数。<br>参数含义：用于指定配置对象告警阈值。<br>取值范围：1~100。<br>默认值：无。<br>配置原则：无。 |
| OBJECTALARMRECTHRESHOLD | 配置对象告警恢复阈值（%） | 可选必选说明：必选参数。<br>参数含义：用于指定配置对象告警恢复阈值。<br>取值范围：1~100。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CFGTHRESHOLD]] · 配置对象告警阈值（CFGTHRESHOLD）

## 使用实例

增加配置对象告警阈值时，执行以下命令：

```
ADD CFGTHRESHOLD: OBJECTNAME="TcmcTypeInner", OBJECTALARMTHRESHOLD=90, OBJECTALARMRECTHRESHOLD=80;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-CFGTHRESHOLD.md`
