---
id: UDG@20.15.2@MMLCommand@ADD HTTPSTATUS
type: MMLCommand
name: ADD HTTPSTATUS（增加HTTP状态码判定配置）
nf: UDG
version: 20.15.2
verb: ADD
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

# ADD HTTPSTATUS（增加HTTP状态码判定配置）

## 功能

![](增加HTTP状态码判定配置（ADD HTTPSTATUS）_67769736.assets/notice_3.0-zh-cn.png)

执行该命令会改变HTTP特定场景下的行为，可能导致业务受损。

该命令用于设置HTTP收到特定状态码时，是否执行对应场景下的动作。

> **说明**
> - 该命令执行后立即生效。
>
> - 故障下一跳，指的是HTTP在间接路由模式下，收到近端SCP/SEPP回复的指定状态码时，向网元上报近端SCP/SEPP故障。HTTP内部产生状态码并向网元上报近端SCP/SEPP故障的场景，不受本命令控制。
> - HTTP收到4XX、5XX状态码时，已默认执行故障下一跳场景的动作，无需本命令设置。
>
> - 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTPSTATUS配置的索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1024。<br>默认值：无<br>配置原则：无 |
| SCENE | 场景 | 可选必选说明：必选参数<br>参数含义：该参数用于指定特定的场景。<br>数据来源：本端规划<br>取值范围：<br>- ERRNEXTHOP（故障下一跳）<br>默认值：无<br>配置原则：无 |
| TYPE | 配置类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否执行特定场景的动作。<br>数据来源：本端规划<br>取值范围：<br>- “WHITELIST（白名单）”：执行特定场景的动作<br>默认值：无<br>配置原则：无 |
| STATUS | 状态码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定进行判定的状态码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是100~699。<br>默认值：无<br>配置原则：无 |
| DESCRIPTION | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTPSTATUS配置的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPSTATUS]] · HTTP状态码判定配置（HTTPSTATUS）

## 使用实例

设置HTTP收到特定状态码时，是否执行对应场景下的动作，可以用如下命令：

```
ADD HTTPSTATUS: INDEX=1, SCENE=ERRNEXTHOP, TYPE=WHITELIST, STATUS=603;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加HTTP状态码判定配置（ADD-HTTPSTATUS）_67769736.md`
