# 增加灰度升级拨测用户（ADD GRAYUPTSTUSER）

- [命令功能](#ZH-CN_CONCEPT_0000204935710796__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000204935710796__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000204935710796__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000204935710796__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000204935710796__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000204935710796)

**适用NF：UPF、SGW-U、PGW-U**

该命令用于添加拨测用户信息。

#### [注意事项](#ZH-CN_CONCEPT_0000204935710796)

- 该命令执行后立即生效。
- 该命令最大记录数为200。
- 该命令基于号段最多配置16条。

#### [操作用户权限](#ZH-CN_CONCEPT_0000204935710796)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000204935710796)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRAYUSERNAME | 拨测用户名称 | 可选必选说明：必选参数<br>参数含义：拨测用户名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| TESTTYPE | 类型 | 可选必选说明：必选参数<br>参数含义：拨测类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI：根据IMSI配置拨测用户信息。<br>- IMSIMSISDNSEG：根据IMSI或者MSISDN号段配置拨测用户信息。<br>默认值：无<br>配置原则：1.IMSI：基于IMSI配置拨测用户信息。 2、IMSIMSISDNSEG：基于号段配置拨测用户信息。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“TESTTYPE”配置为“IMSI”时为必选参数。<br>参数含义：IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |
| IMSIMSISDNSEG | IMSI/MSISDN号段 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TESTTYPE”配置为“IMSIMSISDNSEG”时为必选参数。<br>参数含义：IMSI/MSISDN号段。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：该参数使用ADD UPIMSIMSSEG命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0000204935710796)

增加拨测用户的IMSI信息：

```
ADD GRAYUPTSTUSER: GRAYUSERNAME="test", TESTTYPE=IMSI, IMSI="123456789123456";
```
