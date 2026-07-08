---
id: UNC@20.15.2@MMLCommand@SET CCLIMITRC
type: MMLCommand
name: SET CCLIMITRC（设置在线计费欠费结果码）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CCLIMITRC
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- 信用控制
- 在线计费欠费返回码控制
status: active
---

# SET CCLIMITRC（设置在线计费欠费结果码）

## 功能

**适用NF：PGW-C、SMF**

该命令用于配置判断欠费用户的OCS返回码。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 在大规模流量统付业务中，当需要根据返回码判断用户是否欠费时，使用此命令。
- 该命令配置后，如果OCS返回的消息中携带FUI（Final-Unit-Indication）信元，即使OCS返回的响应码与本命令配置的不同，也判断为该用户欠费。
- 当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSCCRC1 | MSCC层返回码一 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MSCC层返回码一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：无 |
| MSCCRC2 | MSCC层返回码二 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MSCC层返回码二。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：无 |
| MSCCRC3 | MSCC层返回码三 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MSCC层返回码三。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：无 |
| MSCCRC4 | MSCC层返回码四 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MSCC层返回码四。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：无 |
| MSCCRC5 | MSCC层返回码五 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MSCC层返回码五。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：无 |
| CMDRC1 | Command层返回码一 | 可选必选说明：可选参数<br>参数含义：该参数用于指定command层返回码一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：无 |
| CMDRC2 | Command层返回码二 | 可选必选说明：可选参数<br>参数含义：该参数用于指定command层返回码二。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：无 |
| CMDRC3 | Command层返回码三 | 可选必选说明：可选参数<br>参数含义：该参数用于指定command层返回码三。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：无 |
| CMDRC4 | Command层返回码四 | 可选必选说明：可选参数<br>参数含义：该参数用于指定command层返回码四。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：无 |
| CMDRC5 | Command层返回码五 | 可选必选说明：可选参数<br>参数含义：该参数用于指定command层返回码五。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CCLIMITRC]] · 在线计费欠费返回码（CCLIMITRC）

## 使用实例

配置在线计费欠费结果码：

```
SET CCLIMITRC: MSCCRC1="4012", CMDRC1="4012";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CCLIMITRC.md`
