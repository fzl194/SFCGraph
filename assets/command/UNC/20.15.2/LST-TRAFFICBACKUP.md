---
id: UNC@20.15.2@MMLCommand@LST TRAFFICBACKUP
type: MMLCommand
name: LST TRAFFICBACKUP（查询流量备份配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TRAFFICBACKUP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- RADIUS计费管理
- 流量备份
status: active
---

# LST TRAFFICBACKUP（查询流量备份配置）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询流量备份配置的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/TRAFFICBACKUP]] · 流量备份配置（TRAFFICBACKUP）

## 使用实例

查询流量备份配置：

```
LST TRAFFICBACKUP:;
```

```

RETCODE = 0  操作成功。

流量备份配置
------------
   流量备份开关  =  允许
备份间隔 (分钟)  =  30
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询流量备份配置（LST-TRAFFICBACKUP）_09896774.md`
