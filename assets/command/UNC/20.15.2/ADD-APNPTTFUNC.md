---
id: UNC@20.15.2@MMLCommand@ADD APNPTTFUNC
type: MMLCommand
name: ADD APNPTTFUNC（增加基于APN的一键通功能配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNPTTFUNC
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 一键通
- APN的一键通配置
status: active
---

# ADD APNPTTFUNC（增加基于APN的一键通功能配置）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用于开启或关闭指定APN的一键通功能。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |
| LTEPTTSWITCH | LTE一键通功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启和关闭基于APN的LTE一键通功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：DISABLE<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNPTTFUNC]] · 基于APN的一键通功能配置（APNPTTFUNC）

## 使用实例

增加“APN”为"HUAWEI.COM"的LTE一键通功能：

```
ADD APNPTTFUNC: APN="HUAWEI.COM", LTEPTTSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加基于APN的一键通功能配置（ADD-APNPTTFUNC）_06399904.md`
