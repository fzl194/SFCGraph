---
id: UNC@20.15.2@MMLCommand@SET PODCONFIG
type: MMLCommand
name: SET PODCONFIG（POD配置设置）
nf: UNC
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

![](POD配置设置（SET PODCONFIG）_95117138.assets/notice_3.0-zh-cn_2.png)

设置系统的修复Pod功能开关状态，可能会导致业务受到影响，请谨慎使用该命令。

本命令用于设置系统的修复Pod功能开关状态。

## 注意事项

- “实例故障修复开关”的系统初始值为“ON”。
- 当服务实例出现异常时，“实例故障修复开关”由“OFF”设置为“ON”，系统会在30分钟后对故障Pod进行修复。
- “实例故障修复开关”打开时，如果服务实例出现异常从注册中心下线，那么服务治理模块会修复异常实例所在Pod来自愈业务；“实例故障修复开关”关闭时，不会修复异常实例所在的Pod。
- 在网元应用升级或回退、补丁安装或回退过程中，“实例故障修复开关”应当处于关闭状态，因此请勿执行此命令。
- “网络亚健康修复开关”的系统初始值为“OFF”**，"重建周期"**的初始值为"10"。
- “网络亚健康修复开关”打开后只对在RSCheck中配置了容器网络亚健康探测的POD生效。
- 系统盘重建场景，“网络亚健康修复开关”与**"重建周期"**会丢失，需要重新设置。
- “网络亚健康修复开关”打开后需要设置“[网络亚健康告警上报阈值(%)](../../设备管理/容器管理/设置容器资源阈值（SET CNTRESTHD）_61025381.md)”到100。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| SWITCHTYPE | 开关类型 | 可选必选说明：可选参数。<br>参数含义：用于设置修复开关的类型。<br>取值范围：<br>- FixSwitch(实例故障修复开关)：实例故障修复开关。<br>- RebuildingSwitch (网络亚健康修复开关)：网络亚健康修复开关。NOTE:RebuildingSwitch (网络亚健康修复开关)仅在Full-stack裸机场景下支持。<br>SWITCHTYPE参数不支持选择空选项，空选项只用于在机机命令下发。<br>默认值：FixSwitch。<br>配置原则：无。 |
| PODRESTORATION | 实例故障修复开关 | 可选必选说明：该参数在<br>**开关类型**<br>取值为<br>**FixSwitch(实例故障修复开关)**<br>时为必选参数。<br>参数含义：用于设置实例故障修复开关的状态。<br>取值范围：<br>- ON(打开)：打开。<br>- OFF(关闭)：关闭。<br>默认值：无。<br>配置原则：无。 |
| PODREBUILD | 网络亚健康修复开关 | 可选必选说明：该参数在<br>**开关类型**<br>取值为RebuildingSwitch (网络亚健康修复开关)时为必选参数。<br>参数含义：用于设置网络亚健康修复开关的状态。<br>取值范围：<br>- ON(打开)：打开。<br>- OFF(关闭)：关闭。<br>默认值：无。<br>配置原则：无。 |
| REBUILDTIME | 重建周期 | 可选必选说明：该参数在<br>**网络亚健康修复开关**<br>取值为ON(打开)时为必选参数。<br>参数含义：用于设置网络亚健康修复状态下POD重建的周期。<br>取值范围：1-300。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PODCONFIG]] · POD配置查询（PODCONFIG）

## 使用实例

1. 设置实例故障修复开关状态：
  ```
  SET PODCONFIG: SWITCHTYPE=FixSwitch, PODRESTORATION=ON;
  ```
  ```
  %%SET PODCONFIG: SWITCHTYPE=FixSwitch, PODRESTORATION=ON;%%
  RETCODE = 0  操作成功

  ---    END
  ```
2. 设置网络亚健康修复开关状态与重建周期：
  ```
  SET PODCONFIG: SWITCHTYPE=RebuildingSwitch, PODREBUILD=ON, REBUILDTIME=20;
  ```
  ```
  %%SET PODCONFIG: SWITCHTYPE=RebuildingSwitch, PODREBUILD=ON, REBUILDTIME=20;%%
  RETCODE = 0  操作成功

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/POD配置设置（SET-PODCONFIG）_95117138.md`
