---
id: UNC@20.15.2@MMLCommand@RMV NSEUSR
type: MMLCommand
name: RMV NSEUSR（删除NSE列表下的用户）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NSEUSR
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- MS上下文管理
- 基于NSE的MS上下文管理
status: active
---

# RMV NSEUSR（删除NSE列表下的用户）

## 功能

![](删除NSE列表下的用户(RMV NSEUSR)_26305832.assets/notice_3.0-zh-cn_2.png)

- 删除任务一旦启动后无法强行终止。
- 该操作会删除指定NSE列表下的所有用户，导致这些用户被强制下线，请谨慎操作。

**适用网元：SGSN**

启动删除任务，删除 [**ADD NSELST**](增加NSE列表(ADD NSELST)_72345621.md) NSE列表下所有的用户。该命令执行后，系统启动任务，逐个扫描NSE列表中的所有NSEI，分离系统中属于这些NSE的用户。

## 注意事项

- 如果NSE列表（[**LST NSELST**](查询NSE列表(LST NSELST)_72225701.md)）为空，则任务启动失败。
- 删除任务一旦启动后无法强行终止。
- 删除任务处理需要较长时间，请耐心等待。通过命令[**DSP NSEUSR**](显示删除NSE列表下的用户任务运行状态(DSP NSEUSR)_72345623.md)可以查询任务运行状态和剩余时间。
- 该操作会删除指定NSE列表下的所有用户，导致这些用户被强制下线，请谨慎操作。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSEUSR]] · NSE列表下的用户（NSEUSR）

## 使用实例

启动删除NSE列表下的用户的任务：

RMV NSEUSR:;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NSEUSR.md`
