---
id: UNC@20.15.2@MMLCommand@LST DRGROUPABLEMENT
type: MMLCommand
name: LST DRGROUPABLEMENT（查询是否使能热备容灾组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DRGROUPABLEMENT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST DRGROUPABLEMENT（查询是否使能热备容灾组）

## 功能

该命令用于查询是否使能热备容灾组。

## 注意事项

该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [是否使能热备容灾组（DRGROUPABLEMENT）](configobject/UNC/20.15.2/DRGROUPABLEMENT.md)

## 使用实例

查询是否使能热备容灾组:

```
%%LST DRGROUPABLEMENT:;%%
RETCODE = 0  操作成功

结果如下
--------
是否使能热备容灾组  =  去使能热备容灾功能
      是否自动升主  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询是否使能热备容灾组（LST-DRGROUPABLEMENT）_00761578.md`
