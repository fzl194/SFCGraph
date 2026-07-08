---
id: UDG@20.15.2@MMLCommand@ADD CFTEMPLATE
type: MMLCommand
name: ADD CFTEMPLATE（增加内容过滤模板）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: CFTEMPLATE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤模板配置
status: active
---

# ADD CFTEMPLATE（增加内容过滤模板）

## 功能

**适用NF：PGW-U、UPF**

该命令用于增加一个内容过滤模板的配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 整机最多可以配置100个内容过滤模板实例。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFTEMPLATENAME | 内容过滤模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ICAPSRVGMNAME | 主用CONTENT_FILTERING类型的ICAP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置主用URL_FILTERING类型的ICAP服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD ICAPSVRGRP命令配置生成。 |
| ICAPSRVGSNAME | 备用CONTENT_FILTERING类型的ICAP服务器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置备用URL_FILTERING类型的ICAP服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD ICAPSVRGRP命令配置生成。 |
| TIMELIMITNUM | 响应超时限制次数 | 可选必选说明：可选参数<br>参数含义：该参数用于设置响应超时限制次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～65535。<br>默认值：100<br>配置原则：无 |
| RESPTIMEOUT | 响应超时时间（毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设置响应超时时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～3000，单位是毫秒。<br>默认值：300<br>配置原则：无 |
| ACTION | 缺省动作 | 可选必选说明：可选参数<br>参数含义：该参数用于设置缺省动作。<br>数据来源：本端规划<br>取值范围：<br>- PASS：报文转发。<br>- BLOCK：报文丢弃。<br>- REDIRECT：报文重定向。<br>默认值：PASS<br>配置原则：无 |
| DEFREDNAME | 缺省重定向名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ACTION”配置为“REDIRECT”时为必选参数。<br>参数含义：该参数用于设置缺省重定向名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD REDIRECT命令配置生成。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CFTEMPLATE]] · 内容过滤模板（CFTEMPLATE）

## 关联任务

- [[UDG@20.15.2@Task@0-00253]]

## 使用实例

增加一个内容过滤模板的配置：

```
ADD CFTEMPLATE: CFTEMPLATENAME="test", ICAPSRVGMNAME="srg", ACTION=BLOCK;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-CFTEMPLATE.md`
