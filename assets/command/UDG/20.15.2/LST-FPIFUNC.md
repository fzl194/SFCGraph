---
id: UDG@20.15.2@MMLCommand@LST FPIFUNC
type: MMLCommand
name: LST FPIFUNC（查询FPI差异化控制功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FPIFUNC
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 无线资源优化
- FPI
status: active
---

# LST FPIFUNC（查询FPI差异化控制功能）

## 功能

**适用NF：UPF、PGW-U**

该命令用于查询FPI差异化控制功能状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [FPI差异化控制功能（FPIFUNC）](configobject/UDG/20.15.2/FPIFUNC.md)

## 使用实例

查询FPI差异化控制功能状态：

```
LST FPIFUNC:;
```

```

RETCODE = 0  操作成功

结果如下
--------
FPI使能开关  =  使能
FPI传递类型  =  DSCP
   策略来源  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询FPI差异化控制功能（LST-FPIFUNC）_75405265.md`
