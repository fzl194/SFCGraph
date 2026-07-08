---
id: UDG@20.15.2@MMLCommand@LST SFEPKTRCVMODE
type: MMLCommand
name: LST SFEPKTRCVMODE（查询SFE当前收包模式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SFEPKTRCVMODE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP性能配置
- SFE收包模式配置
status: active
---

# LST SFEPKTRCVMODE（查询SFE当前收包模式）

## 功能

该命令用来查询SFE当前收包模式。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [SFE当前收包模式（SFEPKTRCVMODE）](configobject/UDG/20.15.2/SFEPKTRCVMODE.md)

## 使用实例

查询SFE当前收包模式：

```
LST SFEPKTRCVMODE:;
```

```

RETCODE = 0 操作成功

结果如下
------------------------
SFE收包模式  =  相对优先级
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SFE当前收包模式（LST-SFEPKTRCVMODE）_00441053.md`
