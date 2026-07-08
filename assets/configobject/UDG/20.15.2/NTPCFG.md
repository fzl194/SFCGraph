---
id: UDG@20.15.2@ConfigObject@NTPCFG
type: ConfigObject
name: NTPCFG（NTP时间同步参数）
nf: UDG
version: 20.15.2
object_name: NTPCFG
object_kind: global_setting
status: active
---

# NTPCFG（NTP时间同步参数）

## 说明

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

## 操作本对象的命令

- [LST NTPCFG](command/UDG/20.15.2/LST-NTPCFG.md)
- [SET NTPCFG](command/UDG/20.15.2/SET-NTPCFG.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询NTP时间同步参数(LST-NTPCFG)_67679934.md`
- 原始手册：`evidence/UDG/20.15.2/配置NTP时间同步参数(SET-NTPCFG)_67679933.md`
