# 设置QosShape配置（SET QOSSHAPE）

- [命令功能](#ZH-CN_CONCEPT_0182837671__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837671__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837671__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837671__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837671__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837671)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于配置用户上下行shaping功能的全局开关，可以指定无线接入类型、漫游属性来配置用户上下行shaping功能，当使能shaping功能后，系统会根据用户协商后的上下行最大带宽和保证带宽对用户的报文发送速率做控制。

#### [注意事项](#ZH-CN_CONCEPT_0182837671)

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为3。
- 用户CAR功能和shaping功能是系统控制带宽的两种方式，只能同时使能一种方式，当CAR功能开关和shaping功能开关同时使能时，系统会优先根据shaping功能开关进行控制。
- 开启后会导致性能下降。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | USERTYPE | ULRAT | DLRAT |
| --- | --- | --- | --- |
| 初始值 | HOME | NULL | NULL |
| 初始值 | ROAMING | NULL | NULL |
| 初始值 | VISITING | NULL | NULL |

#### [操作用户权限](#ZH-CN_CONCEPT_0182837671)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837671)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERTYPE | 用户漫游类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的漫游属性。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- HOME：表示本地用户。<br>- ROAMING：表示漫游用户。<br>- VISITING：表示拜访用户。<br>默认值：无<br>配置原则：无 |
| ULRAT | 上行RAT类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户上行的接入类型。<br>数据来源：全网规划<br>取值范围：位域类型。<br>- unknown：表示RAT类型为未知类型。<br>- utran：表示RAT类型为UTRAN类型。<br>- geran：表示RAT类型为GERAN类型。<br>- wlan：表示RAT类型为WLAN类型。<br>- gan：表示RAT类型为GAN类型。<br>- hspae：表示RAT类型为HSPAE类型。<br>- eutran：表示RAT类型为EUTRAN类型。<br>- eutran_nb_iot：表示RAT类型为EUTRAN-NB-IoT类型。<br>- lte_m：表示RAT类型为LTE_M类型。<br>- nr：表示RAT类型为NR类型。<br>- redcap：表示RAT类型为REDCAP类型。<br>默认值：无<br>配置原则：<br>- SELECT ALL：表示unknown，utran，geran，wlan，gan，hspae，eutran，eutran-nb-iot，lte-m，nr，redcap 11种类型都选择。<br>- CLEAR ALL：表示unknown，utran，geran，wlan，gan，hspae，eutran，eutran-nb-iot，lte-m，nr，redcap 11种类型都不选择。<br>- GREYED ALL：表示unknown，utran，geran，wlan，gan，hspae，eutran，eutran-nb-iot，lte-m，nr，redcap 11种类型都置灰，都不选择。 |
| DLRAT | 下行RAT类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户下行的接入类型。<br>数据来源：全网规划<br>取值范围：位域类型。<br>- unknown：表示RAT类型为未知类型。<br>- utran：表示RAT类型为UTRAN类型。<br>- geran：表示RAT类型为GERAN类型。<br>- wlan：表示RAT类型为WLAN类型。<br>- gan：表示RAT类型为GAN类型。<br>- hspae：表示RAT类型为HSPAE类型。<br>- eutran：表示RAT类型为EUTRAN类型。<br>- eutran_nb_iot：表示RAT类型为EUTRAN-NB-IoT类型。<br>- lte_m：表示RAT类型为LTE_M类型。<br>- nr：表示RAT类型为NR类型。<br>- redcap：表示RAT类型为REDCAP类型。<br>默认值：无<br>配置原则：<br>- SELECT ALL：表示unknown，utran，geran，wlan，gan，hspae，eutran，eutran-nb-iot，lte-m，nr，redcap 11种类型都选择。<br>- CLEAR ALL：表示unknown，utran，geran，wlan，gan，hspae，eutran，eutran-nb-iot，lte-m，nr，redcap 11种类型都不选择。<br>- GREYED ALL：表示unknown，utran，geran，wlan，gan，hspae，eutran，eutran-nb-iot，lte-m，nr，redcap 11种类型都置灰，都不选择。 |

#### [使用实例](#ZH-CN_CONCEPT_0182837671)

设置使能用户上行shaping功能，配置用户上行接入类型为geran，漫游属性visiting：

```
SET QOSSHAPE: USERTYPE=VISITING, ULRAT=geran-1;
```
