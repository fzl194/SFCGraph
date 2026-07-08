# 增加UE重载控制策略（ADD UEOVERLDCTRL）

- [命令功能](#ZH-CN_MMLREF_0000002091067090__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000002091067090__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000002091067090__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000002091067090__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000002091067090)

**适用NF：AMF**

该命令用于为指定的用户（群）配置重载控制策略参数。

该命令的使用场景：若基站需要通过MPS和MCS能力实行重载控制功能，可通过本命令控制AMF是否将UDM签约或本地配置的MPS和MCS能力携带给基站。

## [注意事项](#ZH-CN_MMLREF_0000002091067090)

- 该命令执行后下一次注册流程或签约变更流程生效。

- 最多可输入128条记录。
- 重载控制功能在基站侧生效。
- 本地MPS/MCS能力通过ADD NGMMSUBDATA命令中的“MPSMCSPRI”参数控制，请结合ADD NGMMSUBDATA命令进行配置。

#### [操作用户权限](#ZH-CN_MMLREF_0000002091067090)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000002091067090)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于表示AMF上配置重载控制策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：<br>对于指定的用户群，策略匹配的优先级从高到低依次为：“IMSI_PREFIX(IMSI前缀)”、“HOME_USER(本网用户)”或“FOREIGN_USER(外网用户)”、“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定应用重载控制策略的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。 只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MPSMCSSWITCH | MPSMCS开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置AMF是否支持MPS/MCS功能。功能开关开启后，如果用户没有匹配的ADD NGMMSUBDATA配置，或者匹配的ADD NGMMSUBDATA配置中“MPSMCS优先级（MPSMCSPRI）”取值为“SUB_FIRST(签约优先)”且签约的MPS/MCS有效时，AMF将UDM签约的MPS/MCS能力下发给UE，否则将本地配置(使用ADD NGMMSUBDATA命令配置)的MPS/MCS下发给UE。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：OFF<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000002091067090)

为IMSI前缀为“123456”的用户增加UE重载控制策略，执行如下命令：

```
ADD UEOVERLDCTRL: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456", MPSMCSSWITCH=ON;
```
