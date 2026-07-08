---
id: UNC@20.15.2@ConfigObject@IMEIFORFD
type: ConfigObject
name: IMEIFORFD（强制分离策略）
nf: UNC
version: 20.15.2
object_name: IMEIFORFD
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# IMEIFORFD（强制分离策略）

## 说明

**适用网元：SGSN**

此命令用于增加强制分离非活动用户时的IMEISV（International Mobile station Equipment Identity and Software Version）匹配规则。分离非活动用户功能由分离非活动用户定时器（ [**SET GBDETACH**](../分离非活动用户/Gb模式分离非活动用户参数/设置Gb分离非活动用户参数(SET GBDETACH)_72345095.md) 或 [**SET IUDETACH**](../分离非活动用户/Iu模式分离非活动用户参数/设置Iu分离非活动用户参数(SET IUDETACH)_26305310.md) ）控制，定时器（NACTTMR）默认时长为360分钟。定时器超时后， UNC 将根据此命令的配置，使用手机所携带的IMEISV与规则的掩码按位进行"与"运算，并和匹配规则比较。如果相同， UNC 将保留该用户；否则 UNC 将强制分离该非活动用户。如果手机不携带IMEISV，则默认不匹配规则， UNC 强制分离该用户。

在业务扩展特性配置中开启“分离非活动用户”功能后，如果运营商需要对某些用户（如VIP用户）不启用分离非活动用户功能，需要执行此命令。

可执行 [**SET GBDETACH**](../分离非活动用户/Gb模式分离非活动用户参数/设置Gb分离非活动用户参数(SET GBDETACH)_72345095.md) 或 [**SET IUDETACH**](../分离非活动用户/Iu模式分离非活动用户参数/设置Iu分离非活动用户参数(SET IUDETACH)_26305310.md) 命令，开启“分离非活动用户”功能。

## 操作本对象的命令

- [ADD IMEIFORFD](command/UNC/20.15.2/ADD-IMEIFORFD.md)
- [LST IMEIFORFD](command/UNC/20.15.2/LST-IMEIFORFD.md)
- [MOD IMEIFORFD](command/UNC/20.15.2/MOD-IMEIFORFD.md)
- [RMV IMEIFORFD](command/UNC/20.15.2/RMV-IMEIFORFD.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改强制分离策略(MOD-IMEIFORFD)_26145488.md`
- 原始手册：`evidence/UNC/20.15.2/删除强制分离策略(RMV-IMEIFORFD)_72345085.md`
- 原始手册：`evidence/UNC/20.15.2/增加强制分离策略(ADD-IMEIFORFD)_26305298.md`
- 原始手册：`evidence/UNC/20.15.2/查询强制分离策略(LST-IMEIFORFD)_72225169.md`
