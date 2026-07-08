---
id: UDG@20.15.2@MMLCommand@LST MULTIDNNCOND
type: MMLCommand
name: LST MULTIDNNCOND（查询多DNN条件）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MULTIDNNCOND
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- MultiDNN业务控制
- 多DNN条件
status: active
---

# LST MULTIDNNCOND（查询多DNN条件）

## 功能

**适用NF：UPF**

该命令用于查询多DNN条件。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/MULTIDNNCOND]] · 多DNN条件（MULTIDNNCOND）

## 使用实例

假如运营商需要查询多DNN条件：

```
LST MULTIDNNCOND:;
```

```

RETCODE = 0  操作成功

多DNN条件信息
-------------
DNN条件类型  =  DNN名称以DNNCONDVAL结束
  DNN条件值  =  dnn1
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询多DNN条件（LST-MULTIDNNCOND）_15895831.md`
