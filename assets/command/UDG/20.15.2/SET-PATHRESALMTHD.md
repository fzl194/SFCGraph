---
id: UDG@20.15.2@MMLCommand@SET PATHRESALMTHD
type: MMLCommand
name: SET PATHRESALMTHD（设置路径资源不足告警阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PATHRESALMTHD
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
- 路径资源不足告警阈值
status: active
---

# SET PATHRESALMTHD（设置路径资源不足告警阈值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来设置路径资源不足告警的阈值和恢复阈值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | WARNTHRESH | RECVTHRESH |
| --- | --- | --- |
| 初始值 | 80 | 75 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WARNTHRESH | 告警产生阈值（%） | 可选必选说明：必选参数<br>参数含义：路径资源不足告警的阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100，单位是百分比。<br>默认值：无<br>配置原则：告警产生阈值必须大于恢复告警阈值。 |
| RECVTHRESH | 告警恢复阈值（%） | 可选必选说明：必选参数<br>参数含义：路径资源不足告警的恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100，单位是百分比。<br>默认值：无<br>配置原则：恢复告警阈值必须小于告警产生阈值。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PATHRESALMTHD]] · 路径资源不足告警阈值（PATHRESALMTHD）

## 使用实例

设置路径资源不足告警的阈值为80%，恢复阈值是75%：

```
SET PATHRESALMTHD:WARNTHRESH=80,RECVTHRESH=75;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-PATHRESALMTHD.md`
