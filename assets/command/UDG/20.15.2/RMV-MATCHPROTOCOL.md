---
id: UDG@20.15.2@MMLCommand@RMV MATCHPROTOCOL
type: MMLCommand
name: RMV MATCHPROTOCOL（删除路由协议匹配路由策略）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: MATCHPROTOCOL
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 匹配路由协议
status: active
---

# RMV MATCHPROTOCOL（删除路由协议匹配路由策略）

## 功能

该命令用于删除路由协议匹配路由策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用来表示路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用来表示路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MATCHPROTOCOL]] · 路由协议匹配路由策略（MATCHPROTOCOL）

## 使用实例

删除policy路由策略10节点下的协议匹配路由策略：

```
RMV MATCHPROTOCOL:POLICYNAME="policy",NODESEQUENCE=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-MATCHPROTOCOL.md`
