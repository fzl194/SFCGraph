---
id: UDG@20.15.2@MMLCommand@CLR L2TPSTATISTICS
type: MMLCommand
name: CLR L2TPSTATISTICS（清除L2TP报文统计信息）
nf: UDG
version: 20.15.2
verb: CLR
object_keyword: L2TPSTATISTICS
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2TP报文统计维护
status: active
---

# CLR L2TPSTATISTICS（清除L2TP报文统计信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于清除系统的L2TP控制报文统计信息。运营商需要清除之前统计的L2TP控制报文数场景，可以使用该命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [L2TP报文统计信息（L2TPSTATISTICS）](configobject/UDG/20.15.2/L2TPSTATISTICS.md)

## 使用实例

假设运营商想清除L2TP控制报文统计信息：

```
CLR L2TPSTATISTICS:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除L2TP报文统计信息（CLR-L2TPSTATISTICS）_35373534.md`
