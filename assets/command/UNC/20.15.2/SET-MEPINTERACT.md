---
id: UNC@20.15.2@MMLCommand@SET MEPINTERACT
type: MMLCommand
name: SET MEPINTERACT（设置MEP_SMF联动功能开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MEPINTERACT
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- SMF公共配置
- MEP_SMF联动功能开关
status: active
---

# SET MEPINTERACT（设置MEP_SMF联动功能开关）

## 功能

**适用NF：SMF**

该命令用来控制MEP_SMF联动处理，使能开关时，SMF向MEP订阅并接受MEP推送的分流规则和DNS重定向规则，去使能开关时，SMF向MEP去订阅。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SWITCH |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置SMF是否与MEP联动。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（不使能）”：MEP_SMF联动开关不使能<br>- “ENABLE（使能）”：MEP_SMF联动开关使能<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MEPINTERACT查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MEPINTERACT]] · MEP_SMF联动功能开关（MEPINTERACT）

## 使用实例

设置MEP_SMF联动功能开关，SWITCH为ENABLE：

```
SET MEPINTERACT: SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置MEP_SMF联动功能开关（SET-MEPINTERACT）_09652370.md`
