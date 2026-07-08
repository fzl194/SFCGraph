---
id: UNC@20.15.2@MMLCommand@LST AUTOCONFIG
type: MMLCommand
name: LST AUTOCONFIG（查询自动配置开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AUTOCONFIG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- 自动配置开关
status: active
---

# LST AUTOCONFIG（查询自动配置开关）

## 功能

该命令用于查询自动配置开关。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/AUTOCONFIG]] · 自动配置开关（AUTOCONFIG）

## 使用实例

查询自动配置开关：

```
LST AUTOCONFIG:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
自动配置开关  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AUTOCONFIG.md`
