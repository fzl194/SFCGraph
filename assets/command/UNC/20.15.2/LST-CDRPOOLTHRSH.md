---
id: UNC@20.15.2@MMLCommand@LST CDRPOOLTHRSH
type: MMLCommand
name: LST CDRPOOLTHRSH（查询话单池空间告警阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CDRPOOLTHRSH
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 告警管理
- 话单池空间告警阈值
status: active
---

# LST CDRPOOLTHRSH（查询话单池空间告警阈值）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查询话单池空间不足告警阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CDRPOOLTHRSH]] · 话单池空间告警阈值（CDRPOOLTHRSH）

## 使用实例

查询话单池空间不足告警的上报和恢复阈值信息：

```
LST CDRPOOLTHRSH:;
```

```

RETCODE = 0  操作成功。

话单池告警门限
--------------
告警产生阈值（%）  =  80
告警恢复阈值（%）  =  70
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CDRPOOLTHRSH.md`
