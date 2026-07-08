---
id: UDG@20.15.2@MMLCommand@DSP AFDB
type: MMLCommand
name: DSP AFDB（查询防欺诈业务规则数据库）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: AFDB
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- 防欺诈业务规则数据库
status: active
---

# DSP AFDB（查询防欺诈业务规则数据库）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询系统中当前使用的防欺诈业务规则数据库的版本信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/AFDB]] · 防欺诈业务规则数据库（AFDB）

## 使用实例

查询防欺诈业务规则数据库版本信息：

```
DSP AFDB:;
```

```

RETCODE = 0  操作成功

防欺诈业务规则数据库版本信息
----------------------------
防欺诈业务规则数据库版本号  =  0001.01.0086.0001.001
                引擎版本号  =  01
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-AFDB.md`
