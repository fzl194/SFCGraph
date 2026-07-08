---
id: UNC@20.15.2@MMLCommand@STP SMSFEXITUDMBYPASS
type: MMLCommand
name: STP SMSFEXITUDMBYPASS（停止用户退出UDM Bypass任务）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: SMSFEXITUDMBYPASS
command_category: 动作类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- UDM Bypass管理
status: active
---

# STP SMSFEXITUDMBYPASS（停止用户退出UDM Bypass任务）

## 功能

![](停止用户退出UDM Bypass任务（STP SMSFEXITUDMBYPASS）_04735169.assets/notice_3.0-zh-cn_2.png)

当启动用户退出UDM Bypass任务时，CPU和内存使用率会升高，和周边网元交互消息量增大，待用户退出UDM Bypass任务完成后，系统会恢复正常。

**适用NF：SMSF**

该命令用于启动用户退出UDM Bypass任务。当UDM故障已恢复但用户尚未退出UDM Bypass状态时，可以执行该命令使用户退出UDM Bypass状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSFEXITUDMBYPASS]] · 用户退出UDM Bypass任务（SMSFEXITUDMBYPASS）

## 使用实例

当运营商希望停止退出UDM Bypass任务，执行如下命令：

```
STP SMSFEXITUDMBYPASS:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STP-SMSFEXITUDMBYPASS.md`
