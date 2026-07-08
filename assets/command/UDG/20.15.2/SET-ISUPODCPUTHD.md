---
id: UDG@20.15.2@MMLCommand@SET ISUPODCPUTHD
type: MMLCommand
name: SET ISUPODCPUTHD（设置ISU POD的业务CPU过载告警阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: ISUPODCPUTHD
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
- 业务CPU过载告警阈值
status: active
---

# SET ISUPODCPUTHD（设置ISU POD的业务CPU过载告警阈值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置ISU POD业务的CPU过载告警的上报和恢复阈值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | WARNTHD | RECVTHD |
| --- | --- | --- |
| 初始值 | 80 | 70 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WARNTHD | 告警上报阈值 | 可选必选说明：可选参数<br>参数含义：设置告警上报阈值。<br>数据来源：本端规划<br>取值范围：当参数配置为0时表示关闭告警功能。当参数配置为非0时，“告警上报阈值”必须大于“告警恢复阈值”。<br>默认值：无<br>配置原则：无 |
| RECVTHD | 告警恢复阈值 | 可选必选说明：可选参数<br>参数含义：设置告警恢复阈值。<br>数据来源：本端规划<br>取值范围：当参数配置为0时表示关闭告警功能。当参数配置为非0时，“告警恢复阈值”必须小于“告警上报阈值”。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ISUPODCPUTHD]] · ISU POD业务CPU过载告警阈值（ISUPODCPUTHD）

## 使用实例

设置 ISU POD的业务CPU过载告警的上报阈值为85%，恢复阈值为75%：

```
SET ISUPODCPUTHD: WARNTHD=85, RECVTHD=75;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-ISUPODCPUTHD.md`
