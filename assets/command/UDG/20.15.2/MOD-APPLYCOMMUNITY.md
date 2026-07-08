---
id: UDG@20.15.2@MMLCommand@MOD APPLYCOMMUNITY
type: MMLCommand
name: MOD APPLYCOMMUNITY（修改团体属性设置）
nf: UDG
version: 20.15.2
verb: MOD
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

# MOD APPLYCOMMUNITY（修改团体属性设置）

## 功能

该命令用于修改应用团体属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：区分大小写。 |
| NODESEQUENCE | 路由策略节点ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| OPERATIONTYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定团体属性的应用方式。支持3种方式： 追加：配置的团体属性将追加到路由原有团体属性上。 替换：配置的团体属性将替换路由原有团体属性。 删除：将路由原有团体属性全部删除。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- delete：删除。<br>- replace：替换。<br>- additive：相加。<br>默认值：无 |

## 操作的配置对象

- [团体属性设置（APPLYCOMMUNITY）](configobject/UDG/20.15.2/APPLYCOMMUNITY.md)

## 使用实例

修改设置团体属性的操作：

```
MOD APPLYCOMMUNITY:NODESEQUENCE=10,POLICYNAME="a",OPERATIONTYPE=replace;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改团体属性设置（MOD-APPLYCOMMUNITY）_00865993.md`
