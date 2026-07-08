---
id: UNC@20.15.2@MMLCommand@MOD ULCLAREADPMODE
type: MMLCommand
name: MOD ULCLAREADPMODE（修改指定DNAI服务区域的ULCL部署模式）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD ULCLAREADPMODE（修改指定DNAI服务区域的ULCL部署模式）

## 功能

**适用NF：SMF**

该命令用于修改指定DNAI服务区域的ULCL部署模式。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数指定APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD APN命令中参数“APN”保持一致。 |
| DNAI | 数据网络访问标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DNAREANAME | DNAI服务区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNAI服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。不区分大小写。<br>默认值：无<br>配置原则：<br>与DNAREA配置中的AREANAME取值对应，且区域类型只能是5G的TAI粒度服务区。 |
| ULCLDEPLOYMODE | ULCL部署模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ULCL部署模式。适用于5G通用分流场景。不影响4G ULCL分流、超级漫游分流场景。<br>数据来源：本端规划<br>取值范围：<br>- “AUXSHUNTPREFER（优先使用辅锚点分流）”：优先辅锚点分流。如果没有与辅锚点合设的ULCL，则使用分离的ULCL。在此基础上，如果依然没有分离的ULCL，则退出ULCL分流场景。<br>- “AUXSHUNTMUST（只使用辅锚点分流）”：只使用辅锚点分流。如果没有与辅锚点合设的ULCL，则退出ULCL分流场景。<br>- “PSASHUNTMUST（只使用主锚点分流）”：只使用主锚点分流。如果没有与主锚点合设的ULCL，则退出ULCL分流场景。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ULCLAREADPMODE]] · 指定DNAI服务区域的ULCL部署模式（ULCLAREADPMODE）

## 使用实例

修改SMF在DNAI服务区域内选择主锚点作为分流ULCL，APN为huawei1，DNAI名称为huawei2，DNAI服务区域为dnarea1。

```
MOD ULCLAREADPMODE:APN="huawei1",DNAI="huawei2",DNAREANAME="dnarea1",ULCLDEPLOYMODE=PSASHUNTMUST;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-ULCLAREADPMODE.md`
