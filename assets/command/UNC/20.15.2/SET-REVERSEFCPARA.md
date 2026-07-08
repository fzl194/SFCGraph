---
id: UNC@20.15.2@MMLCommand@SET REVERSEFCPARA
type: MMLCommand
name: SET REVERSEFCPARA（设置PAE寻呼反压流控启动/恢复阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: REVERSEFCPARA
command_category: 配置类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- PAE寻呼反压流控管理
status: active
---

# SET REVERSEFCPARA（设置PAE寻呼反压流控启动/恢复阈值）

## 功能

**适用NF：MME、AMF**

该命令用于设置系统反压流控检测门限参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTRLPLCY | 控制策略 | 可选必选说明：必选参数<br>参数含义：该参数用于指定系统进入反压流控状态的判断方式。<br>数据来源：本端规划<br>取值范围：<br>- PERCENT（百分比）<br>- INSTANCENUM（实例个数）<br>默认值：PERCENT（百分比）<br>配置原则：当取值为“PERCENT(百分比)”时，则按照过载的link-pod实例个数占系统中所有link-pod实例个数的百分比进行过载恢复阈值配置。当取值为“INSTANCENUM（实例个数）”时，则按照过载link-pod实例个数进行过载恢复阈值配置。 |
| PERCENTTRGTHD | 过载阈值（%） | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定系统启动反压流控的阈值。<br>前提条件：该参数在“CTRLPLCY”配置为“PERCENT（百分比）”后生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～99。<br>默认值：50<br>配置原则： 无 |
| PERCENTRESUMTHD | 恢复阈值（%） | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定系统停止反压流控的阈值。<br>前提条件：该参数在“CTRLPLCY”配置为“PERCENT（百分比）”后生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～99。<br>默认值：5<br>配置原则： 无 |
| INSTTRIGTHD | 过载阈值（个） | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定系统启动反压流控的阈值。<br>前提条件：该参数在“CTRLPLCY”配置为“INSTANCENUM（实例个数）”后生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：1<br>配置原则： 无 |
| INSTRESUMTHD | 恢复阈值（个） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统停止反压流控的阈值。<br>前提条件：该参数在“CTRLPLCY”配置为“INSTANCENUM（实例个数）”后生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：0<br>配置原则： 过载恢复阈值需要小于过载阈值。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/REVERSEFCPARA]] · PAE寻呼反压流控启动/恢复阈值（REVERSEFCPARA）

## 使用实例

设置PAE寻呼反压流控启动/恢复阈值的控制策略为百分比，过载阈值（%）为50，恢复阈值（%）为5：

```
SET REVERSEFCPARA: CTRLPLCY=PERCENT, PERCENTTRGTHD=50, PERCENTRESUMTHD=5;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置PAE寻呼反压流控启动_恢复阈值(SET-REVERSEFCPARA)_58751785.md`
