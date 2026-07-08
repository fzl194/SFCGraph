---
id: UDG@20.15.2@MMLCommand@LST WLRSITE
type: MMLCommand
name: LST WLRSITE（查询无线路由全局属性配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: WLRSITE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 无线路由管理
- 无线路由全局配置
status: active
---

# LST WLRSITE（查询无线路由全局属性配置）

## 功能

该命令用于查询无线路由全局属性配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [无线路由全局属性配置（WLRSITE）](configobject/UDG/20.15.2/WLRSITE.md)

## 使用实例

查询无线路由全局属性配置：

```
LST WLRSITE:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
     GR定时器（s）  =  1
PAE延时定时器（s）  =  30
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询无线路由全局属性配置（LST-WLRSITE）_49961286.md`
