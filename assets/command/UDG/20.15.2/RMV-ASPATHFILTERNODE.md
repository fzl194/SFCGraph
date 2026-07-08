---
id: UDG@20.15.2@MMLCommand@RMV ASPATHFILTERNODE
type: MMLCommand
name: RMV ASPATHFILTERNODE（删除AS路径过滤节点）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ASPATHFILTERNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- AS路由过滤节点
status: active
---

# RMV ASPATHFILTERNODE（删除AS路径过滤节点）

## 功能

该命令用来删除一个AS路径过滤器表项。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | AS路径过滤器名字或号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定AS路径过滤器名字或号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～51。<br>默认值：无<br>配置原则：区分大小写，不支持空格。如果是数字则取值范围为1-256。 |
| NODESEQUENCE | AS路径过滤器节点号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定AS路径过滤器节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [AS路径过滤节点（ASPATHFILTERNODE）](configobject/UDG/20.15.2/ASPATHFILTERNODE.md)

## 使用实例

删除AS路径过滤器：

```
RMV ASPATHFILTERNODE: NAME ="a",NODESEQUENCE=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除AS路径过滤节点（RMV-ASPATHFILTERNODE）_50120878.md`
