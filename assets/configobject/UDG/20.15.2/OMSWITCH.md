---
id: UDG@20.15.2@ConfigObject@OMSWITCH
type: ConfigObject
name: OMSWITCH（OM功能开关）
nf: UDG
version: 20.15.2
object_name: OMSWITCH
object_kind: global_setting
status: active
---

# OMSWITCH（OM功能开关）

## 说明

![](设置OM功能开关（SET OMSWITCH）_86362910.assets/notice_3.0-zh-cn.png)

执行该命令关闭功能开关时会导致 OM Portal 不可用，影响OM网络运维通道，请谨慎操作。

此命令用于设置OM功能开关的开关状态。

> **说明**
> - 关闭Portal功能开关会导致OM Portal不可用，无法通过OM Portal进行运维。
> - 该命令为二次授权命令，执行该命令前请先收集二次授权的账户和密码。
> - 关闭Portal功能开关会导致31943端口关闭，周边部件依赖该通道的功能不可用，如：
>     - LCM
>           - VNF更新
>           - VNF扩缩容
>           - VNF自愈
>           - VNF卸载
>     - 网管
>           - 网元信息采集
>           - 创建网元跟踪任务
>           - 同步、上传、激活、删除、下载网元license文件
>           - 网元备份
>           - 维护台跳转网元
>           - 网元证书激活、回退、导入
>           - syslog对接网元
>           - 网元MML配置导出下载
>           - 网元升级
>           - 网元话单查询和下载
>     - 4A对接
> - 关闭Portal功能开关后，如需开启，需要在网管界面执行此MML命令开启。

## 操作本对象的命令

- [LST OMSWITCH](command/UDG/20.15.2/LST-OMSWITCH.md)
- [SET OMSWITCH](command/UDG/20.15.2/SET-OMSWITCH.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OM功能开关（LST-OMSWITCH）_86522834.md`
- 原始手册：`evidence/UDG/20.15.2/设置OM功能开关（SET-OMSWITCH）_86362910.md`
