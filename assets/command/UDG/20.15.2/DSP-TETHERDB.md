---
id: UDG@20.15.2@MMLCommand@DSP TETHERDB
type: MMLCommand
name: DSP TETHERDB（查询Tethering检测特征库）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TETHERDB
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- Tethering检测
- Tethering检测特征库
status: active
---

# DSP TETHERDB（查询Tethering检测特征库）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询系统中当前使用的Tethering检测特征库的版本信息。

## 注意事项

- 该命令执行后立即生效。
- 此命令的生效范围为整机。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TETHERDB]] · Tethering检测特征库（TETHERDB）

## 使用实例

假如需要查询系统中当前使用的Tethering检测特征库的版本信息：

```
DSP TETHERDB:;
```

```

RETCODE = 0  操作成功。

Tethering检测特征库版本信息
-------------------------------------
Tethering检测特征库版本号 = 9001.01.0000.0000.115
引擎版本号 = 00
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-TETHERDB.md`
