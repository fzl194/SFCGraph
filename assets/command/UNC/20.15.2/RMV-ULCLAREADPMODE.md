---
id: UNC@20.15.2@MMLCommand@RMV ULCLAREADPMODE
type: MMLCommand
name: RMV ULCLAREADPMODE（删除指定DNAI服务区域的ULCL部署模式）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ULCLAREADPMODE
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- ULCL分流部署策略
- DNAI服务区域粒度的ULCL部署模式
status: active
---

# RMV ULCLAREADPMODE（删除指定DNAI服务区域的ULCL部署模式）

## 功能

**适用NF：SMF**

该命令删除指定DNAI服务区域的ULCL部署模式。

## 注意事项

- 该命令执行后立即生效。

- 删除本配置后，在此服务区域内的ULCL部署模式由更粗粒度的配置(ULCLDNAIDPMODE、ULCLAPNDPMODE)控制。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数指定APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD APN命令中参数“APN”保持一致。 |
| DNAI | 数据网络访问标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DNAREANAME | DNAI服务区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNAI服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。不区分大小写。<br>默认值：无<br>配置原则：<br>与DNAREA配置中的AREANAME取值对应，且区域类型只能是5G的TAI粒度服务区。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ULCLAREADPMODE]] · 指定DNAI服务区域的ULCL部署模式（ULCLAREADPMODE）

## 使用实例

删除SMF在DNAI服务区域内的ULCL部署模式，APN为huawei1，DNAI名称为huawei2，DNAI服务区域为dnarea1。

```
RMV ULCLAREADPMODE:APN="huawei1",DNAI="huawei2",DNAREANAME="dnarea1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ULCLAREADPMODE.md`
