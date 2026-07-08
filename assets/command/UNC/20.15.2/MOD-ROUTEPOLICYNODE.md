---
id: UNC@20.15.2@MMLCommand@MOD ROUTEPOLICYNODE
type: MMLCommand
name: MOD ROUTEPOLICYNODE（修改路由策略节点）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: ROUTEPOLICYNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 路由策略节点
status: active
---

# MOD ROUTEPOLICYNODE（修改路由策略节点）

## 功能

该命令用于修改指定路由策略的路由策略节点信息。

## 注意事项

- 该命令执行后立即生效。
- 配置该命令前，必须已经配置了该节点指定路由策略的名字，必须配置了要修改的节点。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用来指定路由策略的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：不支持输入空格，区分大小写。 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用来指定路由策略的节点序列号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| MATCHMODE | 匹配模式 | 可选必选说明：可选参数<br>参数含义：该参数用来指定路由策略的匹配模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：允许。<br>- deny：拒绝。<br>默认值：无 |
| DESCRIPTION | 路由策略节点描述 | 可选必选说明：可选参数<br>参数含义：该参数用来指定路由策略节点的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～80。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ROUTEPOLICYNODE]] · 路由策略节点（ROUTEPOLICYNODE）

## 使用实例

修改路由策略a的一个节点属性，节点号为10：

```
MOD ROUTEPOLICYNODE:NODESEQUENCE=10,MATCHMODE=permit,POLICYNAME="a",DESCRIPTION="111";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-ROUTEPOLICYNODE.md`
