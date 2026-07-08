---
id: UNC@20.15.2@MMLCommand@LST NRFDISCPARARULE
type: MMLCommand
name: LST NRFDISCPARARULE（查询NF发现参数防呆规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFDISCPARARULE
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF服务发现参数处理规则
status: active
---

# LST NRFDISCPARARULE（查询NF发现参数防呆规则）

## 功能

**适用NF：NRF**

该命令用于查询NRF发现参数处理规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示发现参数处理规则对应的目标NF类型。其中，DEFAULT范围为下面列举的具体NF外的其他NF类型。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（DEFAULT）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NF发现参数防呆规则（NRFDISCPARARULE）](configobject/UNC/20.15.2/NRFDISCPARARULE.md)

## 使用实例

查询NF发现参数处理规则。

```
LST NRFDISCPARARULE:;
%%LST NRFDISCPARARULE:;%%
RETCODE = 0  操作成功

结果如下
--------
网元类型    发现参数防呆规则                                     

DEFAULT     NULL                                                 
NRF         服务发现参数中的目标NF类型&服务发现参数中的服务名称  
UDM         服务发现参数中的目标NF类型&服务发现参数中的服务名称  
AMF         服务发现参数中的目标NF类型&服务发现参数中的服务名称  
SMF         服务发现参数中的目标NF类型&服务发现参数中的服务名称  
AUSF        服务发现参数中的目标NF类型&服务发现参数中的服务名称  
NEF         服务发现参数中的目标NF类型&服务发现参数中的服务名称  
PCF         服务发现参数中的目标NF类型&服务发现参数中的服务名称  
SMSF        NULL                                                 
NSSF        服务发现参数中的目标NF类型&服务发现参数中的服务名称  
UDR         服务发现参数中的目标NF类型&服务发现参数中的服务名称  
LMF         NULL                                                 
GMLC        服务发现参数中的目标NF类型&服务发现参数中的服务名称  
EIR_5G      服务发现参数中的目标NF类型&服务发现参数中的服务名称  
SEPP        服务发现参数中的目标NF类型&服务发现参数中的服务名称  
UPF         服务发现参数中的目标NF类型&服务发现参数中的服务名称  
N3IWF       服务发现参数中的目标NF类型&服务发现参数中的服务名称  
AF          服务发现参数中的目标NF类型&服务发现参数中的服务名称  
UDSF        服务发现参数中的目标NF类型&服务发现参数中的服务名称  
BSF         服务发现参数中的目标NF类型&服务发现参数中的服务名称  
CHF         服务发现参数中的目标NF类型&服务发现参数中的服务名称  
NWDAF       服务发现参数中的目标NF类型&服务发现参数中的服务名称  
CUSTOM_OCS  服务发现参数中的目标NF类型&服务发现参数中的服务名称  
SCP         服务发现参数中的目标NF类型&服务发现参数中的服务名称  
(结果个数 = 24)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF发现参数防呆规则（LST-NRFDISCPARARULE）_88697030.md`
