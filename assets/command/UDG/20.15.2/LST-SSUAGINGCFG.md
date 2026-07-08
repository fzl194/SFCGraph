---
id: UDG@20.15.2@MMLCommand@LST SSUAGINGCFG
type: MMLCommand
name: LST SSUAGINGCFG（查询SSU容器业务相关老化功能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SSUAGINGCFG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 智能板管理
- vvip
- 流老化时间
status: active
---

# LST SSUAGINGCFG（查询SSU容器业务相关老化功能配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询SSU容器业务相关老化功能配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [SSU容器业务相关老化功能配置（SSUAGINGCFG）](configobject/UDG/20.15.2/SSUAGINGCFG.md)

## 使用实例

查询SSU容器业务相关老化功能配置：

```
%%LST SSUAGINGCFG:;
```

```
%%
RETCODE = 0  Operation succeeded

Configuring the Aging Function for SSU Container Services
---------------------------------------------------------
Service flow aging time (s)  =  36
   Session Aging Time (min)  =  1440
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SSU容器业务相关老化功能配置（LST-SSUAGINGCFG）_28486287.md`
