---
id: UDG@20.15.2@MMLCommand@RMV MQCPOLICY
type: MMLCommand
name: RMV MQCPOLICY（删除流策略）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: MQCPOLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- MQC
- 分类策略
status: active
---

# RMV MQCPOLICY（删除流策略）

## 功能

该命令用于删除一个已经定义的流量策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：指定流策略的名称，不允许为系统预定义策略default。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MQCPOLICY]] · 流策略配置（MQCPOLICY）

## 使用实例

删除流量策略p1：

```
RMV MQCPOLICY:POLICYNAME="p1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-MQCPOLICY.md`
