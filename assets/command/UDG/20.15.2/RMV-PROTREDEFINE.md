---
id: UDG@20.15.2@MMLCommand@RMV PROTREDEFINE
type: MMLCommand
name: RMV PROTREDEFINE（删除重定义协议）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PROTREDEFINE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- 协议重定义
status: active
---

# RMV PROTREDEFINE（删除重定义协议）

## 功能

**适用NF：PGW-U、UPF**

![](删除重定义协议（RMV PROTREDEFINE）_52053412.assets/notice_3.0-zh-cn.png)

本命令属于高危命令,执行本命令后将删除指定或所有重定义协议配置，可能影响业务识别结果，导致计费或控制策略发生变化，请谨慎使用。

该命令用来删除所有PROTOREDEFINE配置信息，或者根据SRCPROTNAME，FILTERNAME和DSTPROTNAME条件删除指定的PROTREDEFINE配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCPROTNAME | 源协议名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置源协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该协议只能为默认协议，不支持自定义协议。 |
| FILTERNAME | 过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD FILTER命令配置生成。 |
| DSTPROTNAME | 目的协议名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置目的协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。必须为缺省协议列表中的协议名称，不能自定义。<br>默认值：无<br>配置原则：该协议只能为默认三级协议，不支持自定义协议。 |

## 操作的配置对象

- [重定义协议（PROTREDEFINE）](configobject/UDG/20.15.2/PROTREDEFINE.md)

## 使用实例

删除重定义协议protredefine：

```
RMV PROTREDEFINE:SRCPROTNAME="tls";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除重定义协议（RMV-PROTREDEFINE）_52053412.md`
