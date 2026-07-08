---
id: UNC@20.15.2@MMLCommand@MOD PNFDISCPLCY
type: MMLCommand
name: MOD PNFDISCPLCY（修改对端NF的服务发现策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PNFDISCPLCY
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- NF发现策略管理
status: active
---

# MOD PNFDISCPLCY（修改对端NF的服务发现策略）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于修改对端NF的服务发现策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |
| POLICY | 服务发现策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务发现策略。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL_FIRST（LOCAL_FIRST）”：本地优先，先从本地配置查找满足服务发现条件的网元，如没有命中服务发现条件则再去缓存查找（如果缓存功能关闭，则跳过此步），如仍无命中则再去NRF查找。<br>- “LOCAL_ONLY（LOCAL_ONLY）”：仅本地查找，只从本地配置查找。<br>- “REMOTE_ONLY（REMOTE_ONLY）”：仅远端查找，先在缓存查找（如果缓存功能关闭，则跳过此步），如没命中则再去NRF查找。<br>- “REMOTE_FIRST（REMOTE_FIRST）”：远端优先，先在缓存查找满足服务发现条件的网元（如果缓存功能关闭，则跳过此步），如没有命中服务发现条件则去NRF查找，如仍无命中再在本地配置查找。<br>默认值：无<br>配置原则：<br>本地和远端为互补或相互备份的关系，如果在某一策略下能在某一数据来源中找到匹配服务发现条件的网元，则此处不会在另一数据来源中再进行服务发现。<br>如果同时配置PNFDISCPLY和NFDISCPLCY，以PNFDISCPLY的服务发现策略为准。 |

## 操作的配置对象

- [对端NF的服务发现策略（PNFDISCPLCY）](configobject/UNC/20.15.2/PNFDISCPLCY.md)

## 使用实例

修改NFTYPE为NfSMSF的对端NF的服务发现策略，将POLICY修改为LOCAL_ONLY。

```
MOD PNFDISCPLCY: NFTYPE=NfSMSF, POLICY=LOCAL_ONLY;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端NF的服务发现策略（MOD-PNFDISCPLCY）_21861981.md`
