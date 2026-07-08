---
id: UDG@20.15.2@MMLCommand@LST DROPFINALPKT
type: MMLCommand
name: LST DROPFINALPKT（显示配额耗尽末包动作）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DROPFINALPKT
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 配额耗尽末包动作
status: active
---

# LST DROPFINALPKT（显示配额耗尽末包动作）

## 功能

**适用NF：PGW-U、UPF**

本命令用于查询当配额耗尽时，UPF是否阻塞最后一个超出配额范围的数据报文。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [配额耗尽末包动作（DROPFINALPKT）](configobject/UDG/20.15.2/DROPFINALPKT.md)

## 使用实例

查询UPF是否阻塞最后一个超出配额范围的数据报文：

```
LST DROPFINALPKT:;
```

```

RETCODE = 0  操作成功

配额耗尽时末包动作
-----------------
开关  =  ENABLE
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示配额耗尽末包动作（LST-DROPFINALPKT）_06213368.md`
