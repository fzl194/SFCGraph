---
id: UDG@20.15.2@MMLCommand@RMV EXTENDCOMMUNITYFILTERNODE
type: MMLCommand
name: RMV EXTENDCOMMUNITYFILTERNODE（删除基础扩展团体属性过滤器节点）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: EXTENDCOMMUNITYFILTERNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 基础扩展团体属性过滤器节点
status: active
---

# RMV EXTENDCOMMUNITYFILTERNODE（删除基础扩展团体属性过滤器节点）

## 功能

该命令用于删除基础扩展团体属性过滤器节点。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 扩展团体属性过滤器名字或号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定扩展团体属性过滤器名字或扩展团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，团体属性过滤器名称其长度范围是1～51。<br>默认值：无 |
| NODESEQUENCE | 扩展团体属性过滤器节点ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定扩展团体属性过滤器节点ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EXTENDCOMMUNITYFILTERNODE]] · 基础扩展团体属性过滤器节点（EXTENDCOMMUNITYFILTERNODE）

## 使用实例

删除基本扩展团体属性过滤器节点：

```
RMV EXTENDCOMMUNITYFILTERNODE:NODESEQUENCE=10,NAME="a";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除基础扩展团体属性过滤器节点（RMV-EXTENDCOMMUNITYFILTERNODE）_49801654.md`
