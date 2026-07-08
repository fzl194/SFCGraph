---
id: UDG@20.15.2@ConfigObject@IKEGLOBALCONFIG
type: ConfigObject
name: IKEGLOBALCONFIG（IKE全局配置）
nf: UDG
version: 20.15.2
object_name: IKEGLOBALCONFIG
object_kind: global_setting
status: active
---

# IKEGLOBALCONFIG（IKE全局配置）

## 说明

![](设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.assets/notice_3.0-zh-cn.png)

如果安全日志阈值不为0，链路协商失败时，可能会导致日志大量打印，影响问题定位，对业务性能无影响。

该命令用于设置IKE全局配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 需要CPU告警上报阈值大于等于CPU告警恢复阈值，且建议上报阈值大至少10个百分点，否则告警可能会持续上报。
> - 在用户级模板模式场景下NATKLI参数不生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | DFBITCLEAR | FRAGBEFOREENCR | TRAFFSADISFLG | TRAFFICSADURTN | TIMESADURTN | ANTIREPLFLG | WINDOWSIZE | DPDTYPE | NUMBER | DOSTHRESHOLD | NATKLI | CPUREPORTTHRES | CPUCLEARTHRES |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | FALSE | FALSE | FALSE | 1843200 | 3600 | True | Size_1024 | None | 30 | 0 | 20 | 80 | 70 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-IKEGLOBALCONFIG]] · LST IKEGLOBALCONFIG
- [[command/UDG/20.15.2/SET-IKEGLOBALCONFIG]] · SET IKEGLOBALCONFIG

## 证据

- 原始手册：`evidence/UDG/20.15.2/IKEGLOBALCONFIG.md`
- 原始手册：`evidence/UDG/20.15.2/IKEGLOBALCONFIG.md`
