---
id: UNC@20.15.2@MMLCommand@ADD MATCHCOMMUNITYFILTER
type: MMLCommand
name: ADD MATCHCOMMUNITYFILTER（增加匹配团体属性过滤器）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MATCHCOMMUNITYFILTER
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
- 匹配团体属性过滤器
status: active
---

# ADD MATCHCOMMUNITYFILTER（增加匹配团体属性过滤器）

## 功能

该命令用于添加匹配团体属性过滤器。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 配置该命令前，必须已经通过ADD ROUTEPOLICY配置了指定路由策略的名字以及通过ADD ROUTEPOLICYNODE配置了该策略下的节点。
- 配置该命令前，必须已经通过ADD COMMUNITYFILTER配置了团体属性过滤器。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：区分大小写。 |
| NODESEQUENCE | 路由策略节点ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| CMNTYNAMEORNUM | 团体属性过滤器名字或号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定团体属性过滤器名字或团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，团体属性过滤器名称其长度范围是1～51。<br>默认值：无<br>配置原则：团体属性过滤器号为整数形式，其中基本团体属性过滤器号的取值范围为1～99，高级团体属性过滤器号的取值范围为100～199。团体属性过滤器名称为字符串形式，区分大小写，不支持空格，长度范围是1～51，且不能都是数字。 |
| WHOLEMATCH | 完全匹配 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否需要完全匹配。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MATCHCOMMUNITYFILTER]] · 匹配团体属性过滤器（MATCHCOMMUNITYFILTER）

## 使用实例

增加基于团体属性过滤器的匹配规则：

```
ADD MATCHCOMMUNITYFILTER:NODESEQUENCE=10,CMNTYNAMEORNUM="aaa",POLICYNAME="a";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加匹配团体属性过滤器（ADD-MATCHCOMMUNITYFILTER）_49802110.md`
