---
id: UNC@20.15.2@MMLCommand@STP NGUSRBATCHDEREG
type: MMLCommand
name: STP NGUSRBATCHDEREG（停止批量去注册任务）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: NGUSRBATCHDEREG
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 用户数据库管理
status: active
---

# STP NGUSRBATCHDEREG（停止批量去注册任务）

## 功能

**适用NF：AMF**

该命令用于停止批量去注册任务，命令执行后，对剩余待去注册的用户不再发起网络侧去注册处理。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGUSRBATCHDEREG]] · 批量去注册任务（NGUSRBATCHDEREG）

## 使用实例

当需要停止批量去注册任务，执行如下命令：

```
STP NGUSRBATCHDEREG:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STP-NGUSRBATCHDEREG.md`
