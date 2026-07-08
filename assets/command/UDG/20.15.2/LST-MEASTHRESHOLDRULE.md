---
id: UDG@20.15.2@MMLCommand@LST MEASTHRESHOLDRULE
type: MMLCommand
name: LST MEASTHRESHOLDRULE（查询话统阈值规则）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MEASTHRESHOLDRULE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计
status: active
---

# LST MEASTHRESHOLDRULE（查询话统阈值规则）

## 功能

该命令用于查询话统阈值规则。

> **说明**
> 无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数。<br>参数含义：标识网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |
| TRN | 阈值规则名称 | 可选必选说明：可选参数。<br>参数含义：阈值规则名称。<br>取值范围：字符串类型，长度不超过80个字符。<br>默认值：无。<br>配置原则：仅支持“A-Z”、“a-z”、“0-9”、“-_”、“\u4e00-\u9fa5”中文字符组合，支持模糊查询。 |
| TRT | 阈值规则类型 | 可选必选说明：可选参数。<br>参数含义：阈值规则类型。<br>取值范围：SIMPLE(简单阈值)<br>默认值：无。<br>配置原则：无。 |
| PRD | 测量周期 | 可选必选说明：可选参数。<br>参数含义：标识指标数据的周期。<br>取值范围：<br>- FIVE_SECOND(5秒)<br>- ONE_MINUTE(1分钟)<br>默认值：无。<br>配置原则：无。 |
| MOIID | 对象实例ID | 可选必选说明：可选参数。<br>参数含义：对象实例ID，可以通过<br>[DSP MEASOBJ](查询话统测量对象实例(DSP MEASOBJ)_01094728.md)<br>命令查询获取。<br>取值范围：字符串类型，长度不超过256个字符。<br>默认值：无。<br>配置原则：支持模糊查询。 |
| METRICID | 测量指标ID | 可选必选说明：可选参数。<br>参数含义：测量指标ID，可以通过<br>[LST MEASUNIT](查询测量指标模型(LST MEASUNIT)_47814449.md)<br>命令查询获取。<br>取值范围：0~4294967294的整数。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [话统阈值规则（MEASTHRESHOLDRULE）](configobject/UDG/20.15.2/MEASTHRESHOLDRULE.md)

## 使用实例

查询话统阈值规则：

```
%%LST MEASTHRESHOLDRULE:;%%
RETCODE = 0  操作成功
话统阈值规则（简单阈值类型）
----------------------------
网元ID  阈值规则名称  测量周期  激活开始时间  激活结束时间  对象实例ID  测量指标ID  测量指标名称   趋势  连续触发次数  连续恢复次数  紧急告警阈值  紧急告警偏移  重要告警阈值  重要告警偏移  次要告警阈值  次要告警偏移  提示告警阈值  提示告警偏移  
10      tes4          5         13:51         16:51         moc_4001    4100144     CSDK04指标144  下降  4             4             56            1             67            1             77            1             90            5             
10      test          60        NULL          NULL          moc         4100145     CSDK04指标145  上升  3             4             58            NULL          40            NULL          NULL          NULL          NULL          NULL          
10      test2         60        16:48         NULL          moc         4100145     CSDK04指标145  上升  3             4             58            NULL          40            NULL          NULL          NULL          NULL          NULL          
10      test3         60        NULL          16:49         moc         4100145     CSDK04指标145  上升  3             4             58            NULL          40            NULL          NULL          NULL          NULL          NULL          
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询话统阈值规则(LST-MEASTHRESHOLDRULE)_75782757.md`
