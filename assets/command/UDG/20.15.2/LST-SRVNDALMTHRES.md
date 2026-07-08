---
id: UDG@20.15.2@MMLCommand@LST SRVNDALMTHRES
type: MMLCommand
name: LST SRVNDALMTHRES（查询业务节点资源不足告警阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SRVNDALMTHRES
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
- 业务节点资源不足告警阈值
status: active
---

# LST SRVNDALMTHRES（查询业务节点资源不足告警阈值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询业务节点告警阈值和恢复告警阈值。当业务节点资源使用率超过配置的告警门限时产生告警。当使用率低于配置的恢复门限时恢复告警。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [业务节点资源不足告警阈值（SRVNDALMTHRES）](configobject/UDG/20.15.2/SRVNDALMTHRES.md)

## 使用实例

假如运营商想要查询业务节点的告警阈值和恢复告警阈值，使用此命令：

```
LST SRVNDALMTHRES:;
```

```

RETCODE = 0  操作成功。

业务节点资源不足告警阈值信息
----------------------------
    业务节点告警阈值  =  85
业务节点恢复告警阈值  =  75
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询业务节点资源不足告警阈值（LST-SRVNDALMTHRES）_82837875.md`
