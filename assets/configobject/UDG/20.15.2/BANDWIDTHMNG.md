---
id: UDG@20.15.2@ConfigObject@BANDWIDTHMNG
type: ConfigObject
name: BANDWIDTHMNG（带宽管理参数）
nf: UDG
version: 20.15.2
object_name: BANDWIDTHMNG
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# BANDWIDTHMNG（带宽管理参数）

## 说明

**适用NF：PGW-U、UPF**

![](设置带宽管理参数（SET BANDWIDTHMNG）_82837465.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，Range发生变化后，其他带宽管理命令（bwmcontroller，bwmservice等）也需要同步修改。

该命令用于设置带宽控制器中用户组级业务带宽和连接数配置的生效范围，以及带宽资源动态统计和调整周期。

系统由多个业务处理单元组成，每个处理单元都是独立运行，如果带宽控制器中用户组级业务带宽和连接数是整机配置，就需要周期性统计汇总各业务处理单元的业务使用状态，然后统计结果，动态调整每个单元可以使用的资源，如CAR桶参数、连接数阈值等。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-BANDWIDTHMNG]] · LST BANDWIDTHMNG
- [[command/UDG/20.15.2/SET-BANDWIDTHMNG]] · SET BANDWIDTHMNG

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询带宽管理参数（LST-BANDWIDTHMNG）_86526893.md`
- 原始手册：`evidence/UDG/20.15.2/设置带宽管理参数（SET-BANDWIDTHMNG）_82837465.md`
