---
id: UDG@20.15.2@MMLCommand@SET SESSCHKFUNC
type: MMLCommand
name: SET SESSCHKFUNC（设置会话核查配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SESSCHKFUNC
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
- 会话管理
- 业务恢复管理
- 业务核查
status: active
---

# SET SESSCHKFUNC（设置会话核查配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来配置会话核查相关的配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | PATHDWNCHK | DAYCHK | SGRECOVERYCHK | SESSLIMITCHK | ESTABLISHCHK | SESSNUMTHD |
| --- | --- | --- | --- | --- | --- | --- |
| 初始值 | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | 4 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATHDWNCHK | 路径断核查开关 | 可选必选说明：可选参数<br>参数含义：该参数控制N4链路从断到正常后是否触发与SGW-C/PGW-C/SMF之间的会话信息核查。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| DAYCHK | 每日核查开关 | 可选必选说明：可选参数<br>参数含义：该参数控制系统每天是否触发与SGW-C/PGW-C/SMF之间的会话信息核查。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| SGRECOVERYCHK | SG恢复核查开关 | 可选必选说明：可选参数<br>参数含义：该参数控制系统Session SG进程故障恢复后是否触发与SGW-C/PGW-C/SMF之间的会话信息核查。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| SESSLIMITCHK | 会话规格限制核查开关 | 可选必选说明：可选参数<br>参数含义：该参数控制会话规格达到阈值90%时是否触发跟SMF的会话信息核查。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| ESTABLISHCHK | 会话创建核查开关 | 可选必选说明：可选参数<br>参数含义：该参数控制新会话创建时对UPF上已经存在的相同IMSI的会话是否触发核查。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| SESSNUMTHD | 会话创建核查阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ESTABLISHCHK”配置为“ENABLE”时为可选参数。<br>参数含义：该参数控制新会话创建时，相同IMSI下触发核查的会话数阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～21。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SESSCHKFUNC]] · 会话核查配置（SESSCHKFUNC）

## 关联任务

- [[UDG@20.15.2@Task@0-00220]]

## 使用实例

当运营商需要打开Session SG恢复会话核查开关时，进行如下设置：

```
SET SESSCHKFUNC:SGRECOVERYCHK=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SESSCHKFUNC.md`
