---
id: UNC@20.15.2@MMLCommand@SET CFGSYNC
type: MMLCommand
name: SET CFGSYNC（设置配置同步开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CFGSYNC
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 业务调测
- 配置同步开关
status: active
---

# SET CFGSYNC（设置配置同步开关）

## 功能

**适用网元：SGSN、MME**

该命令用于控制ACS_VNFC和USN_VNFC、LINK_VNFC、GB_VNFC之间配置自动同步功能是否开启。

## 注意事项

- 该命令执行后立即生效。
- 该命令在OMU复位后失效。
- 去使能配置同步开关可能导致ACS_VNFC上的配置数据不能同步到USN_VNFC、LINK_VNFC、GB_VNFC，导致业务受损。请谨慎使用本命令。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SYNCFLAG | 配置同步开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否开启配置自动同步功能。<br>数据来源：全网规划<br>取值范围：<br>- “ENABLE(使能)”：开启配置同步功能。<br>- “DISABLE(去使能)”：关闭配置同步功能。<br>系统初始设置值：ENABLE(使能) |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CFGSYNC]] · 配置同步开关（CFGSYNC）

## 使用实例

如果希望关闭ACS_VNFC和USN_VNFC、LINK_VNFC、GB_VNFC之间配置自动同步功能，执行如下命令：

SET CFGSYNC:SYNCFLAG=DISABLE;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CFGSYNC.md`
