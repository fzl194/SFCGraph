---
id: UDG@20.15.2@MMLCommand@MOD REMINDTIME
type: MMLCommand
name: MOD REMINDTIME（修改证书到期提醒时间）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: REMINDTIME
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 证书维护
status: active
---

# MOD REMINDTIME（修改证书到期提醒时间）

## 功能

本命令用于修改系统内所有证书到期提醒时间。证书即将到期时有告警，可在菜单 “ 安全>证书管理 ” 中更换证书。

> **说明**
> 该命令存在系统初始记录，参数REMINDTIME (证书到期提醒时间（天）)的初始设定值为180。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| REMINDTIME | 证书到期提醒时间（天） | 可选必选说明：必选参数<br>参数含义：证书到期提醒时间。<br>取值范围：30～180<br>默认值：180<br>配置原则：无。 |

## 操作的配置对象

- [证书到期提醒时间（REMINDTIME）](configobject/UDG/20.15.2/REMINDTIME.md)

## 使用实例

修改证书到期提醒时间。

```
%%MOD REMINDTIME: REMINDTIME=66;%% 
RETCODE = 0  操作成功  
---    END 
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改证书到期提醒时间（MOD-REMINDTIME）_92045220.md`
