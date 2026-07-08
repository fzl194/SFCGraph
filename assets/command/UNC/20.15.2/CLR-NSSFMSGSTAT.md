---
id: UNC@20.15.2@MMLCommand@CLR NSSFMSGSTAT
type: MMLCommand
name: CLR NSSFMSGSTAT（清除收发消息内部统计）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: NSSFMSGSTAT
command_category: 动作类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF维测管理
status: active
---

# CLR NSSFMSGSTAT（清除收发消息内部统计）

## 功能

**适用NF：NSSF**

该命令用于清除收发消息内部统计。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFMSGSTAT]] · NSSF收发消息内部统计（NSSFMSGSTAT）

## 使用实例

运营商想要清除NSSF收发消息内部统计信息，执行此命令。

```
CLR NSSFMSGSTAT:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除收发消息内部统计（CLR-NSSFMSGSTAT）_76878552.md`
