---
id: UDG@20.15.2@MMLCommand@LST VONRMOSCLASS
type: MMLCommand
name: LST VONRMOSCLASS（查询MOS分类信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VONRMOSCLASS
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- VoNR质量监控配置
- VoNR MOS分类
status: active
---

# LST VONRMOSCLASS（查询MOS分类信息）

## 功能

**适用NF：UPF**

该命令用于查询MOS分类区间值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VONRMOSCLASS]] · MOS分类区间值（VONRMOSCLASS）

## 使用实例

查询MOS分类信息：

```
LST VONRMOSCLASS:;
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

- 原始手册：`evidence/UDG/20.15.2/LST-VONRMOSCLASS.md`
