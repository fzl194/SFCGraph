---
id: UDG@20.15.2@MMLCommand@LST KPIMONSWITCH
type: MMLCommand
name: LST KPIMONSWITCH（查询KPI异常检测功能开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: KPIMONSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 指标监控
status: active
---

# LST KPIMONSWITCH（查询KPI异常检测功能开关）

## 功能

该命令用于查询KPI异常检测功能开关。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/KPIMONSWITCH]] · KPI异常检测功能开关（KPIMONSWITCH）

## 使用实例

查询KPI异常检测功能开关状态。

```
%%LST KPIMONSWITCH:;%%
RETCODE = 0  操作成功

结果如下
--------
KPI异常检测开关  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询KPI异常检测功能开关（LST-KPIMONSWITCH）_87483782.md`
