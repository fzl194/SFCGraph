---
id: UDG@20.15.2@MMLCommand@DSP PARSERDB
type: MMLCommand
name: DSP PARSERDB（查询协议解析数据库加载状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PARSERDB
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 协议识别
- 特征库管理
- 解析特征库
status: active
---

# DSP PARSERDB（查询协议解析数据库加载状态）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询系统当前使用的协议解析数据库的版本信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/PARSERDB]] · 协议解析数据库（PARSERDB）

## 使用实例

查询协议解析库：

```
DSP PARSERDB:;
```

```

RETCODE = 0  操作成功。

协议解析数据库信息
------------------------------------
解析库加载模式  =  最新解析数据库信息
　　　　版本号  =  009.013.010.003
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PARSERDB.md`
