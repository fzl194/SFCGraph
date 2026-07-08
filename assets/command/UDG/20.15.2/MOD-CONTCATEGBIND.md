---
id: UDG@20.15.2@MMLCommand@MOD CONTCATEGBIND
type: MMLCommand
name: MOD CONTCATEGBIND（修改内容分类组绑定关系）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: CONTCATEGBIND
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容分类组绑定配置
status: active
---

# MOD CONTCATEGBIND（修改内容分类组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改内容分类组绑定关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFPROFILENAME | 内容过滤策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CFPROFILE命令配置生成。 |
| CONTCATEGNAME | 内容分类组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容分类组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CONTCATEGROUP命令配置生成。 |
| ACTION | 动作 | 可选必选说明：可选参数<br>参数含义：该参数用于设置动作。<br>数据来源：本端规划<br>取值范围：<br>- PASS：报文转发。<br>- BLOCK：报文丢弃。<br>- REDIRECT：报文重定向。<br>默认值：无<br>配置原则：无 |
| REDIRECTNAME | 缺省重定向名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ACTION”配置为“REDIRECT”时为必选参数。<br>参数含义：该参数用于设置缺省重定向名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD REDIRECT命令配置生成。 |
| TIMERANGENAME | TimeRange名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置TimeRange名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD TIMERANGE命令配置生成。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [内容分类组绑定关系（CONTCATEGBIND）](configobject/UDG/20.15.2/CONTCATEGBIND.md)

## 使用实例

修改内容分类组动作为报文丢弃：

```
MOD CONTCATEGBIND: CFPROFILENAME="cf_profile1", CONTCATEGNAME="cf_contcategrprange1", ACTION=BLOCK;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改内容分类组绑定关系（MOD-CONTCATEGBIND）_43518651.md`
