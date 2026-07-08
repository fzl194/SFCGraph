---
id: UNC@20.15.2@MMLCommand@LST GLBCDRFLDTEMP
type: MMLCommand
name: LST GLBCDRFLDTEMP（查询全局话单模板）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBCDRFLDTEMP
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
- 话单字段控制
- 全局话单字段模板
status: active
---

# LST GLBCDRFLDTEMP（查询全局话单模板）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询全局话单模板配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBCDRFLDTEMP]] · 全局话单模板（GLBCDRFLDTEMP）

## 使用实例

查询全局话单模板：

```
LST GLBCDRFLDTEMP:;
```

```

RETCODE = 0  操作成功

全局话单字段模板
----------------
  G-CDR话单字段模板名  =  gcdr
PGW-CDR话单字段模板名  =  pgwcdr
SGW-CDR话单字段模板名  =  sgwcdr
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局话单模板（LST-GLBCDRFLDTEMP）_09896896.md`
