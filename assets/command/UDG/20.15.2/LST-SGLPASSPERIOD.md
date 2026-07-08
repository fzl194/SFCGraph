---
id: UDG@20.15.2@MMLCommand@LST SGLPASSPERIOD
type: MMLCommand
name: LST SGLPASSPERIOD（查询单通检测周期）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SGLPASSPERIOD
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- 网络侧连通性检测
- 单通检测周期
status: active
---

# LST SGLPASSPERIOD（查询单通检测周期）

## 功能

**适用NF：PGW-U、UPF**

查询单通故障检测时间周期。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SGLPASSPERIOD]] · 单通检测周期（SGLPASSPERIOD）

## 使用实例

查询单通故障检测时间周期：

```
LST SGLPASSPERIOD:;
```

```

RETCODE = 0  操作成功。

单通检测周期
------------
周期  =  20
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SGLPASSPERIOD.md`
