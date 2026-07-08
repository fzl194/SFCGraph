---
id: UNC@20.15.2@MMLCommand@MOD AMFIMRFUNC
type: MMLCommand
name: MOD AMFIMRFUNC（修改用户消息统计功能配置）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD AMFIMRFUNC（修改用户消息统计功能配置）

## 功能

**适用NF：AMF**

该命令用于修改消息统计任务，配置消息统计的用户范围和接口范围，以方便问题定位。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>默认值：无<br>配置原则：无 |
| INTERFACETYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口类型。<br>数据来源：本端规划<br>取值范围：<br>- “NAS（Nas）”：Nas<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用户消息统计功能配置（AMFIMRFUNC）](configobject/UNC/20.15.2/AMFIMRFUNC.md)

## 使用实例

修改“用户范围”为“所有用户”的记录，关闭Nas消息记录：

```
MOD AMFIMRFUNC:SUBRANGE=ALL_USER,INTERFACETYPE=NAS-0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改用户消息统计功能配置（MOD-AMFIMRFUNC）_44007302.md`
