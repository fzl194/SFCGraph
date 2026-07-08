---
id: UNC@20.15.2@ConfigObject@AUTOCONFIG
type: ConfigObject
name: AUTOCONFIG（自动配置开关）
nf: UNC
version: 20.15.2
object_name: AUTOCONFIG
object_kind: global_setting
status: active
---

# AUTOCONFIG（自动配置开关）

## 说明

![](设置自动配置开关（SET AUTOCONFIG）_00840833.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会导致自动化配置相关业务失败，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置自动配置开关，开关打开自动化配置会运行，开关未关闭的情况下如果执行主备倒换、VNRS重启或扩缩容，自动化配置会运行。

1、自动化配置在系统初始配置或设备扩容时使用。相比手工配置，自动化配置只需用户预先指定业务规划参数（IP地址段分配、目的地址、下一跳网关等），即可在系统初始化或新增资源时自动生成接口IP路由等配置，无需再依次为每个接口手动配置。

2、使用自动化配置，需要先部署自动化配置接口模板（ADD AUTOSCALINGSERVICE），再根据需求部署其他自动化配置模板（如静态路由自动化配置ADD AUTOSCALINGSRROUTE、BFD会话自动化配置ADD AUTOSCALINGBFD等），然后执行SET AUTOCONFIG命令打开自动化配置开关。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-AUTOCONFIG]] · LST AUTOCONFIG
- [[command/UNC/20.15.2/SET-AUTOCONFIG]] · SET AUTOCONFIG

## 证据

- 原始手册：`evidence/UNC/20.15.2/AUTOCONFIG.md`
- 原始手册：`evidence/UNC/20.15.2/AUTOCONFIG.md`
