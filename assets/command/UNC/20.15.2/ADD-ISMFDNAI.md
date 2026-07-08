---
id: UNC@20.15.2@MMLCommand@ADD ISMFDNAI
type: MMLCommand
name: ADD ISMFDNAI（增加I-SMF支持的DNAI）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ISMFDNAI
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- DNAI管理
- I-SMF DNAI管理
status: active
---

# ADD ISMFDNAI（增加I-SMF支持的DNAI）

## 功能

**适用NF：SMF**

该命令用于增加I-SMF支持的DNAI。I-SMF支持的DNAI有两种类型：DNN级别和整系统级别。DNN级别的DNAI仅对激活该DNN的PDU会话生效。整系统级别DNAI对所有PDU会话均生效。

在I-SMF插入或改变流程中I-SMF会将整系统DNAI以及用户当前会话DNN所关联的DNAI发送给锚点SMF，锚点SMF会在响应消息中将协商出的会话DNAI携带给I-SMF。当用户位置移动时，如果用户在新的区域需要进行UL CL/BP分流，I-SMF会根据从锚点SMF获取的DNAI为用户插入UL CL/BP UPF和辅锚点UPF。

## 注意事项

- 该命令执行后只对新接入该设备且把该设备作为I-SMF的PDU会话生效。

- 最多可输入512条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识符 | 可选必选说明：必选参数<br>参数含义：该参数用于指定I-SMF支持的DNAI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DNAITYPE | DNAI类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNAI的类型。<br>数据来源：全网规划<br>取值范围：<br>- DNN_LEVEL（DNN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：该参数在"DNAITYPE"配置为"DNN_LEVEL"时为条件必选参数。<br>参数含义：该参数用于指定该DNAI关联的DNN，即用户请求的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| AUXDNAISELECTSW | 仅使用DNAI查询辅锚点的控制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制基于当前DNAI查询辅锚点时，是否支持仅使用DNAI来查询。该开关开启时，I-SMF查询辅锚点时，仅使用该DNAI来查询。开关关闭时，I-SMF查询辅锚点时，使用DNN+DNAI来查询。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：DISABLE<br>配置原则：<br>I-SMF开启仅使用DNAI来查询辅锚点功能，需要端到端规划。该功能当前仅支持测试。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ISMFDNAI]] · I-SMF支持的DNAI（ISMFDNAI）

## 使用实例

新增一条I-SMF支持的DNAI为“huawei.com.dnai”，DNAITYPE为DNN_LEVEL，DNN为“huawei.com”的DNAI，执行如下命令:

```
ADD ISMFDNAI: DNAI="huawei.com.dnai", DNAITYPE=DNN_LEVEL, DNN="huawei.com", AUXDNAISELECTSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-ISMFDNAI.md`
