---
id: UDG@20.15.2@MMLCommand@LST MEASMU
type: MMLCommand
name: LST MEASMU（查询话统测量单元模型）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MEASMU
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计
status: active
---

# LST MEASMU（查询话统测量单元模型）

## 功能

该命令用于查询网元的测量单元模型信息。

> **说明**
> 无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：标识网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |
| MOCNAME | 测量对象类名称 | 可选必选说明：可选参数。<br>参数含义：测量对象类名称，支持中英文模糊搜索。<br>取值范围：字符串类型，长度不超过256个字符。<br>默认值：无。<br>配置原则：若不输入，则表示该参数不作为查询的限制条件。 |
| MUNAME | 测量单元名称 | 可选必选说明：可选参数。<br>参数含义：测量单元名称，支持中英文模糊搜索。<br>取值范围：字符串类型，长度不超过256个字符。<br>默认值：无。<br>配置原则：若不输入，则表示该参数不作为查询的限制条件。 |
| MUID | 测量单元ID | 可选必选说明：可选参数。<br>参数含义：测量单元ID，可以通过<br>**[**LST MEASUNIT**](查询测量指标模型(LST MEASUNIT)_47814449.md)**<br>命令查询获取。<br>取值范围：整数类型，取值范围为0~4294967294。<br>默认值：无。<br>配置原则：若不输入，则表示该参数不作为查询的限制条件。 |
| SW_CREDIBLE_ENABLE | 支持开关可信 | 可选必选说明：可选参数。<br>参数含义：是否支持开关可信。<br>取值范围：枚举<br>- YES(是)<br>- NO(否)<br>默认值：无。<br>配置原则：无。 |
| DEFMEAS | 默认测量 | 可选必选说明：可选参数。<br>参数含义：任务是否默认测量。<br>取值范围：枚举<br>- YES(是)<br>- NO(否)<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MEASMU]] · 话统测量单元模型（MEASMU）

## 使用实例

查询网元测量单元模型信息：

```
%%LST MEASMU: MEID=0, MOCNAME="POD", SW_CREDIBLE_ENABLE=YES, DEFMEAS=YES;%%
RETCODE = 0  操作成功

测量单元模型信息
----------------
测量对象类名称  测量单元ID  测量单元名称   监控类型        支持5s监控  默认话统周期(分钟)  默认测量指标范围  实例间合并计算  实际打点服务  支持开关可信  默认测量  

POD             1929379843  PodCPU利用率   监控和性能统计  是          5                   全部指标          是              CELL_RMFEXEC  是            是            
POD             1929379844  Pod内存利用率  监控和性能统计  是          5                   全部指标          是              CELL_RMFEXEC  是            是            
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-MEASMU.md`
