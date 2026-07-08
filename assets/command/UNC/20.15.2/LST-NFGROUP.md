---
id: UNC@20.15.2@MMLCommand@LST NFGROUP
type: MMLCommand
name: LST NFGROUP（查询NF组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFGROUP
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
- NF实例组信息管理
status: active
---

# LST NFGROUP（查询NF组）

## 功能

**适用NF：NRF**

该命令用于查询NRF配置的NF实例组信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFGROUPID | NF实例组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示在NRF上配置的NF实例组的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。该参数只能由字母（A-Z或者a-z）、数字（0-9），中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示在NRF上配置的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFGROUP]] · NF组（NFGROUP）

## 使用实例

- 在NRF上查询NF标识为nfgroup001实例组信息：
  ```
  LST NFGROUP: NFGROUPID="nfgroup001";
  %%LST NFGROUP: NFGROUPID="nfgroup001";%%
  RETCODE = 0  执行成功
  操作结果如下:
  -------------------------
   NF实例组标识  =   nfgroup001 
         NF类型  =   CHF             
   NF实例组描述  =   nrfdescription01       

  (结果个数 = 1)

  ---    END
  ```
- 在NRF上查询所有的实例组信息：
  ```
  LST NFGROUP:;
  %%LST NFGROUP:;%%
  RETCODE = 0  执行成功

  操作结果如下:
  -------------------------
  NF实例组标识      NF类型    NF实例组描述       
  nfgroup001        CHF       nrfdescription01     
  nfgroup002        UDM       nrfdescription02      

  (结果个数 = 2)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFGROUP.md`
