---
id: UDG@20.15.2@MMLCommand@RMV RPTPOLICY
type: MMLCommand
name: RMV RPTPOLICY（删除基于策略的报表开关）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RPTPOLICY
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
category_path:
- 业务报表管理
- 报表本地策略管理
- 报表业务策略
status: active
---

# RMV RPTPOLICY（删除基于策略的报表开关）

## 功能

**适用NF：PGW-U、UPF**

![](删除基于策略的报表开关（RMV RPTPOLICY）_04409549.assets/notice_3.0-zh-cn.png)

本命令属于高危命令,执行本命令后将删除指定或所有策略的业务报表功能开关，可能导致全量用户都上报（性能下降）或都不上报报表，请谨慎使用。

此命令用于删除指定策略的业务报表功能开关。如果没有指定策略名称，表示删除所有配置。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令执行60s后对承载更新的用户或者新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定报表功能使用的策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTPOLICY]] · 基于策略的报表开关（RPTPOLICY）

## 使用实例

运营商需要删除基于策略的业务报表开关，指定策略名称为“policy01”：

```
RMV RPTPOLICY:POLICYNAME="policy01";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除基于策略的报表开关（RMV-RPTPOLICY）_04409549.md`
