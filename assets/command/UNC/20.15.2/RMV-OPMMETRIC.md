---
id: UNC@20.15.2@MMLCommand@RMV OPMMETRIC
type: MMLCommand
name: RMV OPMMETRIC（删除话统指标优化公式）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV OPMMETRIC（删除话统指标优化公式）

## 功能

![](删除话统指标优化公式(RMV OPMMETRIC)_50269958.assets/notice_3.0-zh-cn_2.png)

执行该命令会删除话统指标的优化公式，影响该话统指标的测量结果值，请慎重执行。

该命令用于删除网元的话统指标的优化公式。

## 注意事项

该命令有高危提示，请谨慎执行。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：标识网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |
| METRICID | 测量指标ID | 可选必选说明：必选参数。<br>参数含义：测量指标ID，可以通过<br>[**LST MEASUNIT**](查询测量指标模型(LST MEASUNIT)_47814449.md)<br>命令查询获取。<br>取值范围：整数类型，取值范围为0~4294967294。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OPMMETRIC]] · 话统指标优化公式（OPMMETRIC）

## 使用实例

删除话统指标优化公式：

```
%%RMV OPMMETRIC: MEID=10, METRICID=24100151;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除话统指标优化公式(RMV-OPMMETRIC)_50269958.md`
