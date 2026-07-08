---
id: UDG@20.15.2@MMLCommand@LST TOEVALUATEPARA
type: MMLCommand
name: LST TOEVALUATEPARA（查询TCP优化评估配置信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOEVALUATEPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP优化评估配置
status: active
---

# LST TOEVALUATEPARA（查询TCP优化评估配置信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询TCP优化评估配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOEVALUATEPARA]] · TCP优化评估配置信息（TOEVALUATEPARA）

## 使用实例

查询设置TCP优化评估配置：

```
LST TOEVALUATEPARA:;
```

```

RETCODE = 0 操作成功。

结果如下
------------------------
TCP优化评估开关 = Enable
TCP优化评估抽样比率 = 50
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询TCP优化评估配置信息（LST-TOEVALUATEPARA）_08865124.md`
