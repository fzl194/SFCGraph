---
id: UDG@20.15.2@MMLCommand@LST DRAUTOSWOVER
type: MMLCommand
name: LST DRAUTOSWOVER（查询热备模式下是否开启自动倒换功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DRAUTOSWOVER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST DRAUTOSWOVER（查询热备模式下是否开启自动倒换功能）

## 功能

该命令用于查询在热备模式下是否开启自动倒换功能。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/DRAUTOSWOVER]] · 热备模式下是否开启自动倒换功能（DRAUTOSWOVER）

## 使用实例

查询在热备模式下是否开启自动倒换功能。

```
%%LST DRAUTOSWOVER:;%%
RETCODE = 0  操作成功

结果如下
--------
自动倒回功能开关  =  关闭
  等待时间(分钟)  =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询热备模式下是否开启自动倒换功能（LST-DRAUTOSWOVER）_80076380.md`
