---
id: UDG@20.15.2@MMLCommand@LST PATHRESALMTHD
type: MMLCommand
name: LST PATHRESALMTHD（查询路径资源不足告警阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PATHRESALMTHD
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
- 路径资源不足告警阈值
status: active
---

# LST PATHRESALMTHD（查询路径资源不足告警阈值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来显示路径资源不足告警的阈值和恢复阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/PATHRESALMTHD]] · 路径资源不足告警阈值（PATHRESALMTHD）

## 使用实例

查询路径资源不足告警的阈值和恢复阈值：

```
LST PATHRESALMTHD:;
```

```

RETCODE = 0  操作成功。

路径资源占用率告警阈值
----------------------
告警产生阈值（%）  =  80
告警恢复阈值（%）  =  75
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PATHRESALMTHD.md`
