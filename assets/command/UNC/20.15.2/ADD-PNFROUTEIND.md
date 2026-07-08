---
id: UNC@20.15.2@MMLCommand@ADD PNFROUTEIND
type: MMLCommand
name: ADD PNFROUTEIND（增加对端NF的路由指示信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PNFROUTEIND
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
- 对端NF路由标识信息
status: active
---

# ADD PNFROUTEIND（增加对端NF的路由指示信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

- 该命令用于增加本地配置对端NF实例支持的路由指示信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。
- 当NFINSTANCEID配置为"sbidialtest"时，该命令用于新增model-D或model-C间接路由拨测用户列表，通过配置PNFPLMN及PNFROUTEIND的方式，配置一组拨测用户。

## 注意事项

- 该命令执行后立即生效。

- 最多配置80条NFINSTANCEID为“sbidialtest”的记录。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~36。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| ROUTINGIND | 路由指示 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF的路由指示信息。路由指示器是SUCI组成的一部分，用于使用SUCI进行AUSF和UDM的选择。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~4。取值范围0-9999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PNFROUTEIND]] · 对端NF的路由指示信息（PNFROUTEIND）

## 使用实例

增加对端NF路由指示信息，NF实例标识为AUSF_Instance_0，路由指示信息为0001。

```
ADD PNFROUTEIND: NFINSTANCEID="AUSF_Instance_0", ROUTINGIND="0001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PNFROUTEIND.md`
