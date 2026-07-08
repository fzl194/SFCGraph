---
id: UDG@20.15.2@MMLCommand@LST GLOBALIMS
type: MMLCommand
name: LST GLOBALIMS（查询全局IMS配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLOBALIMS
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- VOLTE管理
- 全局IMS配置
status: active
---

# LST GLOBALIMS（查询全局IMS配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询全局IMS互通配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLOBALIMS]] · 全局IMS配置（GLOBALIMS）

## 使用实例

显示全局IMS配置：

```
LST GLOBALIMS:;
```

```

RETCODE = 0  操作成功。

全局IMS配置信息
---------------
              IMS功能开关  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全局IMS配置（LST-GLOBALIMS）_82837831.md`
