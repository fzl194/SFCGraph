---
id: UDG@20.15.2@MMLCommand@LST IPPOOLALMTHD
type: MMLCommand
name: LST IPPOOLALMTHD（查询本地地址池占用率告警阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPPOOLALMTHD
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务告警管理
- 地址池占用率告警阈值
status: active
---

# LST IPPOOLALMTHD（查询本地地址池占用率告警阈值）

## 功能

**适用NF：PGW-U、UPF**

此命令用于查询本地地址池使用率的告警阈值和告警恢复阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPPOOLALMTHD]] · 本地地址池占用率告警阈值（IPPOOLALMTHD）

## 使用实例

显示本地地址池使用率的告警阈值和告警恢复阈值：

```
LST IPPOOLALMTHD:;
```

```

RETCODE = 0  操作成功。

地址池占用率告警阈值
--------------------
告警产生阈值（%）  =  80
告警恢复阈值（%）  =  70
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IPPOOLALMTHD.md`
