---
id: UDG@20.15.2@MMLCommand@LST PODHEALPLY
type: MMLCommand
name: LST PODHEALPLY（查询Pod自愈策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PODHEALPLY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST PODHEALPLY（查询Pod自愈策略）

## 功能

该命令用于查询已经配置的Pod自愈策略。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATUS | Pod状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示Pod状态信息。<br>数据来源：本端规划<br>取值范围：<br>- “NORMAL（正常）”：状态正常<br>- “FAULT（故障）”：状态故障<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [Pod自愈策略（PODHEALPLY）](configobject/UDG/20.15.2/PODHEALPLY.md)

## 使用实例

查询已经配置的状态为NORMAL的Pod自愈策略。

```
%%LST PODHEALPLY: STATUS=NORMAL;%%
RETCODE = 0  操作成功

结果如下
--------
     Pod状态      =  正常
  预等待时间(秒)  =  300
自愈等待时间(秒)  =  210
    自愈次数      =  3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Pod自愈策略（LST-PODHEALPLY）_09587873.md`
