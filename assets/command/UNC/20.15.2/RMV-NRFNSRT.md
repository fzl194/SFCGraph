---
id: UNC@20.15.2@MMLCommand@RMV NRFNSRT
type: MMLCommand
name: RMV NRFNSRT（删除网络切片的路由）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFNSRT
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- 网络切片路由管理
status: active
---

# RMV NRFNSRT（删除网络切片的路由）

## 功能

**适用NF：NRF**

该命令用于删除网络切片信息对应的某条路由或全部路由。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SST | 切片服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示切片服务类型，标识网络切片所具备的特性和服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片描述 | 可选必选说明：必选参数<br>参数含义：该参数用于表示切片描述，是对相同切片服务类型的网络切片实例的差异化描述。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>- CBCF（CBCF）<br>- MB_SMF（MB_SMF）<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为UDM、AMF、SMF、AUSF、PCF、CHF的路由转发功能，其他NF类型为预留功能。 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于网络切属性寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFNSRT]] · 网络切片的路由（NRFNSRT）

## 使用实例

运营商网络为三层组网，最高层PLMN-NRF，中间层H-NRF，最低层L-NRF。L-NRF1归属于H-NRF1，H-HRF1归属于PLMN-NRF。在H-NRF1和PLMN-NRF上分别执行如下命令，删除网络切片类型为0，切片描述为000001的路由信息。

- 在H-NRF1上执行：
  ```
  RMV NRFNSRT: SST=0, SD="000001", NFTYPE=SMF, NEXTNRFGRPNAME="L-NRF1";
  ```
- 在PLMN-NRF上执行：
  ```
  RMV NRFNSRT: SST=0, SD="000001", NFTYPE=SMF, NEXTNRFGRPNAME="H-NRF1";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除网络切片的路由（RMV-NRFNSRT）_09652206.md`
