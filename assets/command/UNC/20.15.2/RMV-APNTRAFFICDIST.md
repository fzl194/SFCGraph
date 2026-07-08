---
id: UNC@20.15.2@MMLCommand@RMV APNTRAFFICDIST
type: MMLCommand
name: RMV APNTRAFFICDIST（删除漫游地动态签约分流控制）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNTRAFFICDIST
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 本地分流管理
- 漫游地动态签约分流控制
status: active
---

# RMV APNTRAFFICDIST（删除漫游地动态签约分流控制）

## 功能

**适用NF：SMF**

该命令用于删除漫游地动态签约分流控制参数。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SELECTEDDNN | Selected DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定基于漫游地动态签约的分流策略控制特性的AMF带给SMF的Selected DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNTRAFFICDIST]] · 漫游地动态签约分流控制（APNTRAFFICDIST）

## 使用实例

假设运营商需要修改计费方式，删除Selected DNN名称为 “mall1”的漫游地动态签约分流控制配置。

```
RMV APNTRAFFICDIST: SELECTEDDNN = "mall1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APNTRAFFICDIST.md`
