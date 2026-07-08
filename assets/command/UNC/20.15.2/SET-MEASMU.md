---
id: UNC@20.15.2@MMLCommand@SET MEASMU
type: MMLCommand
name: SET MEASMU（设置话统测量单元模型）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MEASMU
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 操作维护
- 性能统计
status: active
---

# SET MEASMU（设置话统测量单元模型）

## 功能

该命令用于设置话统测量单元模型参数。

![](设置话统测量单元模型(SET MEASMU)_32481237.assets/notice_3.0-zh-cn_2.png)

该命令为高危命令，执行将修改话统测量单元的参数，影响该话统指标的上报，请慎重执行。

## 注意事项

该命令通过修改测量单元是否默认测量属性，可从网管侧关闭默认测量任务。升级、回退、补丁、补丁回退场景下会自动同步任务，任务最终状态由默认测量属性和网管侧任务状态共同决定。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：标识网元ID。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。 |
| MUID | 测量单元ID | 可选必选说明：必选参数。<br>参数含义：测量单元ID。<br>取值范围：整数类型，取值范围为0~4294967294。<br>默认值：无。<br>配置原则：可以通过<br>[**LST MEASMU**](查询话统测量单元模型(LST MEASMU)_32442313.md)<br>命令查询获取。 |
| TYPE | 类型 | 可选必选说明：必选参数。<br>参数含义：支持变更的参数。<br>取值范围：枚举项<br>- SWITCH_CREDIBLE(开关可信)<br>- DEF_MEAS(默认测量)<br>默认值：无。<br>配置原则：无。 |
| SW_CREDIBLE_ENABLE | 支持开关可信 | 可选必选说明：当<br>**类型**<br>选择<br>“SWITCH_CREDIBLE(开关可信)”<br>时，为必选参数。<br>参数含义：是否支持开关可信。<br>取值范围：枚举<br>- DEFAULT(默认配置)<br>- YES(是)<br>- NO(否)<br>默认值：无。<br>配置原则：无。 |
| DEFMEAS | 默认测量 | 可选必选说明：当<br>**类型**<br>选择<br>“DEF_MEAS(默认测量)”<br>时，为必选参数。<br>参数含义：任务是否默认测量。<br>取值范围：枚举<br>- DEFAULT(默认配置)<br>- YES(是)<br>- NO(否)<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MEASMU]] · 话统测量单元模型（MEASMU）

## 使用实例

设置话统测量单元可信开关：

```
%%SET MEASMU: MEID=12, MUID=1929379844, TYPE=SWITCH_CREDIBLE, SW_CREDIBLE_ENABLE=YES;
%% RETCODE = 0  操作成功
 
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-MEASMU.md`
