---
id: UDG@20.15.2@MMLCommand@DSP PATHNUMBER
type: MMLCommand
name: DSP PATHNUMBER（查询路径数）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PATHNUMBER
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- GTP路径管理
- GTP协议参数管理
- 路径数目
status: active
---

# DSP PATHNUMBER（查询路径数）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询路径数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/PATHNUMBER]] · 路径数（PATHNUMBER）

## 使用实例

在需要查询路径的个数时，使用此命令：

```
DSP PATHNUMBER:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
                最大的路径数  =  630000
          已使用的信令路径数  =  0
          已使用的数据路径数  =  0
                可用的路径数  =  630000
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PATHNUMBER.md`
