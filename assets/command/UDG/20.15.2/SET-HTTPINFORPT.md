---
id: UDG@20.15.2@MMLCommand@SET HTTPINFORPT
type: MMLCommand
name: SET HTTPINFORPT（设置HTTP连接信息上报参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: HTTPINFORPT
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP CHR上报管理
status: active
---

# SET HTTPINFORPT（设置HTTP连接信息上报参数）

## 功能

本命令用于控制HTTP连接信息上报。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | DYNHDRPTMR |
> | --- |
> | 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HTTPLNKINFOLST | HTTP连接信息上报列表 | 可选必选说明：可选参数<br>参数含义：本参数用于指定需要上报的HTTP连接信息。<br>数据来源：本端规划<br>取值范围：<br>- HTTPDYNCOMPHDIDXRPT（HTTP动态头压缩字典上报）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPINFORPT查询当前参数配置值。<br>配置原则：无 |
| DYNHDRPTMR | HTTP动态头域压缩字典上报定时器 (s) | 可选必选说明：可选参数<br>参数含义：本参数用于配置HTTP动态头域压缩字典信息的周期上报定时器。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~3600，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPINFORPT查询当前参数配置值。<br>配置原则：<br>本参数只在HTTPLNKINFOLST参数勾选了HTTPCOMPHDIDXRPT选项时生效。 |

## 操作的配置对象

- [HTTP连接信息上报参数（HTTPINFORPT）](configobject/UDG/20.15.2/HTTPINFORPT.md)

## 使用实例

如果要设置HTTP动态头域压缩字典上报定时器为60，可以用如下命令：

```
SET HTTPINFORPT: DYNHDRPTMR=60;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置HTTP连接信息上报参数（SET-HTTPINFORPT）_29213293.md`
