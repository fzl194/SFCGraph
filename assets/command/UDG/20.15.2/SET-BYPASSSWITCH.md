---
id: UDG@20.15.2@MMLCommand@SET BYPASSSWITCH
type: MMLCommand
name: SET BYPASSSWITCH（设置节点自动进入BYPASS开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: BYPASSSWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- Bypass开关管理
status: active
---

# SET BYPASSSWITCH（设置节点自动进入BYPASS开关）

## 功能

![](设置节点自动进入BYPASS开关（SET BYPASSSWITCH）_97531594.assets/notice_3.0-zh-cn.png)

在存储故障场景，节点在磁盘故障后可能无法自动进入BYPASS状态，导致业务数据无法访问或业务中断，请慎重使用该命令。

本命令用于设置存储故障时，节点是否自动进入BYPASS状态。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

- 该功能仅支持华为虚拟化层软件FusionSphere，不支持第三方虚拟化层软件。
- 如果关闭此开关，存储故障修复后，存储故障告警无法自动恢复，需要通过手工进入、退出BYPASS触发恢复流程或重启节点（通过[**RST NODE**](../节点管理/节点复位（RST NODE）_71765322.md)命令）修复存储故障告警。
- 对于非BYPASS模式部署的节点，该命令也可以配置成功，但是由于此类节点不支持BYPASS，该配置暂不生效，当此类节点改造为BYPASS模式后生效。
- 该命令存在系统初始记录，参数的初始设置值如下：

| 参数名称 | 初始设置值 |
| --- | --- |
| 节点自动进入BYPASS开关 | 开启 |

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| BYPASSSWITCH | 节点自动进入BYPASS开关 | 可选必选说明：必选参数<br>参数含义：用于设置节点自动进入BYPASS开关。<br>取值范围：<br>- “ON(开启自动进入BYPASS功能)”<br>- “OFF(关闭自动进入BYPASS功能)”<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [节点自动进入BYPASS开关（BYPASSSWITCH）](configobject/UDG/20.15.2/BYPASSSWITCH.md)

## 使用实例

1. 打开节点自动进入BYPASS开关，操作成功示例。
  ```
  %%SET BYPASSSWITCH: BYPASSSWITCH=ON;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  详细信息  =  Success
  (结果个数 = 1)

  ---    END
  ```
2. 打开节点自动进入BYPASS开关，部分节点下发失败示例。
  ```
  %%SET BYPASSSWITCH: BYPASSSWITCH=ON;%%
  RETCODE = 130004  部分成功

  操作结果如下
  ------------
  节点名称  =  10.0.0.1
    节点IP  =  10.0.0.1
  详细信息  =  Failed
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置节点自动进入BYPASS开关（SET-BYPASSSWITCH）_97531594.md`
