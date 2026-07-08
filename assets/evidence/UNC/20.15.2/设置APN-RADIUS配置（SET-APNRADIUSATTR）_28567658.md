# 设置APN RADIUS配置（SET APNRADIUSATTR）

- [命令功能](#ZH-CN_MMLREF_0228567658__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0228567658__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0228567658__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0228567658__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0228567658)

**适用NF：PGW-C、SMF、GGSN**

该命令用于设置APN的RADIUS相关信息，当用户需要修改APN下配置的RADIUS信息时，可以使用该命令。

## [注意事项](#ZH-CN_MMLREF_0228567658)

- 该命令执行后立即生效。

- APN的值是由ADD APN命令添加，DOMAINNAMEACT的初始值为不支持增加或剥离域名功能；DOMAINNAMEPOS的初始值为空。

#### [操作用户权限](#ZH-CN_MMLREF_0228567658)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0228567658)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等，不能以“.”开头，也不能有连续的“.”，不区分大小写。<br>默认值：无。<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| DOMAINNAMEACT | 增加或剥离域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定当用户在指定APN下入网时，PGW-C和AAA交互，RADIUS消息中的用户名是否支持增加或剥离域名功能。<br>数据来源：本端规划<br>取值范围：<br>- “ADD_DISABLE_STRIP_DISABLE（不支持增加或剥离域名功能）”：不支持增加或剥离域名功能<br>- “ADD_ENABLE_STRIP_DISABLE（仅支持增加域名功能）”：仅支持增加域名功能<br>- “ADD_DISABLE_STRIP_ENABLE（仅支持剥离域名功能）”：仅支持剥离域名功能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNRADIUSATTR查询当前参数配置值。<br>配置原则：无 |
| DOMAINNAMEPOS | 域名位置 | 可选必选说明：该参数在"DOMAINNAMEACT"配置为"ADD_ENABLE_STRIP_DISABLE"时为条件必选参数。<br>参数含义：该参数用于指定APN下入网的用户增加的域名为前缀域名还是后缀域名。<br>数据来源：本端规划<br>取值范围：<br>- “NULL（NULL）”：NULL<br>- “PREFIX（PREFIX）”：前缀域名<br>- “SUFFIX（SUFFIX）”：后缀域名<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNRADIUSATTR查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0228567658)

假设用户在APN “huawei.com”接入，需要控制鉴权消息中的用户名增加后缀域名，使用该命令配置：

```
SET APNRADIUSATTR: APN="huawei.com", DOMAINNAMEACT=ADD_ENABLE_STRIP_DISABLE, DOMAINNAMEPOS=SUFFIX;
```
