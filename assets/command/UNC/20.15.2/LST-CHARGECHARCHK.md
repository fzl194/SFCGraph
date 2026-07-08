---
id: UNC@20.15.2@MMLCommand@LST CHARGECHARCHK
type: MMLCommand
name: LST CHARGECHARCHK（查询是否检查Serving Node携带的CC）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHARGECHARCHK
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 计费参数
status: active
---

# LST CHARGECHARCHK（查询是否检查Serving Node携带的CC）

## 功能

**适用NF：PGW-C、SMF**

该命令用来查询是否检查Serving Node携带的charge-characteristic。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHARGECHARCHK]] · 是否检查Serving Node携带的CC（CHARGECHARCHK）

## 使用实例

查询是否检查Serving Node携带的charge-characteristic：

```
LST CHARGECHARCHK:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
检查Serving Node携带的charge-characteristic  =  允许
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHARGECHARCHK.md`
