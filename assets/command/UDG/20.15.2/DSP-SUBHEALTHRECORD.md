---
id: UDG@20.15.2@MMLCommand@DSP SUBHEALTHRECORD
type: MMLCommand
name: DSP SUBHEALTHRECORD（显示base平面亚健康链路历史信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SUBHEALTHRECORD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 亚健康检测
status: active
---

# DSP SUBHEALTHRECORD（显示base平面亚健康链路历史信息）

## 功能

该命令用于显示base平面亚健康链路历史信息。

当系统上报“ALM-100319 Base平面Pod级亚健康告警”时，可以执行该命令辅助定位。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCPODID | 源端Pod ID | 可选必选说明：可选参数<br>参数含义：源端Pod ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |
| ALARMSTARTTIME | 查询告警起始时间 | 可选必选说明：可选参数<br>参数含义：查询告警的起始时间。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| ALARMENDTIME | 查询告警结束时间 | 可选必选说明：可选参数<br>参数含义：查询告警结束时间。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SUBHEALTHRECORD]] · base平面亚健康链路历史信息（SUBHEALTHRECORD）

## 使用实例

显示base平面亚健康链路历史信息。

```
%%DSP SUBHEALTHRECORD:;%%
RETCODE = 0  操作成功

结果如下
--------
  源端Pod ID  =  sfm-pod-59948bf4d8-fg9qx
目的端Pod ID  =  netcssim-pod-bdc87787d-l4wt2
告警上报时间  =  2023-06-21 14:25:25
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示base平面亚健康链路历史信息（DSP-SUBHEALTHRECORD）_76794312.md`
