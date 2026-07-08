---
id: UDG@20.15.2@MMLCommand@LST VOLTEMOSCLASS
type: MMLCommand
name: LST VOLTEMOSCLASS（查询MOS分类区间值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VOLTEMOSCLASS
command_category: 查询类
applicable_nf:
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- VoLTE MOS分类
status: active
---

# LST VOLTEMOSCLASS（查询MOS分类区间值）

## 功能

**适用NF：PGW-U**

该命令用于查询MOS分类区间值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/VOLTEMOSCLASS]] · MOS分类区间值（VOLTEMOSCLASS）

## 使用实例

查询MOS分类信息：

```
LST VOLTEMOSCLASS:;
```

```

RETCODE = 0  操作成功

MOS分类配置
-----------
MOS值为excellent和good之间的边界值  =  40
   MOS值为good和accept之间的边界值  =  36
   MOS值为accept和poor之间的边界值  =  31
      MOS值为poor和bad之间的边界值  =  26
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询MOS分类区间值（LST-VOLTEMOSCLASS）_57738483.md`
