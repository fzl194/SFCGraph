---
id: UNC@20.15.2@MMLCommand@MOD MATCHNEXTHOPPREFIXFILTER
type: MMLCommand
name: MOD MATCHNEXTHOPPREFIXFILTER（修改下一跳前缀匹配路由策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: MATCHNEXTHOPPREFIXFILTER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 匹配下一跳前缀
status: active
---

# MOD MATCHNEXTHOPPREFIXFILTER（修改下一跳前缀匹配路由策略）

## 功能

该命令用于修改下一跳前缀过滤器匹配路由策略。

## 注意事项

- 该命令执行后立即生效。
- 配置该命令前，必须已经配置了指定路由策略的名字以及该策略下的节点。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：不支持输入空格，必须存在该路由策略。 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：必须存在该路由策略节点。 |
| PREFIXNAME | IP前缀列表名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP前缀列表名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无 |

## 操作的配置对象

- [下一跳前缀匹配路由策略（MATCHNEXTHOPPREFIXFILTER）](configobject/UNC/20.15.2/MATCHNEXTHOPPREFIXFILTER.md)

## 使用实例

修改路由策略a节点10的匹配条件，前缀过滤器a匹配下一跳：

```
MOD MATCHNEXTHOPPREFIXFILTER:POLICYNAME="a",NODESEQUENCE=10,PREFIXNAME="a";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改下一跳前缀匹配路由策略（MOD-MATCHNEXTHOPPREFIXFILTER）_00841521.md`
