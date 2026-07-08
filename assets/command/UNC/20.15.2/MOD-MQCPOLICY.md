---
id: UNC@20.15.2@MMLCommand@MOD MQCPOLICY
type: MMLCommand
name: MOD MQCPOLICY（修改流策略配置）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD MQCPOLICY（修改流策略配置）

## 功能

该命令用于修改流策略配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：指定流策略的名称，不允许为系统预定义策略default。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| STCENABLE | 统计使能标志 | 可选必选说明：可选参数<br>参数含义：该参数用于使能或去使能流策略的统计状态。NP卡场景下不支持流策略的统计功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- disable：去使能流策略统计。<br>- enable：使能流策略统计。<br>默认值：无 |
| SHAREMODE | 共享模式 | 可选必选说明：可选参数<br>参数含义：该参数用于配置某一个流策略的共享模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- unshared-mode：非共享模式，只统计该接口的策略统计。<br>- shared-mode：共享模式，累加应该相同策略的接口统计。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MQCPOLICY]] · 流策略配置（MQCPOLICY）

## 使用实例

修改流策略p1的配置：

```
MOD MQCPOLICY:POLICYNAME="p1",STCENABLE=enable,SHAREMODE=unshared-mode;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-MQCPOLICY.md`
