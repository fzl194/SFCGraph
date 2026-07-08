---
id: UNC@20.15.2@MMLCommand@LST PERFRPTRANGE
type: MMLCommand
name: LST PERFRPTRANGE（查询性能指标上报范围）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFRPTRANGE
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- 性能统计上报范围管理
status: active
---

# LST PERFRPTRANGE（查询性能指标上报范围）

## 功能

**适用NF：SMF、PGW-C、GGSN、AMF**

该命令用于查询AMF或SMF性能统计指标的上报范围。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOC | 测量对象类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定测量对象类型。<br>数据来源：本端规划<br>取值范围：<br>- “APN_GW（APN_GW）”：表示SMF网元的APN_GW性能统计对象类型。<br>- “DNN（DNN）”：表示SMF网元的DNN性能统计对象类型。<br>- “TAILIST（TAILIST）”：表示SMF网元的TAI组性能统计对象类型。<br>- “AMFTAIGRP（AMFTAIGRP）”：表示AMF网元的TAI组性能统计对象类型。<br>默认值：无<br>配置原则：无 |
| RULERANGE | 规则生效范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本记录生效的范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL（所有）”：表示该记录配置的上报规则针对指定MOC的所有对象实例和所有测量单元生效。<br>- “SPECIFICMU（指定测量单元）”：表示该记录配置的上报规则针对指定MOC的指定测量单元生效。<br>- “SPECIFICMOI（指定测量对象实例）”：表示该记录配置的上报规则针对指定MOC的指定测量对象实例生效。<br>默认值：无<br>配置原则：<br>三种生效范围的优先级为：“指定测量对象实例”>“指定测量单元”>“所有测量对象实例”。 |
| NMMUID | 测量单元ID | 可选必选说明：该参数在"RULERANGE"配置为"SPECIFICMU"时为条件可选参数。<br>参数含义：该参数用于指定测量单元的网管ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967294。<br>默认值：无<br>配置原则：无 |
| MOIID | 测量对象实例ID | 可选必选说明：该参数在"RULERANGE"配置为"SPECIFICMOI"时为条件可选参数。<br>参数含义：该参数用于指定测量对象实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：<br>当“测量对象类型”设置为APN_GW时，本参数设置的APN需要是ADD APN命令配置的APN。<br>当“测量对象类型”设置为DNN时，本参数设置的DNN需要满足“MCC:MNC:SST-SD:DNN”的格式，MNC和MCC需要是ADD NGSRVPLMN命令配置的MNC和MCC，SST和SD需要是ADD PLMNNS命令配置的SST和SD，其中Plmn索引为MCC和MNC在ADD NGSRVPLMN命令配置中的索引，DNN需要是ADD APN命令配置的APN。<br>当“测量对象类型”设置为TAILIST时，本参数设置的“测量对象实例ID”需要通过ADD PERFTAIGROUP命令进行配置。<br>当“测量对象类型”设置为AMFTAIGRP时，本参数设置的“测量对象实例ID”需要通过ADD PERFNGTAIGROUP命令进行配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFRPTRANGE]] · 性能指标上报范围（PERFRPTRANGE）

## 使用实例

查询所有性能指标上报范围：

```
%%LST PERFRPTRANGE: RULERANGE=ALL;%%
RETCODE = 0  操作成功

结果如下
--------
  测量对象类型  =  APN_GW
  规则生效范围  =  所有
    测量单元ID  =  NULL
测量对象实例ID  =  NULL
      上报范围  =  全部
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PERFRPTRANGE.md`
