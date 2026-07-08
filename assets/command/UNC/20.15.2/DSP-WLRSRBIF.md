---
id: UNC@20.15.2@MMLCommand@DSP WLRSRBIF
type: MMLCommand
name: DSP WLRSRBIF（查询无线路由订阅的接口信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: WLRSRBIF
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示引流表统计信息
status: active
---

# DSP WLRSRBIF（查询无线路由订阅的接口信息）

## 功能

该命令用于查询无线路由订阅的接口名称和索引对应关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [无线路由订阅的接口信息（WLRSRBIF）](configobject/UNC/20.15.2/WLRSRBIF.md)

## 使用实例

查询无线路由订阅的接口名称和索引对应关系：

```
DSP WLRSRBIF:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
  接口名称  =  Tunnel1
  接口索引  =  21
  引用计数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询无线路由订阅的接口信息（DSP-WLRSRBIF）_49802074.md`
