---
id: UNC@20.15.2@MMLCommand@LST IPPOOLALMTHD
type: MMLCommand
name: LST IPPOOLALMTHD（查询本地地址池组使用率告警阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPPOOLALMTHD
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址池组使用率告警阈值
status: active
---

# LST IPPOOLALMTHD（查询本地地址池组使用率告警阈值）

## 功能

**适用NF：PGW-C、GGSN、SMF**

此命令用于查询本地地址池组使用率告警的产生阈值和恢复阈值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPPOOLALMTHD]] · 本地地址池组使用率告警阈值（IPPOOLALMTHD）

## 使用实例

查询本地地址池组使用率告警的产生阈值和恢复阈值，执行命令如下： LST IPPOOLALMTHD:;

```
%%LST IPPOOLALMTHD:;%%
RETCODE = 0  操作成功。

结果如下
--------------------
告警产生阈值 （%）  =  80
告警恢复阈值 （%）  =  70
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询本地地址池组使用率告警阈值（LST-IPPOOLALMTHD）_64343886.md`
