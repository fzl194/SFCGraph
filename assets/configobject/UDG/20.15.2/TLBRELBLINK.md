---
id: UDG@20.15.2@ConfigObject@TLBRELBLINK
type: ConfigObject
name: TLBRELBLINK（触发HTTP服务端TCP链路重均衡检测及调整）
nf: UDG
version: 20.15.2
object_name: TLBRELBLINK
object_kind: action
status: active
---

# TLBRELBLINK（触发HTTP服务端TCP链路重均衡检测及调整）

## 说明

![](启动触发HTTP服务端TCP链路重均衡检测及调整（STR TLBRELBLINK）_15914281.assets/notice_3.0-zh-cn.png)

执行重均衡命令可能会拆链导致消息呼损。

该命令用于触发HTTP服务端TCP链路重均衡检测及调整。

> **说明**
> - 该命令执行后立即生效。
>
> - 若期望执行此命令触发重均衡检测及调整，则必须先执行[**LST TLBGLBCONF**](../全局属性/查询TLB全局配置（LST TLBGLBCONF）_15834601.md)命令确认TLBGLBSW开关打开，否则执行此命令将没有任何效果。

## 操作本对象的命令

- [[command/UDG/20.15.2/STR-TLBRELBLINK]] · STR TLBRELBLINK

## 证据

- 原始手册：`evidence/UDG/20.15.2/启动触发HTTP服务端TCP链路重均衡检测及调整（STR-TLBRELBLINK）_15914281.md`
