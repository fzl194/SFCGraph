---
id: UDG@20.15.2@MMLCommand@LST VOLTEMOSALMTHD
type: MMLCommand
name: LST VOLTEMOSALMTHD（查询异常MOS告警阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VOLTEMOSALMTHD
command_category: 查询类
applicable_nf:
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- MOS值异常的用户比例告警阈值
status: active
---

# LST VOLTEMOSALMTHD（查询异常MOS告警阈值）

## 功能

**适用NF：PGW-U**

该命令用于查询异常MOS告警阈值和恢复告警阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [异常MOS告警阈值为系统初始设置值（VOLTEMOSALMTHD）](configobject/UDG/20.15.2/VOLTEMOSALMTHD.md)

## 使用实例

查询异常MOS告警阈值和恢复告警阈值：

```
LST VOLTEMOSALMTHD:;
```

```

RETCODE = 0  操作成功。

异常MOS告警阈值配置
-------------------
    告警阈值  =  10
恢复告警阈值  =  8
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询异常MOS告警阈值（LST-VOLTEMOSALMTHD）_57538681.md`
