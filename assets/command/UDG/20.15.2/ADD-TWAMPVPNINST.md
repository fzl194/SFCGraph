---
id: UDG@20.15.2@MMLCommand@ADD TWAMPVPNINST
type: MMLCommand
name: ADD TWAMPVPNINST（增加VPN实例名称）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: TWAMPVPNINST
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- VPN实例
status: active
---

# ADD TWAMPVPNINST（增加VPN实例名称）

## 功能

该命令用于增加VPN实例名称。

> **说明**
> - 该命令执行后立即生效。
>
> - 最多可输入32条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置VPN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>区分大小写，不支持空格。<br>“_public_”是公网缺省VPN的实例名，不允许用户配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TWAMPVPNINST]] · VPN实例名称（TWAMPVPNINST）

## 关联任务

- [[UDG@20.15.2@Task@0-00224]]

## 使用实例

增加VPN实例名称为ck的实例：

```
ADD TWAMPVPNINST: VRFNAME="ck";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加VPN实例名称（ADD-TWAMPVPNINST）_27102474.md`
