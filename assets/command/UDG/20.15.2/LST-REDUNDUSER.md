---
id: UDG@20.15.2@MMLCommand@LST REDUNDUSER
type: MMLCommand
name: LST REDUNDUSER（查询静态地址用户路由冗余功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: REDUNDUSER
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 静态地址用户路由冗余
- 路由冗余开关
status: active
---

# LST REDUNDUSER（查询静态地址用户路由冗余功能）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示当前设备静态地址用户路由冗余功能使能状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/REDUNDUSER]] · 静态地址用户路由冗余功能（REDUNDUSER）

## 使用实例

显示静态地址用户路由冗余功能是否使能：

```
LST REDUNDUSER:;
```

```

RETCODE = 0 操作成功。
结果如下 
---------------------- 
开关 = 不使能 (结果个数 = 1) 
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询静态地址用户路由冗余功能（LST-REDUNDUSER）_71074368.md`
