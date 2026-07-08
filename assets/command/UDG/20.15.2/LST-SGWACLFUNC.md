---
id: UDG@20.15.2@MMLCommand@LST SGWACLFUNC
type: MMLCommand
name: LST SGWACLFUNC（查询SGW ACL功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SGWACLFUNC
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户ACL管理
- SgwAcl
status: active
---

# LST SGWACLFUNC（查询SGW ACL功能）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询SGW\I-UPF\ULCL\BP上ACL功能是否使能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SGWACLFUNC]] · SGW ACL功能（SGWACLFUNC）

## 使用实例

查询是否使能SGW\I-UPF\ULCL\BP上ACL功能：

```
LST SGWACLFUNC:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
S-GW ACL功能  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SGWACLFUNC.md`
