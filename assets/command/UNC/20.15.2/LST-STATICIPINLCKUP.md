---
id: UNC@20.15.2@MMLCommand@LST STATICIPINLCKUP
type: MMLCommand
name: LST STATICIPINLCKUP（查询静态地址段在锁定UPF的用户处理）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: STATICIPINLCKUP
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF锁定静态IP冲突处理
status: active
---

# LST STATICIPINLCKUP（查询静态地址段在锁定UPF的用户处理）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询静态地址段在锁定UPF的用户处理。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [静态地址段在锁定UPF的用户处理（STATICIPINLCKUP）](configobject/UNC/20.15.2/STATICIPINLCKUP.md)

## 使用实例

查询静态地址段在锁定UPF的用户处理： LST STATICIPINLCKUP:;

```
%%LST STATICIPINLCKUP:;%%
RETCODE = 0  操作成功。

结果如下
------------------------
静态用户在锁定UPF的激活处理  =  静态用户可以在锁定的UPF激活
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询静态地址段在锁定UPF的用户处理（LST-STATICIPINLCKUP）_99442132.md`
