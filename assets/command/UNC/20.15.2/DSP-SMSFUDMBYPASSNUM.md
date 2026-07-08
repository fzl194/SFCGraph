---
id: UNC@20.15.2@MMLCommand@DSP SMSFUDMBYPASSNUM
type: MMLCommand
name: DSP SMSFUDMBYPASSNUM（显示SMSF系统内处于UDM Bypass状态的用户数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMSFUDMBYPASSNUM
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- UDM Bypass管理
status: active
---

# DSP SMSFUDMBYPASSNUM（显示SMSF系统内处于UDM Bypass状态的用户数）

## 功能

**适用NF：SMSF**

该命令用于显示SMSF系统内处于UDM Bypass状态的用户数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [SMSF系统内处于UDM Bypass状态的用户数（SMSFUDMBYPASSNUM）](configobject/UNC/20.15.2/SMSFUDMBYPASSNUM.md)

## 使用实例

当运营商希望查询SMSF系统内处于UDM Bypass状态的用户数，执行如下命令：

```
DSP SMSFUDMBYPASSNUM:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示SMSF系统内处于UDM-Bypass状态的用户数（DSP-SMSFUDMBYPASSNUM）_04735165.md`
