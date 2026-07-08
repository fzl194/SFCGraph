---
id: UDG@20.15.2@MMLCommand@SET VOLTEMOSALMTHD
type: MMLCommand
name: SET VOLTEMOSALMTHD（设置异常MOS告警阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: VOLTEMOSALMTHD
command_category: 配置类
applicable_nf:
- PGW-U
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- MOS值异常的用户比例告警阈值
status: active
---

# SET VOLTEMOSALMTHD（设置异常MOS告警阈值）

## 功能

**适用NF：PGW-U**

该命令用于设置MOS值异常的呼叫比例告警阈值和恢复告警阈值。当MOS值异常的呼叫比例连续10次超过告警阈值时产生“ALM-81152 VoLTE语音质量差”，当低于配置的恢复阈值时“ALM-81152 VoLTE语音质量差”恢复。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ALARMTHRES | RESALARMTHRES |
| --- | --- | --- |
| 初始值 | 10 | 8 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALARMTHRES | 告警阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置MOS值异常的用户比例告警阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100，单位是百分比。1到100之间的整数。<br>默认值：无<br>配置原则：<br>- 告警阈值必须大于恢复告警阈值。<br>- 配置过小时，VoLTE语音MOS值异常告警增多，配置过大时，VoLTE语音MOS值异常监测不及时，建议参考MOS异常的用户量配置。 |
| RESALARMTHRES | 恢复告警阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MOS值异常的用户比例告警恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100，单位是百分比。<br>默认值：无<br>配置原则：<br>- 恢复告警阈值必须小于告警阈值。<br>- 配置过小时，VoLTE语音MOS值异常告警增多，配置过大时，VoLTE语音MOS值异常监测不及时，建议参考MOS异常的用户量配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VOLTEMOSALMTHD]] · 异常MOS告警阈值为系统初始设置值（VOLTEMOSALMTHD）

## 使用实例

设置告警阈值和恢复告警阈值：

```
SET VOLTEMOSALMTHD: ALARMTHRES=12, RESALARMTHRES=8;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-VOLTEMOSALMTHD.md`
