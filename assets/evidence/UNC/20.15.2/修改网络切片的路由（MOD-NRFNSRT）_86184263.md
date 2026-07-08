# 修改网络切片的路由（MOD NRFNSRT）

- [命令功能](#ZH-CN_MMLREF_0286184263__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0286184263__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0286184263__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0286184263__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0286184263)

**适用NF：NRF**

该命令用于修改指定网络切片路由所归属的NRF实例组名称。

## [注意事项](#ZH-CN_MMLREF_0286184263)

- 该命令执行后立即生效。

- 根据输入参数条件，如果待修改的记录在系统中只存在一条，则直接执行此命令进行修改。
- 根据输入参数条件，如果待修改的记录在系统中可以匹配到多条，则系统无法判断待修改记录具体是哪一条，不能通过此MOD命令进行修改，此时需要执行对应的RMV记录先删除待修改记录，再执行对应ADD命令新增新的记录（修改后的记录）完成修改。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### [操作用户权限](#ZH-CN_MMLREF_0286184263)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0286184263)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SST | 切片服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示切片服务类型，标识网络切片所具备的特性和服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片描述 | 可选必选说明：必选参数<br>参数含义：该参数用于表示切片描述，是对相同切片服务类型的网络切片实例的差异化描述。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>- CBCF（CBCF）<br>- MB_SMF（MB_SMF）<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为UDM、AMF、SMF、AUSF、PCF、CHF的路由转发功能，其他NF类型为预留功能。 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于网络切属性寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## [使用实例](#ZH-CN_MMLREF_0286184263)

运营商网络规划变更，当前NRF上寻址网络切片的路由发生变化了，网络切片的服务类型为0，切片描述为000001，但是归属NRF组名称变化为L-NRF2，需要执行。

```
MOD NRFNSRT: SST=0, SD="000001", NFTYPE=SMF, NEXTNRFGRPNAME="L-NRF2";
```
