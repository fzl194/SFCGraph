---
id: UNC@20.15.2@MMLCommand@RMV MATCHDESTINATIONACL
type: MMLCommand
name: RMV MATCHDESTINATIONACL（删除目的IP地址基础ACL匹配路由策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MATCHDESTINATIONACL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 匹配目的IPv4地址基础ACL
status: active
---

# RMV MATCHDESTINATIONACL（删除目的IP地址基础ACL匹配路由策略）

## 功能

该命令用于删除目的IP地址基础ACL匹配路由策略。

## 注意事项

- 该命令执行后立即生效。
- 配置该命令前，必须已经通过ADD ROUTEPOLICY配置了指定路由策略的名字以及通过ADD ROUTEPOLICYNODE配置了该策略下的节点。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| ACLNAMEORNUM | ACL名字或ACL号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ACL规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：如果输入控制号的话，取值范围是2000～2999，若输入名字的话，需要输入以英文字母a～z或A～Z开头的1～32位字符串。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MATCHDESTINATIONACL]] · 目的IP地址基础ACL匹配路由策略（MATCHDESTINATIONACL）

## 使用实例

取消路由策略a，节点10的匹配条件，匹配ACL：

```
RMV MATCHDESTINATIONACL:POLICYNAME="a",NODESEQUENCE=10,ACLNAMEORNUM="abc";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MATCHDESTINATIONACL.md`
