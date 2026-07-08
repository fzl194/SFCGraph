---
id: UDG@20.15.2@MMLCommand@LST PATHCTRLALMTHD
type: MMLCommand
name: LST PATHCTRLALMTHD（查询大量路径断告警告警阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PATHCTRLALMTHD
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务告警管理
- 大量GTPU路径断告警门限
status: active
---

# LST PATHCTRLALMTHD（查询大量路径断告警告警阈值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来显示ALM-81100 GTPU大量路径断告警的上报阈值和恢复阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [大量路径断告警告警阈值（PATHCTRLALMTHD）](configobject/UDG/20.15.2/PATHCTRLALMTHD.md)

## 使用实例

查询大量路径断告警的上报阈值和恢复阈值：

```
LST PATHCTRLALMTHD:;
```

```

RETCODE = 0  操作成功。

大量路径断告警告警阈值
----------------------
大量路径断告警上报的阈值  =  100
大量路径断告警恢复的阈值  =  50
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询大量路径断告警告警阈值（LST-PATHCTRLALMTHD）_82837860.md`
