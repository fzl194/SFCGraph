---
id: UDG@20.15.2@MMLCommand@OPR ACSUPDPRECHK
type: MMLCommand
name: OPR ACSUPDPRECHK（升级前检查）
nf: UDG
version: 20.15.2
verb: OPR
object_keyword: ACSUPDPRECHK
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 升级维护
status: active
---

# OPR ACSUPDPRECHK（升级前检查）

## 功能

该命令用于基础版本、补丁或者基础版本和补丁升级前执行风险检查。

本命令只适用于ACS服务，其他微服务请使用OPR UPDPRECHK命令。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令时，请不要执行主备倒换、复位RU和其他消耗系统资源操作，否则会影响检查结果。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VERSIONID | 包版本号 | 可选必选说明：必选参数<br>参数含义：包版本号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| UPDMODE | 升级模式 | 可选必选说明：必选参数<br>参数含义：升级模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SU：普通升级。<br>- ISSU：无损升级。<br>默认值：无 |
| RESULTFILE | 报告名称 | 可选必选说明：必选参数<br>参数含义：报告名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| VERSIONTYPE | 版本类型 | 可选必选说明：条件可选参数，该参数在“UPDMODE”配置为“SU”时为可选参数。<br>参数含义：该参数用于指定版本类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BaseSoftware：包含网元或APP运行所需所有软件的全版本。<br>- ColdPatch：为网元或APP运行所需的部分软件，为对基础版本的补充，冷补丁不能独立运行，冷补丁升级往往会中断业务。<br>- HotPatch：为对基础版本或冷补丁的热补充，热补丁不能独立运行，热补丁升级不中断业务。<br>默认值：BaseSoftware |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ACSUPDPRECHK]] · 升级前检查（ACSUPDPRECHK）

## 使用实例

执行升级前检查：

```
OPR ACSUPDPRECHK:VERSIONID="V100R005C10CHK",UPDMODE=SU,RESULTFILE="UPD_PRE_REPORT";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/OPR-ACSUPDPRECHK.md`
