---
id: UDG@20.15.2@MMLCommand@SET GLOBUEMUTACC
type: MMLCommand
name: SET GLOBUEMUTACC（设置全局用户互访控制配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLOBUEMUTACC
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- 用户互访控制
- 全局用户互访控制
status: active
---

# SET GLOBUEMUTACC（设置全局用户互访控制配置）

## 功能

**适用NF：UPF**

![](设置全局用户互访控制配置（SET GLOBUEMUTACC）_82837773.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，整机终端互访控制功能开启后，如果未在具体APN下关闭相应终端互访控制功能，所有APN内或APN间的终端互访将无法进行。

本命令仅适用于同一UPF网元内不同UE会话的互访控制，如果需要跨UPF网元的不同UE会话的互访控制，需要在UPF上配置ACL规则。

该命令用来配置整机终端互访控制功能。支持配置是否开启整机APN内终端互访控制功能以及整机APN间终端互访控制功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- APN内终端互访禁止功能开关及APN间终端互访禁止功能开关缺省为开启。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | INNERAPNS | INTERAPNS |
| --- | --- | --- |
| 初始值 | ENABLE | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INNERAPNS | 同APN内的控制开关 | 可选必选说明：必选参数<br>参数含义：配置是否开启APN内终端互访控制功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能，允许终端互访。<br>- ENABLE：使能，禁止终端互访。<br>默认值：无<br>配置原则：无 |
| INTERAPNS | 不同APN间的控制开关 | 可选必选说明：必选参数<br>参数含义：配置是否开启和其它APN之间的终端互访控制功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能，允许终端互访。<br>- ENABLE：使能，禁止终端互访。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLOBUEMUTACC]] · 全局用户互访控制配置（GLOBUEMUTACC）

## 使用实例

设置整机粒度APN内终端互访禁止功能开关为开启及APN间终端互访禁止功能开关为开启：

```
SET GLOBUEMUTACC: INNERAPNS=ENABLE, INTERAPNS=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-GLOBUEMUTACC.md`
