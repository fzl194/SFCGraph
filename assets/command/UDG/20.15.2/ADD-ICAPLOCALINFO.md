---
id: UDG@20.15.2@MMLCommand@ADD ICAPLOCALINFO
type: MMLCommand
name: ADD ICAPLOCALINFO（增加ICAP本端信息）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ICAPLOCALINFO
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- ICAPC管理
- ICAP本端信息
status: active
---

# ADD ICAPLOCALINFO（增加ICAP本端信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于添加ICAP本端信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSERVERTYPE | ICAP服务器类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- URL_FILTERING：支持URL过滤的ICAP服务器。<br>默认值：无<br>配置原则：无 |
| USERAGENT | User Agent | 可选必选说明：必选参数<br>参数含义：该参数用于指定客户端类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [ICAP本端信息（ICAPLOCALINFO）](configobject/UDG/20.15.2/ICAPLOCALINFO.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00262]]

## 使用实例

添加一条ICAP本端信息，IcapServerType为URL_FILTERING，UserAgent为test：

```
ADD ICAPLOCALINFO:ICAPSERVERTYPE=URL_FILTERING, USERAGENT="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加ICAP本端信息（ADD-ICAPLOCALINFO）_28984184.md`
