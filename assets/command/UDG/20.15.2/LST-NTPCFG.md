---
id: UDG@20.15.2@MMLCommand@LST NTPCFG
type: MMLCommand
name: LST NTPCFG（查询NTP时间同步参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NTPCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- NTP参数管理
status: active
---

# LST NTPCFG（查询NTP时间同步参数）

## 功能

本命令用于查询时间同步告警阈值、时间偏差告警阈值及自动同步策略。

> **说明**
> 无

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| OPRTYPE | NTP参数选项 | 可选必选说明：必选参数。<br>参数含义：用于查询目前的时间同步告警阈值和自动同步策略。<br>取值范围：<br>- “TIMESYNC(时间同步告警阈值)”：查询时间同步告警阈值和时间偏差告警阈值。<br>- “SYNCSTRATEGY(自动同步策略)”：查询自动同步策略。<br>默认值：<br>“TIMESYNC(时间同步告警阈值)”<br>。<br>配置原则：无。 |

## 操作的配置对象

- [NTP时间同步参数（NTPCFG）](configobject/UDG/20.15.2/NTPCFG.md)

## 使用实例

1. 查询时间同步告警阈值：
  LST NTPCFG: OPRTYPE=TIMESYNC;
  ```
  %%LST NTPCFG: OPRTYPE=TIMESYNC;%% 
  RETCODE = 0  操作成功

  操作结果如下 
  ------------ 
               NTP参数选项  =  时间同步告警阈值 
  自动同步告警阈值（毫秒）  =  8000 
  时间偏差告警阈值（毫秒）  =  4000 
  (结果个数 = 1)

    ---    END
  ```
2. 查询自动同步策略：
  LST NTPCFG: OPRTYPE=SYNCSTRATEGY;
  ```
  %%LST NTPCFG: OPRTYPE=SYNCSTRATEGY;%% 
  RETCODE = 0  操作成功  

  操作结果如下 
  ------------ 
                     NTP参数选项  =  自动同步策略
      超过阈值后是否自动同步开关  =  开启
                    同步周期(秒)  =  60 
  (结果个数 = 1)  

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询NTP时间同步参数(LST-NTPCFG)_67679934.md`
