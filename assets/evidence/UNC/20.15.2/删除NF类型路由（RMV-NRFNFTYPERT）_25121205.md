# 删除NF类型路由（RMV NRFNFTYPERT）

- [命令功能](#ZH-CN_MMLREF_0225121205__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0225121205__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0225121205__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0225121205__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0225121205)

**适用NF：NRF**

该命令用于删除NF类型路由信息。

## [注意事项](#ZH-CN_MMLREF_0225121205)

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### [操作用户权限](#ZH-CN_MMLREF_0225121205)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0225121205)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF类型路由寻址的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：<br>该参数值为UDM、AMF、SMF、AUSF、PCF、CHF、BSF、SCP类型时不生效。 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示当前NRF基于NFTYPE路由寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |

## [使用实例](#ZH-CN_MMLREF_0225121205)

运营商网络为三层网络，最高层PLMN-NRF，中间层H-NRF，最底层L-NRF。L-NRF1归属于H-NRF1，H-NRF1归属于PLMN-NRF。在H-NRF1和PLMN-NRF上分别执行如下命令，删除NF类型为SMSF的NF类型路由信息。

```
RMV NRFNFTYPERT:  NFTYPE=SMSF, NEXTNRFGRPNAME="L-NRF1";
```
