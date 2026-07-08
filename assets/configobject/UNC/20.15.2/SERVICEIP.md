---
id: UNC@20.15.2@ConfigObject@SERVICEIP
type: ConfigObject
name: SERVICEIP（业务IP）
nf: UNC
version: 20.15.2
object_name: SERVICEIP
object_kind: entity
applicable_nf:
- SGSN
- MME
- AMF
status: active
---

# SERVICEIP（业务IP）

## 说明

**适用NF：SGSN、MME、AMF**

该命令用于配置业务IP地址。

- 命令[**ADD S1APLE**](../../S1接口管理/S1AP本地实体/增加S1AP本地实体(ADD S1APLE)_26146254.md)、[**ADD DMLNK**](../../信令传输管理/Diameter管理/Diameter链路/增加Diameter链路配置(ADD DMLNK)_72225953.md)、[**ADD M3LNK**](../../信令传输管理/M3UA管理/M3UA链路/增加M3UA信令链路(ADD M3LNK)_72225983.md)、[**ADD GTPCLE**](../../GTP-C接口管理/Gtpc本端实体管理/增加GTP-C本地实体(ADD GTPCLE)_26145966.md)、[**ADD SGSLNK**](../../电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md)、[**ADD GTPULE**](../../GTP-U接口管理/Gtpu本端实体管理/增加GTP-U本地实体(ADD GTPULE)_72345581.md)、[**ADD DNSLE**](../../GTP-C接口管理/DNS/DNS本端实体管理/增加DNS实体绑定DNS Client IP(ADD DNSLE)_72225567.md)、[**ADD GBEPPOOL**](../../Gb接口管理/Gb自动配置管理/Gb地址池管理/增加IP地址到地址池(ADD GBEPPOOL)_26145998.md)、[**ADD GBIPLOCENDPT**](../../Gb接口管理/Gb over IP管理/本端IP端点配置/增加本端端点配置(ADD GBIPLOCENDPT)_72225689.md)、[**ADD CHGCDPIP**](../../../计费管理/CDPIP 配置/增加计费相关的IP配置参数(ADD CHGCDPIP)_72344961.md)、[**ADD LCSAPLNK**](../../业务安全管理/LCS/LCSAP链路配置/增加LCSAP链路配置(ADD LCSAPLNK)_72345407.md)、[**ADD SBCAPLE**](../../SBc接口管理/SBCAP本地实体/增加SBCAP本地实体(ADD SBCAPLE)_72226055.md)、[**ADD SBCAPLNK**](../../SBc接口管理/SBc链路/增加SBc链路(ADD SBCAPLNK)_72345973.md)、[**ADD SCTPLE**](../../S1接口管理/SCTP本地实体/增加SCTP本地实体(ADD SCTPLE)_11295747.md)中的使用的地址或本端地址都必须引用该业务IP地址。不同的业务允许使用同一个业务IP地址，也允许使用不同的业务IP地址。
- 命令使用的VPN必须引用业务IP所属VPN实例。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SERVICEIP]] · ADD SERVICEIP
- [[command/UNC/20.15.2/DSP-SERVICEIP]] · DSP SERVICEIP
- [[command/UNC/20.15.2/LST-SERVICEIP]] · LST SERVICEIP
- [[command/UNC/20.15.2/MOD-SERVICEIP]] · MOD SERVICEIP
- [[command/UNC/20.15.2/RMV-SERVICEIP]] · RMV SERVICEIP

## 证据

- 原始手册：`evidence/UNC/20.15.2/SERVICEIP.md`
- 原始手册：`evidence/UNC/20.15.2/SERVICEIP.md`
- 原始手册：`evidence/UNC/20.15.2/SERVICEIP.md`
- 原始手册：`evidence/UNC/20.15.2/SERVICEIP.md`
- 原始手册：`evidence/UNC/20.15.2/SERVICEIP.md`
