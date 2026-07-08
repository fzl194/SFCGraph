---
id: UNC@20.15.2@MMLCommand@LST IPEN7SESSFUNC
type: MMLCommand
name: LST IPEN7SESSFUNC（查询智能双N7会话特性是否使能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPEN7SESSFUNC
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 智能双N7会话
status: active
---

# LST IPEN7SESSFUNC（查询智能双N7会话特性是否使能）

## 功能

**适用NF：SMF、PGW-C**

该命令用于查询智能双N7会话特性是否使能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPEN7SESSFUNC]] · 智能双N7会话特性是否使能（IPEN7SESSFUNC）

## 使用实例

查询智能双N7会话特性是否使能：

```
%%LST IPEN7SESSFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
智能N7会话特性开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询智能双N7会话特性是否使能（LST-IPEN7SESSFUNC）_80872788.md`
