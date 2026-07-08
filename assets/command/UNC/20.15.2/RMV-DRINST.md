---
id: UNC@20.15.2@MMLCommand@RMV DRINST
type: MMLCommand
name: RMV DRINST（删除容灾实例）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DRINST
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 容灾管理
status: active
---

# RMV DRINST（删除容灾实例）

## 功能

![](删除容灾实例(RMV DRINST)_51012923.assets/notice_3.0-zh-cn_2.png)

该操作将删除容灾配置，影响容灾数据备份，操作前请先确保已经关闭容灾激活开关。

该命令用于删除本端容灾实例信息。

## 注意事项

- 执行该命令之前，请先确保已经关闭容灾激活开关。
- 本命令执行后，只有当执行命令**[DSP DRINFO](查询容灾信息(DSP DRINFO)_51012929.md)**查询到被删除的容灾实例“数据备份状态”为“容灾配置表已删除”时，才可重新配置新容灾实例。
- 执行该命令后，三分钟内请勿使用**[ADD DRINST](配置容灾实例(ADD DRINST)_51011025.md)**和**[ADD DRCOMM](增加容灾实例地址(ADD DRCOMM)_51012925.md)**等添加容灾配置的命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| DRINSTID | 容灾实例ID | 可选必选说明：必选参数。<br>参数含义：该参数用于配置容灾实例标识。可使用<br>**[LST DRINST](查询容灾实例(LST DRINST)_51012924.md)**<br>命令查询本端已配置的容灾实例ID。<br>数据来源：全网规划。<br>取值范围：整型，0~63。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DRINST]] · 容灾实例（DRINST）

## 使用实例

删除 “容灾实例ID” 为 “2” 的容灾实例：

```
RMV DRINST: DRINSTID=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DRINST.md`
