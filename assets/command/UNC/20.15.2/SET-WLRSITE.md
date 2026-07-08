---
id: UNC@20.15.2@MMLCommand@SET WLRSITE
type: MMLCommand
name: SET WLRSITE（设置无线路由全局属性）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: WLRSITE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 无线路由管理
- 无线路由全局配置
status: active
---

# SET WLRSITE（设置无线路由全局属性）

## 功能

该命令用于设置无线路由全局属性。当需要改变无线路由的老化时间和VNRS_VNFC向CSLB延迟发布PAE地址的时间时，可使用该命令。

## 注意事项

- 该命令执行后立即生效。
- 可选参数至少选一项。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| GRTIMER | PAEDELAYTIMER |
| --- | --- |
| 90000 | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRTIMER | GR定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定GR定时器，当需要改变无线路由的老化时间时设置该定时器为非初始设置值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～90000，单位是秒。<br>默认值：无 |
| PAEDELAYTIMER | PAE延时定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定PAE延时定时器，当VNRS需要向CSLB延时发布PAE地址时设置该定时器时间为非0。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～300，单位是秒。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/WLRSITE]] · 无线路由全局属性配置（WLRSITE）

## 使用实例

设置无线路由全局属性：

```
SET WLRSITE:GRTIMER=80000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置无线路由全局属性（SET-WLRSITE）_00841257.md`
