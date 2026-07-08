# 查询NF发现参数防呆规则（LST NRFDISCPARARULE）

- [命令功能](#ZH-CN_MMLREF_0000001088697030__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001088697030__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001088697030__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001088697030__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001088697030__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001088697030)

**适用NF：NRF**

该命令用于查询NRF发现参数处理规则。

## [注意事项](#ZH-CN_MMLREF_0000001088697030)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001088697030)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001088697030)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示发现参数处理规则对应的目标NF类型。其中，DEFAULT范围为下面列举的具体NF外的其他NF类型。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（DEFAULT）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001088697030)

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

## [输出结果说明](#ZH-CN_MMLREF_0000001088697030)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 网元类型 | 该参数用于表示发现参数处理规则对应的目标NF类型。其中，DEFAULT范围为下面列举的具体NF外的其他NF类型。 |
| 发现参数防呆规则 | 该参数用于表示服务发现参数防呆规则。如果服务发现参数中目标NF相关参数包含勾选项以外的参数，则NRF正常处理服务发现请求，否则，服务发现结果返回403(Forbidden)。如果没有勾选任何选项，NRF不进行上述判断，正常处理服务发现请求。例如，如果此参数只设置了“TARGETNFTYPE”，表示如果服务发现目标NF只携带了“TARGETNFTYPE”，则服务发现结果返回403(Forbidden)，NRF不进行处理。 |
