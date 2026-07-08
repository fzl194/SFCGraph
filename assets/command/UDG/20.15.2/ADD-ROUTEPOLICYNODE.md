---
id: UDG@20.15.2@MMLCommand@ADD ROUTEPOLICYNODE
type: MMLCommand
name: ADD ROUTEPOLICYNODE（增加路由策略节点）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ROUTEPOLICYNODE
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
- 路由策略节点
status: active
---

# ADD ROUTEPOLICYNODE（增加路由策略节点）

## 功能

该命令用于添加指定路由策略的路由策略节点。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 添加该路由策略节点时，要保证该路由策略节点未添加过。
- 添加该路由策略节点时，要保证通过ADD ROUTEPOLICY添加过指定的路由策略的名字。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用来指定路由策略的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：不支持输入空格，区分大小写。 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用来指定路由策略的节点序列号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| MATCHMODE | 匹配模式 | 可选必选说明：必选参数<br>参数含义：该参数用来指定路由策略的匹配模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：允许。<br>- deny：拒绝。<br>默认值：无 |
| DESCRIPTION | 路由策略节点描述 | 可选必选说明：可选参数<br>参数含义：该参数用来指定路由策略节点的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～80。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ROUTEPOLICYNODE]] · 路由策略节点（ROUTEPOLICYNODE）

## 关联任务

- [[UDG@20.15.2@Task@0-00112]]

## 使用实例

添加路由策略a的一个节点，节点号为10：

```
ADD ROUTEPOLICYNODE:NODESEQUENCE=10,MATCHMODE=permit,POLICYNAME="a";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-ROUTEPOLICYNODE.md`
