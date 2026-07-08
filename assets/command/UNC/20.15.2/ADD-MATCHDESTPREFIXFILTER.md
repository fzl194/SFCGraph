---
id: UNC@20.15.2@MMLCommand@ADD MATCHDESTPREFIXFILTER
type: MMLCommand
name: ADD MATCHDESTPREFIXFILTER（增加匹配IPv4地址前缀列表）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MATCHDESTPREFIXFILTER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 匹配目的IP地址IP前缀列表
status: active
---

# ADD MATCHDESTPREFIXFILTER（增加匹配IPv4地址前缀列表）

## 功能

该命令用于增加目的地址前缀过滤器匹配路由策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 配置该命令前，必须已经通过ADD ROUTEPOLICY配置了指定路由策略的名字以及通过ADD ROUTEPOLICYNODE配置了该策略下的节点。
- 配置该命令前，必须已经通过ADD PREFIXFILTERNODE配置了前缀过滤器。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：不支持输入空格，必须存在该路由策略。 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：必须存在该路由策略节点。 |
| PREFIXNAME | IP前缀列表名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP前缀列表名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MATCHDESTPREFIXFILTER]] · 匹配IPv4地址前缀列表（MATCHDESTPREFIXFILTER）

## 使用实例

添加路由策略a节点10的匹配条件，前缀过滤器a匹配目的地址：

```
ADD MATCHDESTPREFIXFILTER: NODESEQUENCE=10,PREFIXNAME="a",POLICYNAME="a";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-MATCHDESTPREFIXFILTER.md`
