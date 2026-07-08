---
id: UDG@20.15.2@MMLCommand@ADD CFWHITEURLLST
type: MMLCommand
name: ADD CFWHITEURLLST（增加URL过滤白名单列表）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: CFWHITEURLLST
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- URL过滤白名单列表配置
status: active
---

# ADD CFWHITEURLLST（增加URL过滤白名单列表）

## 功能

**适用NF：PGW-U、UPF**

该命令用于增加一个URL过滤白名单列表。

## 注意事项

- 该命令执行后60s生效。
- 该命令最大记录数为1。
- WHITELISTNAME由命令ADD WHITEURLLIST配置，同时该WHITELISTNAME必须配置至少一个URL。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WHITELISTNAME | URL过滤白名单名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置URL过滤白名单名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD WHITEURLLIST命令配置生成。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CFWHITEURLLST]] · URL过滤白名单列表（CFWHITEURLLST）

## 使用实例

增加一个URL过滤白名单列表：

```
ADD CFWHITEURLLST: WHITELISTNAME="whitelist1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-CFWHITEURLLST.md`
