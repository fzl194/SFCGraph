---
id: UDG@20.15.2@MMLCommand@LST CFPROTOCOLLST
type: MMLCommand
name: LST CFPROTOCOLLST（查询开启内容过滤的协议列表）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CFPROTOCOLLST
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
- 内容过滤协议类型列表
status: active
---

# LST CFPROTOCOLLST（查询开启内容过滤的协议列表）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询已开启内容过滤功能的协议列表。

## 注意事项

HTTP与WAP协议无需配置，缺省做内容过滤。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [开启内容过滤的协议列表（CFPROTOCOLLST）](configobject/UDG/20.15.2/CFPROTOCOLLST.md)

## 使用实例

查询已开启内容过滤功能的协议列表：

```
LST CFPROTOCOLLST:;
```

```

RETCODE = 0  操作成功

内容过滤协议类型列表
--------------------
内容过滤协议名称  =  HTTPS协议
      配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询开启内容过滤的协议列表（LST-CFPROTOCOLLST）_43357967.md`
