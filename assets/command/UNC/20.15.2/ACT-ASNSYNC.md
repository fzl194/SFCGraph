---
id: UNC@20.15.2@MMLCommand@ACT ASNSYNC
type: MMLCommand
name: ACT ASNSYNC（触发ASN同步）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: ASNSYNC
command_category: 动作类
applicable_nf:
- PGW-C
- GGSN
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- ASN同步管理
status: active
---

# ACT ASNSYNC（触发ASN同步）

## 功能

**适用NF：PGW-C、GGSN、SGW-C**

该命令用于手工触发SGSN/SGW-C信令路径表中的ASN同步处理。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/ASNSYNC]] · 触发ASN同步（ASNSYNC）

## 使用实例

手工同步ASN：

```
ACT ASNSYNC:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACT-ASNSYNC.md`
