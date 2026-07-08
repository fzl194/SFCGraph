---
id: UNC@20.15.2@MMLCommand@SET CDRPOOLTHRSH
type: MMLCommand
name: SET CDRPOOLTHRSH（设置话单池空间告警阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CDRPOOLTHRSH
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 告警管理
- 话单池空间告警阈值
status: active
---

# SET CDRPOOLTHRSH（设置话单池空间告警阈值）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来设置话单池空间不足告警阈值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 告警恢复阈值必须小于告警产生阈值。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ALARMTHRESHOLD | ALARMCLRTHRSH |
| --- | --- | --- |
| 初始值 | 80 | 75 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALARMTHRESHOLD | 告警产生阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定话单池空间不足告警阈值大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2～100。<br>默认值：无<br>配置原则：无 |
| ALARMCLRTHRSH | 告警恢复阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数指定话单池空间不足告警恢复阈值大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～99。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [话单池空间告警阈值（CDRPOOLTHRSH）](configobject/UNC/20.15.2/CDRPOOLTHRSH.md)

## 使用实例

设置当占用话单池容量超过80%时，产生81005话单池空间不足告警，当占用话单池容量下降到70%时，恢复81005话单池空间不足告警：

```
SET CDRPOOLTHRSH:ALARMTHRESHOLD=80,ALARMCLRTHRSH=70;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置话单池空间告警阈值（SET-CDRPOOLTHRSH）_09897347.md`
