---
id: UNC@20.15.2@MMLCommand@LST CDRSTORAGECTRL
type: MMLCommand
name: LST CDRSTORAGECTRL（查询话单存储控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CDRSTORAGECTRL
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
- 计费缓存
- 缓存控制
status: active
---

# LST CDRSTORAGECTRL（查询话单存储控制参数）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

命令用来查看配置的缓存话单文件的有效期。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRSTORAGECTRL]] · 话单存储控制参数（CDRSTORAGECTRL）

## 使用实例

查询缓存话单文件的超期时间信息：

```
LST CDRSTORAGECTRL:;
```

```

RETCODE = 0  操作成功。

话单存储控制参数
----------------
话单缓存超期天数  =  3
话单缓存超期周数  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询话单存储控制参数（LST-CDRSTORAGECTRL）_09897002.md`
