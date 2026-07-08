---
id: UNC@20.15.2@MMLCommand@LST ROUTEPOLICY
type: MMLCommand
name: LST ROUTEPOLICY（查询路由策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ROUTEPOLICY
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 路由策略
status: active
---

# LST ROUTEPOLICY（查询路由策略）

## 功能

该命令用于查询配置的路由策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROUTEPOLICY]] · 路由策略（ROUTEPOLICY）

## 使用实例

查询所有配置的路由策略信息：

```
LST ROUTEPOLICY:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
路由策略名字  =  a
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ROUTEPOLICY.md`
