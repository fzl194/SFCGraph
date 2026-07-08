---
id: UDG@20.15.2@MMLCommand@RMV SPECIFICAPNVAL
type: MMLCommand
name: RMV SPECIFICAPNVAL（删除用户APN与消息交互使用APN的映射关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SPECIFICAPNVAL
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- DN管理
- APN管理
- 指定上报的APN
status: active
---

# RMV SPECIFICAPNVAL（删除用户APN与消息交互使用APN的映射关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](删除用户APN与消息交互使用APN的映射关系（RMV SPECIFICAPNVAL）_07016802.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会改变上报给周边网元的APN，可能会导致用户激活失败或影响用户计费和用户业务。

该命令用于删除用户APN与消息交互使用APN的映射关系。在用户需要删除已有的用户APN与消息交互使用APN的映射关系时使用该命令。

## 注意事项

- 该命令执行后立即生效。
- 要删除的映射关系记录必须是已经添加配置过的。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBSCRIBERAPN | 用户APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户使用的别名APN、虚拟APN或真实APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：必须是已经配置过映射关系的消息记录。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SPECIFICAPNVAL]] · 用户APN与消息交互使用APN的映射关系（SPECIFICAPNVAL）

## 使用实例

删除一个名为“apn1.com”的用户APN和与之对应的上报APN之间的映射关系：

```
RMV SPECIFICAPNVAL:SUBSCRIBERAPN="apn1.com";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-SPECIFICAPNVAL.md`
