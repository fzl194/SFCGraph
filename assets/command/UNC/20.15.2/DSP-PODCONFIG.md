---
id: UNC@20.15.2@MMLCommand@DSP PODCONFIG
type: MMLCommand
name: DSP PODCONFIG（POD配置查询）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PODCONFIG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- Pod管理
status: active
---

# DSP PODCONFIG（POD配置查询）

## 功能

该命令用于查询系统修复Pod功能的开关状态。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| SWITCHTYPE | 开关类型 | 可选必选说明：可选参数。<br>参数含义：用于设置修复开关的类型。<br>取值范围：<br>- FixSwitch(实例故障修复开关)：实例故障修复开关。<br>- RebuildingSwitch (网络亚健康修复开关)：网络亚健康修复开关。NOTE:RebuildingSwitch (网络亚健康修复开关)仅在Full-stack裸机场景下支持。<br>默认值：FixSwitch。<br>配置原则：无。 |

## 操作的配置对象

- [POD配置查询（PODCONFIG）](configobject/UNC/20.15.2/PODCONFIG.md)

## 使用实例

使用实例

1. 查询实例故障修复开关状态：
  ```
  DSP PODCONFIG: SWITCHTYPE=FixSwitch;
  ```
  ```
  %%DSP PODCONFIG: SWITCHTYPE=FixSwitch;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  实例故障修复开关  =  OFF
  (结果个数 = 1)
  ---    END
  ```
2. 查询网络亚健康修复开关状态与重建周期：
  ```
  DSP PODCONFIG: SWITCHTYPE=RebuildingSwitch;
  ```
  ```
  %%DSP PODCONFIG: SWITCHTYPE=RebuildingSwitch;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
    网络亚健康修复开关  =  OFF
              重建周期  =  10
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/POD配置查询（DSP-PODCONFIG）_95277150.md`
