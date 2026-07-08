---
id: UDG@20.15.2@MMLCommand@LST SBIAPLE
type: MMLCommand
name: LST SBIAPLE（查询服务化接口本端实体）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SBIAPLE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口本端实体管理
status: active
---

# LST SBIAPLE（查询服务化接口本端实体）

## 功能

该命令用于查询服务化接口本端实体信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务化接口本端实体的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SBIAPLE]] · 服务化接口本端实体（SBIAPLE）

## 使用实例

若运营商想查询所有配置的服务化接口本端实体信息，可以执行如下命令：

```
LST SBIAPLE:;

%%LST SBIAPLE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                        索引  =  1
          HTTP本端实体组标识  =  1
                  本端NF类型  =  NFTypeAMF
                  目的NF类型  =  INVALID
                  CHF的目的NF类型  =  INVALID
                  目的NF服务  =  INVALID
                  描述  =  NULL
                  CHF的目的NF实例ID = NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询服务化接口本端实体（LST-SBIAPLE）_29213285.md`
