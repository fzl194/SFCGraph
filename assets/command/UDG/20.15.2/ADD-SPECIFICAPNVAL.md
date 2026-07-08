---
id: UDG@20.15.2@MMLCommand@ADD SPECIFICAPNVAL
type: MMLCommand
name: ADD SPECIFICAPNVAL（增加用户APN与消息交互使用APN的映射关系）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SPECIFICAPNVAL
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 3000
category_path:
- 用户面服务管理
- DN管理
- APN管理
- 指定上报的APN
status: active
---

# ADD SPECIFICAPNVAL（增加用户APN与消息交互使用APN的映射关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于新增用户使用的别名APN、虚拟APN或真实APN与交互消息中使用的指定的APN之间的映射关系。其中交互消息包括：头增强交互消息。在用户需要设置新的APN映射关系时使用该命令。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为3000。
- 用户APN和上报APN必须是在APN 实例表或APN别名表中已配置过的。
- 若APN实例表或APN别名表中删除了某个APN名称 ，也需将相应的映射关系从本表中删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBSCRIBERAPN | 用户APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户使用的别名APN、虚拟APN或真实APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：必须是系统已经配置的APN或APN别名。 |
| REPORTOBJECT | 上报对象 | 可选必选说明：必选参数<br>参数含义：该参数用于设置所使用的上报APN服务类型。<br>数据来源：本端规划<br>取值范围：位域类型。<br>- HEAD_ENRICH：指定当前要进行配置的服务类型为HEAD_ENRICH。<br>默认值：无<br>配置原则：无 |
| SPECIFICAPN | 具体上报APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户使用的上报APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：必须是系统已经配置的APN或APN别名。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SPECIFICAPNVAL]] · 用户APN与消息交互使用APN的映射关系（SPECIFICAPNVAL）

## 使用实例

运营商需要增加一个用户APN和头增强类型的上报APN之间的映射关系，用户APN名称为“apn1.com”，上报APN名称为“headname”，上报对象选择HEAD_ENRICH，配置命令如下：

```
ADD SPECIFICAPNVAL:SUBSCRIBERAPN="apn1.com",REPORTOBJECT=HEAD_ENRICH-1,SPECIFICAPN="headname";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-SPECIFICAPNVAL.md`
