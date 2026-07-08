---
id: UDG@20.15.2@MMLCommand@SET SRVNDALMTHRES
type: MMLCommand
name: SET SRVNDALMTHRES（设置业务节点资源不足告警阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SRVNDALMTHRES
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
- 业务节点资源不足告警阈值
status: active
---

# SET SRVNDALMTHRES（设置业务节点资源不足告警阈值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于配置业务节点告警阈值和恢复告警阈值。当业务节点资源使用率超过配置的告警门限时产生告警。当使用率低于配置的恢复门限时恢复告警。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ALARMTHRES | RESALARMTHRES |
| --- | --- | --- |
| 初始值 | 80 | 75 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALARMTHRES | 业务节点告警阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置业务节点告警阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：告警阈值必须大于恢复告警阈值，建议根据业务节点的使用情况配置。 |
| RESALARMTHRES | 业务节点恢复告警阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置业务节点恢复告警阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：恢复告警阈值必须小于告警阈值。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRVNDALMTHRES]] · 业务节点资源不足告警阈值（SRVNDALMTHRES）

## 使用实例

假如运营商想在业务节点资源使用率超过85%时产生告警，当使用率低于75%时恢复告警，命令如下：

```
SET SRVNDALMTHRES: ALARMTHRES=85,RESALARMTHRES=75;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置业务节点资源不足告警阈值（SET-SRVNDALMTHRES）_82837874.md`
