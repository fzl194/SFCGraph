---
id: UNC@20.15.2@MMLCommand@SET ROUTERELAYTUNNEL
type: MMLCommand
name: SET ROUTERELAYTUNNEL（设置路由迭代隧道功能开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ROUTERELAYTUNNEL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由基础
- 使能路由迭代隧道
status: active
---

# SET ROUTERELAYTUNNEL（设置路由迭代隧道功能开关）

## 功能

该命令用于设置路由迭代隧道功能开关。

缺省情况下，非标签公网BGP路由、静态路由只能迭代到出接口和下一跳，不会迭代到隧道。配置了该特性后，上述路由将优先迭代到LSP隧道，如果没有LSP隧道，上述路由也可以迭代到出接口和下一跳。

该命令和SET SRROUTERELAYTUNNEL命令迭代隧道使能开关不能同时配置为TRUE。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| RELAYENABLE |
| --- |
| False |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYENABLE | 迭代隧道使能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于迭代隧道使能开关。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| PREFIXNAME | 前缀列表名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定前缀列表名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 前缀列表需要通过ADD PREFIXFILTERNODE命令提前配置。 |
| TNLPOLICYNAME | 隧道策略名 | 可选必选说明：可选参数<br>参数含义：该参数用于表示隧道策略名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～39。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 隧道策略需要通过ADD TUNNELPOLICY命令提前配置。 |

## 操作的配置对象

- [路由迭代隧道功能开关（ROUTERELAYTUNNEL）](configobject/UNC/20.15.2/ROUTERELAYTUNNEL.md)

## 使用实例

设置路由迭代隧道开关为开：

```
SET ROUTERELAYTUNNEL:RELAYENABLE=TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置路由迭代隧道功能开关（SET-ROUTERELAYTUNNEL）_00865701.md`
