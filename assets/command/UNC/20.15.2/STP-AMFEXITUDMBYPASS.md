---
id: UNC@20.15.2@MMLCommand@STP AMFEXITUDMBYPASS
type: MMLCommand
name: STP AMFEXITUDMBYPASS（停止用户退出UDM Bypass状态任务）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: AMFEXITUDMBYPASS
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- AMF的UDM故障BYPASS功能
status: active
---

# STP AMFEXITUDMBYPASS（停止用户退出UDM Bypass状态任务）

## 功能

**适用NF：AMF**

该命令用于停止退出UDM Bypass。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [用户退出UDM Bypass状态任务（AMFEXITUDMBYPASS）](configobject/UNC/20.15.2/AMFEXITUDMBYPASS.md)

## 使用实例

当需要停止用户退出UDM Bypass任务，执行如下命令：

```
STP AMFEXITUDMBYPASS:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/停止用户退出UDM-Bypass状态任务（STP-AMFEXITUDMBYPASS）_58840357.md`
