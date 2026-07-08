---
id: UDG@20.15.2@MMLCommand@LST PAESCHEDMOD
type: MMLCommand
name: LST PAESCHEDMOD（查询PAE Channel调度模式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PAESCHEDMOD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- PAE统计信息
status: active
---

# LST PAESCHEDMOD（查询PAE Channel调度模式）

## 功能

该命令用于查询PAE Channel调度模式。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/PAESCHEDMOD]] · PAE Channel调度模式（PAESCHEDMOD）

## 使用实例

查询PAE Channel调度模式：

```
%%
LST PAESCHEDM
OD:;%%
RETCODE = 0  操作成功

结果如下:
---------
PAE Channel调度模式  =  绝对优先级
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询PAE-Channel调度模式（LST-PAESCHEDMOD）_61218393.md`
