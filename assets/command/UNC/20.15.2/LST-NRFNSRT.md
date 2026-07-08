---
id: UNC@20.15.2@MMLCommand@LST NRFNSRT
type: MMLCommand
name: LST NRFNSRT（查询网络切片的路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFNSRT
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
- 网络切片路由管理
status: active
---

# LST NRFNSRT（查询网络切片的路由）

## 功能

**适用NF：NRF**

该命令用于查询已配置的基于网络切片的路由信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SST | 切片服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示切片服务类型，标识网络切片所具备的特性和服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片描述 | 可选必选说明：可选参数<br>参数含义：该参数用于表示切片描述，是对相同切片服务类型的网络切片实例的差异化描述。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>- CBCF（CBCF）<br>- MB_SMF（MB_SMF）<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为UDM、AMF、SMF、AUSF、PCF、CHF的路由转发功能，其他NF类型为预留功能。 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于网络切属性寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFNSRT]] · 网络切片的路由（NRFNSRT）

## 使用实例

- 查询所有的网络切片路由：
  ```
  LST NRFNSRT:;
  %%LST NRFNSRT:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  切片服务类型  切片描述  NF类型  归属NRF组名称  

  0             000001    SMF     L-NRF1    
  128           100001    AMF     L-NRF2    
  128           100011    SMF     L-NRF3    
  (结果个数 = 3)
  ```
- 查询切片服务类型为128，切片描述为100001，NF类型为SMF的网络切片路由：
  ```
  LST NRFNSRT: SST=128, SD="100001", NFTYPE=SMF;
  %%LST NRFNSRT: SST=128, SD="100001", NFTYPE=SMF;%%
  RETCODE = 0  操作成功

  结果如下
  --------
   切片服务类型  =  128
       切片描述  =  100001
         NF类型  =  SMF
  归属NRF组名称  =  L-NRF2
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询网络切片的路由（LST-NRFNSRT）_09653222.md`
