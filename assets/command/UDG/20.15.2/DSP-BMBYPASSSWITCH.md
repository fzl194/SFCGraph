---
id: UDG@20.15.2@MMLCommand@DSP BMBYPASSSWITCH
type: MMLCommand
name: DSP BMBYPASSSWITCH（查询裸机节点自动进入BYPASS开关）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: BMBYPASSSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- Bypass开关管理
status: active
---

# DSP BMBYPASSSWITCH（查询裸机节点自动进入BYPASS开关）

## 功能

本命令用于查询存储故障时，裸机节点自动进入BYPASS开关的状态。

> **说明**
> 该命令仅在Full-stack裸机场景下支持。

> **说明**
> 无。

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/BMBYPASSSWITCH]] · 裸机节点自动进入BYPASS开关（BMBYPASSSWITCH）

## 使用实例

1. 查询自动进入BYPASS开关成功。
  ```
  %%DSP BMBYPASSSWITCH:;%% 
  RETCODE = 0  操作成功  
  操作结果如下 
  ------------ 
  节点名称                           节点IP       自动进入BYPASS开关
  e23d6419-cie-qb8it-dbf4467df-6vpwh XX.XX.XX.XX  开启
  e23d6419-cie-qb8it-dbf4467df-mx6cj XX.XX.XX.XX  开启
  e23d6419-cie-qb8it-dbf4467df-6vpwh XX.XX.XX.XX  开启             
  (结果个数 = 3) 
  ---    END
  ```
2. 查询自动进入BYPASS开关部分失败。
  ```
  %%DSP BMBYPASSSWITCH:;%% 
  RETCODE = 20026  部分失败  
  操作结果如下 
  ------------ 
  节点名称                           节点IP       自动进入BYPASS开关
  e23d6419-cie-qb8it-dbf4467df-6vpwh XX.XX.XX.XX  未知
  e23d6419-cie-qb8it-dbf4467df-mx6cj XX.XX.XX.XX  开启
  e23d6419-cie-qb8it-dbf4467df-6vpwh XX.XX.XX.XX  开启             
  (结果个数 = 3) 
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-BMBYPASSSWITCH.md`
