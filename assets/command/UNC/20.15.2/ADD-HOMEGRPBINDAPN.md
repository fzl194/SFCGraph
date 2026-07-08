---
id: UNC@20.15.2@MMLCommand@ADD HOMEGRPBINDAPN
type: MMLCommand
name: ADD HOMEGRPBINDAPN（增加Home Group和APN的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: HOMEGRPBINDAPN
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- Home Group绑定APN
status: active
---

# ADD HOMEGRPBINDAPN（增加Home Group和APN的绑定关系）

## 功能

**适用NF：PGW-C、GGSN**

该命令用来配置指定APN实例与Home Group的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 每个APN下最多配置128个Home Group，一个Home Group可以被多个APN绑定。
- APN绑定Home Group后，只使用该APN下绑定的Home Group进行号段匹配。

- 最多可输入384000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| HOMEGROUPINDX | Home Group编号 | 可选必选说明：必选参数<br>参数含义：该参数用来设置Home Group的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：<br>该参数使用ADD HOMEGROUP命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HOMEGRPBINDAPN]] · Home Group和APN的绑定关系（HOMEGRPBINDAPN）

## 使用实例

增加“APN”为“huawei.com”，“Home Group编号”为“1”的Home Group和APN的绑定关系配置：

```
ADD HOMEGRPBINDAPN: APN="huawei.com", HOMEGROUPINDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-HOMEGRPBINDAPN.md`
