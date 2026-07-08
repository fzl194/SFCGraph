---
id: UDG@20.15.2@MMLCommand@MOD RDFILTERNODE
type: MMLCommand
name: MOD RDFILTERNODE（修改RD路由过滤节点）
nf: UDG
version: 20.15.2
verb: MOD
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

# MOD RDFILTERNODE（修改RD路由过滤节点）

## 功能

该命令用来修改一个RD属性过滤器。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | RD过滤器索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RD过滤器索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1024。<br>默认值：无 |
| NODESEQUENCE | RD过滤索引节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RD过滤索引节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| MATCHMODE | 匹配模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定匹配模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：允许。<br>- deny：拒绝。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RDFILTERNODE]] · RD路由过滤节点（RDFILTERNODE）

## 使用实例

修改RD属性过滤器：

```
MOD RDFILTERNODE:INDEX=55,NODESEQUENCE=10,MATCHMODE=permit;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改RD路由过滤节点（MOD-RDFILTERNODE）_00865861.md`
