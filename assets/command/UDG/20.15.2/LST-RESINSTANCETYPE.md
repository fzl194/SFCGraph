---
id: UDG@20.15.2@MMLCommand@LST RESINSTANCETYPE
type: MMLCommand
name: LST RESINSTANCETYPE（查询资源实例类型）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RESINSTANCETYPE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- RU管理
status: active
---

# LST RESINSTANCETYPE（查询资源实例类型）

## 功能

该命令用于查询资源实例类型。当用户需要知道本网元VNFC下支持哪些资源实例类型时，可以使用此命令查询。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RESINSTANCETYPE]] · 资源实例类型（RESINSTANCETYPE）

## 使用实例

查询资源实例类型：

```
LST RESINSTANCETYPE:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功。

结果如下
------------------------
资源实例类型 

CSDB_SD_RU
CSDB_OM_RU
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询资源实例类型（LST-RESINSTANCETYPE）_59103378.md`
