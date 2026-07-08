---
id: UNC@20.15.2@MMLCommand@ADD OPMMETRIC
type: MMLCommand
name: ADD OPMMETRIC（添加话统指标优化公式）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: OPMMETRIC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计
status: active
---

# ADD OPMMETRIC（添加话统指标优化公式）

## 功能

![](添加话统指标优化公式(ADD OPMMETRIC)_50748706.assets/notice_3.0-zh-cn_2.png)

执行该命令会新增话统指标的优化公式，影响该话统指标的测量结果值，请慎重执行。

该命令用于添加网元的话统指标的优化公式，且支持配置导出。

## 注意事项

该命令有高危提示，请谨慎执行。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：标识网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |
| METRICID | 测量指标ID | 可选必选说明：必选参数。<br>参数含义：测量指标ID，可以通过<br>[**LST MEASUNIT**](查询测量指标模型(LST MEASUNIT)_47814449.md)<br>命令查询获取。<br>取值范围：整数类型，取值范围为0~4294967294。<br>默认值：无。<br>配置原则：无。 |
| OPMFORMULA | 测量指标优化公式 | 可选必选说明：必选参数。<br>参数含义：指标优化公式。<br>取值范围：字符串类型，长度不超过512个字符。<br>默认值：无。<br>配置原则：计算公式填写规范如下：<br>- 当前的运算符包括“+”、“-”、“*”、“/”、“(”、“)”。<br>- 指标ID是以用“[]” 括起的形式表示，并且符号之间不能有空格。<br>- 常数是以用"{}"括起的浮点类型数字的形式表示。<br>- 粒度周期是以“{GP}”的形式表示，为秒值，表示参与运算的各个指标的粒度周期，不允许不同粒度周期的测量指标进行运算。示例： [1929937501]+{123.23}*{GP}/{60} |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OPMMETRIC]] · 话统指标优化公式（OPMMETRIC）

## 使用实例

添加话统指标优化公式：

```
%%ADD OPMMETRIC: MEID=10, METRICID=24100151, OPMFORMULA="[24100151]+{200}";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-OPMMETRIC.md`
