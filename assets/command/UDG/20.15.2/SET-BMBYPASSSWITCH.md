---
id: UDG@20.15.2@MMLCommand@SET BMBYPASSSWITCH
type: MMLCommand
name: SET BMBYPASSSWITCH（设置裸机节点自动进入BYPASS开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: BMBYPASSSWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- Bypass开关管理
status: active
---

# SET BMBYPASSSWITCH（设置裸机节点自动进入BYPASS开关）

## 功能

![](设置裸机节点自动进入BYPASS开关（SET BMBYPASSSWITCH）_58120294.assets/notice_3.0-zh-cn.png)

在存储故障场景，节点可能无法自动进入BYPASS状态，请慎重使用该命令。

本命令用于设置存储故障时，裸机节点是否自动进入BYPASS状态。

> **说明**
> 该命令仅在Full-stack裸机场景下支持。

> **说明**
> - 如果关闭此开关，存储故障修复后，存储故障告警无法自动恢复，需要通过手工进入、退出BYPASS触发恢复流程或重启节点修复存储故障告警。
> - 该命令存在系统初始记录，参数的初始设置值如下：
>
> | 参数名称 | 初始设置值 |
> | --- | --- |
> | 自动进入BYPASS开关 | 开启 |

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| SSW_BYPASS_SWITCH | 自动进入BYPASS开关 | 可选必选说明：必选参数<br>参数含义：用于设置节点自动进入BYPASS开关的状态。<br>取值范围：<br>- “ON(开启自动进入BYPASS功能)”<br>- “OFF(关闭自动进入BYPASS功能)”<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [裸机节点自动进入BYPASS开关（BMBYPASSSWITCH）](configobject/UDG/20.15.2/BMBYPASSSWITCH.md)

## 使用实例

1. 设置自动进入BYPASS开关。
  ```
  %%SET BMBYPASSSWITCH: SSW_BYPASS_SWITCH=ON;%% 
  RETCODE = 0  操作成功  
  操作结果如下 
  ------------ 
  节点名称                           节点IP      详细信息    
  e23d6419-cie-qb8it-dbf4467df-6vpwh XX.XX.XX.XX Success
  e23d6419-cie-qb8it-dbf4467df-mx6cj XX.XX.XX.XX Success
  e23d6419-cie-qb8it-dbf4467df-6vpwh XX.XX.XX.XX Success             
  (结果个数 = 3) 
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置裸机节点自动进入BYPASS开关（SET-BMBYPASSSWITCH）_58120294.md`
