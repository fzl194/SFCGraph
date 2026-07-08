---
id: UDG@20.15.2@MMLCommand@SET PFCPLOADRPT
type: MMLCommand
name: SET PFCPLOADRPT（设置负荷上报开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PFCPLOADRPT
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
- 路径管理
- PFCP路径管理
- PFCP负荷上报管理
- PFCP负荷上报
status: active
---

# SET PFCPLOADRPT（设置负荷上报开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来设置系统的负荷上报功能的配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | LOADRPTSW | RPTTHD | STOPTHD | RANGETHD |
| --- | --- | --- | --- | --- |
| 初始值 | DISABLE | 50 | 45 | 5 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOADRPTSW | 负荷上报开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定负荷上报开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| RPTTHD | 上报阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“LOADRPTSW”配置为“ENABLE”时为可选参数。<br>参数含义：负载上报通知阈值。负载达到阈值后，将负载信息随PFCP消息发送给SMF。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |
| STOPTHD | 停止上报阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“LOADRPTSW”配置为“ENABLE”时为可选参数。<br>参数含义：负荷停止上报阈值。负荷低于阈值时，则不再通知SMF LCI信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |
| RANGETHD | 变化范围阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“LOADRPTSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于表示负荷上报变化范围阈值。本次负荷比上一次负荷变化范围超过变化范围阈值时才需上报。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PFCPLOADRPT]] · 系统负荷上报开关（PFCPLOADRPT）

## 关联任务

- [[UDG@20.15.2@Task@0-00218]]

## 使用实例

设置负荷上报功能配置：

```
SET PFCPLOADRPT: LOADRPTSW=ENABLE, RPTTHD=80, STOPTHD=75, RANGETHD=5;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-PFCPLOADRPT.md`
