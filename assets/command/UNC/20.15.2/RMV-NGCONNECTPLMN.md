---
id: UNC@20.15.2@MMLCommand@RMV NGCONNECTPLMN
type: MMLCommand
name: RMV NGCONNECTPLMN（删除5G Connect PLMN）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGCONNECTPLMN
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- 互联PLMN管理
status: active
---

# RMV NGCONNECTPLMN（删除5G Connect PLMN）

## 功能

**适用NF：AMF**

该命令用于删除可接入到本运营商的某个Connect PLMN。

## 注意事项

- 该命令执行后立即生效。

- 当删除记录时，则归属该记录里的PLMN的，且满足配置中的IMSI范围的所有用户将无法接入到本运营商网络。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定在UNC系统中唯一标识某个运营商。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成Connect PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成Connect PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用5G Connect PLMN的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “SPECIFIED_IMSI_RANGE（指定IMSI范围）”：指定IMSI范围<br>默认值：ALL_USER<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIED_IMSI_RANGE"时为条件必选参数。<br>参数含义：该参数用于指定应用5G Connect PLMN的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGCONNECTPLMN]] · 5G Connect PLMN（NGCONNECTPLMN）

## 使用实例

禁止PLMN为12345的所有漫游用户接入到本运营商网络，将该PLMN从互联PLMN列表中删除，执行如下命令：

```
RMV NGCONNECTPLMN: NOID=0, MCC="123", MNC="45";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGCONNECTPLMN.md`
