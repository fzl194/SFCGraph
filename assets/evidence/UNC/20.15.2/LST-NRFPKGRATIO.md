# 查询NRF内外包长比例（LST NRFPKGRATIO）

- [命令功能](#ZH-CN_MMLREF_0000001088248948__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001088248948__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001088248948__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001088248948__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001088248948__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001088248948)

**适用NF：NRF**

该命令用于查询NRF内部报文长度和http接口json报文长度的比例系数。

## [注意事项](#ZH-CN_MMLREF_0000001088248948)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001088248948)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001088248948)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRF处理注册/更新的NF类型或服务发现的目标NF类型。<br>数据来源：全网规划<br>取值范围：<br>- DEFAULT（DEFAULT）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001088248948)

查询NRF包长比例：

```
LST NRFPKGRATIO:;
%%LST NRFPKGRATIO:;%%
RETCODE = 0  操作成功

结果如下
--------
      NF类型  =  AMF
 比例系数(%)  =  30
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001088248948)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF类型 | 该参数用于表示NRF处理注册/更新的NF类型或服务发现的目标NF类型。 |
| 比例系数(%) | 该参数用于表示该NFType对应的内部报文长度和http接口json原始报文长度的百分比，即(内部报文长度/http接口json原始报文长度)*100%。其中内部报文是http接口json原始报文转换后的报文，即NRF实际处理的报文。不同的NFType可以分别设置不同的比例，该参数用法详见SET NRFBIGPKGPARA中MAXPKGSIZE参数说明。 |
