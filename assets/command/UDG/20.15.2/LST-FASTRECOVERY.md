---
id: UDG@20.15.2@MMLCommand@LST FASTRECOVERY
type: MMLCommand
name: LST FASTRECOVERY（查询全局业务快速恢复配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FASTRECOVERY
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 业务恢复管理
- 业务快速恢复
status: active
---

# LST FASTRECOVERY（查询全局业务快速恢复配置）

## 功能

**适用NF：SGW-U、PGW-U**

该命令用于显示业务快速恢复功能的配置。

## 注意事项

该命令执行后需要关闭已经创建了数据面跟踪的所有跟踪任务，重新创建新的跟踪任务才能生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/FASTRECOVERY]] · 全局业务快速恢复配置（FASTRECOVERY）

## 使用实例

当用户需要查询快速业务恢复功能配置时：

```
LST FASTRECOVERY:;
```

```

RETCODE = 0 操作成功。

业务快速恢复配置信息
--------------------
防闪断定时器时长（秒） = 120
保留承载的超时时长（分） = 59
故障重启业务恢复功能PGW开关 = 不使能
PDTN功能开关 = 不使能
故障重启业务恢复功能SGW开关 = 不使能
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全局业务快速恢复配置（LST-FASTRECOVERY）_97884700.md`
