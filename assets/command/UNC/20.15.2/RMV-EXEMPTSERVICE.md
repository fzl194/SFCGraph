---
id: UNC@20.15.2@MMLCommand@RMV EXEMPTSERVICE
type: MMLCommand
name: RMV EXEMPTSERVICE（删除豁免业务）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: EXEMPTSERVICE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 分组数据离线状态管理
- 豁免业务配置
status: active
---

# RMV EXEMPTSERVICE（删除豁免业务）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除豁免业务。豁免业务（3GPP PS data off Exempt Services）不受3GPP PS data off能力控制，即使3GPP PS data off能力使能，这类业务也不受影响。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXEMPTAPN | 豁免APN | 可选必选说明：必选参数<br>参数含义：该参数用于配置豁免业务的APN，APN指真实APN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入的APN名称需要符合APN命名规则。 |

## 操作的配置对象

- [豁免业务（EXEMPTSERVICE）](configobject/UNC/20.15.2/EXEMPTSERVICE.md)

## 使用实例

当运营商需要删除豁免业务，执行如下命令：

```
RMV EXEMPTSERVICE: EXEMPTAPN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除豁免业务（RMV-EXEMPTSERVICE）_35439600.md`
