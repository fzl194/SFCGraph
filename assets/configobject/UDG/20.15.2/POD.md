---
id: UDG@20.15.2@ConfigObject@POD
type: ConfigObject
name: POD（POD停止）
nf: UDG
version: 20.15.2
object_name: POD
object_kind: action
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# POD（POD停止）

## 说明

![](POD停止（STP POD）_57196802.assets/notice_3.0-zh-cn.png)

Pod停止运行可能会导致业务受损，请谨慎使用该命令。

该命令用于停止Pod运行。

> **说明**
> - 在第三方场景下不支持该命令。
> - 该命令功能依赖NFV_FusionStage能力，CSP配套NFV_FusionStage 22.1.0及之后的版本，支持该命令，配套其它版本执行该命令不生效或执行失败。

> **说明**
> 无。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-POD]] · DSP POD
- [[command/UDG/20.15.2/LCK-POD]] · LCK POD
- [[command/UDG/20.15.2/RST-POD]] · RST POD
- [[command/UDG/20.15.2/STP-POD]] · STP POD
- [[command/UDG/20.15.2/STR-POD]] · STR POD

## 证据

- 原始手册：`evidence/UDG/20.15.2/POD停止（STP-POD）_57196802.md`
- 原始手册：`evidence/UDG/20.15.2/POD启动（STR-POD）_06802245.md`
- 原始手册：`evidence/UDG/20.15.2/POD复位（RST-POD）_69830278.md`
- 原始手册：`evidence/UDG/20.15.2/POD查询（DSP-POD）_69830277.md`
- 原始手册：`evidence/UDG/20.15.2/锁定_解锁POD（LCK-POD）_64015273.md`
