---
id: UDG@20.15.2@MMLCommand@RMV USERSTATISTICS
type: MMLCommand
name: RMV USERSTATISTICS（删除用户信息统计功能）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: USERSTATISTICS
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务报表管理
- 用户信息统计管理
- 用户信息统计功能
status: active
---

# RMV USERSTATISTICS（删除用户信息统计功能）

## 功能

**适用NF：PGW-U、UPF**

该命令用于根据功能开关FUNCTION，删除指定功能的配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FUNCTION | 功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- HIGH_RATE_USRSTATS：高带宽用户统计功能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/USERSTATISTICS]] · 用户信息统计功能（USERSTATISTICS）

## 使用实例

删除高带宽用户统计功能：

```
RMV USERSTATISTICS: FUNCTION=HIGH_RATE_USRSTATS;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除用户信息统计功能（RMV-USERSTATISTICS）_56092939.md`
