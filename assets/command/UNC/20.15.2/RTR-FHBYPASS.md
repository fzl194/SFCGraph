---
id: UNC@20.15.2@MMLCommand@RTR FHBYPASS
type: MMLCommand
name: RTR FHBYPASS（恢复旁路失败处理的配置参数）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: FHBYPASS
command_category: 动作类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- 失败旁路处理
status: active
---

# RTR FHBYPASS（恢复旁路失败处理的配置参数）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来恢复故障网元的旁路配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [旁路失败处理的配置参数（FHBYPASS）](configobject/UNC/20.15.2/FHBYPASS.md)

## 使用实例

OCS故障恢复，恢复在线计费旁路配置为缺省值：

```
RTR FHBYPASS:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/恢复旁路失败处理的配置参数（RTR-FHBYPASS）_09896716.md`
