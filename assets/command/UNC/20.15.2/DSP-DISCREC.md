---
id: UNC@20.15.2@MMLCommand@DSP DISCREC
type: MMLCommand
name: DSP DISCREC（显示服务发现记录）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DISCREC
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF访问记录管理
status: active
---

# DSP DISCREC（显示服务发现记录）

## 功能

**适用NF：NRF**

该命令查询系统中保存的NF服务发现记录。

若要查询系统中保存的所有NF服务发现记录，请不要输入任何参数。

若要查询特定请求方NF类型或特定目标NF类型的NF服务发现记录，请输入“请求NF类型”或“目标NF类型”参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REQNFTYPE | 请求NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示服务发现的请求方NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>- CBCF（CBCF）<br>- MB_SMF（MB_SMF）<br>默认值：无<br>配置原则：无 |
| TARGETNFTYPE | 目标NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示服务发现的目标NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>- CBCF（CBCF）<br>- MB_SMF（MB_SMF）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DISCREC]] · 服务发现记录（DISCREC）

## 使用实例

- 当希望查询请求NF类型为AMF，目标NF类型为AMF时，使用此命令。
  ```
  DSP DISCREC: REQNFTYPE=AMF, TARGETNFTYPE=AMF;
  %%DSP DISCREC: REQNFTYPE=AMF, TARGETNFTYPE=AMF;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  服务发现请求时间                  请求NF类型       目标NF类型      服务发现参数                                    服务发现结果   对端IP             用户代理             HTTP响应的via头域  是否本地发现   服务发现NF数量   NF关键属性数量                              服务发现结果包长(byte)   NRF处理时长(ms)   Pod名称     内部资源号

  2019-12-06 09:47:29.954807534 +0  AMF              AMF             {"targetNfType":"AMF","requesterNfType":"AMF"}  成功_200       10.70.185.1:5165   Go-http-client/2.0   NULL  TRUE           1                SNssais(1);Tai(1);TaiRange(1);totalNum:3;   1208                     33                unc-pod1    1
  2019-12-06 09:40:47.574121992 +0  AMF              AMF             {"targetNfType":"AMF","requesterNfType":"AMF"}  成功_200       10.70.185.1:5165   Go-http-client/2.0   NULL  TRUE           1                SNssais(1);Tai(1);TaiRange(1);totalNum:3;   1218                     36                unc-pod1    2
  (结果个数 = 2)

  ---    END
  ```
- 当希望查询所有NF服务发现记录时，使用此命令。
  ```
  DSP DISCREC:;
  %%DSP DISCREC:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  服务发现请求时间                  请求NF类型       目标NF类型      服务发现参数                                    服务发现结果   对端IP             用户代理             HTTP响应的via头域  是否本地发现   服务发现NF数量   NF关键属性数量                              服务发现结果包长(byte)   NRF处理时长(ms)   Pod名称     内部资源号

  2019-12-06 09:47:29.954807534 +0  AMF              AMF             {"targetNfType":"AMF","requesterNfType":"AMF"}  成功_200       10.70.185.1:5165   Go-http-client/2.0   NULL    TRUE           1                SNssais(1);Tai(1);TaiRange(1);totalNum:3;   1200                     25                unc-pod1    1
  2019-12-06 09:40:47.574121992 +0  AMF              AMF             {"targetNfType":"AMF","requesterNfType":"AMF"}  成功_200       10.70.185.1:5165   Go-http-client/2.0   NULL    TRUE           1                SNssais(1);Tai(1);TaiRange(1);totalNum:3;   1207                     36                unc-pod1    2
  2019-12-06 09:39:41.545648777 +0  SMF              SMF             {"targetNfType":"SMF","requesterNfType":"SMF"}  成功_200       10.70.185.1:5165   Go-http-client/2.0   NULL    TRUE           1                SNssais(1);Tai(1);TaiRange(1);totalNum:3;   1208                     36                unc-pod1    3
  2019-12-06 09:38:45.987464664 +0  SMF              SMF             {"targetNfType":"SMF","requesterNfType":"SMF"}  成功_200       10.70.185.1:5165   Go-http-client/2.0   NULL    TRUE           1                SNssais(1);Tai(1);TaiRange(1);totalNum:3;   1100                     20                unc-pod1    4
  (结果个数 = 4)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DISCREC.md`
