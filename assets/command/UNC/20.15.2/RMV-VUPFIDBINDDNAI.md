---
id: UNC@20.15.2@MMLCommand@RMV VUPFIDBINDDNAI
type: MMLCommand
name: RMV VUPFIDBINDDNAI（删除虚拟UPF实例标识的DNAI）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: VUPFIDBINDDNAI
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- 虚拟UPF管理
- DNAI绑定管理
status: active
---

# RMV VUPFIDBINDDNAI（删除虚拟UPF实例标识的DNAI）

## 功能

**适用NF：SMF**

该命令用于删除虚拟UPF实例标识的DNAI。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VUPFINSTANCEID | 虚拟UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于虚拟UPF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。该参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD VIRTUALUPFID中参数“VUPFINSTANCEID”保持一致，使用该前需通过ADD VIRTUALUPFID添加一组记录。 |
| DNAI | 数据网络访问标识符 | 可选必选说明：必选参数<br>参数含义：该参数表示虚拟UPF实例标识的DNAI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VUPFIDBINDDNAI]] · 虚拟UPF实例标识的DNAI（VUPFIDBINDDNAI）

## 使用实例

删除虚拟UPF实例标识为v_upf1,DNAI为huawei.com：

```
RMV VUPFIDBINDDNAI:VUPFINSTANCEID="v_upf1",DNAI="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-VUPFIDBINDDNAI.md`
