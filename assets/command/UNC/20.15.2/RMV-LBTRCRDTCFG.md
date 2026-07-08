---
id: UNC@20.15.2@MMLCommand@RMV LBTRCRDTCFG
type: MMLCommand
name: RMV LBTRCRDTCFG（删除跟踪重定向）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LBTRCRDTCFG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 跟踪管理
status: active
---

# RMV LBTRCRDTCFG（删除跟踪重定向）

## 功能

该命令用于删除已有的跟踪重定向参数配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 重定向索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪重定向参数配置的索引。<br>数据来源：本端规划<br>取值范围：1~32<br>默认值：无<br>配置原则：<br>- 输入参数必须是当前配置记录中已存在的索引。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LBTRCRDTCFG]] · 跟踪重定向（LBTRCRDTCFG）

## 使用实例

1. 删除INDEX为2的跟踪重定向参数配置记录。
  RMV LBTRCRDTCFG: INDEX=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-LBTRCRDTCFG.md`
