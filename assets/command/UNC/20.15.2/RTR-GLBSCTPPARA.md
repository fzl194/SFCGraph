---
id: UNC@20.15.2@MMLCommand@RTR GLBSCTPPARA
type: MMLCommand
name: RTR GLBSCTPPARA（恢复SCTP全局参数）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: GLBSCTPPARA
command_category: 动作类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- SCTP管理
- SCTP基础参数
status: active
---

# RTR GLBSCTPPARA（恢复SCTP全局参数）

## 功能

**适用NF：PGW-C、SMF**

此命令用于删除SCTP全局参数，恢复默认值。

## 注意事项

命令执行后对新建立的SCTP链路生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GLBSCTPPARA]] · SCTP全局参数（GLBSCTPPARA）

## 使用实例

根据网络规划，需要将SCTP全局参数恢复为默认值，则可以按如下配置：

```
RTR GLBSCTPPARA:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-GLBSCTPPARA.md`
