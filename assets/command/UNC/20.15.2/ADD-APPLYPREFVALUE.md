---
id: UNC@20.15.2@MMLCommand@ADD APPLYPREFVALUE
type: MMLCommand
name: ADD APPLYPREFVALUE（增加BGP路由首选值设置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APPLYPREFVALUE
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
- 应用BGP路由首选值
status: active
---

# ADD APPLYPREFVALUE（增加BGP路由首选值设置）

## 功能

该命令用于增加BGP路由首选值设置。使用ADD APPLYPREFVALUE命令配置优先级后，在不同协议发现到达同一目的地的不同路由时，优先级高的路由协议发现的路由将作为当前的有效路由。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 配置该命令前，必须首先配置ADD ROUTEPOLICYNODE命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于表示路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| PREFERREDVALUE | BGP路由首选值 | 可选必选说明：必选参数<br>参数含义：该参数用于表示BGP路由的首选值。在选择路由时，优选协议首选值最高的BGP路由。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APPLYPREFVALUE]] · BGP路由首选值设置（APPLYPREFVALUE）

## 使用实例

配置abc路由策略1节点下，首选值设置为1：

```
ADD APPLYPREFVALUE:POLICYNAME="abc",NODESEQUENCE=1,PREFERREDVALUE=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APPLYPREFVALUE.md`
