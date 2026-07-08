---
id: UNC@20.15.2@MMLCommand@ADD MATCHRTSRCPREFIX6FILTER
type: MMLCommand
name: ADD MATCHRTSRCPREFIX6FILTER（增加匹配IPv6路由源前缀列表）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MATCHRTSRCPREFIX6FILTER
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
- 匹配IPv6路由源前缀列表
status: active
---

# ADD MATCHRTSRCPREFIX6FILTER（增加匹配IPv6路由源前缀列表）

## 功能

该命令用来增加基于发布路由的源地址IPv6信息的匹配规则。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 配置该命令前，必须已经通过ADD ROUTEPOLICY配置了指定路由策略的名字以及通过ADD ROUTEPOLICYNODE配置了该策略下的节点。
- 配置该命令前，必须已经通过ADD IPV6PREFIXFILTERNODE配置了IPv6-Prefix过滤器。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：区分大小写。 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| IPV6PREFIXNAME | IPv6前缀列表名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP前缀列表名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [匹配IPv6路由源前缀列表（MATCHRTSRCPREFIX6FILTER）](configobject/UNC/20.15.2/MATCHRTSRCPREFIX6FILTER.md)

## 使用实例

增加基于发布路由的源地址IPv6信息的匹配规则：

```
ADD MATCHRTSRCPREFIX6FILTER:POLICYNAME="a",NODESEQUENCE=10,IPV6PREFIXNAME="a";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加匹配IPv6路由源前缀列表（ADD-MATCHRTSRCPREFIX6FILTER）_00865841.md`
