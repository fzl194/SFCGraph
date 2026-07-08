---
id: UNC@20.15.2@ConfigObject@SIGATTR
type: ConfigObject
name: SIGATTR（信令网属性状态）
nf: UNC
version: 20.15.2
object_name: SIGATTR
object_kind: global_setting
applicable_nf:
- SGSN
- MME
- SMSF
status: active
---

# SIGATTR（信令网属性状态）

## 说明

![](设置信令网属性(SET SIGATTR)_72226021.assets/notice_3.0-zh-cn_2.png)

如果设置信令网属性后未立即复位相关进程，在后续的系统运行中如果发生部分进程的复位，将会导致系统内进程运行的信令网属性表现不同，导致业务中断。比较 [**DSP SIGATTR**](显示信令网属性状态(DSP SIGATTR)_72345943.md) 和 [**LST SIGATTR**](查询信令网属性(LST SIGATTR)_26306154.md) 命令查询的查询结果的一致性，可以排查SPP、SGP、LLP上实际运行的信令网属性是否异常。

**适用网元：SGSN、MME、SMSF**

此命令用于设置和修改信令网属性，信令网属性定义了本局支持的信令特性。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-SIGATTR]] · DSP SIGATTR
- [[command/UNC/20.15.2/LST-SIGATTR]] · LST SIGATTR
- [[command/UNC/20.15.2/SET-SIGATTR]] · SET SIGATTR

## 证据

- 原始手册：`evidence/UNC/20.15.2/SIGATTR.md`
- 原始手册：`evidence/UNC/20.15.2/SIGATTR.md`
- 原始手册：`evidence/UNC/20.15.2/SIGATTR.md`
