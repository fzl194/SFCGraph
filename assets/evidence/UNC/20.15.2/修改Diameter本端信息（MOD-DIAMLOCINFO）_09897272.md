# 修改Diameter本端信息（MOD DIAMLOCINFO）

- [命令功能](#ZH-CN_CONCEPT_0209897272__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897272__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897272__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897272__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897272__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897272)

**适用NF：PGW-C、SMF**

![](修改Diameter本端信息（MOD DIAMLOCINFO）_09897272.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改Diameter本端信息可能导致Diameter链路重建或中断，进而影响用户使用业务，比如用户被去活等。

此命令用来修改Diameter本端信息。

#### [注意事项](#ZH-CN_CONCEPT_0209897272)

- 该命令执行后立即生效。
- 修改后，将导致所有使用该LocalInfo的所有链路断开并重建，已建立的IP-CAN Session会话状态不受影响，但该会话的后续授权操作将失败。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897272)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897272)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 本端主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格。<br>默认值：无<br>配置原则：无 |
| REALMNAME | 本端域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格。<br>默认值：无<br>配置原则：无 |
| PRODUCTNAME | 产品名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定产品名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |
| VENDORID | Vendor-Id AVP值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Vendor-Id AVP值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：无 |
| FIRMWAREREV | Firmware-Revision AVP值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Firmware-Revision AVP值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：如果配置为4294967295，表示Diameter消息不携带Firmware-Revision AVP。 |
| ORIGINSTATEID | Origin-State-Id AVP使能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Origin-State-Id AVP。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：<br>- DISABLE：表示Diameter消息不携带Origin-State-Id AVP。<br>- ENABLE：表示Diameter消息携带Origin-State-Id AVP。 |
| SUPPORTVENDORID | Supported-Vendor-Id AVP使能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Supported-Vendor-Id AVP。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：<br>- DISABLE：表示Diameter消息不携带Supported-Vendor-Id AVP。<br>- ENABLE：表示Diameter消息携带Supported-Vendor-Id AVP。 |

#### [使用实例](#ZH-CN_CONCEPT_0209897272)

修改Diameter本端信息，HOSTNAME为“test”，REALMNAME为“test”，PRODUCTNAME为“product”，VENDORID为0,FIRMWAREREV为1，ORIGINSTATEID为DISABLE，SUPPORTVENDORID为DISABLE：

```
MOD DIAMLOCINFO:HOSTNAME="vepcs50.epc.mnc004.mcc123.3gppnetwork.org",REALMNAME="epc.mnc004.mcc123.3gppnetwork.org",PRODUCTNAME="product",VENDORID=0,FIRMWAREREV=1,ORIGINSTATEID=DISABLE,SUPPORTVENDORID=DISABLE;
```
