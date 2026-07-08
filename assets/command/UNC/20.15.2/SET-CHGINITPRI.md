---
id: UNC@20.15.2@MMLCommand@SET CHGINITPRI
type: MMLCommand
name: SET CHGINITPRI（设置RADIUS计费和在线计费消息优先级）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CHGINITPRI
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 计费参数
status: active
---

# SET CHGINITPRI（设置RADIUS计费和在线计费消息优先级）

## 功能

**适用NF：PGW-C、SMF**

该命令用于设置用户激活过程中RADIUS计费消息和在线计费消息交互优先级。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 当前仅支持RADIUS计费消息交互的优先级低于等于在线计费交互的优先级，其中0为最高优先级。如果RADIUS计费消息的交互优先级与在线计费的交互优先级相等，RADIUS计费消息的交互优先；如果RADIUS计费消息的交互优先级低于在线计费的交互优先级，在线计费消息交互优先。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | RADIUSPRIORITY | ONLINEPRIORITY |
| --- | --- | --- |
| 初始值 | 5 | 5 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RADIUSPRIORITY | RADIUS计费消息交互的优先级 | 可选必选说明：可选参数<br>参数含义：RADIUS计费消息交互的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～5。<br>默认值：无<br>配置原则：无 |
| ONLINEPRIORITY | 在线计费消息交互的优先级 | 可选必选说明：可选参数<br>参数含义：在线计费消息交互的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～5。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGINITPRI]] · RADIUS计费和在线计费消息优先级（CHGINITPRI）

## 使用实例

设置RADIUS计费和在线计费消息优先级，RADIUSPRIORITY为“1”，ONLINEPRIORITY为“1”：

```
SET CHGINITPRI:RADIUSPRIORITY=1, ONLINEPRIORITY=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CHGINITPRI.md`
