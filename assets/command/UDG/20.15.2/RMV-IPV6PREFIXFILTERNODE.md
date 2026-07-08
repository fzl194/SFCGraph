---
id: UDG@20.15.2@MMLCommand@RMV IPV6PREFIXFILTERNODE
type: MMLCommand
name: RMV IPV6PREFIXFILTERNODE（删除IPv6前缀过滤器节点）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IPV6PREFIXFILTERNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- IPv6前缀过滤器节点
status: active
---

# RMV IPV6PREFIXFILTERNODE（删除IPv6前缀过滤器节点）

## 功能

该命令用于删除基于IPv6信息的前缀过滤器。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | IPv6前缀列表名字 | 可选必选说明：必选参数<br>参数含义：IP前缀列表名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无 |
| NODESEQUENCE | IPv6前缀列表节点号 | 可选必选说明：可选参数<br>参数含义：IP前缀列表节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：当不输入此参数时，删除所有节点。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPV6PREFIXFILTERNODE]] · IPv6前缀过滤器节点（IPV6PREFIXFILTERNODE）

## 使用实例

删除IPv6前缀过滤器：

```
RMV IPV6PREFIXFILTERNODE:NAME="c",NODESEQUENCE=25;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-IPV6PREFIXFILTERNODE.md`
