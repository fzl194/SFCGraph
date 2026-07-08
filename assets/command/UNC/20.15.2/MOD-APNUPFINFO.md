---
id: UNC@20.15.2@MMLCommand@MOD APNUPFINFO
type: MMLCommand
name: MOD APNUPFINFO（修改指定APN的UPF节点信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNUPFINFO
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- APN UPF信息管理
status: active
---

# MOD APNUPFINFO（修改指定APN的UPF节点信息）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用户修改指定APN的UPF节点信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数表示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD APN命令中参数“APN”保持一致，使用该前需通过ADD APN添加一组记录。 |
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数表示UPF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。该参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD UPNODE中参数“NFINSTANCENAME”保持一致，使用该前需通过ADD UPNODE添加一组记录。 |
| LOCATION | UPF的位置特征 | 可选必选说明：可选参数<br>参数含义：该参数表示UPF的位置特征。<br>数据来源：本端规划<br>取值范围：<br>- “INHERIT（继承）”：继承ADD UPNODE配置下LOCATION的取值。<br>- “BOTH（中心节点和本地节点）”：指定APN下，既可以做中心节点又可以做边缘节点，既可以作为主锚点也可以作为辅锚点。<br>- “LOCALONLY（仅本地节点）”：指定APN下，做本地节点，只能作为辅锚点。<br>- “CENTERONLY（仅中心节点）”：指定APN下，做中心节点，只能作为主锚点。<br>默认值：无<br>配置原则：无 |
| PSACOMBINEULCL | 主锚点与分流节点合设功能 | 可选必选说明：该参数在"LOCATION"配置为"BOTH"、"CENTERONLY"时为条件可选参数。<br>参数含义：该参数用来控制是否支持主锚点与分流节点合设功能。<br>数据来源：全网规划<br>取值范围：<br>- “INHERIT（继承）”：继承ADD UPNODE配置下PSACOMBINEULCL的取值。<br>- “DISABLE（不使能）”：指定APN下，不支持PSA和分流节点合设。<br>- “ENABLE（使能）”：指定APN下，支持主锚点和分流节点合设<br>默认值：无<br>配置原则：无 |
| LOCKINFO | UPF的锁定信息 | 可选必选说明：可选参数<br>参数含义：该参数用于标识UPF是否被锁定。SMF不会选择到已锁定的UPF。<br>数据来源：全网规划<br>取值范围：<br>- “INHERIT（继承）”：继承ADD UPNODE配置下LOCK的取值。<br>- “UNLOCKED（解锁）”：在指定APN下标识UPF被解锁，SMF可以选择到已解锁的UPF。<br>- “LOCKED（锁定）”：在指定APN下标识UPF被锁定，SMF不会选择到已锁定的UPF。<br>- “SPECIFIC（锁定主锚点）”：该UPF在指定APN下无法被新激活的用户选择作为主锚点UPF。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [指定APN的UPF节点信息（APNUPFINFO）](configobject/UNC/20.15.2/APNUPFINFO.md)

## 使用实例

将UPF实例为upf1的位置特征修改为继承，对应的APN名称为huawei.com：

```
MOD APNUPFINFO:APN="huawei.com",UPFINSTANCEID="upf1",LOCATION=INHERIT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改指定APN的UPF节点信息（MOD-APNUPFINFO）_96242549.md`
