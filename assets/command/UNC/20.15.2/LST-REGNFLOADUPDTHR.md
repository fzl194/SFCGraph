---
id: UNC@20.15.2@MMLCommand@LST REGNFLOADUPDTHR
type: MMLCommand
name: LST REGNFLOADUPDTHR（查询NF负载更新阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: REGNFLOADUPDTHR
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
- NF负载管理
status: active
---

# LST REGNFLOADUPDTHR（查询NF负载更新阈值）

## 功能

**适用NF：NRF**

当运营商希望查询NF负载更新阈值时，可以使用此命令。

若要查询全部NF负载更新阈值的配置信息，请不要输入任何参数。

若要查询某类NF负载更新阈值的配置信息，请输入“NF类型”参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示要配置的负载更新阈值的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- DEFAULT（系统默认值）<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@REGNFLOADUPDTHR]] · NF负载更新阈值（REGNFLOADUPDTHR）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-REGNFLOADUPDTHR.md`
