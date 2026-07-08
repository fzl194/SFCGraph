---
id: UNC@20.15.2@MMLCommand@LST NRFSRVSCOPERT
type: MMLCommand
name: LST NRFSRVSCOPERT（查询ServingScope路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFSRVSCOPERT
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
- ServingScope路由管理
status: active
---

# LST NRFSRVSCOPERT（查询ServingScope路由）

## 功能

**适用NF：NRF**

该命令用于查询基于服务范围的路由信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示支持服务范围路由寻址的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| SRVSCOPE | NF服务范围 | 可选必选说明：可选参数<br>参数含义：该参数用于表示服务范围。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于服务范围寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFSRVSCOPERT]] · ServingScope路由（NRFSRVSCOPERT）

## 使用实例

- 查询所有的基于服务范围的路由信息：
  ```
  LST NRFBSFINDEXRT:;
  %%LST NRFBSFINDEXRT:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  NF类型 NF服务范围 归属NRF组名称
  NRF    city1      L-NRF
  NRF    city1      H-NRF
  (结果个数 = 2)
  ```
- 查询NF类型为NRF, NF服务范围为"scope01",归属NRF组名称为H-NRF的路由信息：
  ```
  LST NRFSRVSCOPERT: NFTYPE=NRF, SRVSCOPE="city1", NEXTNRFGRPNAME="H-NRF";
  %%LST NRFSRVSCOPERT:NFTYPE=NRF, SRVSCOPE="city1", NEXTNRFGRPNAME="H-NRF";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
         NF类型 = NRF
     NF服务范围 = city1
  归属NRF组名称 = H-NRF
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询ServingScope路由（LST-NRFSRVSCOPERT）_44007065.md`
