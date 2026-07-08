# 删除对端NF的SUPI信息（RMV PNFSUPI）

- [命令功能](#ZH-CN_MMLREF_0209652379__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652379__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652379__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652379__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652379)

![](删除对端NF的SUPI信息（RMV PNFSUPI）_09652379.assets/notice_3.0-zh-cn_2.png)

RMV PNFSUPI不输入任何参数时会清空配置的所有号段，可能会导致业务损失。

RMV PNFSUPI只输入RANGESTART和RANGEEND，但未输入INDEX，会删除所有包含此号段的所有SUPI信息。

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于删除本地配置的对端NF实例支持的SUPI的信息。

## [注意事项](#ZH-CN_MMLREF_0209652379)

- 该命令执行后立即生效。

- 支持删除指定NFINSTANCEID的所有SUPI信息。
- 支持删除包含RANGESTART到RANGEEND之间任一号段的所有SUPI信息。

#### [操作用户权限](#ZH-CN_MMLREF_0209652379)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652379)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| RANGESTART | 起始号段 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SUPI的起始号段。当QUERYTYPE参数设置为START_END模式时有效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>SUPI的终止号段需要不小于SUPI的起始号段，且终止号段和起始号段长度需相等。 |
| RANGEEND | 终止号段 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SUPI的终止号段。当QUERYTYPE参数设置为START_END模式时有效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>SUPI的终止号段需要不小于SUPI的起始号段，且终止号段和起始号段长度需相等。 |

## [使用实例](#ZH-CN_MMLREF_0209652379)

删除对端NF实例支持的SUPI信息，索引为1。

```
RMV PNFSUPI: INDEX=1;
```
