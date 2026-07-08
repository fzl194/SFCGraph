---
id: UNC@20.15.2@MMLCommand@ADD MATCHPROTOCOL
type: MMLCommand
name: ADD MATCHPROTOCOL（增加路由协议匹配路由策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MATCHPROTOCOL
command_category: 配置类
effect_mode: ''
is_dangerous: false
max_records: 6
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 匹配路由协议
status: active
---

# ADD MATCHPROTOCOL（增加路由协议匹配路由策略）

## 功能

该命令用于增加路由协议匹配路由策略。通过ADD MATCHPROTOCOL命令可对路由的类型进行过滤，即只允许指定路由协议类型的路由通过策略。

## 注意事项

- 该命令最大记录数为6。
- 配置该命令前，必须首先配置ADD ROUTEPOLICYNODE命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用来表示路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用来表示路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| PROTOCOLTYPE | 协议类型 | 可选必选说明：必选参数<br>参数含义：该参数用来表示路由类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DIRECT：直连路由。<br>- OSPF：OSPF路由。<br>- STATIC：静态路由。<br>- BGP：BGP路由。<br>- OSPFV3：OSPFv3路由。<br>- WLR：WLR路由。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MATCHPROTOCOL]] · 路由协议匹配路由策略（MATCHPROTOCOL）

## 使用实例

配置policy路由策略10节点下，协议匹配路由策略设置为OSPF：

```
ADD MATCHPROTOCOL:POLICYNAME="policy",NODESEQUENCE=10,PROTOCOLTYPE=OSPF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-MATCHPROTOCOL.md`
