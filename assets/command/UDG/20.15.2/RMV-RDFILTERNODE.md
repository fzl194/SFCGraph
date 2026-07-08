---
id: UDG@20.15.2@MMLCommand@RMV RDFILTERNODE
type: MMLCommand
name: RMV RDFILTERNODE（删除RD路由过滤节点）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RDFILTERNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- RD路由过滤节点
status: active
---

# RMV RDFILTERNODE（删除RD路由过滤节点）

## 功能

该命令用来删除一个RD属性过滤器。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | RD过滤器索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RD过滤器索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1024。<br>默认值：无 |
| NODESEQUENCE | RD过滤索引节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RD过滤索引节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [RD路由过滤节点（RDFILTERNODE）](configobject/UDG/20.15.2/RDFILTERNODE.md)

## 使用实例

删除RD属性过滤器：

```
RMV RDFILTERNODE:INDEX=55,NODESEQUENCE=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除RD路由过滤节点（RMV-RDFILTERNODE）_50120790.md`
