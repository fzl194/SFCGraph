---
id: UNC@20.15.2@MMLCommand@ADD APPLYCOMMUNITY
type: MMLCommand
name: ADD APPLYCOMMUNITY（增加团体属性设置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APPLYCOMMUNITY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 应用团体属性
status: active
---

# ADD APPLYCOMMUNITY（增加团体属性设置）

## 功能

该命令用于添加应用团体属性。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 配置该命令前，必须已经通过ADD ROUTEPOLICY配置了指定路由策略的名字以及通过ADD ROUTEPOLICYNODE配置了该策略下的节点。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：区分大小写。 |
| NODESEQUENCE | 路由策略节点ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| OPERATIONTYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定团体属性的应用方式。支持3种方式： 追加：配置的团体属性将追加到路由原有团体属性上。 替换：配置的团体属性将替换路由原有团体属性。 删除：将路由原有团体属性全部删除。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- delete：删除。<br>- replace：替换。<br>- additive：相加。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APPLYCOMMUNITY]] · 团体属性设置（APPLYCOMMUNITY）

## 使用实例

增加设置团体属性的操作：

```
ADD APPLYCOMMUNITY:NODESEQUENCE=10,POLICYNAME="a",OPERATIONTYPE=replace;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APPLYCOMMUNITY.md`
