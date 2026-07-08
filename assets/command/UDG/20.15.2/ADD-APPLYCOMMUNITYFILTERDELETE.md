---
id: UDG@20.15.2@MMLCommand@ADD APPLYCOMMUNITYFILTERDELETE
type: MMLCommand
name: ADD APPLYCOMMUNITYFILTERDELETE（增加删除团体属性过滤器设置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: APPLYCOMMUNITYFILTERDELETE
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
- 应用删除团体属性过滤器
status: active
---

# ADD APPLYCOMMUNITYFILTERDELETE（增加删除团体属性过滤器设置）

## 功能

该命令用来根据团体属性过滤器中指定的值删除BGP路由团体属性。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 配置该命令前，必须已经通过ADD ROUTEPOLICY配置了指定路由策略的名字以及通过ADD ROUTEPOLICYNODE配置了该策略下的节点。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：区分大小写。 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| COMMUNITYNAMEORNUM | 团体属性过滤器名字或号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定团体属性过滤器名字或团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，团体属性过滤器名称其长度范围是1～51。<br>默认值：无<br>配置原则：区分大小写。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@APPLYCOMMUNITYFILTERDELETE]] · 删除团体属性过滤器设置（APPLYCOMMUNITYFILTERDELETE）

## 使用实例

增加对BGP路由团体属性删除规则：

```
ADD APPLYCOMMUNITYFILTERDELETE:POLICYNAME="a",NODESEQUENCE=10,COMMUNITYNAMEORNUM="a";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-APPLYCOMMUNITYFILTERDELETE.md`
