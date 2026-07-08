---
id: UDG@20.15.2@MMLCommand@ADD APNBINDPATH
type: MMLCommand
name: ADD APNBINDPATH（添加APNBindPath配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: APNBINDPATH
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 2000
category_path:
- 用户面服务管理
- 路径管理
- N6路径管理
- APN与路径绑定关系
status: active
---

# ADD APNBINDPATH（添加APNBindPath配置）

## 功能

**适用NF：UPF**

使用该命令添加APN/DNN与探测路径的关联关系。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为2000。
- APN与探测路径绑定关系大于1K时，请参考SET FWDFCPARA命令调整探测消息流控阈值。
- 一个APN最多关联10个路径配置。
- 一个路径只能被一个APN关联。应用上如果需要探测一个对端，可以配置不同的路径关联不同的本端地址和相同的对端地址来支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| DETECTPATH | 路径名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定绑定APN的探测路径名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD DETECTPATH命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNBINDPATH]] · APNBindPath配置（APNBINDPATH）

## 使用实例

添加名为“testapn”的apn与名为“testpath3”的探测路径的绑定关系：

```
ADD APNBINDPATH: APN="testapn", DETECTPATH="testpath3";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加APNBindPath配置（ADD-APNBINDPATH）_47981245.md`
