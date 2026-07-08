---
id: UDG@20.15.2@MMLCommand@LST ACLDEFAULT
type: MMLCommand
name: LST ACLDEFAULT（查询缺省Acl绑定）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ACLDEFAULT
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
- 缺省ACL绑定
status: active
---

# LST ACLDEFAULT（查询缺省Acl绑定）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询默认的ACL。默认ACL是在APN下没有配置任何ACL时，如果APN需要使用ACL，则会使用默认ACL。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/ACLDEFAULT]] · 缺省Acl绑定（ACLDEFAULT）

## 使用实例

假如运营商需要查询系统当前所有的默认ACL：

```
LST ACLDEFAULT:;
```

```

RETCODE = 0  操作成功。

缺省ACL绑定信息
---------------
   方向  =  上行入
ACL名称  =  testacl1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ACLDEFAULT.md`
