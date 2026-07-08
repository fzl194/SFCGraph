---
id: UDG@20.15.2@MMLCommand@LST VOLTEABNORMOS
type: MMLCommand
name: LST VOLTEABNORMOS（查询配置的MOS值异常门限值信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VOLTEABNORMOS
command_category: 查询类
applicable_nf:
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- VoLTE MOS值的异常门限值
status: active
---

# LST VOLTEABNORMOS（查询配置的MOS值异常门限值信息）

## 功能

**适用NF：PGW-U**

该命令用于查询异常MOS值的门限值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VOLTEABNORMOS]] · MOS值的异常门限为系统初始设置值（VOLTEABNORMOS）

## 使用实例

查询异常MOS值的门限值：

```
LST VOLTEABNORMOS:;
```

```

RETCODE = 0  操作成功

MOS值的异常门限值
-----------------
MOS值的异常门限  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-VOLTEABNORMOS.md`
