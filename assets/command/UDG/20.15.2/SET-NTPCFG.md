---
id: UDG@20.15.2@MMLCommand@SET NTPCFG
type: MMLCommand
name: SET NTPCFG（配置NTP时间同步参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NTPCFG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- NTP参数管理
status: active
---

# SET NTPCFG（配置NTP时间同步参数）

## 功能

![](配置NTP时间同步参数(SET NTPCFG)_67679933.assets/notice_3.0-zh-cn.png)

修改时间同步告警阈值参数会影响NTP相关告警的上报。

系统开启自动同步策略后，每个同步周期会无条件与NTP服务器同步一次时间。

本命令用于设置NTP时间同步参数。

本命令的使用场景为：在开局或日常的操作维护活动中，操作员可使用本命令配置NTP服务器时间同步参数。

> **说明**
> - 参数设置中自动同步策略的开关应当与FusionStage中时间设置的同步策略开关保持一致。
> - 在缺省的情况下，系统在初始化的时候就已经在配置数据库中预置了NTP时间同步参数相关配置。
>     - “自动同步告警阈值(毫秒)”参数的初始设置是3000。
>     - “时间偏差告警阈值(毫秒)”参数的初始设置是3000。
>     - “自动同步策略”参数的初始设置是OFF(关闭)。
>     - “同步周期(秒)”参数的初始设置是60。
> - 需要指出的是，本命令中所描述的初始设置值，是指操作员通过[**LST NTPCFG**](查询NTP时间同步参数(LST NTPCFG)_67679934.md)命令后得出系统在初始化时的阈值参数值。
> - 禁止在升级、打补丁、回退过程中、升级观察期内配置NTP时间同步参数

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| OPRTYPE | NTP参数选项 | 可选必选说明：必选参数。<br>参数含义：用于指定设置的参数类型 。<br>取值范围：<br>- “TIMESYNC(时间同步告警阈值)”：对自动同步告警阈值和时间偏差告警阈值进行设置。<br>- “SYNCSTRATEGY(自动同步策略)”：对自动同步策略进行设置。<br>默认值：<br>“TIMESYNC(时间同步告警阈值)”<br>。<br>配置原则：无。 |
| SYNCTHRESHOLD | 自动同步告警阈值(毫秒) | 可选必选说明：该参数在<br>“NTP参数选项 ”<br>配置为<br>“TIMESYNC(时间同步告警阈值)”<br>时为条件必选参数。<br>参数含义：用于具体定义自动同步的阈值告警阈值。当超过阈值的时候，系统不会与NTP服务器进行时间同步。超过自动同步告警阈值之后系统会自动上报告警。<br>取值范围：100~10000 。<br>默认值：无。<br>配置原则：<br>- 该参数不能为空。<br>- 仅当本命令中的“NTP参数选项”参数为“TIMESYNC(时间同步告警阈值)”时该参数有效。 |
| OFFSETTHRESHOLD | 时间偏差告警阈值(毫秒) | 可选必选说明：该参数在<br>“NTP参数选项 ”<br>配置为<br>“TIMESYNC(时间同步告警阈值)”<br>时为条件必选参数。<br>参数含义：用于定义时间偏差发出告警时的所需的阈值。<br>取值范围：50~5000 。<br>默认值：无。<br>配置原则：<br>- 时间偏差告警阈值不能为空。<br>- 仅当本命令中的“NTP参数选项”参数为“TIMESYNC(时间同步告警阈值)”时该参数有效。 |
| NTPCONFIG | 超过阈值后是否自动同步开关 | 可选必选说明：该参数在<br>“NTP参数选项 ”<br>配置为<br>“SYNCSTRATEGY(自动同步策略)”<br>时为条件必选参数。<br>参数含义：选择自动同步策略。<br>取值范围：<br>- “OFF(关闭)”：超过自动同步告警阈值时也不进行同步。<br>- “ON(开启)”：不论是否超过自动同步告警阈值都会进行同步。<br>默认值：<br>“OFF(关闭)”<br>。<br>配置原则：<br>- 仅当本命令中的“NTP参数选项”参数为“SYNCSTRATEGY(自动同步策略)”时该参数有效。 |
| SYNCPERIOD | 同步周期(秒) | 可选必选说明：该参数在<br>“NTP参数选项 ”<br>配置为<br>“SYNCSTRATEGY(自动同步策略)”<br>时为条件必选参数。<br>参数含义：用于设置主节点与外部时钟源同步的间隔周期。<br>取值范围：60~600。<br>默认值：<br>“60”<br>。<br>配置原则：<br>- 仅当本命令中的“NTP参数选项”参数为“SYNCSTRATEGY(自动同步策略)”时该参数有效。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NTPCFG]] · NTP时间同步参数（NTPCFG）

## 使用实例

1. 设置时间同步告警阈值，分别设置自动同步告警阈值和时间偏差告警阈值为8000、4000：
  SET NTPCFG: OPRTYPE=TIMESYNC, SYNCTHRESHOLD=8000, OFFSETTHRESHOLD=4000;
  ```
  %%SET NTPCFG: OPRTYPE=TIMESYNC, SYNCTHRESHOLD=8000, OFFSETTHRESHOLD=4000;%% 
  RETCODE = 0  操作成功
  
  ---    END
  ```
2. 设置自动同步策略为"ON"，同步周期值为60：
  SET NTPCFG: OPRTYPE=SYNCSTRATEGY, NTPCONFIG=ON, SYNCPERIOD=60;
  ```
  %%SET NTPCFG: OPRTYPE=SYNCSTRATEGY, NTPCONFIG=ON, SYNCPERIOD=60;%% 
  RETCODE = 0  操作成功  

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/配置NTP时间同步参数(SET-NTPCFG)_67679933.md`
