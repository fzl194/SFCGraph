---
id: UDG@20.15.2@MMLCommand@LST MONNFTHR
type: MMLCommand
name: LST MONNFTHR（查询正常状态网元的占比阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MONNFTHR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST MONNFTHR（查询正常状态网元的占比阈值）

## 功能

该命令用于查询与当前网元具有容灾关系的其他网元中，状态正常的网元数目在所有网元数目的占比阈值。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/MONNFTHR]] · 正常状态网元的占比阈值（MONNFTHR）

## 使用实例

查询正常状态网元的占比阈值。

```
%%LST MONNFTHR:;%%
RETCODE = 0  操作成功

结果如下
--------
正常状态网元占比阈值（%）  =  100
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询正常状态网元的占比阈值（LST-MONNFTHR）_02844813.md`
