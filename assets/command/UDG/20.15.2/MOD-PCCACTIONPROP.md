---
id: UDG@20.15.2@MMLCommand@MOD PCCACTIONPROP
type: MMLCommand
name: MOD PCCACTIONPROP（修改PCC动作属性）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: PCCACTIONPROP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- PCC控制策略
- PCC动作属性
status: active
---

# MOD PCCACTIONPROP（修改PCC动作属性）

## 功能

**适用NF：PGW-U、UPF**

此命令用于修改PCC动作属性，只有已经添加成功的PccActionProp才能够修改。可以通过命令，修改PCC策略相关的动作属性，包括Gate、URL Redirect动作。支持配置不同业务发起端定义不同的上下行报文处理动作。

## 注意事项

- 该命令执行后立即生效。
- 如果上行或下行发起业务的相应策略没有配置，则按照默认Pass处理。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCACTPROPNAME | PCC动作属性名称 | 可选必选说明：必选参数<br>参数含义：设置PCC动作属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| UPINITREDIRNM | 上行发起重定向名称 | 可选必选说明：可选参数<br>参数含义：设置上行发起业务的URL重定向动作。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD REDIRECT命令配置生成。<br>- 如果运营商需要定义上行发起的业务命中该PCC动作属性，可以主动触发URL重定向动作，建议配置执行URL重定向动作时使用的Redirect对象名称。 |
| UPINITUPGATE | 上行发起上行门控 | 可选必选说明：可选参数<br>参数含义：设置上行发起业务的上行门控动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PASS：表示业务报文直接通过。<br>- DISCARD：表示业务报文直接丢弃。<br>默认值：无<br>配置原则：<br>- 如果运营商需要定义上行发起的业务命中该PCC动作属性时，上行报文的门控动作是通过，则配置为PASS。<br>- 如果运营商需要定义上行发起的业务命中该PCC动作属性时，上行报文的门控动作是丢弃，则配置为DISCARD。 |
| UPINITDNGATE | 上行发起下行门控 | 可选必选说明：可选参数<br>参数含义：设置上行发起业务的下行门控动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PASS：表示业务报文直接通过。<br>- DISCARD：表示业务报文直接丢弃。<br>默认值：无<br>配置原则：<br>- 如果运营商需要定义上行发起的业务命中该PCC动作属性时，下行报文的门控动作是通过，则配置为PASS。<br>- 如果运营商需要定义上行发起的业务命中该PCC动作属性时，下行报文的门控动作是丢弃，则配置为DISCARD。 |
| DNINITREDIRNM | 下行发起重定向名称 | 可选必选说明：可选参数<br>参数含义：设置下行发起业务的URL重定向动作。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD REDIRECT命令配置生成。<br>- 如果运营商需要定义下行发起的业务命中该PCC动作属性，可以主动触发URL重定向动作，建议配置执行URL重定向动作时使用的Redirect对象名称。 |
| DNINITUPGATE | 下行发起上行门控 | 可选必选说明：可选参数<br>参数含义：设置下行发起业务的上行门控动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PASS：表示业务报文直接通过。<br>- DISCARD：表示业务报文直接丢弃。<br>默认值：无<br>配置原则：<br>- 如果运营商需要定义下行发起的业务命中该PCC动作属性时，上行报文的门控动作是通过，则配置为PASS。<br>- 如果运营商需要定义下行发起的业务命中该PCC动作属性时，上行报文的门控动作是丢弃，则配置为DISCARD。 |
| DNINITDNGATE | 下行发起下行门控 | 可选必选说明：可选参数<br>参数含义：设置下行发起业务的下行门控动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PASS：表示业务报文直接通过。<br>- DISCARD：表示业务报文直接丢弃。<br>默认值：无<br>配置原则：<br>- 如果运营商需要定义下行发起的业务命中该PCC动作属性时，下行报文的门控动作是通过，则配置为PASS。<br>- 如果运营商需要定义下行发起的业务命中该PCC动作属性时，下行报文的门控动作是丢弃，则配置为DISCARD。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PCCACTIONPROP]] · PCC动作属性（PCCACTIONPROP）

## 使用实例

假如运营商需要定义一个PCC动作属性，要求对于上行发起的业务，上下行报文均可以正常通过，下行发起的业务，上下行报文均丢弃。 修改一个PCC动作属性，“PCCACTPROPNAME”为“TestPccActPropName”，“UPINITUPGATE”为“PASS”，“UPINITDNGATE”为“PASS”，“DNINITUPGATE”为“DISCARD”，“DNINITDNGATE”为“DISCARD”：

```
MOD PCCACTIONPROP:PCCACTPROPNAME="TestPccActPropName",UPINITUPGATE=PASS,UPINITDNGATE=PASS,DNINITUPGATE=DISCARD,DNINITDNGATE=DISCARD;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-PCCACTIONPROP.md`
