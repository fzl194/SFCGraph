---
id: UDG@20.15.2@MMLCommand@LST CPTEIDUALLOC
type: MMLCommand
name: LST CPTEIDUALLOC（查询CP分配TEID-U开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CPTEIDUALLOC
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- GTP隧道管理
- CP分配TEID-U控制
status: active
---

# LST CPTEIDUALLOC（查询CP分配TEID-U开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

此命令用于查询CP分配TEID-U功能的开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/CPTEIDUALLOC]] · CP分配TEID-U开关（CPTEIDUALLOC）

## 使用实例

查询系统是否支持CP分配TEID-U功能：

```
LST CPTEIDUALLOC:;
```

```

RETCODE = 0 操作成功.

CP分配TEID-U开关配置
-----------
开关标识 = 不使能
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CP分配TEID-U开关（LST-CPTEIDUALLOC）_86527096.md`
