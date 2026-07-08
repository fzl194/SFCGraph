---
id: UDG@20.15.2@MMLCommand@LST ISUPODCPUTHD
type: MMLCommand
name: LST ISUPODCPUTHD（查询ISU POD业务CPU过载告警阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ISUPODCPUTHD
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
- 业务CPU过载告警阈值
status: active
---

# LST ISUPODCPUTHD（查询ISU POD业务CPU过载告警阈值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

查询ISU POD业务CPU过载告警阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [ISU POD业务CPU过载告警阈值（ISUPODCPUTHD）](configobject/UDG/20.15.2/ISUPODCPUTHD.md)

## 使用实例

查询ISU POD业务CPU过载告警阈值：

```
LST ISUPODCPUTHD:;
```

```

RETCODE = 0  Operation succeeded

The result is as follows
------------------------
Alarm Reporting Threshold  =  85
 Alarm Recovery threshold  =  75
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ISU-POD业务CPU过载告警阈值（LST-ISUPODCPUTHD）_83535543.md`
