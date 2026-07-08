---
id: UDG@20.15.2@ConfigObject@MSFAULTTOLERANCE
type: ConfigObject
name: MSFAULTTOLERANCE（故障检测参数）
nf: UDG
version: 20.15.2
object_name: MSFAULTTOLERANCE
object_kind: global_setting
status: active
---

# MSFAULTTOLERANCE（故障检测参数）

## 说明

![](设置故障检测参数（SET MSFAULTTOLERANCE）_09587879.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置小于默认值可能会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置正向监控和反向监控的超时时长，防脑裂自杀功能开关。

> **说明**
> - 该命令执行后立即生效。
>
> - 当前版本参数PROCESSFORWARD，PROCESSREVERSE的配置不生效。
> - 配置小于默认值可能会导致业务故障，建议保持默认值不变，如果要修改，建议配置不小于默认值。
> - 超时时长(毫秒)等于超时周期数乘以心跳周期乘以100。
> - 如需修改，要求进程级正向监控超时时长大于进程级反向监控超时时长，多连接正向监控超时时长大于多连接反向监控超时时长，多连接正向监控超时时长小于等于进程级正向监控超时时长，多连接反向监控超时时长小于等于进程级反向监控超时时长。
> - 如需修改正反向监控超时时长，建议通过命令[**LST MCSWITCH**](查询多连接开关配置数据（LST MCSWITCH）_46243299.md)查询多连接开关，如果开关开启，建议配置多连接正反向监控超时时长，否则配置进程级正反向监控超时时长。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | HBTYPE | HBCYCLE | HBTIMEOUT | SWITCH |
> | --- | --- | --- | --- |
> | PROCESSFORWARD | 5 | 12 | OFF |
> | PROCESSREVERSE | 5 | 10 | ON |
> | DOMAINFORWARD | 5 | 26 | OFF |
> | MCPROCESSFORWARD | 5 | 12 | OFF |
> | MCPROCESSREVERSE | 5 | 10 | ON |

## 操作本对象的命令

- [LST MSFAULTTOLERANCE](command/UDG/20.15.2/LST-MSFAULTTOLERANCE.md)
- [SET MSFAULTTOLERANCE](command/UDG/20.15.2/SET-MSFAULTTOLERANCE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询故障检测参数（LST-MSFAULTTOLERANCE）_09587939.md`
- 原始手册：`evidence/UDG/20.15.2/设置故障检测参数（SET-MSFAULTTOLERANCE）_09587879.md`
