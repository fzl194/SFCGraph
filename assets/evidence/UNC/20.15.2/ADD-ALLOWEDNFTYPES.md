# 增加允许访问的NF类型（ADD ALLOWEDNFTYPES）

- [命令功能](#ZH-CN_MMLREF_0209652560__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652560__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652560__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652560__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652560)

**适用NF：NRF**

该命令用于为NF对象新增允许访问的NF类型信息。

NF/NFS可以通过访问授权控制策略控制访问自己的NF/NFS范围：只允许特定PLMN内的NF访问、只允许特定NF类型访问、只允许特定NF Domain访问、只允许支持特定切片的NF访问。访问授权控制策略可以在NF/NFS向NRF注册或更新时通过属性控制，也可以在NRF上配置控制，本命令是在NRF上配置访问授权控制时使用。

## [注意事项](#ZH-CN_MMLREF_0209652560)

- 该命令执行后并不会立即生效，需要执行CMT ALLOWPLCY命令后生效。

- 当该允许访问属性未配置时，表示针对此对象在NRF上的设置是可以被任何NF类型的NF实例访问。
- 如果NF/NFS在注册或更新时携带了允许访问NF类型的属性，此命令也配置了允许访问的NF类型，NRF最终取访问授权策略的交集。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入2048条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0209652560)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652560)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJNAME | 授权对象名称 | 可选必选说明：必选参数<br>参数含义：该参数表示设置访问授权控制的NF对象名称。该参数通过LST ALLOWEDOBJNAME命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |
| ALLOWEDNFTYPE | 允许访问该对象的NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示指定NF对象允许访问的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652560)

运营商为对象名称为objname001（FQDN为huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org）的NF设置允许访问的NF类型为NRF。

```
ADD ALLOWEDOBJNAME: OBJNAME="objname001";
ADD ALLOWEDOBJ:OBJNAME="objname001",FQDN="huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org";
ADD ALLOWEDNFTYPES: OBJNAME="objname001", ALLOWEDNFTYPE=NRF;
```
