# 增加ServingScope路由（ADD NRFSRVSCOPERT）

- [命令功能](#ZH-CN_MMLREF_0244006510__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0244006510__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0244006510__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0244006510__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0244006510)

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增基于服务范围的路由信息。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

如果针对同一个ServingScope配置了多个不同的下一跳归属NRF组名称，那么当前NRF会选取下一跳所有归属NRF组中优先级最高的NRF。

## [注意事项](#ZH-CN_MMLREF_0244006510)

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入10240条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0244006510)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0244006510)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示支持服务范围路由寻址的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| SRVSCOPE | NF服务范围 | 可选必选说明：必选参数<br>参数含义：该参数用于表示服务范围。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示当前NRF基于服务范围寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## [使用实例](#ZH-CN_MMLREF_0244006510)

- 运营商网络为三层组网，最高层PLMN-NRF，中间层H-NRF，最低层L-NRF。L-NRF1归属于H-NRF1，H-HRF1归属于PLMN-NRF。当跨NRF进行服务发现，希望发现的目标NF使用的NF类型为NRF，NF服务范围为city1时，需要在H-NRF1和PLMN-NRF上分别配置到如下路由信息。 在H-NRF1上执行：
  ```
  ADD NRFSRVSCOPERT: NFTYPE=NRF, SRVSCOPE="city1", NEXTNRFGRPNAME="L-NRF1";
  ```
- 在PLMN-NRF上执行：
  ```
  ADD NRFSRVSCOPERT: NFTYPE=NRF, SRVSCOPE="city1", NEXTNRFGRPNAME="H-NRF1";
  ```
