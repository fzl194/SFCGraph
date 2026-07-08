---
id: UDG@20.15.2@MMLCommand@STR TLBRELBLINK
type: MMLCommand
name: STR TLBRELBLINK（启动触发HTTP服务端TCP链路重均衡检测及调整）
nf: UDG
version: 20.15.2
verb: STR
object_keyword: TLBRELBLINK
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP服务端负载管理
- 整系统负载管理
- 重均衡调整
status: active
---

# STR TLBRELBLINK（启动触发HTTP服务端TCP链路重均衡检测及调整）

## 功能

![](启动触发HTTP服务端TCP链路重均衡检测及调整（STR TLBRELBLINK）_15914281.assets/notice_3.0-zh-cn.png)

执行重均衡命令可能会拆链导致消息呼损。

该命令用于触发HTTP服务端TCP链路重均衡检测及调整。

> **说明**
> - 该命令执行后立即生效。
>
> - 若期望执行此命令触发重均衡检测及调整，则必须先执行[**LST TLBGLBCONF**](../全局属性/查询TLB全局配置（LST TLBGLBCONF）_15834601.md)命令确认TLBGLBSW开关打开，否则执行此命令将没有任何效果。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TLBRELBLINK]] · 触发HTTP服务端TCP链路重均衡检测及调整（TLBRELBLINK）

## 使用实例

如果服务端链路分布不均衡，希望调整链路分布，可以执行如下命令：

```
STR TLBRELBLINK:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/STR-TLBRELBLINK.md`
