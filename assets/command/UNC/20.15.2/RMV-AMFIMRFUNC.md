---
id: UNC@20.15.2@MMLCommand@RMV AMFIMRFUNC
type: MMLCommand
name: RMV AMFIMRFUNC（删除用户消息统计功能配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AMFIMRFUNC
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 信令采集
status: active
---

# RMV AMFIMRFUNC（删除用户消息统计功能配置）

## 功能

**适用NF：AMF**

该命令用于删除用户消息统计功能配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFIMRFUNC]] · 用户消息统计功能配置（AMFIMRFUNC）

## 使用实例

删除“用户范围”是“所有用户”的记录：

```
RMV AMFIMRFUNC:SUBRANGE=ALL_USER;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户消息统计功能配置（RMV-AMFIMRFUNC）_44007528.md`
