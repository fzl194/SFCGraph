---
id: UDG@20.15.2@MMLCommand@SET TOSERVERIPBYPASS
type: MMLCommand
name: SET TOSERVERIPBYPASS（设置异常Server IP自动bypass功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TOSERVERIPBYPASS
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 1
category_path:
- TCP优化服务管理
- 异常Server IP地址bypass功能
status: active
---

# SET TOSERVERIPBYPASS（设置异常Server IP自动bypass功能）

## 功能

**适用NF：UPF**

该命令用于设置异常Server IP自动bypass功能，当开启该功能后，若存在五次及以上建链尝试仍无法正常建链的Server IP地址，该Server IP地址后续的所有流将被Bypass。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 当Server地址和POD内部网络冲突时，需要开启异常Server IP自动bypass功能。
- 老化时间应该大于异常状态重置为初始状态时间。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SERVERIPBYPASSSWITCH | AGETIME | RESETTIME |
| --- | --- | --- | --- |
| 初始值 | DISABLE | 86400 | 21600 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVERIPBYPASSSWITCH | 异常Server IP自动bypass功能开关 | 可选必选说明：必选参数<br>参数含义：设置异常Server IP自动bypass功能开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| AGETIME | 老化时间（秒） | 可选必选说明：可选参数<br>参数含义：设置异常ServerIP表节点老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：无 |
| RESETTIME | 异常状态重置为初始状态时间（秒） | 可选必选说明：可选参数<br>参数含义：设置异常ServerIP表节点异常状态重置为初始状态时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [异常Server IP自动bypass功能配置（TOSERVERIPBYPASS）](configobject/UDG/20.15.2/TOSERVERIPBYPASS.md)

## 使用实例

开启异常Server IP自动bypass功能：

```
SET TOSERVERIPBYPASS: SERVERIPBYPASSSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置异常Server-IP自动bypass功能（SET-TOSERVERIPBYPASS）_77522776.md`
