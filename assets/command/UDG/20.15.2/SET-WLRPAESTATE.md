---
id: UDG@20.15.2@MMLCommand@SET WLRPAESTATE
type: MMLCommand
name: SET WLRPAESTATE（设置无线路由PAE使能状态）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: WLRPAESTATE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 无线路由PAE使能状态
status: active
---

# SET WLRPAESTATE（设置无线路由PAE使能状态）

## 功能

![](设置无线路由PAE使能状态（SET WLRPAESTATE）_49801786.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致转发中断，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置PAE使能状态。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令可能会导致转发中断。
- 该命令仅供灰度升级使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ISENABLENTF | 是否使能PAE通告 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否使能PAE通告。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/WLRPAESTATE]] · 无线路由PAE使能状态（WLRPAESTATE）

## 使用实例

设置PAE使能状态：

```
SET WLRPAESTATE:ISENABLENTF = TRUE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置无线路由PAE使能状态（SET-WLRPAESTATE）_49801786.md`
