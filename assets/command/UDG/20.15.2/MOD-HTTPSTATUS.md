---
id: UDG@20.15.2@MMLCommand@MOD HTTPSTATUS
type: MMLCommand
name: MOD HTTPSTATUS（修改HTTP状态码判定配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: HTTPSTATUS
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP状态码管理
status: active
---

# MOD HTTPSTATUS（修改HTTP状态码判定配置）

## 功能

![](修改HTTP状态码判定配置（MOD HTTPSTATUS）_04329849.assets/notice_3.0-zh-cn.png)

执行该命令会改变HTTP特定场景下的行为，可能导致业务受损。

该命令用于修改已有的HTTP状态码判定配置。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTPSTATUS配置的索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1024。<br>默认值：无<br>配置原则：无 |
| SCENE | 场景 | 可选必选说明：可选参数<br>参数含义：该参数用于指定特定的场景。<br>数据来源：本端规划<br>取值范围：<br>- ERRNEXTHOP（故障下一跳）<br>默认值：无<br>配置原则：无 |
| TYPE | 配置类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否执行特定场景的动作。<br>数据来源：本端规划<br>取值范围：<br>- “WHITELIST（白名单）”：执行特定场景的动作<br>默认值：无<br>配置原则：无 |
| STATUS | 状态码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进行判定的状态码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是100~699。<br>默认值：无<br>配置原则：无 |
| DESCRIPTION | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTPSTATUS配置的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPSTATUS]] · HTTP状态码判定配置（HTTPSTATUS）

## 使用实例

修改已有的HTTP状态码判定配置，可以用如下命令：

```
MOD HTTPSTATUS: INDEX=1, STATUS=604;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改HTTP状态码判定配置（MOD-HTTPSTATUS）_04329849.md`
