---
id: UNC@20.15.2@MMLCommand@LST CCLIMITRC
type: MMLCommand
name: LST CCLIMITRC（查询在线计费欠费返回码）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CCLIMITRC
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- 信用控制
- 在线计费欠费返回码控制
status: active
---

# LST CCLIMITRC（查询在线计费欠费返回码）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询在线计费欠费结果码。

## 注意事项

当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CCLIMITRC]] · 在线计费欠费返回码（CCLIMITRC）

## 使用实例

查询在线计费欠费结果码：

```
LST CCLIMITRC:;
```

```

RETCODE = 0  操作成功。

在线计费欠费返回码
------------------
   MSCC层返回码一  =  4012
   MSCC层返回码二  =  NULL
   MSCC层返回码三  =  NULL
   MSCC层返回码四  =  NULL
   MSCC层返回码五  =  NULL
Command层返回码一  =  4012
Command层返回码二  =  NULL
Command层返回码三  =  NULL
Command层返回码四  =  NULL
Command层返回码五  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CCLIMITRC.md`
