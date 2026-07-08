---
id: UDG@20.15.2@MMLCommand@CHK BLK
type: MMLCommand
name: CHK BLK（CSDB检查闭塞RU）
nf: UDG
version: 20.15.2
verb: CHK
object_keyword: BLK
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 闭塞管理
status: active
---

# CHK BLK（CSDB检查闭塞RU）

## 功能

该命令用于CSDB服务端检查能否闭塞指定SCALEGROUP包含的RU。

## 注意事项

- 该命令在容器场景下不支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCALEGROUP | 物理资源组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定唯一一个物理资源组。<br>数据来源：该物理资源组名称可以通过<br>**[LST SERVICERUSTATE](../../../单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>命令查询获取，对应ScaleGroup的名字。<br>取值范围：字符串类型，长度为1～63。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BLK]] · CSDB检查闭塞RU（BLK）

## 使用实例

检查SG1_CSDB_ForCommon物理资源组是否可以闭塞RU:

```
CHK BLK: SCALEGROUP="SG1_CSDB_ForCommon";
RETCODE = 0  操作成功。

操作结果如下：
--------------
是否支持闭塞RU  =  支持闭塞RU
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/CSDB检查闭塞RU（CHK-BLK）_52427868.md`
