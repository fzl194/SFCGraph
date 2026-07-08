---
id: UDG@20.15.2@MMLCommand@RMV APPLYIPV6NEXTHOP
type: MMLCommand
name: RMV APPLYIPV6NEXTHOP（删除IPv6下一跳设置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: APPLYIPV6NEXTHOP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 应用替换IPv6下一跳地址
status: active
---

# RMV APPLYIPV6NEXTHOP（删除IPv6下一跳设置）

## 功能

该命令用于删除基于IPv6信息的设置路由下一跳。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APPLYIPV6NEXTHOP]] · IPv6下一跳设置（APPLYIPV6NEXTHOP）

## 使用实例

路由策略a节点10，删除设置下一跳：

```
RMV APPLYIPV6NEXTHOP:NODESEQUENCE=10, POLICYNAME="a";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-APPLYIPV6NEXTHOP.md`
