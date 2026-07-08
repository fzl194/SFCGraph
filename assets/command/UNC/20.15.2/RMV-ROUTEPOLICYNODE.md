---
id: UNC@20.15.2@MMLCommand@RMV ROUTEPOLICYNODE
type: MMLCommand
name: RMV ROUTEPOLICYNODE（删除路由策略节点）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ROUTEPOLICYNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 路由策略节点
status: active
---

# RMV ROUTEPOLICYNODE（删除路由策略节点）

## 功能

该命令用于删除配置指定路由策略名字的路由策略节点。

## 注意事项

- 该命令执行后立即生效。
- 配置该命令前，必须已经配置了指定路由策略的名字和节点。
- 若删除节点，则当前节点下的条件语句与动作语句将被同时删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用来指定路由策略的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用来指定路由策略的节点序列号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ROUTEPOLICYNODE]] · 路由策略节点（ROUTEPOLICYNODE）

## 使用实例

删除路由策略a的一个节点，节点号为10：

```
RMV ROUTEPOLICYNODE:NODESEQUENCE=10,POLICYNAME="a";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ROUTEPOLICYNODE.md`
