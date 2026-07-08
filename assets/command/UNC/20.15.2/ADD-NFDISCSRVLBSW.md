---
id: UNC@20.15.2@MMLCommand@ADD NFDISCSRVLBSW
type: MMLCommand
name: ADD NFDISCSRVLBSW（增加服务发现NF Service负载均衡开关）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NFDISCSRVLBSW
command_category: 配置类
applicable_nf:
- AMF
- SMF
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
- 本地NRF功能管理
- NF发现NFS负载均衡管理
status: active
---

# ADD NFDISCSRVLBSW（增加服务发现NF Service负载均衡开关）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于开启或关闭服务发现时的NF Service负载均衡功能。业务进行服务发现时，如果未指定NF Service负载均衡策略，则根据此命令决定是否需要NF Service负载均衡；如果已指定NF Service负载均衡策略，则此命令不生效。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入30条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TARGETNFTYPE | 对端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |
| LBSWITCH | 负载均衡开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否开启NF Service负载均衡功能。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFDISCSRVLBSW]] · 服务发现Service负载均衡功能（NFDISCSRVLBSW）

## 使用实例

开启服务发现UDM时的NF Service负载均衡功能。

```
ADD NFDISCSRVLBSW: TARGETNFTYPE=NfUDM, LBSWITCH=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NFDISCSRVLBSW.md`
