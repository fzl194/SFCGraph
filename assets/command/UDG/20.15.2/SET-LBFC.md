---
id: UDG@20.15.2@MMLCommand@SET LBFC
type: MMLCommand
name: SET LBFC（设置流控开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: LBFC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 系统调测
- 流控参数
status: active
---

# SET LBFC（设置流控开关）

## 功能

该命令用于设置流控开关状态。

## 注意事项

当流控开关关闭时，业务表项大量下发会对CSLB造成拥塞。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCSWITCH | 流控开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示流控开关。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- “ON：打开”<br>- “OFF：关闭”<br>系统初始设置值：ON<br>配置原则：通常情况下，不建议修改本参数取值，当流控功能发生异常时，把本参数设置为OFF。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LBFC]] · 流控开关（LBFC）

## 使用实例

设置流控开关状态为打开。

SET LBFC: FCSWITCH=ON;

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-LBFC.md`
