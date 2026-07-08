---
id: UDG@20.15.2@MMLCommand@LST DBSOFTPARA
type: MMLCommand
name: LST DBSOFTPARA（查询CSDB软件调试参数表）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DBSOFTPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 软件参数管理
status: active
---

# LST DBSOFTPARA（查询CSDB软件调试参数表）

## 功能

该命令用于查询软件调试参数表。

## 注意事项

该命令参数的具体说明请参见产品文档中“CSDB软件参数”。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARAID | 参数标识 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定唯一一个参数标识号。<br>数据来源：本端规划<br>取值范围：0～1023。<br>默认值：无。<br>配置原则：如果不指定参数标识，则显示所有参数信息。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DBSOFTPARA]] · CSDB软件调试参数表（DBSOFTPARA）

## 使用实例

查询 “参数标识” 为 “1012” 的软调参数：

```
LST DBSOFTPARA: PARAID=1012;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CSDB软件调试参数表(LST-DBSOFTPARA)_80429703.md`
