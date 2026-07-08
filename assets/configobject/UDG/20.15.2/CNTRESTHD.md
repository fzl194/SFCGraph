---
id: UDG@20.15.2@ConfigObject@CNTRESTHD
type: ConfigObject
name: CNTRESTHD（容器资源阈值）
nf: UDG
version: 20.15.2
object_name: CNTRESTHD
object_kind: global_setting
status: active
---

# CNTRESTHD（容器资源阈值）

## 说明

![](设置容器资源阈值（SET CNTRESTHD）_61025381.assets/notice_3.0-zh-cn.png)

告警阈值的调整会影响告警的触发条件，请注意设置合理的告警阈值。

该命令用于设置容器的资源告警上报、清除阈值，CPU突变检测阈值和检测间隔，容器网络亚健康资源检测。

> **说明**
> - 告警阈值会持久化写入到Gauss数据库中，各容器阈值更新会有一定的延迟，可通过[**DSP CNTRESSTAT**](查询容器资源信息（DSP CNTRESSTAT）_60785913.md)命令查看。
> - 本命令若按照“容器类型”配置后再次按照“网元级”配置，则不覆盖该网元下的“容器类型”的配置。
>
> - 该命令系统初始值参数设置如下：
>
> | 参数名称 | 初始值 |
> | --- | --- |
> | 网络亚健康告警开关 | on |
> | 单链路丢包率阈值(%) | 2.0 |
> | 网络亚健康告警上报阈值(%) | 70 |
> | 网络亚健康告警清除阈值(%) | 30 |
> | 网络亚健康响应阈值(ms) | 200 |

## 操作本对象的命令

- [SET CNTRESTHD](command/UDG/20.15.2/SET-CNTRESTHD.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置容器资源阈值（SET-CNTRESTHD）_61025381.md`
