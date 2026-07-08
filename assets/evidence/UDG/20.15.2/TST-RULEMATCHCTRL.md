# 安装规则匹配控制面信息（TST RULEMATCHCTRL）

- [命令功能](#ZH-CN_CONCEPT_0000202989889241__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202989889241__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202989889241__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202989889241__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202989889241__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202989889241)

**适用NF：PGW-U、UPF**

该命令用于安装规则匹配控制面信息。

#### [注意事项](#ZH-CN_CONCEPT_0000202989889241)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202989889241)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202989889241)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MATCHCTRLTYPE | 匹配控制类型 | 可选必选说明：必选参数<br>参数含义：规则匹配时选择的控制面信息类型。<br>数据来源：本端规划<br>取值范围：<br>- POLICY_INFO：表示选择匹配时使用的策略信息。<br>- SPECIFIED_USER：表示选择匹配时使用指定用户的规则。<br>默认值：POLICY_INFO<br>配置原则：指定控制面信息类型。 |
| PREDEFRULENAME | 预定义规则名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MATCHCTRLTYPE”配置为“POLICY_INFO”时为必选参数。<br>参数含义：该参数用于设置预定义规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：指定预定义规则名称进行规则安装。预定义规则名称可以为UserProfile名称或Rule名称。UserProfile名称和Rule名称相同时，两者都安装。 |
| PREDEFRULENAME1 | 预定义规则名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MATCHCTRLTYPE”配置为“POLICY_INFO”时为可选参数。<br>参数含义：该参数用于设置预定义规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：指定预定义规则名称进行规则安装。预定义规则名称可以为UserProfile名称或Rule名称。UserProfile名称和Rule名称相同时，两者都安装。 |
| PREDEFRULENAME2 | 预定义规则名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MATCHCTRLTYPE”配置为“POLICY_INFO”时为可选参数。<br>参数含义：该参数用于设置预定义规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：指定预定义规则名称进行规则安装。预定义规则名称可以为UserProfile名称或Rule名称。UserProfile名称和Rule名称相同时，两者都安装。 |
| PREDEFRULENAME3 | 预定义规则名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MATCHCTRLTYPE”配置为“POLICY_INFO”时为可选参数。<br>参数含义：该参数用于设置预定义规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：指定预定义规则名称进行规则安装。预定义规则名称可以为UserProfile名称或Rule名称。UserProfile名称和Rule名称相同时，两者都安装。 |
| PREDEFRULENAME4 | 预定义规则名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MATCHCTRLTYPE”配置为“POLICY_INFO”时为可选参数。<br>参数含义：该参数用于设置预定义规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：指定预定义规则名称进行规则安装。预定义规则名称可以为UserProfile名称或Rule名称。UserProfile名称和Rule名称相同时，两者都安装。 |
| PREDEFRULENAME5 | 预定义规则名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MATCHCTRLTYPE”配置为“POLICY_INFO”时为可选参数。<br>参数含义：该参数用于设置预定义规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：指定预定义规则名称进行规则安装。预定义规则名称可以为UserProfile名称或Rule名称。UserProfile名称和Rule名称相同时，两者都安装。 |
| PREDEFRULENAME6 | 预定义规则名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MATCHCTRLTYPE”配置为“POLICY_INFO”时为可选参数。<br>参数含义：该参数用于设置预定义规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：指定预定义规则名称进行规则安装。预定义规则名称可以为UserProfile名称或Rule名称。UserProfile名称和Rule名称相同时，两者都安装。 |
| PREDEFRULENAME7 | 预定义规则名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MATCHCTRLTYPE”配置为“POLICY_INFO”时为可选参数。<br>参数含义：该参数用于设置预定义规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：指定预定义规则名称进行规则安装。预定义规则名称可以为UserProfile名称或Rule名称。UserProfile名称和Rule名称相同时，两者都安装。 |
| PREDEFRULENAME8 | 预定义规则名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MATCHCTRLTYPE”配置为“POLICY_INFO”时为可选参数。<br>参数含义：该参数用于设置预定义规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：指定预定义规则名称进行规则安装。预定义规则名称可以为UserProfile名称或Rule名称。UserProfile名称和Rule名称相同时，两者都安装。 |
| PREDEFRULENAME9 | 预定义规则名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MATCHCTRLTYPE”配置为“POLICY_INFO”时为可选参数。<br>参数含义：该参数用于设置预定义规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：指定预定义规则名称进行规则安装。预定义规则名称可以为UserProfile名称或Rule名称。UserProfile名称和Rule名称相同时，两者都安装。 |
| USERTYPE | 查询方式 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MATCHCTRLTYPE”配置为“SPECIFIED_USER”时为必选参数。<br>参数含义：查询方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：IMSI。<br>- MSISDN：MSISDN。<br>默认值：无<br>配置原则：无 |
| IMSI | 用户imsi号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERTYPE”配置为“IMSI”时为必选参数。<br>参数含义：用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |
| MSISDN | 用户msisdn号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERTYPE”配置为“MSISDN”时为必选参数。<br>参数含义：用户的MSISDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERTYPE”配置为“IMSI” 或 “MSISDN”时为必选参数。<br>参数含义：该参数用于指定APN实例名。该APN必须在系统上已经配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及部分特殊字符。可以支持的特殊字符有“.”和“-”，“.”不可以是第一个字符且不可以连续出现。<br>默认值：无<br>配置原则：a string of 1 to 63 characters without any spaces or special characters other than periods (.) and hyphens (-). It must not start with a period (.) or contain consecutive periods (.).。 |

#### [使用实例](#ZH-CN_CONCEPT_0000202989889241)

- 安装预定义规则test用于规则匹配：
  ```
  TST RULEMATCHCTRL: MATCHCTRLTYPE=POLICY_INFO, PREDEFRULENAME="test";
  ```
- 设置指定用户用于规则匹配：
  ```
  TST RULEMATCHCTRL: MATCHCTRLTYPE=SPECIFIED_USER, USERTYPE=IMSI, IMSI= "xxxx", APN="xxxx";
  ```
