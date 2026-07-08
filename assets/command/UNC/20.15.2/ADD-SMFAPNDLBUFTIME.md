---
id: UNC@20.15.2@MMLCommand@ADD SMFAPNDLBUFTIME
type: MMLCommand
name: ADD SMFAPNDLBUFTIME（增加APN的下行报文缓存时长配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMFAPNDLBUFTIME
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- GTP会话协议参数管理
- 下行报文缓存时长
status: active
---

# ADD SMFAPNDLBUFTIME（增加APN的下行报文缓存时长配置）

## 功能

**适用NF：SGW-C**

该命令用来增加APN的下行报文缓存时长配置。

## 注意事项

- 该命令执行后立即生效。

- 该命令应与UPF的APNDLBUFTIME保持一致。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| NORMALUSER | 普通用户下行报文缓存时长(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN下的普通用户下行报文缓存时长。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是3~15，单位是秒。<br>默认值：6<br>配置原则：无 |
| NBIOTUSER | NB-IoT用户下行报文缓存时长(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN下的NB-IoT用户下行报文缓存时长。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是3~200，单位是秒。<br>默认值：6<br>配置原则：无 |

## 操作的配置对象

- [APN的下行报文缓存时长配置（SMFAPNDLBUFTIME）](configobject/UNC/20.15.2/SMFAPNDLBUFTIME.md)

## 使用实例

增加huawei.com的用户下行报文缓存时长配置，普通用户下行报文缓存时长(秒)为7s，NB-IoT用户下行报文缓存时长(秒)为7s：

```
ADD SMFAPNDLBUFTIME: APN="huawei.com", NORMALUSER=7, NBIOTUSER=7;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加APN的下行报文缓存时长配置（ADD-SMFAPNDLBUFTIME）_96805378.md`
