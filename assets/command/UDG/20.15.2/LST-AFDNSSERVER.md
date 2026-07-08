---
id: UDG@20.15.2@MMLCommand@LST AFDNSSERVER
type: MMLCommand
name: LST AFDNSSERVER（查询防欺诈可信DNS服务器）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AFDNSSERVER
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- 防欺诈可信DNS服务器
status: active
---

# LST AFDNSSERVER（查询防欺诈可信DNS服务器）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询当前防欺诈功能配置的可信DNS服务器信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [防欺诈可信DNS服务器（AFDNSSERVER）](configobject/UDG/20.15.2/AFDNSSERVER.md)

## 使用实例

显示当前可信dns服务器IP地址：

```
LST AFDNSSERVER:;
```

```

RETCODE = 0  操作成功。

防欺诈DNS服务器信息
-------------------
 IP地址版本类型  =  IPV4
DNS服务器IP地址  =  192.168.0.1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询防欺诈可信DNS服务器（LST-AFDNSSERVER）_86526284.md`
