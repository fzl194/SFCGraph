---
id: UNC@20.15.2@MMLCommand@LST APNCHGMODE
type: MMLCommand
name: LST APNCHGMODE（查询基于APN的计费接口选择方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNCHGMODE
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- APN计费模式
status: active
---

# LST APNCHGMODE（查询基于APN的计费接口选择方式）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用来查询不同基于APN的终端和接入类型下所使用的计费接口。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNCHGMODE]] · 基于APN的计费接口选择方式（APNCHGMODE）

## 使用实例

查询基于APN的计费接口选择方式，“APN名称”为“huawei.com”。

```
%%LST APNCHGMODE: APN="huawei.com";%%
RETCODE = 0  操作成功

结果如下
--------
APN名称     指定终端和接入类型  按5GS互操作指示选择计费接口  指定的计费模式  作为SGW计费模式  作为V-SMF计费模式  ISMF是否支持计费  按5GC无限制接入标识选择计费接口

huawei.com  5G终端4G接入        是                           GaGy模式        继承其他选项     Nchf模式           不使能            否
huawei.com  5G终端5G接入        否                           Nchf模式        GaGy模式         Nchf模式           不使能            否
huawei.com  非5G终端4G接入      否                           GaGy模式        GaGy模式         Nchf模式           不使能            否
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNCHGMODE.md`
