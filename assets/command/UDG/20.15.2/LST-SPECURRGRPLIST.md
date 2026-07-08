---
id: UDG@20.15.2@MMLCommand@LST SPECURRGRPLIST
type: MMLCommand
name: LST SPECURRGRPLIST（查询特殊URR组列表）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SPECURRGRPLIST
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 特殊使用率上报规则组列表
status: active
---

# LST SPECURRGRPLIST（查询特殊URR组列表）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询当前系统的特殊使用量上报规则组列表配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [特殊URR组列表（SPECURRGRPLIST）](configobject/UDG/20.15.2/SPECURRGRPLIST.md)

## 使用实例

查询特殊URR组列表配置信息：

```
LST SPECURRGRPLIST:;
```

```

RETCODE = 0 操作成功。

特殊URR组列表信息：
----------------------------------
使用量上报规则组名称 = aaa
         配置域名称  =  NULL
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询特殊URR组列表（LST-SPECURRGRPLIST）_82837645.md`
