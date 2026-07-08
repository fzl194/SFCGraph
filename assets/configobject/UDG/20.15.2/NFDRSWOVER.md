---
id: UDG@20.15.2@ConfigObject@NFDRSWOVER
type: ConfigObject
name: NFDRSWOVER（人工倒回命令）
nf: UDG
version: 20.15.2
object_name: NFDRSWOVER
object_kind: action
status: active
---

# NFDRSWOVER（人工倒回命令）

## 说明

![](启动人工倒回命令（STR NFDRSWOVER）_66924856.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当可能会导致用户接入异常网元影响业务，请谨慎使用并联系华为技术支持协助操作。

该命令用于启动基于业务KPI容灾倒换后的人工倒回操作。

> **说明**
> - 该命令执行后立即生效。
>
> - 执行该命令之前请先执行“[**DSP DBGHAFG**](显示HAFG相关信息（DSP DBGHAFG）_66924852.md): QUERYTYPE="APPID|DSP SELFSTATUS";”命令（其中APPID为可变内容，需要执行[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)查询获取执行倒回操作的网元的MEID），关注查询结果中“Status”是否为“normal”，如果是才可以执行本命令。若查询结果中“Status”不是为“normal”，还需通过本命令做强制倒回操作，则需联系华为技术支持。

## 操作本对象的命令

- [[command/UDG/20.15.2/STR-NFDRSWOVER]] · STR NFDRSWOVER

## 证据

- 原始手册：`evidence/UDG/20.15.2/启动人工倒回命令（STR-NFDRSWOVER）_66924856.md`
