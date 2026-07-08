---
id: UDG@20.15.2@MMLCommand@SET LINKALMCFG
type: MMLCommand
name: SET LINKALMCFG（设置TWAMP的Light模式“链路丢包率过高告警”配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: LINKALMCFG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- IPAPM链路告警配置
status: active
---

# SET LINKALMCFG（设置TWAMP的Light模式“链路丢包率过高告警”配置）

## 功能

该命令用于设置TWAMP的Light模式“链路丢包率过高告警”配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | THRESHOLD | CLEARTHRESHOLD | PERIOD |
> | --- | --- | --- |
> | 10 | 5 | 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| THRESHOLD | 阈值 | 可选必选说明：可选参数<br>参数含义：丢包率告警阈值，检测周期内TWAMP链路丢包率大于等于阈值后产生告警。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~100，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LINKALMCFG查询当前参数配置值。<br>配置原则：<br>阈值必须大于恢复阈值。 |
| CLEARTHRESHOLD | 恢复阈值 | 可选必选说明：可选参数<br>参数含义：丢包率告警恢复阈值，检测周期内TWAMP链路丢包率小于等于阈值后恢复告警。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~99，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LINKALMCFG查询当前参数配置值。<br>配置原则：<br>恢复阈值必须小于阈值。 |
| PERIOD | 检测周期 | 可选必选说明：可选参数<br>参数含义：检测周期，设置TWAMP链路丢包率的检测周期。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是10~180，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LINKALMCFG查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LINKALMCFG]] · TWAMP的Light模式“链路丢包率过高告警”配置（LINKALMCFG）

## 关联任务

- [[UDG@20.15.2@Task@0-00230]]

## 使用实例

设置TWAMP链路告警配置的实例：

```
SET LINKALMCFG: THRESHOLD=30, CLEARTHRESHOLD=10, PERIOD=40;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-LINKALMCFG.md`
