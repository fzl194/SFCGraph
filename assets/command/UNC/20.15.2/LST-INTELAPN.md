---
id: UNC@20.15.2@MMLCommand@LST INTELAPN
type: MMLCommand
name: LST INTELAPN（查询可按携带智能分流关键词进行处理的APN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: INTELAPN
command_category: 查询类
applicable_nf:
- PGW-C
effect_mode: ''
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

# LST INTELAPN（查询可按携带智能分流关键词进行处理的APN）

## 功能

**适用NF：PGW-C**

该命令用于查询可按携带智能分流关键词进行处理的APN。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指示2B2C双DNN特性中专用DNN会话的APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [可按携带智能分流关键词进行处理的APN（INTELAPN）](configobject/UNC/20.15.2/INTELAPN.md)

## 使用实例

为不携带智能分流关键词的APN huawei.com,查询是否开启2B2C漫游双DNN特性。

```
LST INTELAPN: APN="huawei.com"; 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询可按携带智能分流关键词进行处理的APN（LST-INTELAPN）_40119809.md`
