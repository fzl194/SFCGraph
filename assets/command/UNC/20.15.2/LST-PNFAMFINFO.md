---
id: UNC@20.15.2@MMLCommand@LST PNFAMFINFO
type: MMLCommand
name: LST PNFAMFINFO（查询对端AMF信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFAMFINFO
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端AMF信息管理
status: active
---

# LST PNFAMFINFO（查询对端AMF信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询本地配置的对端AMF的信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端AMF的NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~38。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4；不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| AMFREGIONID | AMF区域标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端AMF所在区域的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。本参数的构成字符建议由字母A～F或a～f、数字0～9组成。<br>默认值：无<br>配置原则：<br>大小写不敏感。 |
| AMFSETID | AMF组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端AMF所在集合（即Pool）的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。本参数的构成字符建议是字母A～F或a～f、数字0～9，且第一个字符是数字0-3。<br>默认值：无<br>配置原则：<br>大小写不敏感。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PNFAMFINFO]] · 对端AMF信息（PNFAMFINFO）

## 使用实例

查询对端AMF信息。

```
%%LST PNFAMFINFO:;%%
RETCODE = 0 操作成功

结果如下
------------------------
 NF实例标识 = amf_instance_1
AMF区域标识 = 00
  AMF组标识 = 001
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PNFAMFINFO.md`
