---
id: UDG@20.15.2@MMLCommand@LST PAEDYETRACECFG
type: MMLCommand
name: LST PAEDYETRACECFG（查询PAE染色流控开关及阈值参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PAEDYETRACECFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 染色流控
status: active
---

# LST PAEDYETRACECFG（查询PAE染色流控开关及阈值参数）

## 功能

该命令用于查询PAE染色跟踪流控开关及阈值参数。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [PAE染色流控开关及阈值参数（PAEDYETRACECFG）](configobject/UDG/20.15.2/PAEDYETRACECFG.md)

## 使用实例

查询PAE染色跟踪流控开关及阈值参数：

```
+++    UNC/*MEID:0 MENAME:env103*/        2024-12-13 00:58:26
O&M    #125
%%LST PAEDYETRACECFG:;%%
RETCODE = 0  操作成功

结果如下
------------------------
              全流控开关  =  开
        起控阈值X86 (‰)  =  880
        停控阈值X86 (‰)  =  800
        起控阈值ARM (‰)  =  1000
        停控阈值ARM (‰)  =  900
染色消耗CPU比例阈值 (‰)  =  40
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询PAE染色流控开关及阈值参数（LST-PAEDYETRACECFG）_20521310.md`
