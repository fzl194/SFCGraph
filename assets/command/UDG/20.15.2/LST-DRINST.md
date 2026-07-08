---
id: UDG@20.15.2@MMLCommand@LST DRINST
type: MMLCommand
name: LST DRINST（查询容灾实例）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DRINST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 容灾管理
status: active
---

# LST DRINST（查询容灾实例）

## 功能

该命令用于查询本端容灾实例信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| DRINSTID | 容灾实例ID | 可选必选说明：可选参数。<br>参数含义：该参数用于配置容灾实例标识。<br>数据来源：全网规划。<br>取值范围：整型，0~63。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DRINST]] · 容灾实例（DRINST）

## 使用实例

查询容灾实例：

```
LST DRINST:;
%%LST DRINST:;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
  容灾实例ID  =  0
容灾实例名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询容灾实例(LST-DRINST)_51012924.md`
