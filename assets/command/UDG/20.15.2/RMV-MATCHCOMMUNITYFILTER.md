---
id: UDG@20.15.2@MMLCommand@RMV MATCHCOMMUNITYFILTER
type: MMLCommand
name: RMV MATCHCOMMUNITYFILTER（删除匹配团体属性过滤器）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: MATCHCOMMUNITYFILTER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 匹配团体属性过滤器
status: active
---

# RMV MATCHCOMMUNITYFILTER（删除匹配团体属性过滤器）

## 功能

该命令用于删除匹配团体属性过滤器。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| NODESEQUENCE | 路由策略节点ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| CMNTYNAMEORNUM | 团体属性过滤器名字或号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定团体属性过滤器名字或团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，团体属性过滤器名称其长度范围是1～51。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MATCHCOMMUNITYFILTER]] · 匹配团体属性过滤器（MATCHCOMMUNITYFILTER）

## 使用实例

删除基于团体属性过滤器的匹配规则：

```
RMV MATCHCOMMUNITYFILTER:NODESEQUENCE=10,CMNTYNAMEORNUM="aaa",POLICYNAME="a";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除匹配团体属性过滤器（RMV-MATCHCOMMUNITYFILTER）_50281086.md`
