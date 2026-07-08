---
id: UDG@20.15.2@MMLCommand@RTR UPGLBSCTPPARA
type: MMLCommand
name: RTR UPGLBSCTPPARA（恢复SCTP全局参数）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: UPGLBSCTPPARA
command_category: 动作类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- SCTP管理
- SCTP基础参数
status: active
---

# RTR UPGLBSCTPPARA（恢复SCTP全局参数）

## 功能

**适用NF：UPF**

此命令用于删除SCTP全局参数，恢复默认值。

## 注意事项

命令执行后对新建立的SCTP链路生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPGLBSCTPPARA]] · SCTP全局参数（UPGLBSCTPPARA）

## 使用实例

根据网络规划，需要将SCTP全局参数恢复为默认值，则可以按如下配置：

```
RTR UPGLBSCTPPARA:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-UPGLBSCTPPARA.md`
