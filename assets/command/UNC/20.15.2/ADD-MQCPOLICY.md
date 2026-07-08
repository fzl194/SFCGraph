---
id: UNC@20.15.2@MMLCommand@ADD MQCPOLICY
type: MMLCommand
name: ADD MQCPOLICY（增加流策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MQCPOLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1023
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- MQC
- 分类策略
status: active
---

# ADD MQCPOLICY（增加流策略）

## 功能

该命令用于创建流量策略；当需要对某种规则的流分类配置复杂流分类的QoS策略时需要使用该命令配置流策略，然后应用到接口上。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1023。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：指定流策略的名称，不允许为系统预定义策略default。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| STCENABLE | 统计使能标志 | 可选必选说明：可选参数<br>参数含义：该参数用于使能或去使能流策略的统计状态。<br>NP卡场景下不支持流策略的统计功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- disable：去使能流策略统计。<br>- enable：使能流策略统计。<br>默认值：disable |
| SHAREMODE | 共享模式 | 可选必选说明：可选参数<br>参数含义：该参数用于配置某一个流策略的共享模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- unshared-mode：非共享模式，只统计该接口的策略统计。<br>- shared-mode：共享模式，累加应该相同策略的接口统计。<br>默认值：无<br>配置原则：如果不设置该参数，则流策略不指定共享模式。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MQCPOLICY]] · 流策略配置（MQCPOLICY）

## 使用实例

创建流量策略p1：

```
ADD MQCPOLICY:POLICYNAME="p1",STCENABLE=disable,SHAREMODE=unshared-mode;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-MQCPOLICY.md`
