---
id: UDG@20.15.2@MMLCommand@LST TOPOLICYMATCH
type: MMLCommand
name: LST TOPOLICYMATCH（查询TCP优化策略匹配规则）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOPOLICYMATCH
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP优化策略匹配
status: active
---

# LST TOPOLICYMATCH（查询TCP优化策略匹配规则）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询TCP优化策略匹配规则。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOPOLICYMATCH]] · TCP优化策略匹配规则（TOPOLICYMATCH）

## 使用实例

运营商需要查询所有的TCP优化策略匹配规则：

```
LST TOPOLICYMATCH:;
```

```

RETCODE = 0  操作成功

TCP优化策略匹配规则
----------------
小区组名称          IMSI组名称        RAT类型    策略ID
TestCellGroupName   TestIMSIGroupName  NR         1
TestCellGroupName   TestIMSIGroupName  EUTRAN     2
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TOPOLICYMATCH.md`
