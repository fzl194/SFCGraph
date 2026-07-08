---
id: UDG@20.15.2@MMLCommand@MOD PROTOCOLDEFINE
type: MMLCommand
name: MOD PROTOCOLDEFINE（修改自定义协议）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: PROTOCOLDEFINE
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
- 三四层规则管理
- 自定义协议
status: active
---

# MOD PROTOCOLDEFINE（修改自定义协议）

## 功能

**适用NF：PGW-U、UPF**

该命令用来修改自定义协议类型，可以配置自定义协议所属协议大类，带服务器IP地址、端口范围、或HOST值的过滤器，以及协议识别匹配时的优先级，通过该命令的设置，系统可以根据设置的IP地址、端口或HOST值识别出7层协议类型。

## 注意事项

- 该命令执行后立即生效。
- PROTOCOLDEFINE中引用的FILTERNAME必须是FILTER配置过的过滤器名称。
- 如果自定义协议被引用，不允许执行修改操作，必须先解除引用关系。
- 被本命令引用的FILTERNAME不能配置MSIP，MSPORT和TOS，若配置系统会提示 MOD PROTOCOLDEFINE失败。
- 多个配置间的PRIORITY取值不能相同。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTDEFINENAME | 自定义协议名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置自定义协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。必须和默认的协议大类/协议/协议子类名称不同。<br>默认值：无<br>配置原则：无 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置自定义协议分类所属的协议大类分组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。必须为系统缺省协议列表中的协议大类分组名称，不能自定义。<br>默认值：无<br>配置原则：无 |
| FILTERNAME | 过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。数据源为ADD FILTER配置。<br>默认值：无<br>配置原则：该参数使用ADD FILTER命令配置生成。 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于设置协议识别匹配的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PROTOCOLDEFINE]] · 自定义协议（PROTOCOLDEFINE）

## 使用实例

把名称为protdefine的自定义协议绑定的过滤器修改为filter2：

```
MOD PROTOCOLDEFINE:PROTDEFINENAME="protdefine",PROTGROUPNAME="p2p",FILTERNAME="filter2",PRIORITY=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-PROTOCOLDEFINE.md`
