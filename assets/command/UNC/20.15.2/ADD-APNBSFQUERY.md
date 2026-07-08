---
id: UNC@20.15.2@MMLCommand@ADD APNBSFQUERY
type: MMLCommand
name: ADD APNBSFQUERY（增加APN的BSF查询功能配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNBSFQUERY
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- BSF管理
- BSF查询管理
status: active
---

# ADD APNBSFQUERY（增加APN的BSF查询功能配置）

## 功能

**适用NF：SMF、PGW-C**

该命令用于增加指定APN的BSF查询功能配置。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| BSFDNNQUERYSW | BSF支持基于DNN过滤查询会话绑定信息特性开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BSF支持基于DNN过滤查询会话绑定信息特性开关。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（使能）”：使能<br>- “DISABLE（不使能）”：不使能<br>- “INHERIT（继承全局）”：继承全局<br>默认值：INHERIT<br>配置原则：<br>配置为INHERIT时，则以SMFFUNC中的BSFDNNQUERYSW配置值为准。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNBSFQUERY]] · APN的BSF查询功能配置（APNBSFQUERY）

## 使用实例

新增APN为"huawei.com"的BSF查询功能属性，使能支持基于DNN过滤查询会话绑定信息特性开关：

```
ADD APNBSFQUERY: APN="huawei.com", BSFDNNQUERYSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APNBSFQUERY.md`
