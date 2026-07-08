---
id: UDG@20.15.2@MMLCommand@SET TCPRST
type: MMLCommand
name: SET TCPRST（设置欠费用户下行RST报文处理动作）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TCPRST
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 欠费用户下行RST报文控制
status: active
---

# SET TCPRST（设置欠费用户下行RST报文处理动作）

## 功能

**适用NF：PGW-U、UPF**

该命令用来配置欠费用户下行TCP RST报文的处理动作。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ACTION | SIGONLYRSTACT |
| --- | --- | --- |
| 初始值 | PASS | PASS |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACTION | 欠费用户下行RST报文处理动作 | 可选必选说明：必选参数<br>参数含义：欠费用户下行RST报文处理动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PASS：允许报文通过。<br>- DROP：报文丢弃。<br>默认值：无<br>配置原则：无 |
| SIGONLYRSTACT | 欠费用户纯RST信令报文处理动作 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACTION”配置为“PASS”时为可选参数。<br>参数含义：欠费用户纯RST信令报文处理动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PASS：允许报文通过。<br>- DROP：报文丢弃。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [欠费用户下行RST报文处理动作（TCPRST）](configobject/UDG/20.15.2/TCPRST.md)

## 使用实例

配置允许欠费用户下行RST报文通过，但是丢弃欠费用户下行纯RST信令报文：

```
SET TCPRST: ACTION=PASS, SIGONLYRSTACT=DROP;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置欠费用户下行RST报文处理动作（SET-TCPRST）_82837626.md`
