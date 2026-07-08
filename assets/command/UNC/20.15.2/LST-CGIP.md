---
id: UNC@20.15.2@MMLCommand@LST CGIP
type: MMLCommand
name: LST CGIP（查询CGIP测量对象）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CGIP
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 离线计费维护
- CGIP测量对象
status: active
---

# LST CGIP（查询CGIP测量对象）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用于查询CGIP测量对象。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [CGIP测量对象（CGIP）](configobject/UNC/20.15.2/CGIP.md)

## 使用实例

查询CGIP测量对象：

```
LST CGIP:;
```

```

RETCODE = 0  操作成功。

CGIP地址
--------
IP地址  =  192.168.1.12
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CGIP测量对象（LST-CGIP）_09897024.md`
