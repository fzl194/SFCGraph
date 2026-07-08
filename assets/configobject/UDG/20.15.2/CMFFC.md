---
id: UDG@20.15.2@ConfigObject@CMFFC
type: ConfigObject
name: CMFFC（CMF流控参数）
nf: UDG
version: 20.15.2
object_name: CMFFC
object_kind: global_setting
status: active
---

# CMFFC（CMF流控参数）

## 说明

![](设置CMF流控参数（SET CMFFC）_68820021.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置小于默认值可能会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置开启CMF流控的CPU阈值、停止CMF流控的CPU阈值和停控时间窗。

> **说明**
> - 该命令执行后立即生效。
>
> - CMF Pod单节点部署时不支持CMF流控，第三方CaaS场景不支持CMF流控，CSPEdge裸机场景不支持CMF流控。
> - 未执行本命令时，CMF流控参数默认配置为代码默认值，可通过[**DSP DBGHAFD**](显示HAFD调试命令结果（DSP DBGHAFD）_94730404.md)命令查询实际运行的值。查询时，参数DEBUGNAME取值为"cmf fc config"。
> - 配置修改可能会导致系统故障，建议保持参数初始设置值不变。
> - 如需修改，要求二级起控阈值大于二级停控阈值，二级停控阈值大于等于一级起控阈值，一级起控阈值大于一级停控阈值，停控时间窗取值范围在5-120秒之间。
> - 首次执行该命令不允许缺省参数，否则将导致命令下发失败。
> - 执行该命令时，有参数取值为0，将导致配置下发失败。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | FCTYPE | LOWSTARTTH | LOWSTOPTH | HIGHSTARTTH | HIGHSTOPTH | DELAYTIME |
> | --- | --- | --- | --- | --- | --- |
> | POD | 0 | 0 | 0 | 0 | 0 |
> | RESOURCEBOX | 0 | 0 | 0 | 0 | 0 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-CMFFC]] · LST CMFFC
- [[command/UDG/20.15.2/SET-CMFFC]] · SET CMFFC

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CMF流控参数（LST-CMFFC）_21100212.md`
- 原始手册：`evidence/UDG/20.15.2/设置CMF流控参数（SET-CMFFC）_68820021.md`
