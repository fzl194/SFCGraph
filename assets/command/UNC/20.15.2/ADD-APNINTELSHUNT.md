---
id: UNC@20.15.2@MMLCommand@ADD APNINTELSHUNT
type: MMLCommand
name: ADD APNINTELSHUNT（增加APN智能分流关键词）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNINTELSHUNT
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- APN智能分流关键词
status: active
---

# ADD APNINTELSHUNT（增加APN智能分流关键词）

## 功能

**适用NF：PGW-C**

该命令用于增加APN智能分流关键词。

## 注意事项

- 该命令执行后立即生效。

- 每个APN下最多配置1个智能分流关键词，一个智能分流关键词可以被多个APN绑定。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定2B2C双DNN特性中通用DNN会话的APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| INTELSHUNT | 智能分流关键词 | 可选必选说明：必选参数<br>参数含义：该参数用于指定智能分流关键词。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNINTELSHUNT]] · APN智能分流关键词（APNINTELSHUNT）

## 使用实例

增加“APN”为“huawei.com”，智能分流关键词为“huawei1”的配置：

```
ADD APNINTELSHUNT: APN="huawei.com", INTELSHUNT="huawei1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APNINTELSHUNT.md`
