---
id: UDG@20.15.2@MMLCommand@DSP BYPASSSWITCH
type: MMLCommand
name: DSP BYPASSSWITCH（查询节点自动进入BYPASS开关）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: BYPASSSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- Bypass开关管理
status: active
---

# DSP BYPASSSWITCH（查询节点自动进入BYPASS开关）

## 功能

![](查询节点自动进入BYPASS开关（DSP BYPASSSWITCH）_97531593.assets/notice_3.0-zh-cn.png)

该功能仅支持华为虚拟化层软件FusionSphere，不支持第三方虚拟化层软件。

本命令用于查询存储故障时，节点自动进入BYPASS开关的状态。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/BYPASSSWITCH]] · 节点自动进入BYPASS开关（BYPASSSWITCH）

## 使用实例

1. 查询节点自动进入BYPASS开关，操作成功示例。
  ```
  %%DSP BYPASSSWITCH:;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  节点名称  节点IP    节点自动进入BYPASS开关  

  10.0.0.1  10.0.0.1  开启                      
  10.0.0.2  10.0.0.2  开启                      
  10.0.0.3  10.0.0.3  开启                      
  (结果个数 = 3)

  ---    END
  ```
2. 查询节点自动进入BYPASS开关，部分成功示例。
  ```
  %%DSP BYPASSSWITCH:;%%
  RETCODE = 130004  部分成功

  操作结果如下
  ------------
  节点名称  节点IP    节点自动进入BYPASS开关  

  10.0.0.1  10.0.0.1  未知                 
  10.0.0.2  10.0.0.2  开启                      
  10.0.0.2  10.0.0.3  开启                      
  (结果个数 = 3)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询节点自动进入BYPASS开关（DSP-BYPASSSWITCH）_97531593.md`
