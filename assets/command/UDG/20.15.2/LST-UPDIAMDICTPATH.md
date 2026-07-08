---
id: UDG@20.15.2@MMLCommand@LST UPDIAMDICTPATH
type: MMLCommand
name: LST UPDIAMDICTPATH（查询Diameter字典加载路径）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPDIAMDICTPATH
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter管理
- Diameter字典管理
- 加载路径
status: active
---

# LST UPDIAMDICTPATH（查询Diameter字典加载路径）

## 功能

**适用NF：UPF**

该命令用于查询Diameter字典加载路径。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPDIAMDICTPATH]] · Diameter字典加载路径（UPDIAMDICTPATH）

## 使用实例

当需要查询当前配置的Diameter字典加载路径时：

```
LST UPDIAMDICTPATH:;
```

```

RETCODE = 0  操作成功
Diameter字典加载路径
--------------------
        应用  =  SWM
    字典序号  =  1
字典加载路径  =  EPC标准字典路径
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPDIAMDICTPATH.md`
