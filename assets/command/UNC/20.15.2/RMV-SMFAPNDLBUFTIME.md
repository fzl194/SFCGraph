---
id: UNC@20.15.2@MMLCommand@RMV SMFAPNDLBUFTIME
type: MMLCommand
name: RMV SMFAPNDLBUFTIME（删除APN的下行报文缓存时长配置）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV SMFAPNDLBUFTIME（删除APN的下行报文缓存时长配置）

## 功能

**适用NF：SGW-C**

该命令用来删除APN的下行报文缓存时长配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFAPNDLBUFTIME]] · APN的下行报文缓存时长配置（SMFAPNDLBUFTIME）

## 使用实例

删除huawei.com的下行报文缓存时长配置：

```
RMV SMFAPNDLBUFTIME: APN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN的下行报文缓存时长配置（RMV-SMFAPNDLBUFTIME）_96805500.md`
