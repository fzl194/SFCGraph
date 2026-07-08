---
id: UDG@20.15.2@MMLCommand@MOD CFTEMPLATE
type: MMLCommand
name: MOD CFTEMPLATE（修改内容过滤模板）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: CFTEMPLATE
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
- 内容过滤模板配置
status: active
---

# MOD CFTEMPLATE（修改内容过滤模板）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改一个内容过滤模板实例。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFTEMPLATENAME | 内容过滤模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ICAPSRVGMNAME | 主用CONTENT_FILTERING类型的ICAP服务器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置主用URL_FILTERING类型的ICAP服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD ICAPSVRGRP命令配置生成。<br>- 输入单空格将删除该参数已有配置项。 |
| ICAPSRVGSNAME | 备用CONTENT_FILTERING类型的ICAP服务器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置备用URL_FILTERING类型的ICAP服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD ICAPSVRGRP命令配置生成。<br>- 输入单空格将删除该参数已有配置项。 |
| TIMELIMITNUM | 响应超时限制次数 | 可选必选说明：可选参数<br>参数含义：该参数用于设置响应超时限制次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～65535。<br>默认值：无<br>配置原则：无 |
| RESPTIMEOUT | 响应超时时间（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设置响应超时时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～3000，单位是毫秒。<br>默认值：无<br>配置原则：无 |
| ACTION | 缺省动作 | 可选必选说明：可选参数<br>参数含义：该参数用于设置缺省动作。<br>数据来源：本端规划<br>取值范围：<br>- PASS：报文转发。<br>- BLOCK：报文丢弃。<br>- REDIRECT：报文重定向。<br>默认值：无<br>配置原则：无 |
| DEFREDNAME | 缺省重定向名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ACTION”配置为“REDIRECT”时为必选参数。<br>参数含义：该参数用于设置缺省重定向名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD REDIRECT命令配置生成。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CFTEMPLATE]] · 内容过滤模板（CFTEMPLATE）

## 使用实例

修改一个内容过滤模板实例：

```
MOD CFTEMPLATE: CFTEMPLATENAME="test", ACTION=PASS;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-CFTEMPLATE.md`
