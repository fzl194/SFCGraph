---
id: UDG@20.15.2@MMLCommand@SET PODCONFIG
type: MMLCommand
name: SET PODCONFIG（POD配置设置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PODCONFIG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- Pod管理
status: active
---

# SET PODCONFIG（POD配置设置）

## 功能

![](POD配置设置（SET PODCONFIG）_95117138.assets/notice_3.0-zh-cn.png)

设置系统的修复Pod功能开关状态，可能会导致业务受到影响，请谨慎使用该命令。

本命令用于设置系统的修复Pod功能开关状态。

> **说明**
> - “修复开关”的系统初始值为“ON”。
> - 当服务实例出现异常时，“修复开关”由“OFF”设置为“ON”，系统会在30分钟后对故障Pod进行修复。
> - “修复开关”打开时，如果服务实例出现异常从注册中心下线，那么服务治理模块会修复异常实例所在Pod来自愈业务；“修复开关”关闭时，不会修复异常实例所在的Pod。
> - 在网元应用升级或回退、补丁安装或回退过程中，“修复开关”应当处于关闭状态，因此请勿执行此命令。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| PODRESTORATION | 修复开关 | 可选必选说明：必选参数。<br>参数含义：用于设置修复Pod功能开关的状态。<br>取值范围：<br>- ON(打开)：打开。<br>- OFF(关闭)：关闭。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PODCONFIG]] · POD配置查询（PODCONFIG）

## 使用实例

1. 设置系统修复Pod的功能为关闭状态：
  ```
  %%SET PODCONFIG: PODRESTORATION=OFF;%%
  RETCODE = 0  操作成功

  ---    END
  ```
2. 设置系统修复Pod的功能为打开状态：
  ```
  %%SET PODCONFIG: PODRESTORATION=ON;%%
  RETCODE = 0  操作成功

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-PODCONFIG.md`
