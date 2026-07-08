---
id: UDG@20.15.2@MMLCommand@LST NODEREPSWITCH
type: MMLCommand
name: LST NODEREPSWITCH（节点查询自动修复开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NODEREPSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 节点管理
status: active
---

# LST NODEREPSWITCH（节点查询自动修复开关）

## 功能

本命令用于查询节点故障自愈开关状态。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [节点查询自动修复开关（NODEREPSWITCH）](configobject/UDG/20.15.2/NODEREPSWITCH.md)

## 使用实例

1. 查询系统节点故障自愈开关：
  ```
  %%LST NODEREPSWITCH:;%%
  RETCODE = 0  操作成功  

         节点故障自愈开关  =  开启
    Error节点故障自愈开关  =  关闭
  Unknown节点故障自愈开关  =  关闭
  (结果个数 = 1)  
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/节点查询自动修复开关（LST-NODEREPSWITCH）_72291814.md`
