---
id: UDG@20.15.2@MMLCommand@SET PATHCTRLALMTHD
type: MMLCommand
name: SET PATHCTRLALMTHD（设置大量路径断告警的告警阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PATHCTRLALMTHD
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务运维
- 业务告警管理
- 大量GTPU路径断告警门限
status: active
---

# SET PATHCTRLALMTHD（设置大量路径断告警的告警阈值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

系统对接海量的eNodeB/gNodeB，如果出现大量路径断，需要设置ALM-81100 GTPU大量路径断告警的上报阈值和恢复阈值，避免告警风暴。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 告警上报阈值必须大于告警恢复阈值。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | WARNTHRESH | RECVTHRESH |
| --- | --- | --- |
| 初始值 | 100 | 50 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WARNTHRESH | 大量路径断告警上报的阈值 | 可选必选说明：可选参数<br>参数含义：大量路径断告警上报的阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～500。<br>默认值：无<br>配置原则：无 |
| RECVTHRESH | 大量路径断告警恢复的阈值 | 可选必选说明：可选参数<br>参数含义：大量路径断告警恢复的阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～500。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PATHCTRLALMTHD]] · 大量路径断告警告警阈值（PATHCTRLALMTHD）

## 使用实例

设置大量路径断告警的上报阈值和恢复阈值：

```
SET PATHCTRLALMTHD:WARNTHRESH=100,RECVTHRESH=50;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置大量路径断告警的告警阈值（SET-PATHCTRLALMTHD）_82837861.md`
