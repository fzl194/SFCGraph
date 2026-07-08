---
id: UDG@20.15.2@MMLCommand@LST COSTOS
type: MMLCommand
name: LST COSTOS（查询COS TOS映射策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: COSTOS
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 传输层控制
- COSTOS映射策略
status: active
---

# LST COSTOS（查询COS TOS映射策略）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询是否使能Cos Tos映射策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [COS TOS映射策略（COSTOS）](configobject/UDG/20.15.2/COSTOS.md)

## 使用实例

查询是否使能Cos Tos映射策略：

```
LST COSTOS:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
TOS策略  =  不使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询COS-TOS映射策略（LST-COSTOS）_82837706.md`
