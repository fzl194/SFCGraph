---
id: UDG@20.15.2@MMLCommand@SET DEACTIVERATE
type: MMLCommand
name: SET DEACTIVERATE（配置去活用户会话的速率）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: DEACTIVERATE
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 会话去活速率
status: active
---

# SET DEACTIVERATE（配置去活用户会话的速率）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](配置去活用户会话的速率（SET DEACTIVERATE）_82837081.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，需要根据周边设备的处理能力设置合适的去活速率。若设置去活速率过高，将导致周边设备过载。

该命令用于当系统主动去活用户时，配置去活用户的速率。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 如果配置速率过低，则用户去活时间较长，如果配置速率过高，会导致系统负荷过高，CPU占用率升高，影响用户接入。建议使用系统初始值。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | RATE |
| --- | --- |
| 初始值 | 25 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATE | 去活速率(会话每秒) | 可选必选说明：必选参数<br>参数含义：表示每个ISU/APU VM每秒钟去活的速率，ISU/APU VM数量可由命令DSP NODE进行查询。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～2000，单位是个/秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DEACTIVERATE]] · 去活用户会话的速率（DEACTIVERATE）

## 使用实例

运营商需要配置主动去活用户会话的速率时，使用该命令。配置用户去活速率为25：

```
SET DEACTIVERATE:RATE=25;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/配置去活用户会话的速率（SET-DEACTIVERATE）_82837081.md`
