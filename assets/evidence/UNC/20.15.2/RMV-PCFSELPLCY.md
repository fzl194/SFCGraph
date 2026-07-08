# 删除PCF选择策略（RMV PCFSELPLCY）

- [命令功能](#ZH-CN_MMLREF_0244007721__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0244007721__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0244007721__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0244007721__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0244007721)

**适用NF：AMF**

该命令用于对指定的用户群删除PCF的选择策略。

## [注意事项](#ZH-CN_MMLREF_0244007721)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0244007721)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0244007721)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用PCF选择策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “USER_GROUP（用户群）”：用户群<br>- “IMSI_PREFIX（IMSI前缀）”：IMSI前缀<br>默认值：无<br>配置原则：<br>对于指定的用户（群），PCF选择策略的匹配优先级从高到低依次为：“USER_GROUP(用户群)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定应用PCF策略的用户的IMSI前缀。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>“IMSIPRE”为预留参数，该策略暂未实现。 |

## [使用实例](#ZH-CN_MMLREF_0244007721)

删除为漫游用户配置的目标PCF选择策略，恢复到默认的选择策略，执行如下命令：

```
RMV PCFSELPLCY: SUBRANGE=FOREIGN_USER;
```
