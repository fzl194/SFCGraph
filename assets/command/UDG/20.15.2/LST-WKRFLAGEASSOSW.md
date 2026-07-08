---
id: UDG@20.15.2@MMLCommand@LST WKRFLAGEASSOSW
type: MMLCommand
name: LST WKRFLAGEASSOSW（查询Worker流表老化关联开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: WKRFLAGEASSOSW
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务五元组管理
- Worker五元组老化关联开关
status: active
---

# LST WKRFLAGEASSOSW（查询Worker流表老化关联开关）

## 功能

**适用NF：UPF**

该命令用于查询Worker的流表老化关联功能是否开启。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/WKRFLAGEASSOSW]] · Worker流表老化关联开关（WKRFLAGEASSOSW）

## 使用实例

当需要查询所有worker的流表老化关联功能开关时，执行一下命令：

```
LST WKRFLAGEASSOSW:;
```

```

```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Worker流表老化关联开关（LST-WKRFLAGEASSOSW）_28361117.md`
