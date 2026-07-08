---
id: UNC@20.15.2@ConfigObject@UNIHTR
type: ConfigObject
name: UNIHTR（统一HTR功能）
nf: UNC
version: 20.15.2
object_name: UNIHTR
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# UNIHTR（统一HTR功能）

## 说明

![](设置统一HTR功能(SET UNIHTR)_26305954.assets/notice_3.0-zh-cn_2.png)

如果统一HTR流控功能被关闭，在网络负荷突增场景下， **UNC** 将不会对周边网元进行保护。

**适用网元：SGSN、MME**

此命令用于设置统一HTR（Hard to Reach）流控功能的相关参数。当由于系统升级或复位导致S11/S4、S6a/S6d、S13/Gf、SGs接口出现拥塞时，可以通过开启此流控功能来保护与这些接口相连的周边网元免于拥塞。 统一HTR流控功能是指 UNC 系统（MME）的周边网元存在过载风险时， UNC 系统能够基于周边网元返回成功应答数的周期变化自动调节Attach、Inter TAU、Inter RAU（S6d接口）、Inter RAT Intra USN TAU、Inter RAT Intra USN RAU流程的处理速率，从而控制向周边网元发送的请求数，达到保护周边网元的目的。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-UNIHTR]] · LST UNIHTR
- [[command/UNC/20.15.2/SET-UNIHTR]] · SET UNIHTR

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询统一HTR功能(LST-UNIHTR)_72345745.md`
- 原始手册：`evidence/UNC/20.15.2/设置统一HTR功能(SET-UNIHTR)_26305954.md`
