---
id: UDG@20.15.2@ConfigObject@SDRPARAMS
type: ConfigObject
name: SDRPARAMS（SDR参数）
nf: UDG
version: 20.15.2
object_name: SDRPARAMS
object_kind: global_setting
status: active
---

# SDRPARAMS（SDR参数）

## 说明

![](设置SDR参数（SET SDRPARAMS）_09587912.assets/notice_3.0-zh-cn.png)

该命令是高危命令，操作不当可能会导致业务受损，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置SDR服务的相关参数。SDR主要功能是为微服务间提供分布式透明通信。

> **说明**
> - 该命令执行后立即生效。
>
> - SDR参数ID为0和6的功能该版本不支持。
> - SDR参数ID为4的功能，其对应的PARAVALUE1表示Fabric平面可靠传输的校验和开关。修改PARAVALUE1的值后，请全量复位POD，否则会上报系统命令配置修改未生效告警。
> - 默认使用系统初始值，如需修改，请联系华为技术支持协助操作。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | PARAID | PARAVALUE1 | PARAVALUE2 |
> | --- | --- | --- |
> | 0 | 0 | 0 |
> | 1 | 1 | 0 |
> | 2 | 0 | 0 |
> | 3 | 1 | 0 |
> | 4 | 0 | 0 |
> | 5 | 1 | 0 |
> | 6 | 1 | 10 |
> | 7 | 1 | 0 |
> | 8 | 0 | 0 |
> | 9 | 1 | 0 |
> | 10 | 1 | 5 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-SDRPARAMS]] · LST SDRPARAMS
- [[command/UDG/20.15.2/SET-SDRPARAMS]] · SET SDRPARAMS

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SDR参数（LST-SDRPARAMS）_09587932.md`
- 原始手册：`evidence/UDG/20.15.2/设置SDR参数（SET-SDRPARAMS）_09587912.md`
