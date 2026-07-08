---
id: UDG@20.15.2@MMLCommand@LST CFCACHEPARA
type: MMLCommand
name: LST CFCACHEPARA（查询内容过滤缓存参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CFCACHEPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤缓存参数配置
status: active
---

# LST CFCACHEPARA（查询内容过滤缓存参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询内容过滤本地缓存参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/CFCACHEPARA]] · 内容过滤缓存参数（CFCACHEPARA）

## 使用实例

查询内容过滤本地缓存参数：

```
LST CFCACHEPARA:;
```

```

RETCODE = 0  操作成功
 
内容过滤本地缓存参数
--------------------
本地缓存过期时间（秒）  =  3600
        缓存开关  =  使能（开启）
(结果个数 = 1)
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-CFCACHEPARA.md`
