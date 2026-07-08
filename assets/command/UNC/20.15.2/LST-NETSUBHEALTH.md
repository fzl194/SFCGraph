---
id: UNC@20.15.2@MMLCommand@LST NETSUBHEALTH
type: MMLCommand
name: LST NETSUBHEALTH（查询网络亚健康参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NETSUBHEALTH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 节点管理
status: active
---

# LST NETSUBHEALTH（查询网络亚健康参数）

## 功能

本命令用于查询网络亚健康参数。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/NETSUBHEALTH]] · 网络亚健康参数（NETSUBHEALTH）

## 使用实例

1. 查询网络亚健康参数。
  ```
  %%LST NETSUBHEALTH:;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
              网络亚健康检测开关  =  开启
          网络亚健康故障自愈开关  =  开启
               上报告警阈值（%）  =  2
               清除告警阈值（%）  =  0.7
          一个错包数等价的丢包数  =  5
  网络亚健康故障检测周期（分钟）  =  5
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询网络亚健康参数（LST-NETSUBHEALTH）_88422284.md`
