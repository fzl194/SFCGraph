---
id: UNC@20.15.2@MMLCommand@SET PERFCHKSWITCH
type: MMLCommand
name: SET PERFCHKSWITCH（设置性能统计核查开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PERFCHKSWITCH
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 性能管理
- 性能统计核查
status: active
---

# SET PERFCHKSWITCH（设置性能统计核查开关）

## 功能

**适用网元：SGSN、MME**

该命令用于设置性能统计核查开关。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 如果修改核查周期，新的核查周期会等到当前周期结束后生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHECKSWITCH | 核查开关 | 可选必选说明：可选参数<br>参数含义：该参数打开/关闭性能核查开关。<br>数据来源：本端规划。<br>取值范围：<br>- “ON(打开)”<br>- “OFF(关闭)”<br>系统初始设置值：<br>“ON(打开)” |
| CHECKPERIOD | 核查周期 | 可选必选说明：条件可选参数<br>参数含义：该参数设置性能核查周期。<br>前提条件：只有<br>“CHECKSWITCH（核查开关）”<br>为<br>“ON(打开)”<br>时，该参数才有效。<br>数据来源：本端规划。<br>取值范围：30-1440(单位：分钟)<br>系统初始设置值：30 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFCHKSWITCH]] · 性能统计核查开关（PERFCHKSWITCH）

## 使用实例

打开性能核查开关，设置核查周期为30分钟。

SET PERFCHKSWITCH:CHECKSWITCH=ON,CHECKPERIOD=30;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-PERFCHKSWITCH.md`
