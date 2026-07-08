---
id: UDG@20.15.2@MMLCommand@RMV HTTPOFC
type: MMLCommand
name: RMV HTTPOFC（删除HTTP局向）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HTTPOFC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP局向管理
status: active
---

# RMV HTTPOFC（删除HTTP局向）

## 功能

该命令用于删除HTTP局向。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCTYPE | 局向类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置局向类型。<br>数据来源：本端规划<br>取值范围：<br>- “NFTYPE（基于网元类型）”：基于网元类型<br>- “IPGROUP（基于IP组）”：基于IP组<br>默认值：无<br>配置原则：<br>该参数不支持修改。 |
| OFCIDX | 局向索引 | 可选必选说明：可选参数<br>参数含义：该参数用于设置局向索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPOFC]] · HTTP局向（HTTPOFC）

## 使用实例

- 按局向索引删除单条配置，可以用如下命令：
  ```
  RMV HTTPOFC: OFCIDX=1;
  ```
- 按局向类型删除配置，可以用如下命令：
  ```
  RMV HTTPOFC: OFCTYPE=NFTYPE;
  ```
- 删除所有局向配置，可以用如下命令：
  ```
  RMV HTTPOFC:;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除HTTP局向（RMV-HTTPOFC）_35550178.md`
