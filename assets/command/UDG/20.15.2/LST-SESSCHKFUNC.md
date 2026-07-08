---
id: UDG@20.15.2@MMLCommand@LST SESSCHKFUNC
type: MMLCommand
name: LST SESSCHKFUNC（查询会话核查配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SESSCHKFUNC
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 业务恢复管理
- 业务核查
status: active
---

# LST SESSCHKFUNC（查询会话核查配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询会话核查配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SESSCHKFUNC]] · 会话核查配置（SESSCHKFUNC）

## 使用实例

显示会话核查配置：

```
LST SESSCHKFUNC:;
```

```

RETCODE = 0 操作成功。
会话核查配置信息
----------------
        路径断核查开关 = 使能
          每日核查开关 = 使能
        SG恢复核查开关 = 使能
  会话规格限制核查开关 = 使能
      会话创建核查开关 = 使能
      会话创建核查阈值 = 4
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SESSCHKFUNC.md`
