---
id: UDG@20.15.2@MMLCommand@LST L2TPN4KEY
type: MMLCommand
name: LST L2TPN4KEY（查询L2TP N4密码配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: L2TPN4KEY
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2TP N4密码
status: active
---

# LST L2TPN4KEY（查询L2TP N4密码配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查看已设置的N4密钥。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/L2TPN4KEY]] · L2TP N4密码配置（L2TPN4KEY）

## 使用实例

查询已设置的N4密钥：

```
LST L2TPN4KEY:;
```

```

RETCODE = 0  操作成功

L2TP N4密码配置
---------------
    N4密钥  =  *****
确认N4密钥  =  *****
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询L2TP-N4密码配置（LST-L2TPN4KEY）_64015281.md`
