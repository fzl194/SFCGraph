# 查询NF服务发现忽略参数规则（LST NRFIGNDISCPARA）

- [命令功能](#ZH-CN_MMLREF_0000001144928651__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001144928651__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001144928651__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001144928651__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001144928651__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001144928651)

**适用NF：NRF**

该命令用于查询NF服务发现忽略参数配置。

## [注意事项](#ZH-CN_MMLREF_0000001144928651)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001144928651)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001144928651)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示忽略发现参数规则对应的目标NF类型。其中，ALL表示适用于所有目标NF类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL（表示适用于所有NF类型）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001144928651)

查询网元类型为NRF的服务发现忽略参数规则。

```
LST NRFIGNDISCPARA:;
%%LST NRFIGNDISCPARA:;%%
RETCODE = 0  操作成功

The result is as follows
------------------------
网元类型          =  NRF
服务发现忽略参数  =  Tai
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001144928651)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 网元类型 | 该参数用于表示忽略发现参数规则对应的目标NF类型。其中，ALL表示适用于所有目标NF类型。 |
| 服务发现忽略参数 | 该参数表示NRF忽略的服务发现参数。NRF在处理指定目标NF类型服务发现时，会忽略该发现参数，当做该参数没有携带，匹配其他条件进行服务发现。 |
