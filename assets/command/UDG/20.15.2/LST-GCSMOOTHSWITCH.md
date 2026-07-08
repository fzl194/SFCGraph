---
id: UDG@20.15.2@MMLCommand@LST GCSMOOTHSWITCH
type: MMLCommand
name: LST GCSMOOTHSWITCH（查询GC平滑开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GCSMOOTHSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 流控管理
status: active
---

# LST GCSMOOTHSWITCH（查询GC平滑开关）

## 功能

该命令用于查询GC（Garbage Collection）平滑开关，决定流控模块计算CPU时是否需要刨除GC。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [GC平滑开关（GCSMOOTHSWITCH）](configobject/UDG/20.15.2/GCSMOOTHSWITCH.md)

## 使用实例

查询GC平滑开关状态。

```
LST GCSMOOTHSWITCH:;
RETCODE = 0  操作成功

结果如下
------------------------
GC平滑开关  =  打开GC平滑开关
令牌刷新周期 = 60
特定周期内最大GC刨除次数 = 10

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询GC平滑开关（LST-GCSMOOTHSWITCH）_43960919.md`
