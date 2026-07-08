# 修改防欺诈策略配置（MOD AFPOLICY）

- [命令功能](#ZH-CN_CONCEPT_0186526988__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186526988__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186526988__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186526988__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186526988__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0186526988)

**适用NF：PGW-U、UPF**

该命令用于修改判断出欺诈行为后的处理策略。

#### [注意事项](#ZH-CN_CONCEPT_0186526988)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0186526988)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186526988)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFPOLICYTYPE | 防欺诈策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定防欺诈策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DNS：指定DNS防欺诈。<br>- HTTP：指定HTTP防欺诈。<br>- HTTPS：指定HTTPS防欺诈。<br>默认值：无<br>配置原则：无 |
| PCCPOLICYGRPNM | PCC策略组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCC策略组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD PCCPOLICYGRP命令配置生成。 |
| AFAPPID | 防欺诈应用标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定上报给PCRF的AFAPPID名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：<br>- 若ADD PCCPOLICYGRP命令中的ADCMUTEFLAG参数为DISABLE时，本参数有效。 |
| CATEPROPNAME | 分类属性名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定分类属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CATEGORYPROP命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0186526988)

- 如果运营商需要修改判断出DNS欺诈行为后的PCC处理策略和带宽处理策略，则配置命令如下：
  ```
  MOD AFPOLICY:AFPOLICYTYPE=DNS,PCCPOLICYGRPNM="pccpolicygroup",CATEPROPNAME="cateprop";
  ```
- 如果运营商需要修改判断出DNS欺诈行为后的处理策略，解除PCC策略组绑定，解除分类属性名称绑定，则配置命令如下：
  ```
  MOD AFPOLICY:AFPOLICYTYPE=DNS,PCCPOLICYGRPNM=" ",CATEPROPNAME=" ";
  ```
