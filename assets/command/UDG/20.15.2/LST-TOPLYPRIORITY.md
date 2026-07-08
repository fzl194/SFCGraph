---
id: UDG@20.15.2@MMLCommand@LST TOPLYPRIORITY
type: MMLCommand
name: LST TOPLYPRIORITY（查询TCP优化策略组合优先级）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOPLYPRIORITY
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP优化策略优先级
status: active
---

# LST TOPLYPRIORITY（查询TCP优化策略组合优先级）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询TCP优化策略组合优先级。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TOPLYPRIORITY]] · TCP优化策略组合优先级（TOPLYPRIORITY）

## 使用实例

运营商需要查询所有的TCP优化策略组合优先级：

```
LST TOPLYPRIORITY:;
```

```

RETCODE = 0  操作成功

TCP优化策略组合优先级
----------------
配置类型           优先级
TO_MATCH_ALL       7
TO_MATCH_RAT_CELL  6
TO_MATCH_CELL_IMSI 5
TO_MATCH_RAT_IMSI  4
TO_MATCH_RAT       3
TO_MATCH_CELL      2
TO_MATCH_IMSI      1
(结果个数 = 7)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TOPLYPRIORITY.md`
