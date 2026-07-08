---
id: UDG@20.15.2@MMLCommand@RMV QOSPROP
type: MMLCommand
name: RMV QOSPROP（删除QoS属性）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: QOSPROP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 业务QOS控制
- 业务质量属性
status: active
---

# RMV QOSPROP（删除QoS属性）

## 功能

**适用NF：PGW-U、UPF**

该命令是用来删除所有或者某个QoS配置。

## 注意事项

- 该命令执行后立即生效。
- 在删除QoS属性执行RMV QOSPROP命令前需要确定QOSPROPNAME名称是否被引用，使用LST PCCPOLICYGRP命令参看QOSPROPNAME名称是否被引用，若被引用则执行RMV QOSPROP命令失败，在删除被引用对象记录才能执行成功。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROPNAME | Qos属性名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoS属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/QOSPROP]] · QoS属性（QOSPROP）

## 使用实例

删除名称为“test”的QoS属性时，命令为：

```
RMV QOSPROP:QOSPROPNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-QOSPROP.md`
