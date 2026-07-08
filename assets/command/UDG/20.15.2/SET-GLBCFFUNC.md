---
id: UDG@20.15.2@MMLCommand@SET GLBCFFUNC
type: MMLCommand
name: SET GLBCFFUNC（设置内容过滤全局开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLBCFFUNC
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤全局开关
status: active
---

# SET GLBCFFUNC（设置内容过滤全局开关）

## 功能

**适用NF：PGW-U、UPF**

![](设置内容过滤全局开关（SET GLBCFFUNC）_54628145.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令会导致用户匹配范围发生变化，可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

该命令用来配置全局是否启用内容过滤功能。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CFSWITCHGLOBAL | REQMODLINKNUM |
| --- | --- | --- |
| 初始值 | DISABLE | 1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFSWITCHGLOBAL | 内容过滤全局开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤全局功能开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：DISABLE<br>配置原则：无 |
| REQMODLINKNUM | 单POD向同一个服务器发送Reqmod消息的链路数 | 可选必选说明：可选参数<br>参数含义：该参数用于配置单pod向同一服务器发送Reqmod消息的链路数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1-32，单位是个。<br>默认值：1<br>配置原则：REQMODLINKNUM参数仅在SET CFSRVMODE命令DBMODE参数配置为CUSTOMIZATION1或CUSTOMIZATION2时生效。 |

## 操作的配置对象

- [内容过滤全局开关（GLBCFFUNC）](configobject/UDG/20.15.2/GLBCFFUNC.md)

## 使用实例

配置全局内容过滤开关：

```
SET GLBCFFUNC: CFSWITCHGLOBAL=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置内容过滤全局开关（SET-GLBCFFUNC）_54628145.md`
