# 删除AM策略和UE策略控制参数（RMV AMUEPLCYCTRL）

- [命令功能](#ZH-CN_MMLREF_0209654397__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209654397__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209654397__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209654397__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209654397)

**适用NF：AMF**

该命令用于删除指定的AM策略和UE策略的控制参数。

## [注意事项](#ZH-CN_MMLREF_0209654397)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209654397)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209654397)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于表示AMF上配置AM策略和UE策略控制参数的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：IMSI前缀<br>- “MSISDN_PREFIX（MSISDN前缀）”：MSISDN前缀<br>默认值：无<br>配置原则：<br>对于指定的用户（群），策略匹配的优先级从高到低依次为：“MSISDN_PREFIX(MSISDN前缀)”、“IMSI_PREFIX(IMSI前缀)”、“HOME_USER(本网用户)”或“FOREIGN_USER(外网用户)”、“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定应用AM策略和UE策略的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"MSISDN_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定应用AM策略和UE策略的用户的MSISDN前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| NSGRPID | 网络切片群组标识 | 可选必选说明：该参数在"SUBRANGE"配置为"ALL_USER"时为条件必选参数。<br>参数含义：该参数用于表示AMF上应用AM策略和UE策略控制参数的网络切片群组。用于AM和UE策略控制的网络切片群组通过ADD PLCYNSGRP命令进行配置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~16。0用于表示无效的网络切片群组，即不按照网络切片对AM策略或者UE策略进行控制。<br>默认值：无<br>配置原则：<br>当运营商希望基于网络切片控制AMF是否需要向PCF建立AM、UE策略偶联时，可通过本参数关联指定的网络切片列表。 |

## [使用实例](#ZH-CN_MMLREF_0209654397)

删除为外网用户配置的AM策略和UE策略控制参数，执行如下命令：

```
RMV AMUEPLCYCTRL: SUBRANGE=FOREIGN_USER;
```
