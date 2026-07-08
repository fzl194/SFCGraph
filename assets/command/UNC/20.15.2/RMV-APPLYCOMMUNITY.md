---
id: UNC@20.15.2@MMLCommand@RMV APPLYCOMMUNITY
type: MMLCommand
name: RMV APPLYCOMMUNITY（删除团体属性设置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APPLYCOMMUNITY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 应用团体属性
status: active
---

# RMV APPLYCOMMUNITY（删除团体属性设置）

## 功能

该命令用于删除应用团体属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| NODESEQUENCE | 路由策略节点ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APPLYCOMMUNITY]] · 团体属性设置（APPLYCOMMUNITY）

## 使用实例

删除设置团体属性的操作：

```
RMV APPLYCOMMUNITY:NODESEQUENCE=10,POLICYNAME="a";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除团体属性设置（RMV-APPLYCOMMUNITY）_49961918.md`
