---
id: UDG@20.15.2@MMLCommand@LST EXTOTTMATCHSW
type: MMLCommand
name: LST EXTOTTMATCHSW（查询OTT业务规则匹配功能是否使能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: EXTOTTMATCHSW
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 百万级业务规则库
- 全局OTT开关
status: active
---

# LST EXTOTTMATCHSW（查询OTT业务规则匹配功能是否使能配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询OTT业务规则匹配功能是否使能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/EXTOTTMATCHSW]] · OTT业务规则匹配功能是否使能（EXTOTTMATCHSW）

## 使用实例

查询外置OTT业务规则匹配功能是否使能信息：

```
LST EXTOTTMATCHSW:;
```

```

RETCODE = 0 操作成功.

外置OTT业务规则匹配功能开关信息
--------------------------------------------
外置OTT业务规则匹配功能开关IPv4 = ENABLE
外置OTT业务规则匹配功能开关IPv6 = ENABLE

(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OTT业务规则匹配功能是否使能配置（LST-EXTOTTMATCHSW）_93531881.md`
