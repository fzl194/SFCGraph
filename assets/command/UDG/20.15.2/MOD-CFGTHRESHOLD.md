---
id: UDG@20.15.2@MMLCommand@MOD CFGTHRESHOLD
type: MMLCommand
name: MOD CFGTHRESHOLD（修改配置对象告警阈值）
nf: UDG
version: 20.15.2
verb: MOD
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

# MOD CFGTHRESHOLD（修改配置对象告警阈值）

## 功能

该命令用于修改配置对象告警阈值。系统通过检测配置对象当前记录数与配置对象最大记录数的比值是否大于配置对象告警阈值决定是否上报“ALM-135602215 配置数量超阈值”。

> **说明**
> 无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| OBJECTNAME | 配置对象名称 | 可选必选说明：必选参数。<br>参数含义：用于指定配置对象名称。<br>取值范围：长度不超过16的字符串。<br>默认值：无。<br>配置原则：无。 |
| OBJECTALARMTHRESHOLD | 配置对象告警阈值（%） | 可选必选说明：必选参数。<br>参数含义：用于指定配置对象告警阈值。<br>取值范围：1~100。<br>默认值：无。<br>配置原则：无。 |
| OBJECTALARMRECTHRESHOLD | 配置对象告警恢复阈值（%） | 可选必选说明：必选参数。<br>参数含义：用于指定配置对象告警恢复阈值。<br>取值范围：1~100。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CFGTHRESHOLD]] · 配置对象告警阈值（CFGTHRESHOLD）

## 使用实例

修改配置对象告警阈值时，执行以下命令：

```
MOD CFGTHRESHOLD: OBJECTNAME="TcmcTypeInner", OBJECTALARMTHRESHOLD=80, OBJECTALARMRECTHRESHOLD=60;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-CFGTHRESHOLD.md`
