---
id: UNC@20.15.2@MMLCommand@LST NRFNFTYPERT
type: MMLCommand
name: LST NRFNFTYPERT（查询NF类型路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFNFTYPERT
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- NFTYPE路由管理
status: active
---

# LST NRFNFTYPERT（查询NF类型路由）

## 功能

**适用NF：NRF**

该命令用于查询已配置的NF类型路由信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF类型路由寻址的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：<br>该参数值为UDM、AMF、SMF、AUSF、PCF、CHF、BSF、SCP类型时不生效。 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于NFTYPE路由寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFNFTYPERT]] · NF类型路由（NRFNFTYPERT）

## 使用实例

- 运营商想要查询NF类型为SMSF，归属NRF组名称为L-NRF1的NF类型路由信息。
  ```
  LST NRFNFTYPERT:  NFTYPE=SMSF, NEXTNRFGRPNAME="L-NRF1";
  %%LST NRFNFTYPERT:  NFTYPE=SMSF, NEXTNRFGRPNAME="L-NRF1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
         NF类型  =  SMSF 
  归属NRF组名称  =  L-NRF1
  (结果个数 = 1)
  ```
- 查询所有NF类型路由信息。
  ```
  LST NRFNFTYPERT:;
  %%LST NRFNFTYPERT:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NF类型    归属NRF组名称  
  SMSF      L-NRF1  
  NRF       L-NRF2  
  (结果个数 = 2)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF类型路由（LST-NRFNFTYPERT）_25121191.md`
