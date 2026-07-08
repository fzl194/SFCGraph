---
id: UDG@20.15.2@MMLCommand@ADD CFPFSPECACTION
type: MMLCommand
name: ADD CFPFSPECACTION（增加指定内容过滤策略特殊场景下的业务动作）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: CFPFSPECACTION
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
- 内容过滤策略特殊场景下的业务动作
status: active
---

# ADD CFPFSPECACTION（增加指定内容过滤策略特殊场景下的业务动作）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置指定内容过滤策略特殊场景下的业务动作，指定内容过滤策略特殊场景下的业务动作包括默认策略动作，错误策略动作和未知策略动作。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 整机支持100个指定内容分类。
- 默认策略适用场景：ICAP响应消息中携带的分类信息有效，且无对应ContentCate配置。
- 错误策略适用场景：ICAP响应码数值不等于200\201\202。
- 未知策略适用场景：ICAP响应消息没有携带分类信息，或者分类值为空。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFPROFILENAME | 套餐名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤策略名称。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：该参数使用ADD CFPROFILE命令配置生成。 |
| DEFACTION | 默认策略动作 | 可选必选说明：必选参数<br>参数含义：该参数用于设置默认策略动作。<br>数据来源：全网规划<br>取值范围：<br>- PASS：报文转发。<br>- BLOCK：报文丢弃。<br>- REDIRECT：报文重定向。<br>默认值：无<br>配置原则：无 |
| DEFREDNAME | 重定向名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DEFACTION”配置为“REDIRECT”时为必选参数。<br>参数含义：该参数用于设置默认策略重定向名称。<br>数据来源：全网规划<br>取值范围：不支持空格。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD REDIRECT命令配置生成。 |
| ERRORACTION | 错误策略动作 | 可选必选说明：必选参数<br>参数含义：该参数用于设置错误策略动作。<br>数据来源：全网规划<br>取值范围：<br>- PASS：报文转发。<br>- BLOCK：报文丢弃。<br>- REDIRECT：报文重定向。<br>默认值：无<br>配置原则：无 |
| ERRREDNAME | 重定向名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ERRORACTION”配置为“REDIRECT”时为必选参数。<br>参数含义：该参数用于设置错误策略重定向名称。<br>数据来源：全网规划<br>取值范围：不支持空格。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD REDIRECT命令配置生成。 |
| UNKNOWNACTION | 未知策略动作 | 可选必选说明：必选参数<br>参数含义：该参数用于设置未知策略动作。<br>数据来源：全网规划<br>取值范围：<br>- PASS：报文转发。<br>- BLOCK：报文丢弃。<br>- REDIRECT：报文重定向。<br>默认值：无<br>配置原则：无 |
| UNKNWREDNAME | 重定向名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“UNKNOWNACTION”配置为“REDIRECT”时为必选参数。<br>参数含义：该参数用于设置未知策略重定向名称。<br>数据来源：全网规划<br>取值范围：不支持空格。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD REDIRECT命令配置生成。 |
| CFGDOMAINNAME | 配置域名城 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CFPFSPECACTION]] · 指定内容过滤策略特殊场景下的业务动作（CFPFSPECACTION）

## 使用实例

新增一条指定内容过滤策略特殊场景下的业务动作配置：

```
ADD CFPFSPECACTION: CFPROFILENAME="profile1_test", DEFACTION=PASS, ERRORACTION=PASS, UNKNOWNACTION=PASS;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-CFPFSPECACTION.md`
