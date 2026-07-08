---
id: UDG@20.15.2@MMLCommand@MOD PROTREDEFINE
type: MMLCommand
name: MOD PROTREDEFINE（修改重定义协议）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: PROTREDEFINE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- 协议重定义
status: active
---

# MOD PROTREDEFINE（修改重定义协议）

## 功能

**适用NF：PGW-U、UPF**

该命令用来修改重定义协议类型，可以配置源和目的协议名称以及对应的filter，系统能够将符合filter条件的源协议重定义为目的协议。

## 注意事项

- 该命令执行后立即生效。
- PROTREDEFINE中引用的FILTERNAME必须是FILTER配置过的过滤器名称。
- 被本命令引用的FILTERNAME不能配置MSIP，MSPORT和TOS，若配置系统会提示MOD PROTREDEFINE失败。
- 多个配置间的PRIORITY取值不能相同。
- 同一条流不支持被此命令映射为多个解析类协议。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCPROTNAME | 源协议名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置源协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该协议只能为默认协议，不支持自定义协议。 |
| FILTERNAME | 过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD FILTER命令配置生成。 |
| DSTPROTNAME | 目的协议名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置目的协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。必须为缺省协议列表中的协议名称，不能自定义。<br>默认值：无<br>配置原则：<br>- 该协议只能为默认三级协议，不支持自定义协议。<br>- 输入单空格将删除该参数已有配置项。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于设置协议识别匹配的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PROTREDEFINE]] · 重定义协议（PROTREDEFINE）

## 使用实例

把源协议为tls，过滤器为filter2的重定义协议规则的目的协议修改为https：

```
MOD PROTREDEFINE:SRCPROTNAME="tls",DSTPROTNAME="https",FILTERNAME="filter2",PRIORITY=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-PROTREDEFINE.md`
