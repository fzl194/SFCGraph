---
id: UNC@20.15.2@MMLCommand@LST PNFGUAMI
type: MMLCommand
name: LST PNFGUAMI（查询对端AMF的GUAMI信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFGUAMI
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
- 对端GUAMI信息管理
status: active
---

# LST PNFGUAMI（查询对端AMF的GUAMI信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询本地配置的对端AMF实例支持的GUAMI信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端AMF的实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端AMF的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：<br>本参数由3个十进制数字组成。 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端AMF的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：<br>本参数由2~3个十进制数字组成。 |
| AMFID | AMF标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端AMF的AMF标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [对端AMF的GUAMI信息（PNFGUAMI）](configobject/UNC/20.15.2/PNFGUAMI.md)

## 使用实例

查询本地配置的对端AMF支持的GUAMI信息。

```
%%LST PNFGUAMI:;%%
RETCODE = 0 操作成功

结果如下
------------------------
  NF实例标识 = amf_instance_1
  移动国家码 = 460
    移动网号 = 03
     AMF标识 = 000001
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询对端AMF的GUAMI信息（LST-PNFGUAMI）_09653685.md`
