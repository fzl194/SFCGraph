# 删除SMF选择策略（RMV SMFSELPLCY）

- [命令功能](#ZH-CN_MMLREF_0209652104__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652104__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652104__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652104__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652104)

![](删除SMF选择策略（RMV SMFSELPLCY）_09652104.assets/notice_3.0-zh-cn_2.png)

执行该命令配置用户范围会影响部分用户SMF选择策略，可能导致业务受损。

**适用NF：AMF**

该命令用于对指定的用户（群）删除SMF的选择策略。

## [注意事项](#ZH-CN_MMLREF_0209652104)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209652104)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652104)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用SMF选择策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：<br>对于指定的用户（群），SMF选择策略的匹配优先级从高到低依次为：“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定应用SMF选择策略的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652104)

调测结束，删除指定拨测用户根据IMSI选择目标SMF的策略配置，执行如下命令：

```
RMV SMFSELPLCY:SUBRANGE=IMSI_PREFIX,IMSIPRE="1230312";
```
