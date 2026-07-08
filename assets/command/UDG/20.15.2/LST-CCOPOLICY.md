---
id: UDG@20.15.2@MMLCommand@LST CCOPOLICY
type: MMLCommand
name: LST CCOPOLICY（查询CCO策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CCOPOLICY
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 智能板管理
- cco
- ccopolicy
status: active
---

# LST CCOPOLICY（查询CCO策略）

## 功能

**适用NF：UPF**

该命令用于查询CCO策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CCOPOLICY]] · CCO策略（CCOPOLICY）

## 使用实例

显示CCO策略：

```
LST CCOPOLICY:;
```

```

RETCODE = 0  操作成功

CCO策略:
------------
    BWMCAR策略开关  = ENABLE
 BWMSHAPING策略开关 = ENABLE
 大象流抑制策略开关 = ENABLE
     TO分流策略开关 = ENABLE
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-CCOPOLICY.md`
