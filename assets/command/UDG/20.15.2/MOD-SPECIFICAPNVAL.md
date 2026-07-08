---
id: UDG@20.15.2@MMLCommand@MOD SPECIFICAPNVAL
type: MMLCommand
name: MOD SPECIFICAPNVAL（修改用户APN与消息交互使用APN的映射关系）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: SPECIFICAPNVAL
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- APN管理
- 指定上报的APN
status: active
---

# MOD SPECIFICAPNVAL（修改用户APN与消息交互使用APN的映射关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于修改用户使用的别名APN、虚拟APN或真实APN与交互消息中使用的指定的APN之间的映射关系。其中交互消息包括：头增强以及同网关上报报表服务器交互消息。在用户需要修改已有的APN映射关系时使用该命令。

## 注意事项

- 该命令执行后立即生效。
- 要修改的映射关系记录必须是已经添加配置过的。
- 修改某条记录只需填写需要修改项的值，未填写部分将会保持与原记录一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBSCRIBERAPN | 用户APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户使用的别名APN、虚拟APN或真实APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：必须是已经配置过的APN或APN别名。 |
| REPORTOBJECT | 上报对象 | 可选必选说明：可选参数<br>参数含义：该参数用于设置所使用的上报APN服务类型。<br>数据来源：本端规划<br>取值范围：位域类型。<br>- HEAD_ENRICH：指定当前要进行配置的服务类型为HEAD_ENRICH。<br>默认值：无<br>配置原则：<br>- 当需要修改某条映射关系中的上报APN名称时，配置该参数。<br>- 在参数SpecificAPN有输入的情况下，需对该参数进行配置。 |
| SPECIFICAPN | 具体上报APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户使用的上报APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 当需要修改某条映射关系中的上报APN名称时，配置该参数。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SPECIFICAPNVAL]] · 用户APN与消息交互使用APN的映射关系（SPECIFICAPNVAL）

## 使用实例

运营商需要修改一个用户APN和上报APN之间的映射关系，用户APN名称为“apn1.com”，上报APN名称为“reportname”，上报对象选择HEAD_ENRICHG，配置命令如下：

```
MOD SPECIFICAPNVAL:SUBSCRIBERAPN="apn1.com",REPORTOBJECT=HEAD_ENRICH-1,SPECIFICAPN="reportname";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-SPECIFICAPNVAL.md`
