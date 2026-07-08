---
id: UDG@20.15.2@MMLCommand@LST SFIPCPUALMTHD
type: MMLCommand
name: LST SFIPCPUALMTHD（查询告警阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SFIPCPUALMTHD
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- 告警管理
- CPU占用率
status: active
---

# LST SFIPCPUALMTHD（查询告警阈值）

## 功能

该命令用于查询第三方app的CPU过载告警阈值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SFIPCPUALMTHD]] · 告警阈值（SFIPCPUALMTHD）

## 使用实例

查询第三方app的过载告警阈值：

```
LST SFIPCPUALMTHD:;
```

```

RETCODE = 0  操作成功

过载告警阈值
------------
告警产生阈值(%)  =  80
告警恢复阈值(%)  =  60
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SFIPCPUALMTHD.md`
