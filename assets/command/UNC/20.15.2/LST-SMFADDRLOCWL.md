---
id: UNC@20.15.2@MMLCommand@LST SMFADDRLOCWL
type: MMLCommand
name: LST SMFADDRLOCWL（查询位置区域地址分配用户白名单）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFADDRLOCWL
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 位置区域地址分配白名单
status: active
---

# LST SMFADDRLOCWL（查询位置区域地址分配用户白名单）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询位置区域分配地址用户白名单。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFADDRLOCWL]] · 位置区域地址分配用户白名单（SMFADDRLOCWL）

## 使用实例

查询位置区域分配地址用户白名单：

```
LST SMFADDRLOCWL:;
RETCODE = 0  操作成功。

结果如下
----------------------
MSISDN  =  123456
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询位置区域地址分配用户白名单（LST-SMFADDRLOCWL）_35636457.md`
