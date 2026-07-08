---
id: UDG@20.15.2@MMLCommand@SET PAEEXAMINATION
type: MMLCommand
name: SET PAEEXAMINATION（设置PAE故障检测使能开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PAEEXAMINATION
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# SET PAEEXAMINATION（设置PAE故障检测使能开关）

## 功能

该命令用于开启或关闭PAE故障检测功能。

PAE故障检测功能提供了转发线程死循环、通道过载、通道破坏、队列过载等检测能力。

使能PAE故障检测时，当PAE检测到故障后，会根据业务订阅的故障类型，将对应的故障上报给业务，同时PAE会根据故障恢复策略执行故障恢复。

在故障检测去使能的情况下，PAE不会对故障做检测。

建议保持该开关为默认的使能状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENABLEFLAG | 使能标志 | 可选必选说明：必选参数<br>参数含义：该参数用于开启和关闭故障检测功能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：TRUE |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PAEEXAMINATION]] · PAE故障检测使能配置（PAEEXAMINATION）

## 使用实例

去使能PAE故障检测功能：

```
SET PAEEXAMINATION:ENABLEFLAG=FALSE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-PAEEXAMINATION.md`
