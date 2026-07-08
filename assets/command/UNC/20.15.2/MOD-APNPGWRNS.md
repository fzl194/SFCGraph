---
id: UNC@20.15.2@MMLCommand@MOD APNPGWRNS
type: MMLCommand
name: MOD APNPGWRNS（修改PGW重定向功能设置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNPGWRNS
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 增加PGW重定向功能设置
status: active
---

# MOD APNPGWRNS（修改PGW重定向功能设置）

## 功能

**适用NF：PGW-C**

该命令用于修改PGW重定向功能设置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入的APN名称需要符合APN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”。一般情况下用真实APN进行配置，但若开启虚拟APN映射功能，则使用请求APN进行配置。 |
| PGWRNSSWITCH | PGW重定向功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指示是否支持PGW重定向功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：<br>如果打开本开关，即便关闭SMFFUNC中的REPSNSSAI，或关闭软参APN_DWORD_1 BIT9，PGW也会与UDM交互。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNPGWRNS]] · PGW重定向功能设置（APNPGWRNS）

## 使用实例

打开APN为“HUAWEI.COM”的PGW重定向功能开关：

```
MOD APNPGWRNS: APN="HUAWEI.COM", PGWRNSSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改PGW重定向功能设置（MOD-APNPGWRNS）_50919533.md`
