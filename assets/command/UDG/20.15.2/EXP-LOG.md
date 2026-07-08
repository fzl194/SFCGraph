---
id: UDG@20.15.2@MMLCommand@EXP LOG
type: MMLCommand
name: EXP LOG（设置日志导出参数）
nf: UDG
version: 20.15.2
verb: EXP
object_keyword: LOG
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- SFIP日志管理
- 日志导出
status: active
---

# EXP LOG（设置日志导出参数）

## 功能

该命令用于设置日志导出参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 导出开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定日志导出开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：关闭。<br>- ENABLE：打开。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP版本信息 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定IP版本信息。<br>数据来源：本端规划<br>取值范围：<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>- IPV4_IPV6：同时支持IPv4和IPv6地址。<br>默认值：无<br>配置原则：无 |
| IPV4 | 服务器IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定服务器IPV4地址。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |
| IPV6 | 服务器IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定服务器IPV6地址。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |
| PORT | 服务器端口 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定服务器端口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |
| USER | 用户名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定服务器用户名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：无 |
| PASSWORD | 密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定服务器密码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| REMOTEPATH | 远端路径 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定服务器日志导出路径。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～1023。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LOG]] · 日志导出参数（LOG）

## 使用实例

设置日志导出参数：

```
EXP LOG: SWITCH=ENABLE, IPVERSION=IPV4, IPV4="10.104.64.129", PORT=22, USER="user", PASSWORD="password", REMOTEPATH="./logpath";
```

```

```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置日志导出参数（EXP-LOG）_42491895.md`
