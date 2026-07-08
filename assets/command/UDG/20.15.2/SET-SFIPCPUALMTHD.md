---
id: UDG@20.15.2@MMLCommand@SET SFIPCPUALMTHD
type: MMLCommand
name: SET SFIPCPUALMTHD（设置告警阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SFIPCPUALMTHD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- SFIP管理
- 告警管理
- CPU占用率
status: active
---

# SET SFIPCPUALMTHD（设置告警阈值）

## 功能

该命令用于设置第三方app的CPU过载告警阈值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | WARNTHRESH | RECVTHRESH |
| --- | --- | --- |
| 初始值 | 80 | 60 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WARNTHRESH | 告警产生阈值(%) | 可选必选说明：必选参数<br>参数含义：该参数用于指定CPU过载告警触发阈值(%)。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：无 |
| RECVTHRESH | 告警恢复阈值(%) | 可选必选说明：必选参数<br>参数含义：该参数用于指定CPU过载告警恢复阈值(%)。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFIPCPUALMTHD]] · 告警阈值（SFIPCPUALMTHD）

## 使用实例

设置第三方app的过载告警阈值：告警阈值默认值为80%，恢复阈值默认值为60%：

```
SET SFIPCPUALMTHD: WARNTHRESH=80, RECVTHRESH=60;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置告警阈值（SET-SFIPCPUALMTHD）_42536151.md`
