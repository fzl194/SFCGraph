---
id: UDG@20.15.2@MMLCommand@RMV MATCHINTERFACE
type: MMLCommand
name: RMV MATCHINTERFACE（删除出接口匹配路由策略）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: MATCHINTERFACE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 出接口匹配
status: active
---

# RMV MATCHINTERFACE（删除出接口匹配路由策略）

## 功能

该命令用于删除出接口匹配路由策略。

## 注意事项

- 该命令执行后立即生效。
- 配置该命令前，必须已经配置了指定路由策略的名字以及该策略下的节点。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| IFNAME | 接口名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 设备必须存在该接口，不区分大小写。<br>- 通过LST INTERFACE命令查看当前已存在的接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MATCHINTERFACE]] · 出接口匹配路由策略（MATCHINTERFACE）

## 使用实例

取消路由策略a，节点10的匹配条件，匹配路由出接口NULL0：

```
RMV MATCHINTERFACE:POLICYNAME="a",NODESEQUENCE=10,IFNAME="NULL0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除出接口匹配路由策略（RMV-MATCHINTERFACE）_00865821.md`
