---
id: UDG@20.15.2@MMLCommand@LST GLBRLYSHTTPCTL
type: MMLCommand
name: LST GLBRLYSHTTPCTL（查询媒体中继全局业务HTTP控制）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBRLYSHTTPCTL
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继全局业务HTTP控制
status: active
---

# LST GLBRLYSHTTPCTL（查询媒体中继全局业务HTTP控制）

## 功能

**适用NF：UPF、PGW-U**

该命令用于查询媒体中继全局业务HTTP控制。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLBRLYSHTTPCTL]] · 媒体中继全局业务HTTP控制（GLBRLYSHTTPCTL）

## 使用实例

查询媒体中继全局业务HTTP控制：

```
LST GLBRLYSHTTPCTL:;
```

```

RETCODE = 0  操作成功

The result is as follows
------------------------
HTTP连接空闲时间（秒） =  60
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GLBRLYSHTTPCTL.md`
