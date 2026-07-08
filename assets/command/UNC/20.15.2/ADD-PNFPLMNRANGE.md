---
id: UNC@20.15.2@MMLCommand@ADD PNFPLMNRANGE
type: MMLCommand
name: ADD PNFPLMNRANGE（增加对端NF的PLMN范围）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PNFPLMNRANGE
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF实例PLMN范围管理
status: active
---

# ADD PNFPLMNRANGE（增加对端NF的PLMN范围）

## 功能

**适用NF：AMF、SMF、NSSF、NCG**

该命令用于增加本地配置的对端NF实例支持的PLMN范围信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 注意事项

- 该命令执行后立即生效。

- 当本地没有配置对端NF实例支持的PLMN时，代表此对端NF允许所有PLMN号段范围的用户访问。

- 最多可输入8192条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~8191。<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PLMN范围对应的NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| QUERYTYPE | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PLMN范围的配置号段的方式。<br>数据来源：全网规划<br>取值范围：<br>- “START_END（START_END）”：号段<br>- “PATTERN（PATTERN）”：正则表达式<br>默认值：无<br>配置原则：<br>推荐使用START_END方式。 |
| RANGESTART | 起始号段 | 可选必选说明：该参数在"QUERYTYPE"配置为"START_END"时为条件必选参数。<br>参数含义：该参数用于指定PLMN范围的起始号段。当QUERYTYPE参数设置为START_END模式时有效。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~6。<br>默认值：无<br>配置原则：<br>PLMN的终止号段需要不小于PLMN的起始号段，且结束值和开始值长度需相等。 |
| RANGEEND | 终止号段 | 可选必选说明：该参数在"QUERYTYPE"配置为"START_END"时为条件必选参数。<br>参数含义：该参数用于指定PLMN范围的终止号段。当QUERYTYPE参数设置为START_END模式时有效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。<br>默认值：无<br>配置原则：<br>PLMN的终止号段需要不小于PLMN的起始号段，且结束值和开始值长度需相等。 |
| PATTERN | 模式 | 可选必选说明：该参数在"QUERYTYPE"配置为"PATTERN"时为条件必选参数。<br>参数含义：该参数用于指定PLMN范围的具体的号段匹配正则表达式。当QUERYTYPE参数设置为PATTERN模式时有效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>- 正则表达式不需要输入起始符^和结束符$，样例如下：1234[5-9]。<br>- 正则表达式中使用"[]"指定匹配的字符范围时，需要满足"[0-9]"的格式，覆盖十进制的字符。<br>- 正则表达式转化后的字符串总长度需要满足5或6。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PNFPLMNRANGE]] · 对端NF的PLMN范围（PNFPLMNRANGE）

## 使用实例

增加对端NF的PLMN范围信息，NF实例标识为CHF_Instance_0,查询方式为START_END模式，起始号段为12300，终止号段为12303。

```
ADD PNFPLMNRANGE:INDEX=1, NFINSTANCEID="CHF_Instance_0", QUERYTYPE=START_END, RANGESTART="12300",RANGEEND="12303";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PNFPLMNRANGE.md`
