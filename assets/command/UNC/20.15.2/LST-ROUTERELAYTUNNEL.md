---
id: UNC@20.15.2@MMLCommand@LST ROUTERELAYTUNNEL
type: MMLCommand
name: LST ROUTERELAYTUNNEL（查询路由迭代隧道功能开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ROUTERELAYTUNNEL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由基础
- 使能路由迭代隧道
status: active
---

# LST ROUTERELAYTUNNEL（查询路由迭代隧道功能开关）

## 功能

该命令用于查询路由迭代隧道功能开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [路由迭代隧道功能开关（ROUTERELAYTUNNEL）](configobject/UNC/20.15.2/ROUTERELAYTUNNEL.md)

## 使用实例

查询路由迭代隧道开关：

```
LST ROUTERELAYTUNNEL:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
迭代隧道使能开关 =  TRUE
前缀列表名       =  a
隧道策略名       =  a
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询路由迭代隧道功能开关（LST-ROUTERELAYTUNNEL）_50281618.md`
