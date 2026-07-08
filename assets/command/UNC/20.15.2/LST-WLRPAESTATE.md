---
id: UNC@20.15.2@MMLCommand@LST WLRPAESTATE
type: MMLCommand
name: LST WLRPAESTATE（查询无线路由PAE使能状态）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: WLRPAESTATE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 无线路由PAE使能状态
status: active
---

# LST WLRPAESTATE（查询无线路由PAE使能状态）

## 功能

该命令用于查询PAE使能状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/WLRPAESTATE]] · 无线路由PAE使能状态（WLRPAESTATE）

## 使用实例

查询PAE使能状态：

```
LST WLRPAESTATE:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
PAE使能状态 =  TRUE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-WLRPAESTATE.md`
