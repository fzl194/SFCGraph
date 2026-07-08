# 查询NF负载更新阈值（LST REGNFLOADUPDTHR）

- [命令功能](#ZH-CN_MMLREF_0209652555__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652555__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652555__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652555__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209652555__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209652555)

**适用NF：NRF**

当运营商希望查询NF负载更新阈值时，可以使用此命令。

若要查询全部NF负载更新阈值的配置信息，请不要输入任何参数。

若要查询某类NF负载更新阈值的配置信息，请输入“NF类型”参数。

## [注意事项](#ZH-CN_MMLREF_0209652555)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209652555)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652555)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示要配置的负载更新阈值的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- DEFAULT（系统默认值）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652555)

- 查询NF类型为NRF的负载更新阈值。
  ```
  LST REGNFLOADUPDTHR: NFTYPE=NRF;
  %%LST REGNFLOADUPDTHR: NFTYPE=NRF;%%
  RETCODE = 0  操作成功

  结果如下
  --------
          NF类型  =  NRF
  低负载更新阈值  =  5
  中负载更新阈值  =  3
  高负载更新阈值  =  1
  (结果个数 = 1)

  ---    END
  ```
- 查询所有NF的负载更新阈值。
  ```
  LST REGNFLOADUPDTHR:;
  %%LST REGNFLOADUPDTHR:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NF类型      低负载更新阈值  中负载更新阈值  高负载更新阈值  

  DEFAULT     5               3               1               
  NRF         5               3               1               
  UDM         5               3               1               
  AMF         5               3               1               
  SMF         5               3               1               
  AUSF        5               3               1               
  NEF         5               3               1               
  PCF         5               3               1               
  SMSF        5               3               1               
  NSSF        5               3               1               
  UDR         5               3               1               
  LMF         5               3               1               
  GMLC        5               3               1               
  EIR_5G      5               3               1               
  SEPP        5               3               1               
  UPF         5               3               1               
  N3IWF       5               3               1               
  AF          5               3               1               
  UDSF        5               3               1               
  BSF         5               3               1               
  CHF         5               3               1               
  NWDAF       5               3               1               
  CUSTOM_OCS  5               3               1               
  SCP         5               3               1               
  (结果个数 = 24)

  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0209652555)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF类型 | 该参数用于表示要配置的负载更新阈值的NF类型。 |
| 低负载更新阈值 | 该参数用于表示NF低负载（负载值为0-50之间，这里的负载指的是NF上报的load信元）的更新阈值。NF的负载值范围在匹配时以NRF系统中当前的负载值为准。 |
| 中负载更新阈值 | 该参数用于表示NF中负载（负载值为51-70之间，这里的负载指的是NF上报的load信元）的更新阈值。NF的负载值范围在匹配时以NRF系统中当前的负载值为准。 |
| 高负载更新阈值 | 该参数用于表示NF高负载（负载值为71-100之间，这里的负载指的是NF上报的load信元）的更新阈值。NF的负载值范围在匹配时以NRF系统中当前的负载值为准。 |
