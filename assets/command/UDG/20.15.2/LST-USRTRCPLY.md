---
id: UDG@20.15.2@MMLCommand@LST USRTRCPLY
type: MMLCommand
name: LST USRTRCPLY（查询用户跟踪策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: USRTRCPLY
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务跟踪管理
- 用户跟踪策略配置
status: active
---

# LST USRTRCPLY（查询用户跟踪策略）

## 功能

**适用NF：UPF**

该命令用于显示用户跟踪策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/USRTRCPLY]] · 用户跟踪策略（USRTRCPLY）

## 使用实例

查询用户跟踪策略：

```
LST USRTRCPLY:;
```

```

RETCODE = 0 操作成功。

用户跟踪策略
-----------------
最大保留天数  =  7
匿名化开关  =  使能
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-USRTRCPLY.md`
