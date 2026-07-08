---
id: UDG@20.15.2@MMLCommand@LST QOEBASICFUNC
type: MMLCommand
name: LST QOEBASICFUNC（查询QoE基本功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: QOEBASICFUNC
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 智能板管理
- QoE
- QoE基本功能
status: active
---

# LST QOEBASICFUNC（查询QoE基本功能）

## 功能

**适用NF：PGW-U、UPF**

此命令用于查询QoE基本功能相关参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [QoE基本功能（QOEBASICFUNC）](configobject/UDG/20.15.2/QOEBASICFUNC.md)

## 使用实例

查询当前QoE基本功能的设置：

```
%%LST QOEBASICFUNC:;
```

```
%%
RETCODE = 0  操作成功

结果如下
--------
    QoE分析开关  =  使能
QoE智能分析开关  =  使能
       运行模式  =  SSU
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询QoE基本功能（LST-QOEBASICFUNC）_24347197.md`
