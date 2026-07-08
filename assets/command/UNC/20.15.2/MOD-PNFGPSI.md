---
id: UNC@20.15.2@MMLCommand@MOD PNFGPSI
type: MMLCommand
name: MOD PNFGPSI（修改对端NF的GPSI信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PNFGPSI
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF实例GPSI信息
status: active
---

# MOD PNFGPSI（修改对端NF的GPSI信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于修改本地配置的对端NF实例支持的GPSI信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GPSI的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GPSI对应的NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| QUERYTYPE | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GPSI的配置号段的方式。<br>数据来源：本端规划<br>取值范围：<br>- “START_END（START_END）”：号段<br>- “PATTERN（PATTERN）”：正则表达式<br>默认值：无<br>配置原则：<br>推荐使用START_END方式。 |
| RANGESTART | 起始号段 | 可选必选说明：该参数在"QUERYTYPE"配置为"START_END"时为条件可选参数。<br>参数含义：该参数用于指定GPSI的起始号段。当QUERYTYPE参数设置为START_END模式时有效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>GPSI的终止号段需要不小于GPSI的起始号段，且终止号段和起始号段长度需相等。 |
| RANGEEND | 终止号段 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GPSI的终止号段。当QUERYTYPE参数设置为START_END模式时有效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>GPSI的终止号段需要不小于GPSI的起始号段，且终止号段和起始号段长度需相等。 |
| PATTERN | 模式 | 可选必选说明：该参数在"QUERYTYPE"配置为"START_END"、"PATTERN"时为条件可选参数。<br>参数含义：该参数用于指定GPSI的具体的号段匹配正则表达式。当QUERYTYPE参数设置为PATTERN模式时有效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>- 正则表达式不需要输入起始符^和结束符$，样例如下：msisdn-12345678904[0-9]{4}。<br>- 正则表达式转化后的字符串总长度范围是12~22。 |

## 操作的配置对象

- [对端NF的GPSI信息（PNFGPSI）](configobject/UNC/20.15.2/PNFGPSI.md)

## 使用实例

修改对端NF GPSI信息，NF实例标识为UDM_Instance_0，GPSI查询号段为START_END方式，起始号段为138100000000000，终止号段为138100000000001的信息。

```
MOD PNFGPSI: INDEX=1,NFINSTANCEID="UDM_Instance_0", QUERYTYPE=START_END,RANGESTART="138100000000000",RANGEEND="138100000000001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端NF的GPSI信息（MOD-PNFGPSI）_09653229.md`
