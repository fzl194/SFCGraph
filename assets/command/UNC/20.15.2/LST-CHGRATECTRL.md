---
id: UNC@20.15.2@MMLCommand@LST CHGRATECTRL
type: MMLCommand
name: LST CHGRATECTRL（显示计费速率控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGRATECTRL
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
- 计费控制
- 计费相关速率控制
status: active
---

# LST CHGRATECTRL（显示计费速率控制）

## 功能

**适用NF：PGW-C、SMF**

该命令用于显示每个POD上，当在线计费用户转离线后，每秒最大离线转回在线的用户数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGRATECTRL]] · 计费速率控制（CHGRATECTRL）

## 使用实例

查询计费速率控制：

```
LST CHGRATECTRL:;
```

```

RETCODE = 0  操作成功

计费速率控制
------------
在线计费恢复速率  =  500
融合计费恢复速率  =  500
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHGRATECTRL.md`
