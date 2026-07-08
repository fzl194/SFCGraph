# 删除Tcp Mss配置（RMV TCPMSS）

- [命令功能](#ZH-CN_CONCEPT_0182837696__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837696__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837696__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837696__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837696__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837696)

**适用NF：SGW-U、PGW-U、UPF**

![](删除Tcp Mss配置（RMV TCPMSS）_82837696.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除配置后会影响对应APN下传输的TCP报文长度。

该命令用于关闭基于用户归属属性指定APN的TCP MSS调整功能并删除TCP MSS配置。

#### [注意事项](#ZH-CN_CONCEPT_0182837696)

- 该命令执行后立即生效。
- 删除某个APN实例时，会同步删除它的MSS配置。
- 删除配置后，可能导致该APN下的终端和Server协商的TCPMSS过大，造成传输过程中分片报文过多。配置后不建议删除。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837696)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837696)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示APN的名字。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ROAMINGTYPE | 用户漫游类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置用户归属的属性。<br>数据来源：本端规划<br>取值范围：位域类型。<br>- HOME：表示本地用户。<br>- ROAMING：表示漫游用户。<br>- VISITING：表示拜访用户。<br>默认值：无<br>配置原则：<br>- SELECT ALL：表示HOME，ROAMING，VISITING 3种类型都选择。<br>- CLEAR ALL：表示HOME，ROAMING，VISITING 3种类型都不选择。<br>- GREYED ALL：表示HOME，ROAMING，VISITING 3种类型都置灰，都不选择，并保持参数的原始值。<br>- 当选择参数类型后，参数类型后的-1代表使能这个参数，-0代表不使能这个参数。 |

#### [使用实例](#ZH-CN_CONCEPT_0182837696)

关闭apn apn1.com漫游用户的TCP MSS调整功能：

```
RMV TCPMSS: APN="apn1.com", ROAMINGTYPE=ROAMING-1;
```
