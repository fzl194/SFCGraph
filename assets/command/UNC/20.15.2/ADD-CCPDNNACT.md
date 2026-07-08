---
id: UNC@20.15.2@MMLCommand@ADD CCPDNNACT
type: MMLCommand
name: ADD CCPDNNACT（增加融合计费Proxy基于DNN处理动作）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CCPDNNACT
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 融合计费Proxy基于DNN处理动作
status: active
---

# ADD CCPDNNACT（增加融合计费Proxy基于DNN处理动作）

## 功能

**适用NF：NCG**

该命令用于增加融合计费Proxy基于DNN的处理动作。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1010条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNTYPE | DNN类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNN的类型。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（针对未指定的DNN设置处理动作）<br>- VALUE（针对DNN设置处理动作）<br>默认值：无<br>配置原则：无 |
| DNNID | 数据网络名称 | 可选必选说明：该参数在"DNNTYPE"配置为"VALUE"时为条件必选参数。<br>参数含义：该参数用于指定数据网络名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| FWDOCSENABLE | 是否转发OCS | 可选必选说明：必选参数<br>参数含义：该参数用于设置是否转发OCS。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CCPDNNACT]] · 融合计费Proxy基于DNN处理动作（CCPDNNACT）

## 使用实例

增加数据网络名称为“IMS”的融合计费Proxy基于DNN处理动作，设置是否转发OCS为FALSE：

```
ADD CCPDNNACT: DNNTYPE=VALUE, DNNID="IMS", FWDOCSENABLE=FALSE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-CCPDNNACT.md`
