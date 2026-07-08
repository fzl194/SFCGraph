---
id: UNC@20.15.2@MMLCommand@SET APNPLMNRATECTRL
type: MMLCommand
name: SET APNPLMNRATECTRL（设置APN Serving PLMN速率控制配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: APNPLMNRATECTRL
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 速率控制
- PLMN速率控制
- APN Serving PLMN速率控制
status: active
---

# SET APNPLMNRATECTRL（设置APN Serving PLMN速率控制配置）

## 功能

![](设置APN Serving PLMN速率控制配置（SET APNPLMNRATECTRL）_64343912.assets/notice_3.0-zh-cn_2.png)

配置基于APN的Serving PLMN速率控制功能，可能会导致用户业务丢包。

**适用NF：PGW-C、SGW-C**

该命令用于配置基于APN的Serving PLMN速率控制功能，用于限制终端的数据传输速率。

## 注意事项

- 该命令执行后立即生效。

- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：PLMNRATECTRLSW：DISABLE。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无。<br>配置原则：<br>该参数使用<br>[**ADD APN**](../../../APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>命令配置生成。 |
| PLMNRATECTRLSW | APN Serving PLMN速率控制开关 | 可选必选说明：必选参数<br>参数含义：该参数用于基于APN控制开启和关闭Serving PLMN速率控制功能。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：使能<br>- “DISABLE（不使能）”：不使能<br>- “INHERIT（继承全局）”：继承全局<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [APN Serving PLMN速率控制配置（APNPLMNRATECTRL）](configobject/UNC/20.15.2/APNPLMNRATECTRL.md)

## 使用实例

APN名称为test下的PLMN速率控制开关配置为ENABLE：

```
SET APNPLMNRATECTRL:APN="test",PLMNRATECTRLSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置APN-Serving-PLMN速率控制配置（SET-APNPLMNRATECTRL）_64343912.md`
