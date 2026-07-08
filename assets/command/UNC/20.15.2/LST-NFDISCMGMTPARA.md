---
id: UNC@20.15.2@MMLCommand@LST NFDISCMGMTPARA
type: MMLCommand
name: LST NFDISCMGMTPARA（查询网元服务发现功能管理参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFDISCMGMTPARA
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NCG
- SMSF
effect_mode: ''
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

# LST NFDISCMGMTPARA（查询网元服务发现功能管理参数）

## 功能

**适用NF：AMF、SMF、NCG、SMSF**

该命令用于查询网元服务发现功能管理参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定目标NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NWDAF（NWDAF）”：NWDAF<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFDISCMGMTPARA]] · 网元服务发现功能管理参数（NFDISCMGMTPARA）

## 使用实例

查询AMF相关的网元服务发现功能管理参数：

```
%%LST NFDISCMGMTPARA: NFTYPE=NfAMF;%%
RETCODE = 0  操作成功

结果如下
--------
          网元类型  =  NfAMF
 TAI精细化选择开关  =  ON
SUPI精细化选择开关  =  OFF
GPSI精细化选择开关  =  OFF
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFDISCMGMTPARA.md`
