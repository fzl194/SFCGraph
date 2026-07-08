---
id: UDG@20.15.2@MMLCommand@LST NF
type: MMLCommand
name: LST NF（查询NF的锁定信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NF
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
- NF锁定开关
status: active
---

# LST NF（查询NF的锁定信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询NF的状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [NF的锁定信息（NF）](configobject/UDG/20.15.2/NF.md)

## 使用实例

查询当前所有的NF的信息：

```
LST NF:;
```

```

RETCODE = 0  操作成功

NF信息
--------------
NF锁定状态开关  =  使能
(结果个数 = 1)

---    结束
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询NF的锁定信息（LST-NF）_86526378.md`
