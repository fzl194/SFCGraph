---
id: UNC@20.15.2@MMLCommand@RMV MULDNNBINDAREA
type: MMLCommand
name: RMV MULDNNBINDAREA（删除智能分流专网DNN支持的服务区域）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MULDNNBINDAREA
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 智能分流专网DNN管理
status: active
---

# RMV MULDNNBINDAREA（删除智能分流专网DNN支持的服务区域）

## 功能

**适用NF：SMF**

删除指定智能分流专网DNN支持的服务区域。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEDDNN | 智能分流专网DNN | 可选必选说明：必选参数<br>参数含义：该参数指定智能分流专网DNN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| AREANAME | 服务区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务区域名称。服务区域是指智能分流DNN支持的区域，也是企业园区所处的区域。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。<br>默认值：无<br>配置原则：<br>与APNAREA配置中的AREANAME取值对应，且区域类型只能是5G的TAI粒度服务区。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MULDNNBINDAREA]] · 智能分流专网DNN支持的服务区域（MULDNNBINDAREA）

## 使用实例

删除指定智能分流专网DNN支持的服务区域，智能分流专网DNN为“special.dnn”，服务区域名称为“dnnarea1”。

```
RMV MULDNNBINDAREA: DEDDNN="special.dnn", AREANAME="dnnarea1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MULDNNBINDAREA.md`
