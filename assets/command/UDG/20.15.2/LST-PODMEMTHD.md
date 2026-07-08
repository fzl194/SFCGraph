---
id: UDG@20.15.2@MMLCommand@LST PODMEMTHD
type: MMLCommand
name: LST PODMEMTHD（查询POD内存阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PODMEMTHD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# LST PODMEMTHD（查询POD内存阈值）

## 功能

该命令用于查询POD内存阈值。

> **说明**
> - 该命令执行后立即生效。
> - 该命令仅在FusionStage裸机容器下支持。

## 权限

G_1，管理员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/PODMEMTHD]] · POD内存阈值（PODMEMTHD）

## 使用实例

查询POD内存告警阈值。

```
%%LST PODMEMTHD:;%%
RETCODE = 0  操作成功

结果如下
------------------------
告警上报门限  =  90
告警恢复门限  =  80
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询POD内存阈值（LST-PODMEMTHD）_92780526.md`
