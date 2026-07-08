---
id: UNC@20.15.2@MMLCommand@ADD CACHEUPDATEPLCY
type: MMLCommand
name: ADD CACHEUPDATEPLCY（增加缓存更新策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CACHEUPDATEPLCY
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF Cache管理
status: active
---

# ADD CACHEUPDATEPLCY（增加缓存更新策略）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于增加缓存更新策略。

## 注意事项

- 该命令执行后立即生效。

- 对端NF类型为PCF时，链路全故障触发服务发现开关不生效。
- 当未配置对端NF类型的缓存更新策略时，链路全故障触发服务发现开关以及目标NF全为非注册态时触发服务发现开关默认为
  抑制去NRF服务发现。

- 最多可输入26条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERTYPE | 对端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |
| LINKFAULTUPDSW | 链路全故障触发服务发现开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当从缓存中发现的NF的链路全部故障时是否去NRF服务发现。<br>- 当开关置为SUPPRESS时，每个Pod每3分钟最多触发一次向NRF的重新服务发现；<br>- 当开关置为NOTSUPPRESS时，不抑制向NRF的重新服务发现；<br>- 当开关置为FORBIDDEN时，不触发向NRF的重新服务发现。<br>数据来源：本端规划<br>取值范围：<br>- SUPPRESS（抑制去NRF服务发现）<br>- NOTSUPPRESS（不抑制去NRF服务发现）<br>- FORBIDDEN（禁止去NRF服务发现）<br>默认值：SUPPRESS<br>配置原则：无 |
| UNREGQRYSW | 目标NF全为非注册态时触发服务发现开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当从缓存中发现的NF全部为非注册状态时是否去NRF服务发现。<br>- 当开关置为SUPPRESS时，每个Pod每30秒最多触发一次向NRF的重新服务发现；<br>- 当开关置为NOTSUPPRESS时，不抑制向NRF的重新服务发现；<br>- 当开关置为FORBIDDEN时，不触发向NRF的重新服务发现。<br>数据来源：本端规划<br>取值范围：<br>- SUPPRESS（抑制去NRF服务发现）<br>- NOTSUPPRESS（不抑制去NRF服务发现）<br>- FORBIDDEN（禁止去NRF服务发现）<br>默认值：SUPPRESS<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CACHEUPDATEPLCY]] · 缓存更新策略（CACHEUPDATEPLCY）

## 使用实例

运营商A需要增加缓存更新策略，对端NF类型为OCS，链路全故障触发服务发现开关为“禁止去NRF服务发现”，目标NF全为非注册态时触发服务发现开关为“禁止去NRF服务发现”。

```
ADD CACHEUPDATEPLCY: PEERTYPE=NfCUSTOM_OCS, LINKFAULTUPDSW=FORBIDDEN, UNREGQRYSW=FORBIDDEN;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-CACHEUPDATEPLCY.md`
