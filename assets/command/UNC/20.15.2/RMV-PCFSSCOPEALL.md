---
id: UNC@20.15.2@MMLCommand@RMV PCFSSCOPEALL
type: MMLCommand
name: RMV PCFSSCOPEALL（删除所有的PCF的业务服务区）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PCFSSCOPEALL
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCF发现和选择管理
- PCF业务服务区
status: active
---

# RMV PCFSSCOPEALL（删除所有的PCF的业务服务区）

## 功能

![](删除所有的PCF的业务服务区（RMV PCFSSCOPEALL）_38449589.assets/notice_3.0-zh-cn_2.png)

删除PCF的业务服务区不当可能导致动态PCC用户无法基于业务服务区选择PCF，进而影响用户使用业务。

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除所有的PCF的业务服务区。

## 注意事项

- 该命令执行后立即生效。

- 如果PCF业务服务区已经与用户TAI区域绑定，则不允许删除，需要执行命令RMV PCFSSCOPEBIND解除绑定关系后再删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCFSSCOPEALL]] · 所有的PCF的业务服务区（PCFSSCOPEALL）

## 使用实例

删除系统中所有与PCFSSCOPEBIND不存在绑定关系的业务服务区记录。

```
RMV PCFSSCOPEALL:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PCFSSCOPEALL.md`
