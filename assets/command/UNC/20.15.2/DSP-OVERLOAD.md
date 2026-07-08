---
id: UNC@20.15.2@MMLCommand@DSP OVERLOAD
type: MMLCommand
name: DSP OVERLOAD（显示过载控制记录信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OVERLOAD
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 过载控制信息查询
status: active
---

# DSP OVERLOAD（显示过载控制记录信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

此命令用来查询信令抑制列表记录信息。当运营商想了解当前处于信令抑制中的用户的剩余老化时长的时候，执行该命令。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/OVERLOAD]] · 过载控制记录信息（OVERLOAD）

## 使用实例

查询信令抑制记录：

```
DSP OVERLOAD:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OVERLOAD.md`
