---
id: UDG@20.15.2@MMLCommand@LST TOSOFTPARA
type: MMLCommand
name: LST TOSOFTPARA（查询TCP优化软参）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOSOFTPARA
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP软参
status: active
---

# LST TOSOFTPARA（查询TCP优化软参）

## 功能

**适用NF：UPF**

该命令用于查询TCP优化软参。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOSOFTPARA]] · TCP优化软参（TOSOFTPARA）

## 使用实例

查询TCP优化软参：

```
LST TOSOFTPARA:;
```

```

RETCODE = 0  操作成功
 
TCP优化软参
-------------
TCP优化软参1  =  0
TCP优化软参2  =  0
TCP优化软参3  =  0
(结果个数 = 1)
 
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TOSOFTPARA.md`
