# 删除CHR上报用户（RMV CHRRPTSUBID）

- [命令功能](#ZH-CN_CONCEPT_0264015293__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0264015293__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0264015293__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0264015293__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0264015293__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0264015293)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除指定用户本地存储CHR表单。

#### [注意事项](#ZH-CN_CONCEPT_0264015293)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0264015293)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0264015293)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 用户识别码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0264015293)

- 删除IMSI为460030123456789的用户本地存储CHR表单的配置：
  ```
  RMV CHRRPTSUBID: IMSI="460030123456789";
  ```
- 删除所有指定用户本地存储CHR表单配置：
  ```
  RMV CHRRPTSUBID:;
  ```
