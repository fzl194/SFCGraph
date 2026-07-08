---
id: UNC@20.15.2@MMLCommand@SET NODEREPSWITCH
type: MMLCommand
name: SET NODEREPSWITCH（节点设置自动修复开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NODEREPSWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 节点管理
status: active
---

# SET NODEREPSWITCH（节点设置自动修复开关）

## 功能

![](节点设置自动修复开关（SET NODEREPSWITCH）_72291815.assets/notice_3.0-zh-cn_2.png)

I层虚拟机HA开关打开场景下，执行该命令打开Error节点故障自愈或Unknown节点故障自愈开关，可能会导致I层与网元故障自愈冲突，请谨慎使用。

本命令用于设置节点故障自愈开关状态。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

- 开启Error节点故障自愈或Unknown节点故障自愈开关，需要关闭I层虚拟机HA开关，否则可能会导致I层与网元的故障自愈冲突。
- 该命令存在系统初始记录，参数的初始设置值如下：

| 故障自愈开关 | Error节点自愈开关 | Unknown节点自愈开关 |
| --- | --- | --- |
| 开启 | 关闭 | 关闭 |

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| REPAIRSWITCH | 故障自愈开关 | 可选必选说明：必选参数<br>参数含义：用于指示要设置的节点故障自愈开关状态。<br>取值范围：<br>- “ON(开启节点故障自愈)”<br>- “OFF(关闭节点故障自愈)”<br>默认值：<br>“ON(开启节点故障自愈)”<br>。<br>配置原则：关闭故障自愈开关会联动关闭Error节点自愈开关和Unknown节点自愈开关。 |
| REPERRORNODESWITCH | Error节点自愈开关 | 可选必选说明：该参数在<br>“REPAIRSWITCH”<br>配置为<br>“ON(开启节点故障自愈)”<br>时为条件可选参数。<br>参数含义：用于指示要设置的Error节点故障自愈开关状态。<br>取值范围：<br>- “ON(开启Error节点故障自愈)”<br>- “OFF(关闭Error节点故障自愈)”<br>默认值：无。<br>配置原则：无。 |
| REPUNKNOWNNODESWITCH | Unknown节点自愈开关 | 可选必选说明：该参数在<br>“REPAIRSWITCH”<br>配置为<br>“ON(开启节点故障自愈)”<br>时为条件可选参数。<br>参数含义：用于指示要设置的Unknown节点故障自愈开关状态。<br>取值范围：<br>- “ON(开启Unknown节点故障自愈)”<br>- “OFF(关闭Unknown节点故障自愈)”<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NODEREPSWITCH]] · 节点查询自动修复开关（NODEREPSWITCH）

## 使用实例

1. 关闭节点故障自愈开关。
  ```
  %%SET NODEREPSWITCH: REPAIRSWITCH=OFF;%% 
  RETCODE = 0  操作成功  

  ---    END
  ```
2. 打开节点故障自愈开关，打开Error节点自愈开关，打开Unknown节点自愈开关。
  ```
  %%SET NODEREPSWITCH: REPAIRSWITCH=ON, REPERRORNODESWITCH=ON, REPUNKNOWNNODESWITCH=ON;%% 
  RETCODE = 0  操作成功  

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NODEREPSWITCH.md`
