# 增加关口局NF信息（ADD NRFPLMNNF）

- [命令功能](#ZH-CN_MMLREF_0000001180010522__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001180010522__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001180010522__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001180010522__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001180010522)

**适用NF：NRF**

该命令用于增加本NRF管理的关口局NF，对于漫游业务，通过此命令可以使NRF在服务发现流程中优选返回关口局NF。

## [注意事项](#ZH-CN_MMLREF_0000001180010522)

- 该命令执行后立即生效。

- 当增加关口局NF配置时，非漫游场景下该NF将不能被发现。

- 最多可输入1024条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0000001180010522)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001180010522)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示目的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示本NRF管理的关口局NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）、星号（*）组成，不区分大小写。<br>默认值：无<br>配置原则：<br>支持统配ID，通配ID为“*”，表示该NRF下所有的NF均为关口局NF。 |
| NFNAME | NF名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF管理的关口局NF名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001180010522)

使用如下命令增加NF类型为SMF，NF实例标识为123e4567-e89b-12d3-a456-426655440000的关口局信息。

```
ADD NRFPLMNNF: NFTYPE=SMF, NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
```
