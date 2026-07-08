---
id: UNC@20.15.2@MMLCommand@RMV MVNO
type: MMLCommand
name: RMV MVNO（删除MVNO信息表记录）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MVNO
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- MVNO管理
- MVNO配置表
status: active
---

# RMV MVNO（删除MVNO信息表记录）

## 功能

**适用网元：SGSN、MME**

该命令用于删除MNO的配置信息。

## 注意事项

- 该命令执行后立即生效。
- 每次只能删除一条记录。
- 删除的记录不能在MVNONET表（[**LST MVNONET**](../MVNO网络标识配置表/查询MVNO网络配置信息(LST MVNONET)_72225743.md)）、MVNORES表（[**LST MVNORES**](../MVNO资源配置表/查询MVNO资源配置信息(LST MVNORES)_26305876.md)）、MVNOFUN表（[**LST MVNOFUN**](../MVNO功能配置表/查询MVNO功能配置信息(LST MVNOFUN)_72225741.md)）、归属网络信息管理（[**LST HNOINFO**](../../归属网络信息管理/查询归属网络信息(LST HNOINFO)_72225733.md)）、互连PLMN表（[**LST CONNECTPLMN**](../../../互联PLMN管理/查询互联PLMN(LST CONNECTPLMN)_72225723.md)）、SM属性配置表（[**LST IMSISMCHAR**](../../../../QoS管理/Pre-R8 QoS/QoS协商控制/QoS协商参数管理/查询QoS协商参数(LST IMSISMCHAR)_72225909.md)）、GGSN/P-GW选择策略表（[**LST GWSELPLCY**](../../../../GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN_P-GW选择/查询GGSN_P-GW选择策略（LST GWSELPLCY）_72345545.md)）、RFSP配置表（[**LST RFSP**](../../../../移动性管理/RFSP管理/RFSP策略管理/RFSP参数配置/查询RFSP配置(LST RFSP)_72225221.md)）、VOICEDEPLOY配置表（[**LST VOICEDEPLOY**](../../../../业务安全管理/语音业务管理/查询语音部署配置(LST VOICEDEPLOY)_26305572.md)）、EMGCFG配置表（[**LST EMGCFG**](../../../../移动性管理/紧急呼叫配置/紧急呼叫功能配置/查询运营商紧急呼叫功能配置（LST EMGCFG）_72225187.md)）、S1ACCAREALST配置表（[**LST S1ACCAREALST**](../../../../移动性管理/区域漫游限制管理/S1模式区域漫游限制参数/查询S1模式接入控制配置（LST S1ACCAREALST）_26305368.md)）、ZCCONVERT配置表（[**LST ZCCONVERT**](../../../../移动性管理/区域漫游限制管理/区域码转换/查询区域码转换策略(LST ZCCONVERT)_72225249.md)）、M2MPLCY配置表（[**LST M2MPLCY**](../../../../业务安全管理/M2M管理/M2M策略参数配置/查询M2M策略参数(LST M2MPLCY)_26145766.md)）、S1SUBRRLST配置表（ [**LST S1SUBRRLST**](../../../../移动性管理/区域漫游限制管理/S1模式用户漫游限制管理/查询S1模式用户漫游限制列表(LST S1SUBRRLST)_72345157.md) ）、IUSUBRRLST配置表（ [**LST IUSUBRRLST**](../../../../移动性管理/区域漫游限制管理/Iu模式用户漫游限制管理/查询Iu模式用户漫游限制列表(LST IUSUBRRLST)_72225231.md) ）、GBSUBRRLST配置表（ [**LST GBSUBRRLST**](../../../../移动性管理/区域漫游限制管理/Gb模式用户漫游限制管理/查询Gb模式用户漫游限制列表(LST GBSUBRRLST)_26145548.md) ）、GTPCINTFATTR配置表（ [**LST GTPCINTFATTR**](../../../../GTP-C接口管理/GTP-C接口类型属性/查询GTP-C IP地址接口属性(LST GTPCINTFATTR)_26145902.md) ）、GTPUINTFATTR配置表（ [**LST GTPUINTFATTR**](../../../../GTP-U接口管理/GTP-U接口类型属性/查询GTP-U IP地址接口属性(LST GTPUINTFATTR)_72345585.md) ）、UFCSFB配置表（ [**LST UFCSFB**](../../../../电路域联合业务/预留功能策略管理/查询预留功能策略(LST UFCSFB)_72345045.md) ）、NSACTRLPLCY配置表（ [**LST NSACTRLPLCY**](../../../NSA组网管理/NSA控制策略/查询NSA控制策略(LST NSACTRLPLCY)_26146132.md) ）、MAPCMPTBYIMSI配置表（ [**LST MAPCMPTBYIMSI**](../../../../MAP应用协议/MAP功能配置/查询MAP协议接口兼容性IMSI号段配置(LST MAPCMPTBYIMSI)_72225149.md) ）、MMERESELPLCY配置表（ [**LST MMERESELPLCY**](../../../../移动性管理/MME重选管理/MME重选策略参数/查询MME重选策略(LST MMERESELPLCY)_72345225.md) ）、QOSCAP配置表（ [**LST QOSCAP**](../../../../QoS管理/EPS QoS/QoS限制配置/Non-GBR承载QoS限制/查询Non-GBR承载QoS限制配置(LST QOSCAP)_26146220.md) ）、N26GWSELPLCY配置表（ [**LST N26GWSELPLCY**](../../../N26互操作管理/N26融合网关选择策略/查询N26融合网关选择策略(LST N26GWSELPLCY)_26305948.md) ）、N26IWKPLCY配置表（ [**LST N26IWKPLCY**](../../../N26互操作管理/N26互操作策略/查询EPS与5GS互操作本地策略(LST N26IWKPLCY)_72225815.md) ）和DMCMPTBYIMSI配置表（[**LST DMCMPTBYIMSI**](../../../../信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/查询IMSI对应的Diameter兼容性(LST DMCMPTBYIMSI)_26146300.md)）中使用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MVNOID | MVNO标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MVNO的标识。<br>取值范围：1～64<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MVNO]] · MVNO配置信息（MVNO）

## 使用实例

删除MVNO标识为1的MVNO：

RMV MVNO: MVNOID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MVNO信息表记录(RMV-MVNO)_26305878.md`
