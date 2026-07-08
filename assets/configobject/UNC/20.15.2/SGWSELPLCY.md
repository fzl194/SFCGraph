---
id: UNC@20.15.2@ConfigObject@SGWSELPLCY
type: ConfigObject
name: SGWSELPLCY（S-GW选择策略）
nf: UNC
version: 20.15.2
object_name: SGWSELPLCY
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# SGWSELPLCY（S-GW选择策略）

## 说明

![](增加S-GW选择策略(ADD SGWSELPLCY)_26145974.assets/notice_3.0-zh-cn_2.png)

- 参数（IMSI前缀）：为防止误操作，请务必确保IMSI前缀的取值合理有效。
- 参数（MSISDN前缀）：为防止误操作，请务必确保MSISDN前缀的取值合理有效。

**适用网元：SGSN、MME**

该命令用于增加S-GW选择策略，为不同的用户群指定S-GW，运营商可以灵活拨测与维护。用户群是指运营商根据自身的经营策略划分的一组用户。例如：基于MSISDN或IMSI，最小粒度为特定MSISDN或特定IMSI。

- S-GW新割接入网后，运营商指定用户接入新割接入网的S-GW，拨测S-GW设备是否工作正常，这样可以不对现网大部分用户的造成影响。 除上述场景外，4G业务部署的典型应用不应使用本命令的配置选择S-GW，请根据“WSFD-205004S-GW/P-GW 拓扑选择”特性描述部署。
- 若使用本命令直接指定S-GW的查询域名，满足配置条件的用户使用指定的S-GW查询域名解析获得S-GW IP地址。未匹配的用户仍根据终端上报的TAI组装标准查询域名解析获得S-GW IP地址。若指定的S-GW查询域名采用NAPTR查询，“WSFD-205004S-GW/P-GW 拓扑选择”特性和“WSFD-205006基于P-GW锚点选择S-GW”特性继续生效。若指定的S-GW查询域名采用A查询，并且域名命名规则遵循3GPP TS 29.303协议的定义，“WSFD-205004S-GW/P-GW 拓扑选择”特性和“WSFD-205006基于P-GW锚点选择S-GW”特性继续生效。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SGWSELPLCY]] · ADD SGWSELPLCY
- [[command/UNC/20.15.2/LST-SGWSELPLCY]] · LST SGWSELPLCY
- [[command/UNC/20.15.2/MOD-SGWSELPLCY]] · MOD SGWSELPLCY
- [[command/UNC/20.15.2/RMV-SGWSELPLCY]] · RMV SGWSELPLCY

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改S-GW选择策略(MOD-SGWSELPLCY)_26305784.md`
- 原始手册：`evidence/UNC/20.15.2/删除S-GW选择策略(RMV-SGWSELPLCY)_72225653.md`
- 原始手册：`evidence/UNC/20.15.2/增加S-GW选择策略(ADD-SGWSELPLCY)_26145974.md`
- 原始手册：`evidence/UNC/20.15.2/查询S-GW选择策略(LST-SGWSELPLCY)_72345575.md`
