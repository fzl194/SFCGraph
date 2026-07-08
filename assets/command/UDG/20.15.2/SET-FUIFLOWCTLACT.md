---
id: UDG@20.15.2@MMLCommand@SET FUIFLOWCTLACT
type: MMLCommand
name: SET FUIFLOWCTLACT（设置欠费重定向流控动作）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FUIFLOWCTLACT
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
- 重定向控制
- FUI重定向控制
- FUI流控动作
status: active
---

# SET FUIFLOWCTLACT（设置欠费重定向流控动作）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置因重定向放通的欠费DNS或临时流量转正无配额放行流量的控制方式。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 命令用于一旦因欠费重定向放行的欠费DNS或临时流量转正无配额放行流量超过设置的阈值，设置检测或控制，可防止用户恶意欺诈。为避免欠费重定向流控参数配置不合理，建议先配置CHECK，观测相关话统判断是否合理后再开启为CONTROL，或联系华为工程师一起进行评估。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ACTION |
| --- | --- |
| 初始值 | NONE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACTION | 欠费重定向流控动作 | 可选必选说明：必选参数<br>参数含义：该参数用于设置因重定向放通的欠费DNS或临时流量转正无配额放行流量的控制方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NONE：关闭无法计费流量的检测和控制。<br>- CHECK：仅检查用户是否满足流控条件，不做真正流控。可统计该类场景无法实时计费的流量。<br>- CONTROL：对满足流控条件的用户执行流控，被流控的报文丢弃。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FUIFLOWCTLACT]] · 欠费重定向流控动作（FUIFLOWCTLACT）

## 使用实例

如设置对因重定向放通的欠费DNS或临时流量转正无配额放行流量的流控，命令如下：

```
SET FUIFLOWCTLACT: ACTION=CONTROL;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置欠费重定向流控动作（SET-FUIFLOWCTLACT）_82837542.md`
