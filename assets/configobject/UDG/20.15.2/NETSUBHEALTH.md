---
id: UDG@20.15.2@ConfigObject@NETSUBHEALTH
type: ConfigObject
name: NETSUBHEALTH（网络亚健康参数）
nf: UDG
version: 20.15.2
object_name: NETSUBHEALTH
object_kind: global_setting
status: active
---

# NETSUBHEALTH（网络亚健康参数）

## 说明

![](设置网络亚健康参数（SET NETSUBHEALTH）_88773788.assets/notice_3.0-zh-cn.png)

修改网络亚健康参数有可能导致误报告警或漏报告警，业务报文丢失可能无法及时发现，请慎重使用该命令。

本命令用于设置网络亚健康参数，也可以在OM Portal菜单界面选择 “ 监控分析 > 节点健康检查 > 网络亚健康检查 ” 进行设置。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

> **说明**
> - 本命令设置完成后需间隔至少五分钟后再次设置。
> - 该命令存在系统初始记录，参数的初始设置值如下：
>
> | 网络亚健康检测开关 | 网络亚健康故障自愈开关 | 上报告警阈值（%） | 清除告警阈值（%） | 一个错包数等价的丢包数 | 网络亚健康故障检测周期（分钟） |
> | --- | --- | --- | --- | --- | --- |
> | 开启 | 开启 | 2 | 0.7 | 5 | 5 |

## 操作本对象的命令

- [LST NETSUBHEALTH](command/UDG/20.15.2/LST-NETSUBHEALTH.md)
- [SET NETSUBHEALTH](command/UDG/20.15.2/SET-NETSUBHEALTH.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询网络亚健康参数（LST-NETSUBHEALTH）_88422284.md`
- 原始手册：`evidence/UDG/20.15.2/设置网络亚健康参数（SET-NETSUBHEALTH）_88773788.md`
