---
id: UNC@20.15.2@MMLCommand@SET PNFNTFPLCY
type: MMLCommand
name: SET PNFNTFPLCY（设置对端网元的通知抑制时间）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PNFNTFPLCY
command_category: 配置类
applicable_nf:
- AMF
- SMF
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NRF管理
- NRF参数管理
- 注册与订阅管理
status: active
---

# SET PNFNTFPLCY（设置对端网元的通知抑制时间）

## 功能

**适用NF：AMF、SMF、SMSF**

对端NF状态频繁变更时，本端NF不需要频繁感知并处理，本命令用于抑制向本端NF通知对端NF状态变化的频率，配置通知对端NF状态变化的抑制时间。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

> **说明**
> 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| NFTYPE | NTFTIME |
| --- | --- |
| NfUDM | 5 |
| NfSMF | 2 |
| NfPCF | 0 |
| NfSMSF | 5 |
| NfCHF | 0 |
| NfPCSCF | 1 |
| NfNRF | 0 |
| NfAMF | 5 |
| NfAUSF | 0 |
| NfNEF | 0 |
| NfNSSF | 0 |
| NfUDR | 0 |
| NfLMF | 0 |
| NfGMLC | 0 |
| Nf5G_EIR | 5 |
| NfSEPP | 0 |
| NfUPF | 0 |
| NfN3IWF | 0 |
| NfAF | 0 |
| NfUDSF | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF类型。<br>数据来源：全网规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无。<br>配置原则：无 |
| NTFTIME | 通知抑制时间(分钟) | 可选必选说明：必选参数<br>参数含义：参数用于指定向本端NF通知对端NF状态变更的抑制时间(分钟)。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295，单位是分钟。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFNTFPLCY]] · 对端网元的通知抑制时间（PNFNTFPLCY）

## 使用实例

设置对端网元SMF状态变化满10分钟后才通知本端NF。

```
SET PNFNTFPLCY: NFTYPE=NfSMF, NTFTIME=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置对端网元的通知抑制时间（SET-PNFNTFPLCY）_96243197.md`
