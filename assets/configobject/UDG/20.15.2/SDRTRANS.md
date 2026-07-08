---
id: UDG@20.15.2@ConfigObject@SDRTRANS
type: ConfigObject
name: SDRTRANS（SDR传输能力）
nf: UDG
version: 20.15.2
object_name: SDRTRANS
object_kind: global_setting
status: active
---

# SDRTRANS（SDR传输能力）

## 说明

![](设置SDR传输能力（SET SDRTRANS）_30310143.assets/notice_3.0-zh-cn.png)

该命令是高危命令，操作不当可能会导致业务受损，请谨慎使用并联系华为技术支持协助操作。可靠传输能力与安全传输能力有关联关系，操作前请参考联机帮助。

该命令用于设置SDR传输能力。SDR传输能力包括可靠传输能力和安全传输能力。

> **说明**
> - 该命令执行后立即生效。
>
> - 若要设置安全传输能力为ENABLEALL或NOTSET，可靠传输能力不能为DISABLEALL。
> - 若要禁用可靠传输能力，请确认安全传输能力是否处于开启状态；若安全传输能力处于开启状态，请先禁用安全传输能力再禁用可靠传输能力；若只禁用可靠传输能力却开启安全传输能力，则禁用可靠传输能力只对非加密消息生效，对加密消息不生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | FLATTYPE | TRANSABILITY | OPT |
> | --- | --- | --- |
> | BASE | RELIABILITY | NOTSET |
> | BASE | SECURITY | DISABLEALL |
> | FABRIC | RELIABILITY | DISABLEALL |
> | FABRIC | SECURITY | DISABLEALL |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-SDRTRANS]] · LST SDRTRANS
- [[command/UDG/20.15.2/SET-SDRTRANS]] · SET SDRTRANS

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SDR传输能力（LST-SDRTRANS）_30310141.md`
- 原始手册：`evidence/UDG/20.15.2/设置SDR传输能力（SET-SDRTRANS）_30310143.md`
