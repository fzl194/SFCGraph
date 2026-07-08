---
id: UNC@20.15.2@MMLCommand@RMV PNFSERVICEVER
type: MMLCommand
name: RMV PNFSERVICEVER（删除对端NF的服务实例的版本信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PNFSERVICEVER
command_category: 配置类
applicable_nf:
- AMF
- NSSF
- SMF
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
- 对端服务实例版本信息管理
status: active
---

# RMV PNFSERVICEVER（删除对端NF的服务实例的版本信息）

## 功能

**适用NF：AMF、NSSF、SMF、SMSF、NCG**

该命令用于删除本地配置的对端NF实例支持的服务实例的版本信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.不区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| SRVINSTANCEID | 服务实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。大小写不敏感。<br>默认值：无<br>配置原则：无 |
| APIVERSIONINURI | APIURI版本号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要在URI中用于访问API的服务实例的版本号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。大小写不敏感。<br>默认值：无<br>配置原则：无 |
| APIFULLVERSION | API完整版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务访问API的完整版本信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数的构成字符建议是字母A～Z或a～z、数字0～9、点“.”、加号“+”，和中划线“-”，例如1.0.0，1.0.0-alpha.1，3.0.1+orange.2020-09。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFSERVICEVER]] · 对端NF的服务实例的版本信息（PNFSERVICEVER）

## 使用实例

删除对端NF的服务实例版本信息，NF实例标识为AMF_Instance_0， 服务实例标识为Service_Instance_0，APIURI版本号为v1，Api完整版本为1.0.0。

```
RMV PNFSERVICEVER: NFINSTANCEID="AMF_Instance_0", SRVINSTANCEID="Service_Instance_0", APIVERSIONINURI="v1",APIFULLVERSION="1.0.0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端NF的服务实例的版本信息（RMV-PNFSERVICEVER）_09651625.md`
