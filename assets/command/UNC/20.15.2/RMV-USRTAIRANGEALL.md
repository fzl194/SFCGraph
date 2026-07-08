---
id: UNC@20.15.2@MMLCommand@RMV USRTAIRANGEALL
type: MMLCommand
name: RMV USRTAIRANGEALL（删除所有的用户TAI区域）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: USRTAIRANGEALL
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
- 用户TAI区域
status: active
---

# RMV USRTAIRANGEALL（删除所有的用户TAI区域）

## 功能

![](删除所有的用户TAI区域（RMV USRTAIRANGEALL）_38729357.assets/notice_3.0-zh-cn_2.png)

删除用户TAI区域不当可能导致动态PCC用户无法基于用户TAI区域绑定的业务服务区选择PCF，进而影响用户使用业务。

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除所有的用户TAI区域。

## 注意事项

- 该命令执行后立即生效。

- 如果用户TAI区域已经与PCF业务服务区绑定，则不允许删除，需要执行命令RMV PCFSSCOPEBIND解除绑定关系后再删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRTAIRANGEALL]] · 所有的用户TAI区域（USRTAIRANGEALL）

## 使用实例

删除系统内所有与PCFSSCOPEBIND不存在绑定关系的用户TAI区域。

```
RMV USRTAIRANGEALL:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-USRTAIRANGEALL.md`
