---
id: UDG@20.15.2@MMLCommand@SET COMBASEHEALTH
type: MMLCommand
name: SET COMBASEHEALTH（设置Base平面的亚健康检测参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: COMBASEHEALTH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 亚健康检测
status: active
---

# SET COMBASEHEALTH（设置Base平面的亚健康检测参数）

## 功能

该命令用于设置Base平面的亚健康检测参数。当需要开启或关闭Base平面的网络亚健康质量检测任务，或者不想使用系统初始值时，可以使用此命令进行设置。

开启后，当检测出本端Pod与其它Pod之间的链路存在亚健康情况时，系统产生ALM-100319 Base平面Pod级亚健康告警。两个Pod之间的链路存在亚健康情况是指：在最近一个告警统计周期内，每一个告警检测周期计算出的亚健康度都大于告警阈值时。亚健康度是由两个Pod之间1个检测周期内的丢包率和错包率计算出的值，计算公式为（丢包率（千分比）+ 5 * 错包率（千分比））/ 2。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | DETECTINTERVAL | STATISINTERVAL | THRESHOLD | ENABLEFLAG |
> | --- | --- | --- | --- |
> | 1 | 30 | 50 | ENABLE |

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DETECTINTERVAL | 检测周期(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于标识Base平面亚健康检测的检测周期，即每过一个检测周期发一次探测报文。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST COMBASEHEALTH查询当前参数配置值。<br>配置原则：无 |
| STATISINTERVAL | 统计周期(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于标识Base平面亚健康检测的统计周期，即每过一个统计周期统计一次该周期内各项亚健康指标。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~180，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST COMBASEHEALTH查询当前参数配置值。<br>配置原则：无 |
| THRESHOLD | 亚健康告警阈值(‰) | 可选必选说明：可选参数<br>参数含义：该参数用于标识Base平面亚健康检测的阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST COMBASEHEALTH查询当前参数配置值。<br>配置原则：无 |
| ENABLEFLAG | 使能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于标识Base平面亚健康检测的使能开关。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：关闭Base平面亚健康检测功能<br>- “ENABLE（使能）”：打开Base平面亚健康检测功能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST COMBASEHEALTH查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@COMBASEHEALTH]] · Base平面通信质量（COMBASEHEALTH）

## 使用实例

设置Base平面的亚健康检测参数：

```
%%SET COMBASEHEALTH: DETECTINTERVAL=1, STATISINTERVAL=30, THRESHOLD=50, ENABLEFLAG=ENABLE;%%
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-COMBASEHEALTH.md`
