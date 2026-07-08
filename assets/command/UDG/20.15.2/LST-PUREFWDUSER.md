---
id: UDG@20.15.2@MMLCommand@LST PUREFWDUSER
type: MMLCommand
name: LST PUREFWDUSER（显示纯转发用户配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PUREFWDUSER
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
- 会话信息管理
- 用户纯转发配置
status: active
---

# LST PUREFWDUSER（显示纯转发用户配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

此命令用于显示当前纯转发用户配置，输出纯转发配置的IMSI、MSISDN。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/PUREFWDUSER]] · 纯转发用户配置（PUREFWDUSER）

## 使用实例

显示当前的纯转发配置：

```
LST PUREFWDUSER:;
```

```

RETCODE = 0 操作成功。

结果如下
--------
用户类型 = IMSI
IMSI = 460011223344551
MSISDN = NULL
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PUREFWDUSER.md`
