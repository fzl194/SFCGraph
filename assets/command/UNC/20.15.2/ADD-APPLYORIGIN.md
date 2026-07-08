---
id: UNC@20.15.2@MMLCommand@ADD APPLYORIGIN
type: MMLCommand
name: ADD APPLYORIGIN（增加BGP路由信息的路由源设置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APPLYORIGIN
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 应用BGP路由信息的路由源
status: active
---

# ADD APPLYORIGIN（增加BGP路由信息的路由源设置）

## 功能

该命令用于增加BGP路由信息的路由源设置。Origin是BGP协议的私有属性，该属性定义路径信息的来源，标记一条路由是怎么成为BGP路由的。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 配置该命令前，必须首先配置ADD ROUTEPOLICYNODE命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用来表示路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用来表示路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| ORIGINTYPE | 路由源类型 | 可选必选说明：必选参数<br>参数含义：该参数用来表示路由源类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- EGP：外部路由。<br>- IGP：内部路由。<br>- INCOMPLETE：未知源。<br>默认值：无 |
| ASSTRORNUM | AS号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ORIGINTYPE”配置为“EGP”时为必选参数。<br>参数含义：该参数用来表示AS号。支持两种格式的AS值： 1、整数形式，取值范围是1～4294967295。 2、点分式，形式为number<1～65535>.number<0～65535>。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～11。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APPLYORIGIN]] · BGP路由信息的路由源设置（APPLYORIGIN）

## 使用实例

配置policy路由策略10节点下，路由源类型设置为IGP：

```
ADD APPLYORIGIN:POLICYNAME="policy",NODESEQUENCE=10,ORIGINTYPE=IGP;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加BGP路由信息的路由源设置（ADD-APPLYORIGIN）_00866429.md`
