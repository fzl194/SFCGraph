---
id: UNC@20.15.2@MMLCommand@ADD APPLYEXTENDCOMMUNITY
type: MMLCommand
name: ADD APPLYEXTENDCOMMUNITY（增加扩展团体属性设置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APPLYEXTENDCOMMUNITY
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
- 应用扩展团体属性
status: active
---

# ADD APPLYEXTENDCOMMUNITY（增加扩展团体属性设置）

## 功能

该命令用于添加应用扩展团体属性。

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
| ADDITIVEFLAG | 增加已有团体属性标记 | 可选必选说明：可选参数<br>参数含义：该参数用于表示追加标记： true：配置的扩展团体属性将追加到路由原有扩展团体属性上。 false：配置的扩展团体属性将替换路由原有扩展团体属性。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APPLYEXTENDCOMMUNITY]] · 扩展团体属性设置（APPLYEXTENDCOMMUNITY）

## 使用实例

增加设置扩展团体属性的操作：

```
ADD APPLYEXTENDCOMMUNITY:NODESEQUENCE=10,POLICYNAME="a";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加扩展团体属性设置（ADD-APPLYEXTENDCOMMUNITY）_00866577.md`
