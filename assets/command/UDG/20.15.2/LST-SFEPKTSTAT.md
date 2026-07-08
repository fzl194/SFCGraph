---
id: UDG@20.15.2@MMLCommand@LST SFEPKTSTAT
type: MMLCommand
name: LST SFEPKTSTAT（查询软转发报文统计记录开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SFEPKTSTAT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 转发报文统计记录
status: active
---

# LST SFEPKTSTAT（查询软转发报文统计记录开关）

## 功能

该命令用于查询软转发报文统计记录开关配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFEPKTSTAT]] · SFE报文统计信息（SFEPKTSTAT）

## 使用实例

查询软转发报文统计记录开关配置：

```
LST SFEPKTSTAT:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
IsEnable = FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询软转发报文统计记录开关（LST-SFEPKTSTAT）_00441373.md`
