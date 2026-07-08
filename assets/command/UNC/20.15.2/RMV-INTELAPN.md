---
id: UNC@20.15.2@MMLCommand@RMV INTELAPN
type: MMLCommand
name: RMV INTELAPN（删除可按携带智能分流关键词进行处理的APN）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: INTELAPN
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
- 智能分流APN列表
status: active
---

# RMV INTELAPN（删除可按携带智能分流关键词进行处理的APN）

## 功能

**适用NF：PGW-C**

该命令用于删除可按携带智能分流关键词进行处理的APN。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指示2B2C双DNN特性中专用DNN会话的APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@INTELAPN]] · 可按携带智能分流关键词进行处理的APN（INTELAPN）

## 使用实例

为不携带智能分流关键词的APN "huawei.com",删除2B2C漫游双DNN特性

```
RMV INTELAPN: APN="huawei.com"; 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-INTELAPN.md`
