---
id: UNC@20.15.2@MMLCommand@LST QOSDIFFERSERV
type: MMLCommand
name: LST QOSDIFFERSERV（查询DS域）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSDIFFERSERV
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- DS域配置
status: active
---

# LST QOSDIFFERSERV（查询DS域）

## 功能

该命令用来查询系统上所有的DS域。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSNAME | DS域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DS域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [DS域（QOSDIFFERSERV）](configobject/UNC/20.15.2/QOSDIFFERSERV.md)

## 使用实例

查询当前系统存在的所有DS域：

```
LST QOSDIFFERSERV:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
DS域名
default
5p3d
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DS域（LST-QOSDIFFERSERV）_49962062.md`
