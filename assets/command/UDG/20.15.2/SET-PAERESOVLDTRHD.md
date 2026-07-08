---
id: UDG@20.15.2@MMLCommand@SET PAERESOVLDTRHD
type: MMLCommand
name: SET PAERESOVLDTRHD（设置PAE关键资源不足告警参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PAERESOVLDTRHD
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 资源不足告警
status: active
---

# SET PAERESOVLDTRHD（设置PAE关键资源不足告警参数）

## 功能

该命令用于修改PAE关键资源不足告警的参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | RESTYPE | PERIOD | OVERLOADTHD | OVERLOADNUM | RECOVERTHD | RECOVERNUM |
> | --- | --- | --- | --- | --- | --- |
> | PAE_CHANNEL_QUE | 5 | 100 | 5 | 100 | 12 |
> | PAE_EXTPORT_QUE | 5 | 100 | 5 | 100 | 12 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESTYPE | 资源类型 | 可选必选说明：必选参数<br>参数含义：告警参数的资源类型。<br>数据来源：本端规划<br>取值范围：<br>- PAE_CHANNEL_QUE（PAE CHANNEL队列）<br>- PAE_EXTPORT_QUE（PAE EXT口队列）<br>默认值：无。<br>配置原则：无 |
| PERIOD | 检测周期 (秒) | 可选必选说明：可选参数<br>参数含义：资源过载检测周期，表示两次检测之间的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~86400，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PAERESOVLDTRHD查询当前参数配置值。<br>配置原则：无 |
| OVERLOADTHD | 过载阈值 (%) | 可选必选说明：可选参数<br>参数含义：资源过载的阈值，当资源使用率大于等于该阈值时，资源为过载状态。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是2~100，单位是百分比。大于等于过载恢复阈值。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PAERESOVLDTRHD查询当前参数配置值。<br>配置原则：无 |
| OVERLOADNUM | 过载次数 | 可选必选说明：可选参数<br>参数含义：系统检测到资源过载的次数；若该参数设置为N，当资源在前几个周期的检测中，出现N次使用率大于等于过载阈值，且期间每个周期检测使用率大于等于过载恢复阈值，则上报告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~100，单位是次。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PAERESOVLDTRHD查询当前参数配置值。<br>配置原则：无 |
| RECOVERTHD | 过载恢复阈值 (%) | 可选必选说明：可选参数<br>参数含义：资源过载恢复的阈值，当资源过载后使用率再次小于该阈值时，资源从过载状态恢复。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~100，单位是百分比。小于等于过载阈值。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PAERESOVLDTRHD查询当前参数配置值。<br>配置原则：无 |
| RECOVERNUM | 过载恢复次数 | 可选必选说明：可选参数<br>参数含义：系统检测到资源过载恢复的次数；若该参数设置为N，当资源在前几个周期的检测中，出现N次使用率小于过载恢复阈值，且期间每个周期检测使用率小于过载阈值，则消除告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~100，单位是次。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PAERESOVLDTRHD查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PAERESOVLDTRHD]] · PAE关键资源不足告警参数（PAERESOVLDTRHD）

## 使用实例

设置channel队列过载检测的参数，设置检测周期为10秒，过载阈值为80，过载次数为5，过载恢复阈值为60，过载恢复次数为5

```
SET PAERESOVLDTRHD: RESTYPE=PAE_CHANNEL_QUE, PERIOD=10, OVERLOADTHD=80, OVERLOADNUM=5, RECOVERTHD=60, RECOVERNUM=5;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置PAE关键资源不足告警参数（SET-PAERESOVLDTRHD）_53828096.md`
