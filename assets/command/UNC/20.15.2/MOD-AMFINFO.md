---
id: UNC@20.15.2@MMLCommand@MOD AMFINFO
type: MMLCommand
name: MOD AMFINFO（修改AMF信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: AMFINFO
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- AMF
- AMF信息管理
status: active
---

# MOD AMFINFO（修改AMF信息）

## 功能

**适用NF：AMF**

该命令用于修改AMF实例信息，如AMF实例的名称、相对容量等。

## 注意事项

- 该命令执行后立即生效。

- 非必要场景下，INTERPLMNFQDN参数不建议配置包含“_”字符的取值。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AMFINSTANCENAME | AMF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于在UNC系统中唯一指定某个AMF实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。可输入的字符有字母、十进制数字、"_"和“-”，例如，AMF_Instance_0。<br>默认值：无<br>配置原则：无 |
| AMFNAME | AMF名称 | 可选必选说明：可选参数<br>参数含义：该参数用于在运营商网络中唯一标识本AMF实例。当NG-RAN接入时，AMF通过NG Setup Response将本参数值通知给NG-RAN。当AMF向NRF注册时，如果未携带IP地址，则要携带本参数；如果携带了IP地址，则本参数可选携带。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~150。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| INTERPLMNFQDN | PLMN间AMF名称 | 可选必选说明：可选参数<br>参数含义：该参数表示本AMF开放给互联运营商的名称，用于互联运营商的NF访问本AMF提供的服务。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~150。可输入的字符有字母、十进制数字、“_”、“-”和“.”，并且开头和结尾只能是数字或者字母。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。<br>非必要场景下，该参数不建议配置包含“_”字符的取值。 |
| CAPACITY | 相对容量 | 可选必选说明：可选参数<br>参数含义：该参数表示AMF下发给接入网的相对容量。接入网根据该值实现在Pool内多个AMF之间的负载均衡选择。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>基于Pool中AMF的实际容量规划本参数值。本参数取值越大，当用户初始接入时AMF被选中的概率就越大。当该参数取值为0，即表示不期望基站将新用户注册到本AMF。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数表示对AMF的描述信息，在运维过程中起助记作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFINFO]] · AMF信息（AMFINFO）

## 使用实例

Pool内AMF的容量重新规划，将实例名称为AMF_Instance_0的AMF的相对容量值从200修改为100：

```
MOD AMFINFO: AMFINSTANCENAME="AMF_Instance_0", CAPACITY=100;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-AMFINFO.md`
