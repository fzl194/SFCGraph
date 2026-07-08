---
id: UNC@20.15.2@MMLCommand@ADD DMVLE
type: MMLCommand
name: ADD DMVLE（增加Diameter虚拟本地实体）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DMVLE
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter虚拟本地实体
status: active
---

# ADD DMVLE（增加Diameter虚拟本地实体）

## 功能

**适用网元：MME**

该命令用于增加Diameter虚拟本地实体信息。

本命令配置的虚拟本地实体只用于MME链式备份特性（特性编号：WSFD- 201201 ）开启时的S6a接口容灾，即用在容灾时接收并处理对端发送到本虚拟实体的请求消息，并回复响应消息。

除此之外，系统的正常业务流程不能使用本命令配置的虚拟本地实体进行Diameter层通信。

## 注意事项

- 该命令执行后立即生效。
- 本表最大允许配置10条记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOINDEX | 本地实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定虚拟本地实体的索引，在Diameter链路中唯一标识一个虚拟本地实体。<br>数据来源：本端规划<br>取值范围：32~63<br>默认值：32 |
| LOHSTNAME | 本地实体主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定虚拟本地实体的主机名信息，在Diameter协议栈中唯一标识一个虚拟本地实体。数据来源：全网规划<br>取值范围：1～127位字符串<br>默认值：无<br>配置原则：<br>- 大小写不敏感。<br>- 该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。<br>- 该参数建议配置为mmec<MMEC>.mmegi<MMEGI>.mme.epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org，其中<MMEC>、<MMEGI>、<MNC>和<MCC>为十进制数。例如配置为mmec01.mmegi8001.mme.epc.mnc123.mcc123.3gppnetwork.org。<br>- 与容灾MME的DMLE配置的主机名一致。 |
| LORLMNAME | 本地实体域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定虚拟本地实体的域名信息。<br>数据来源：全网规划<br>取值范围：1～127位字符串<br>默认值：无<br>配置原则：<br>- 大小写不敏感。<br>- 该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。<br>- 该参数建议配置为epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org，其中<MNC>和<MCC>为3位十进制数。例如配置为epc.mnc123.mcc123.3gppnetwork.org。<br>- 与容灾MME的DMLE配置的域名一致。 |
| PDTNAME | 产品名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定产品的名称，标识本地的产品信息。<br>数据来源：本端规划<br>取值范围：0～32位字符串<br>默认值：vUSN<br>配置原则：该参数用来标识本端的产品信息，一般可直接填写产品的名称，如填写<br>UNC<br>。 |
| LOINFONAME | 本地实体名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定虚拟本地实体的名称，标示虚拟本地实体。<br>数据来源：本端规划<br>取值范围：0～32位字符串<br>默认值：无<br>配置原则：用来标识本地实体时，一般配置为DMVLE。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMVLE]] · Diameter虚拟本地实体（DMVLE）

## 使用实例

在启用MME链式备份特性场景下，本USN为R-USN，需要配置S-USN的主机名用于S6a接口容灾。增加本地索引为32，本地的主机名为mmec01.mmegi8001.mme.epc.mnc123.mcc123.3gppnetwork.org，域名为epc.mnc123.mcc123.3gppnetwork.org，产品名称为UNC，本体实体名称为DMVLE的虚拟本地实体记录：

ADD DMVLE: LOINDEX=32, LOHSTNAME="mmec01.mmegi8001.mme.epc.mnc123.mcc123.3gppnetwork.org", LORLMNAME="epc.mnc123.mcc123.3gppnetwork.org", PDTNAME="UNC", LOINFONAME="DMVLE";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DMVLE.md`
