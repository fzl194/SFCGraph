# 显示tethering用户终端接入数量（DSP TETHERINGINFO）

- [命令功能](#ZH-CN_CONCEPT_0210261520__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0210261520__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0210261520__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0210261520__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0210261520__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0210261520__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0210261520)

**适用NF：PGW-U、UPF**

该命令用于查询指定用户下tethering终端接入的数量。

#### [注意事项](#ZH-CN_CONCEPT_0210261520)

当SET TETHERDETGLBPARA的STATISTICMETHOD参数设为CONFIG时，每个用户下Tethering节点的最大个数，按照UserProfile下TetheringMaxNum参数配置值加1申请。

#### [操作用户权限](#ZH-CN_CONCEPT_0210261520)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0210261520)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERTYPE | 用户类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：用户标识类型为IMSI。<br>- MSISDN：用户标识类型为MSISDN。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERTYPE”配置为“IMSI”时为必选参数。<br>参数含义：表示用户的IMSI号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。必须全部为整数。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERTYPE”配置为“MSISDN”时为必选参数。<br>参数含义：表示用户的MSISDN号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。必须全部为整数，且不能为“19”。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0210261520)

假设运营商想要查询指定用户下tethering终端接入的数量：

```
DSP TETHERINGINFO: USERTYPE=IMSI, IMSI="123456";
```

```

RETCODE = 0  操作成功

tethering用户终端接入数量
-------------------------
Pod Name = ssgpod-010-30-1-5               
-------------------------------
Tethering User Num = 0         

(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0210261520)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Result | 结果信息。 |
