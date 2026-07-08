---
id: UDG@20.15.2@MMLCommand@SET UPFSTARTPARA
type: MMLCommand
name: SET UPFSTARTPARA（设置系统开工流程中系统开工、系统参数更新、系统停工消息的参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UPFSTARTPARA
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- PFCP参数管理
- UP系统开工参数
status: active
---

# SET UPFSTARTPARA（设置系统开工流程中系统开工、系统参数更新、系统停工消息的参数）

## 功能

**适用NF：UPF**

该命令用来设置系统开工流程发送系统开工、系统参数更新、系统停工消息的发送间隔。发送间隔指当对方不回复响应消息时，需要间隔多久重新发送请求消息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | INTERVAL |
| --- | --- |
| 初始值 | 60 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERVAL | 发送系统开工、系统参数更新、系统停工消息的间隔 | 可选必选说明：必选参数<br>参数含义：设置发送系统开工流程消息的间隔时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～3600，单位是秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPFSTARTPARA]] · UPF系统开工流程消息的参数（UPFSTARTPARA）

## 使用实例

设置发送间隔为80秒：

```
SET UPFSTARTPARA: INTERVAL=80;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置系统开工流程中系统开工、系统参数更新、系统停工消息的参数（SET-UPFSTARTPARA）_82837243.md`
