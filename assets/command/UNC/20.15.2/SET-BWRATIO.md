---
id: UNC@20.15.2@MMLCommand@SET BWRATIO
type: MMLCommand
name: SET BWRATIO（设置带宽占用比例表）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: BWRATIO
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 数据转发管理
- 转发资源管理
- 带宽资源管理
- 带宽占用比例管理
status: active
---

# SET BWRATIO（设置带宽占用比例表）

## 功能

**适用网元：SGSN**

该命令用于设置QoS级别为会话类和流类业务所用的静态带宽能占用的可用带宽的最大百分比。用户面需要对QoS级别为会话类和流类业务所用的静态带宽进行控制。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 可用带宽等于总带宽减去突发预留带宽。总带宽和突发预留带宽可以用[**DSP PFRES**](../带宽资源参数管理/显示带宽资源使用明细(DSP PFRES)_26145850.md)查询。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATICBW | 静态带宽最大百分比（%） | 可选必选说明：可选参数<br>参数含义：该参数用来指定在系统允许的情况下，会话类和流类业务所用静态带宽占可用带宽的最大百分比。<br>数据来源：整网规划<br>取值范围： 0～100(%)。<br>系统初始设置值：<br>“100”<br>。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BWRATIO]] · 带宽占用比例表（BWRATIO）

## 使用实例

配置静态带宽占用可用带宽的最大百分比为30%：

SET BWRATIO: STATICBW=30;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-BWRATIO.md`
