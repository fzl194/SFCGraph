---
id: UNC@20.15.2@MMLCommand@LST SMSFFUNCTION
type: MMLCommand
name: LST SMSFFUNCTION（查询SMSF功能实例信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSFFUNCTION
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMSF性能对象管理
status: active
---

# LST SMSFFUNCTION（查询SMSF功能实例信息）

## 功能

**适用NF：SMSF**

本命令用于查询SMSF功能实例信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSFFUNCTION]] · SMSF功能实例信息（SMSFFUNCTION）

## 使用实例

查看SMSFFUNCTION实例信息。

```
%%LST SMSFFUNCTION:;%%
RETCODE = 0  操作成功
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSFFUNCTION.md`
