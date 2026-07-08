---
id: UDG@20.15.2@MMLCommand@ADD ADVANCEDCOMMUNITYNODE
type: MMLCommand
name: ADD ADVANCEDCOMMUNITYNODE（增加高级团体属性过滤器节点）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ADVANCEDCOMMUNITYNODE
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
- 高级团体属性过滤器节点
status: active
---

# ADD ADVANCEDCOMMUNITYNODE（增加高级团体属性过滤器节点）

## 功能

该命令用来增加高级团体属性过滤器节点。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 配置该命令前，必须已经通过ADD COMMUNITYFILTER配置了高级团体过滤器。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMNTYNAMEORNUM | 团体属性过滤器名字或号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定团体属性过滤器名字或团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，团体属性过滤器名称其长度范围是1～51。<br>默认值：无<br>配置原则：区分大小写，高级团体属性若为整数形式，取值范围100～199。 |
| NODESEQUENCE | 团体属性过滤器节点ID | 可选必选说明：必选参数<br>参数含义：团体属性过滤器节点ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| REGULAR | 正则表达式 | 可选必选说明：必选参数<br>参数含义：正则表达式。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～1024。<br>默认值：无<br>配置原则：支持空格。 |
| MATCHMODE | 匹配模式 | 可选必选说明：必选参数<br>参数含义：匹配模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：允许。<br>- deny：拒绝。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ADVANCEDCOMMUNITYNODE]] · 高级团体属性过滤器节点（ADVANCEDCOMMUNITYNODE）

## 使用实例

增加高级团体属性过滤器节点：

```
ADD ADVANCEDCOMMUNITYNODE:CMNTYNAMEORNUM="ab",NODESEQUENCE=1,REGULAR="1",MATCHMODE=permit;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-ADVANCEDCOMMUNITYNODE.md`
