---
id: UDG@20.15.2@MMLCommand@SET RPTBASICRECCFG
type: MMLCommand
name: SET RPTBASICRECCFG（设置基础单据上报配置开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: RPTBASICRECCFG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
max_records: 1
category_path:
- 业务报表管理
- 报表功能管理
- 报表系统级单据开关
status: active
---

# SET RPTBASICRECCFG（设置基础单据上报配置开关）

## 功能

**适用NF：PGW-U、UPF**

![](设置基础单据上报配置开关（SET RPTBASICRECCFG）_46919341.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令会导致用户匹配数发生变化，可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

该命令用于配置基础单据上报功能开关，包括用户信息开关、用户统计开关、APP统计开关和资源开关。当运营商部署业务报表业务时使用该命令。

## 注意事项

- 该命令执行后60s生效。
- 该命令最大记录数为1。
- 该命令会导致用户匹配数发生变化，可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | USERINFOSW | USERSTATSSW | APPSTATSSW | RESOUCESW |
| --- | --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERINFOSW | 用户信息开关 | 可选必选说明：可选参数<br>参数含义：用户信息开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| USERSTATSSW | 用户统计开关 | 可选必选说明：可选参数<br>参数含义：用户统计开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| APPSTATSSW | APP统计开关 | 可选必选说明：可选参数<br>参数含义：APP统计开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| RESOUCESW | 资源开关 | 可选必选说明：可选参数<br>参数含义：资源开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RPTBASICRECCFG]] · 基础单据上报功能开关（RPTBASICRECCFG）

## 使用实例

使能用户信息开关：

```
SET RPTBASICRECCFG:USERINFOSW = ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-RPTBASICRECCFG.md`
