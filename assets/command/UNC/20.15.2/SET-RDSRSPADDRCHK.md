---
id: UNC@20.15.2@MMLCommand@SET RDSRSPADDRCHK
type: MMLCommand
name: SET RDSRSPADDRCHK（设置全局RADIUS响应消息源IP/端口检查配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: RDSRSPADDRCHK
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
- RADIUS管理
- 连接管理
- RADIUS响应消息地址检查
status: active
---

# SET RDSRSPADDRCHK（设置全局RADIUS响应消息源IP/端口检查配置）

## 功能

**适用NF：PGW-C、SMF**

该命令用来设置全局RADIUS响应消息源IP/端口检查配置。使能该检查功能，如果RADIUS响应消息的源IP或者端口号与UNC配置的不一致，UNC将丢弃此消息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | AUTH | ACCT |
| --- | --- | --- |
| 初始值 | ENABLE | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AUTH | RADIUS鉴权响应消息源IP/端口检查开关 | 可选必选说明：可选参数<br>参数含义：RADIUS鉴权响应消息源IP/端口检查开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| ACCT | RADIUS计费响应消息源IP/端口检查开关 | 可选必选说明：可选参数<br>参数含义：RADIUS计费响应消息源IP/端口检查开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RDSRSPADDRCHK]] · 全局RADIUS响应消息源端口检查配置（RDSRSPADDRCHK）

## 使用实例

使能RADIUS鉴权响应消息和计费响应消息源IP/端口检查：

```
SET RDSRSPADDRCHK: AUTH=ENABLE, ACCT=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-RDSRSPADDRCHK.md`
