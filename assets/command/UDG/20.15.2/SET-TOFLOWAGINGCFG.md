---
id: UDG@20.15.2@MMLCommand@SET TOFLOWAGINGCFG
type: MMLCommand
name: SET TOFLOWAGINGCFG（设置TCP流老化功能配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TOFLOWAGINGCFG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 1
category_path:
- TCP优化服务管理
- TCP流老化功能配置
status: active
---

# SET TOFLOWAGINGCFG（设置TCP流老化功能配置）

## 功能

**适用NF：UPF**

该命令用于设置TCP流老化功能配置。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 此配置时间应该大于保活时间，执行LST TORELIABLECFG命令确认KEEPALIVE配置时间。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | FLOWAGINGSWITCH | FLOWAGINGTIME |
| --- | --- | --- |
| 初始值 | ENABLE | 600 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWAGINGSWITCH | TCP流老化功能开关 | 可选必选说明：必选参数<br>参数含义：设置TCP流的老化功能开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| FLOWAGINGTIME | TCP流老化时间（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“FLOWAGINGSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：TCP流老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围30～7200，单位是秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOFLOWAGINGCFG]] · TCP流老化功能配置（TOFLOWAGINGCFG）

## 使用实例

开启TCP流老化功能开关，设置TCP流老化时间为500秒：

```
SET TOFLOWAGINGCFG: FLOWAGINGSWITCH=ENABLE, FLOWAGINGTIME=500;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置TCP流老化功能配置（SET-TOFLOWAGINGCFG）_31379101.md`
