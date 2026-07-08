---
id: UDG@20.15.2@MMLCommand@LST TOLOADALMTHD
type: MMLCommand
name: LST TOLOADALMTHD（查询告警阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOLOADALMTHD
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP负载告警阈值控制
status: active
---

# LST TOLOADALMTHD（查询告警阈值）

## 功能

**适用NF：UPF**

该命令用于查询告警阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [告警阈值（TOLOADALMTHD）](configobject/UDG/20.15.2/TOLOADALMTHD.md)

## 使用实例

查询告警阈值：

```
LST TOLOADALMTHD:;
```

```

RETCODE = 0  操作成功

TCP负载告警阈值控制
------------------
告警产生阈值（%）  =  80
告警恢复阈值（%）  =  60
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询告警阈值（LST-TOLOADALMTHD）_31379113.md`
