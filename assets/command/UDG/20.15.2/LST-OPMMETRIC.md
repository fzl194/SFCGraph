---
id: UDG@20.15.2@MMLCommand@LST OPMMETRIC
type: MMLCommand
name: LST OPMMETRIC（查询话统指标优化公式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OPMMETRIC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计
status: active
---

# LST OPMMETRIC（查询话统指标优化公式）

## 功能

该命令用于查询网元的话统指标的优化公式。

> **说明**
> 无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数。<br>参数含义：标识网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |
| METRICID | 测量指标ID | 可选必选说明：可选参数。<br>参数含义：测量指标ID，可以通过<br>[**LST MEASUNIT**](查询测量指标模型(LST MEASUNIT)_47814449.md)<br>命令查询获取。<br>取值范围：整数类型，取值范围为0~4294967294。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OPMMETRIC]] · 话统指标优化公式（OPMMETRIC）

## 使用实例

查询话统指标优化公式：

```
%%LST OPMMETRIC:;%%
RETCODE = 0  操作成功

测量指标优化公式
----------------
网元ID  测量指标ID  测量指标名称  测量指标优化公式         公式指标说明                       

100     141100092   指标92        [141100092]*{2}          141100092:指标92                   
100     141100093   指标93        [141100091]+[141100092]  141100091:指标93;141100092:指标93  
100     141100094   指标94        {123}                    NULL                               
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-OPMMETRIC.md`
