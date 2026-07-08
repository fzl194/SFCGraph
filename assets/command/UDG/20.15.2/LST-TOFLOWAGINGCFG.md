---
id: UDG@20.15.2@MMLCommand@LST TOFLOWAGINGCFG
type: MMLCommand
name: LST TOFLOWAGINGCFG（查询TCP流老化功能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOFLOWAGINGCFG
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP流老化功能配置
status: active
---

# LST TOFLOWAGINGCFG（查询TCP流老化功能配置）

## 功能

**适用NF：UPF**

该命令用于查询TCP流老化功能配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TOFLOWAGINGCFG]] · TCP流老化功能配置（TOFLOWAGINGCFG）

## 使用实例

查询TCP流老化功能配置：

```
LST TOFLOWAGINGCFG:;
```

```

RETCODE = 0  操作成功

TCP流老化配置
-------------
TCP流老化功能开关  =  ENABLE
TCP流老化时间（秒）  =  500
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TOFLOWAGINGCFG.md`
