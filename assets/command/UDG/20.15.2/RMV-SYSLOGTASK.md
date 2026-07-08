---
id: UDG@20.15.2@MMLCommand@RMV SYSLOGTASK
type: MMLCommand
name: RMV SYSLOGTASK（删除上报任务）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SYSLOGTASK
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# RMV SYSLOGTASK（删除上报任务）

## 功能

本命令用于删除 UDG 向Syslog日志收集服务器上报日志的任务。

与 OM Portal 界面 “ 系统 > Syslog管理 ” 中删除Syslog转发配置作用相同。

> **说明**
> 无

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| SERVERIP | SysLog服务器IP地址 | 可选必选说明：必选参数。<br>参数含义：接收日志的Syslog服务器IP地址。<br>取值范围：字符串类型，输入最大长度为64字符。<br>默认值：无。<br>配置原则：必须是有效的IP地址类型。 |

## 操作的配置对象

- [上报任务（SYSLOGTASK）](configobject/UDG/20.15.2/SYSLOGTASK.md)

## 使用实例

```
%%RMV SYSLOGTASK: SERVERIP="10.119.178.152";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除上报任务（RMV-SYSLOGTASK）_02790369.md`
